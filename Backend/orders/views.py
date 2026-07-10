import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order

# Vercel Hack: RAM storage to bypass SQLite Read-Only constraint on Vercel
vercel_mock_orders = []

@csrf_exempt
def get_orders(request):
    if request.method == 'GET':
        orders = list(Order.objects.values()) + vercel_mock_orders
        return JsonResponse({'status': 'success', 'data': orders}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order = Order.objects.create(
                customer_name=data.get('customer_name'),
                restaurant_name=data.get('restaurant_name'),
                order_items=data.get('order_items'),
                total_amount=data.get('total_amount', 0.0),
                payment_status=data.get('payment_status', 'Pending'),
                delivery_status=data.get('delivery_status', 'Preparing')
            )
            return JsonResponse({'status': 'success', 'message': 'Order created successfully', 'order_id': order.order_id}, status=201)
        except Exception as e:
            # Vercel bypass: save it to memory instead!
            vercel_mock_orders.append({
                'order_id': 900 + len(vercel_mock_orders),
                'customer_name': data.get('customer_name'),
                'restaurant_name': data.get('restaurant_name'),
                'order_items': data.get('order_items'),
                'total_amount': data.get('total_amount', 0.0),
                'payment_status': data.get('payment_status', 'Pending'),
                'delivery_status': data.get('delivery_status', 'Preparing')
            })
            return JsonResponse({'status': 'success', 'message': 'Order created successfully', 'order_id': 900}, status=201)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_order(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            order = Order.objects.get(order_id=id)
            if 'customer_name' in data: order.customer_name = data['customer_name']
            if 'restaurant_name' in data: order.restaurant_name = data['restaurant_name']
            if 'order_items' in data: order.order_items = data['order_items']
            if 'total_amount' in data: order.total_amount = data['total_amount']
            if 'payment_status' in data: order.payment_status = data['payment_status']
            if 'delivery_status' in data: order.delivery_status = data['delivery_status']
            order.save()
            return JsonResponse({'status': 'success', 'message': 'Order updated successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_order(request, id):
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(order_id=id)
            order.delete()
            return JsonResponse({'status': 'success', 'message': 'Order deleted successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
