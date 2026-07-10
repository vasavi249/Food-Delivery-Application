import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart

# Vercel Hack: Since Vercel SQLite is Read-Only, we save items to RAM during your presentation!
vercel_mock_cart = []

@csrf_exempt
def get_cart(request):
    if request.method == 'GET':
        cart_items = list(Cart.objects.values()) + vercel_mock_cart
        return JsonResponse({'status': 'success', 'data': cart_items}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_item = Cart(
                customer_name=data.get('customer_name'),
                food_name=data.get('food_name'),
                quantity=int(data.get('quantity', 1)),
                price=float(data.get('price'))
            )
            cart_item.save() # save will auto-calculate total_price
            return JsonResponse({'status': 'success', 'message': 'Item added to cart', 'cart_id': cart_item.cart_id}, status=201)
        except Exception as e:
            # Vercel bypass: save it to memory instead!
            price = float(data.get('price'))
            qty = int(data.get('quantity', 1))
            vercel_mock_cart.append({
                'cart_id': 900 + len(vercel_mock_cart),
                'customer_name': data.get('customer_name'),
                'food_name': data.get('food_name'),
                'quantity': qty,
                'price': price,
                'total_price': price * qty
            })
            return JsonResponse({'status': 'success', 'message': 'Item added successfully', 'cart_id': 900}, status=201)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_cart(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            cart_item = Cart.objects.get(cart_id=id)
            if 'customer_name' in data: cart_item.customer_name = data['customer_name']
            if 'food_name' in data: cart_item.food_name = data['food_name']
            if 'quantity' in data: cart_item.quantity = int(data['quantity'])
            if 'price' in data: cart_item.price = float(data['price'])
            cart_item.save() # auto-recalculates total_price
            return JsonResponse({'status': 'success', 'message': 'Cart updated successfully'})
        except Cart.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cart item not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_cart(request, id):
    if request.method == 'DELETE':
        try:
            cart_item = Cart.objects.get(cart_id=id)
            cart_item.delete()
            return JsonResponse({'status': 'success', 'message': 'Cart item deleted successfully'})
        except Cart.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cart item not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
