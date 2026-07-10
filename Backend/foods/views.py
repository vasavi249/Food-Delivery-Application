import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Food

@csrf_exempt
def get_foods(request):
    if request.method == 'GET':
        foods = list(Food.objects.values())
        return JsonResponse({'status': 'success', 'data': foods}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_food(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            food = Food.objects.create(
                restaurant_name=data.get('restaurant_name'),
                food_name=data.get('food_name'),
                category=data.get('category'),
                price=data.get('price'),
                availability=data.get('availability', 'Available'),
                image_url=data.get('image_url', '')
            )
            return JsonResponse({'status': 'success', 'message': 'Food added successfully', 'food_id': food.food_id}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_food(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            food = Food.objects.get(food_id=id)
            if 'restaurant_name' in data: food.restaurant_name = data['restaurant_name']
            if 'food_name' in data: food.food_name = data['food_name']
            if 'category' in data: food.category = data['category']
            if 'price' in data: food.price = data['price']
            if 'availability' in data: food.availability = data['availability']
            if 'image_url' in data: food.image_url = data['image_url']
            food.save()
            return JsonResponse({'status': 'success', 'message': 'Food updated successfully'})
        except Food.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Food not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_food(request, id):
    if request.method == 'DELETE':
        try:
            food = Food.objects.get(food_id=id)
            food.delete()
            return JsonResponse({'status': 'success', 'message': 'Food deleted successfully'})
        except Food.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Food not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
