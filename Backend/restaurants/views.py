import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant

@csrf_exempt
def get_restaurants(request):
    if request.method == 'GET':
        restaurants = list(Restaurant.objects.values())
        return JsonResponse({'status': 'success', 'data': restaurants}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_restaurant(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            restaurant = Restaurant.objects.create(
                restaurant_name=data.get('restaurant_name'),
                owner_name=data.get('owner_name'),
                location=data.get('location'),
                cuisine=data.get('cuisine'),
                rating=data.get('rating', 0.0),
                image_url=data.get('image_url', '')
            )
            return JsonResponse({'status': 'success', 'message': 'Restaurant added successfully', 'restaurant_id': restaurant.restaurant_id}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_restaurant(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            restaurant = Restaurant.objects.get(restaurant_id=id)
            if 'restaurant_name' in data: restaurant.restaurant_name = data['restaurant_name']
            if 'owner_name' in data: restaurant.owner_name = data['owner_name']
            if 'location' in data: restaurant.location = data['location']
            if 'cuisine' in data: restaurant.cuisine = data['cuisine']
            if 'rating' in data: restaurant.rating = data['rating']
            if 'image_url' in data: restaurant.image_url = data['image_url']
            restaurant.save()
            return JsonResponse({'status': 'success', 'message': 'Restaurant updated successfully'})
        except Restaurant.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Restaurant not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_restaurant(request, id):
    if request.method == 'DELETE':
        try:
            restaurant = Restaurant.objects.get(restaurant_id=id)
            restaurant.delete()
            return JsonResponse({'status': 'success', 'message': 'Restaurant deleted successfully'})
        except Restaurant.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Restaurant not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
