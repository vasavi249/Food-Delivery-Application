import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer

@csrf_exempt
def get_customers(request):
    if request.method == 'GET':
        customers = list(Customer.objects.values())
        return JsonResponse({'status': 'success', 'data': customers}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer = Customer.objects.create(
                full_name=data.get('full_name'),
                email=data.get('email'),
                phone=data.get('phone'),
                address=data.get('address'),
                city=data.get('city')
            )
            return JsonResponse({'status': 'success', 'message': 'Customer added successfully', 'customer_id': customer.customer_id}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_customer(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            customer = Customer.objects.get(customer_id=id)
            if 'full_name' in data: customer.full_name = data['full_name']
            if 'email' in data: customer.email = data['email']
            if 'phone' in data: customer.phone = data['phone']
            if 'address' in data: customer.address = data['address']
            if 'city' in data: customer.city = data['city']
            customer.save()
            return JsonResponse({'status': 'success', 'message': 'Customer updated successfully'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Customer not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_customer(request, id):
    if request.method == 'DELETE':
        try:
            customer = Customer.objects.get(customer_id=id)
            customer.delete()
            return JsonResponse({'status': 'success', 'message': 'Customer deleted successfully'})
        except Customer.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Customer not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
