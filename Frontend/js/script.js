const BASE_URL = 'http://127.0.0.1:8000';

function showToast(message) {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerText = message;
    container.appendChild(toast);
    setTimeout(() => { toast.remove(); }, 3500);
}

function showSpinner() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) spinner.style.display = 'block';
}

function hideSpinner() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) spinner.style.display = 'none';
}

async function apiCall(endpoint, method = 'GET', body = null) {
    showSpinner();
    const options = { method: method, headers: { 'Content-Type': 'application/json' } };
    if (body) options.body = JSON.stringify(body);
    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, options);
        const data = await response.json();
        hideSpinner();
        return data;
    } catch (error) {
        hideSpinner();
        showToast('Network error or server is down.');
        console.error(error);
        return { status: 'error' };
    }
}

// ---------------------------------------------------------
// CUSTOMERS (Admin)
// ---------------------------------------------------------
async function loadCustomers() {
    const list = document.getElementById('customers-list');
    if (!list) return;
    const res = await apiCall('/customers/');
    list.innerHTML = '';
    if (res.status === 'success') {
        res.data.forEach(c => {
            list.innerHTML += `<tr>
                <td>${c.full_name}</td>
                <td>${c.email}</td>
                <td>${c.phone}</td>
                <td>${c.city}</td>
                <td><button class="btn btn-danger btn-sm" onclick="deleteCustomer(${c.customer_id})">Delete</button></td>
            </tr>`;
        });
    }
}

async function handleRegister(e) {
    e.preventDefault();
    const body = {
        full_name: document.getElementById('full_name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        address: document.getElementById('address').value,
        city: document.getElementById('city').value
    };
    const res = await apiCall('/customers/add/', 'POST', body);
    if (res.status === 'success') {
        showToast('Registration Successful!');
        setTimeout(() => window.location.href = 'login.html', 1500);
    } else {
        showToast(res.message || 'Registration failed');
    }
}

async function deleteCustomer(id) {
    const res = await apiCall(`/customers/delete/${id}/`, 'DELETE');
    if (res.status === 'success') {
        showToast('Customer deleted');
        loadCustomers();
    }
}

// ---------------------------------------------------------
// RESTAURANTS
// ---------------------------------------------------------
function handleHeroSearch() {
    const input = document.getElementById('hero-search-input');
    if(input && input.value.trim() !== '') {
        window.location.href = `restaurants.html?search=${encodeURIComponent(input.value.trim())}`;
    }
}

async function loadRestaurants() {
    const grid = document.getElementById('restaurants-grid');
    if (!grid) return;
    const res = await apiCall('/restaurants/');
    
    // Check URL for search parameter
    const urlParams = new URLSearchParams(window.location.search);
    const searchParam = urlParams.get('search');
    const searchInput = document.getElementById('res-search');
    
    if (searchInput) {
        if (searchParam) {
            searchInput.value = searchParam;
        }
        searchInput.oninput = () => renderRestaurants(res.data, grid, searchInput.value);
    }
    
    renderRestaurants(res.data, grid, searchParam || '');
}

function renderRestaurants(data, grid, query) {
    grid.innerHTML = '';
    const lowerQuery = query.toLowerCase();
    
    // Simple filter matching restaurant_name or cuisine
    const filtered = data.filter(r => 
        r.restaurant_name.toLowerCase().includes(lowerQuery) || 
        r.cuisine.toLowerCase().includes(lowerQuery)
    );
    
    if(filtered.length === 0) {
        grid.innerHTML = `<p style="grid-column: 1/-1; text-align: center; padding: 2rem;">No restaurants found matching "${query}".</p>`;
        return;
    }
    
    filtered.forEach(r => {
        const img = r.image_url ? r.image_url : 'https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=600&q=80';
        grid.innerHTML += `<div class="card restaurant-card">
            <img src="${img}" class="card-img" alt="${r.restaurant_name}">
            <div class="card-body">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3>${r.restaurant_name}</h3>
                    <span class="badge rating">⭐ ${r.rating}</span>
                </div>
                <p><strong>Cuisine:</strong> ${r.cuisine}</p>
                <p><strong>Location:</strong> ${r.location}</p>
                <div class="card-footer">
                    <button class="btn btn-primary" style="width:100%" onclick="window.location.href='menu.html?restaurant=${encodeURIComponent(r.restaurant_name)}'">View Menu</button>
                </div>
            </div>
        </div>`;
    });
}

function searchRestaurants() {
    const q = document.getElementById('search-restaurant').value.toLowerCase();
    const cards = document.querySelectorAll('.restaurant-card');
    cards.forEach(card => {
        const title = card.querySelector('h3').innerText.toLowerCase();
        card.style.display = title.includes(q) ? 'flex' : 'none';
    });
}

// ---------------------------------------------------------
// FOOD MENU
// ---------------------------------------------------------
async function loadMenu() {
    const grid = document.getElementById('menu-grid');
    if (!grid) return;

    // Check if filtering by restaurant from URL
    const urlParams = new URLSearchParams(window.location.search);
    const filterRestaurant = urlParams.get('restaurant');

    if (filterRestaurant) {
        document.getElementById('menu-title').innerText = `Menu for ${filterRestaurant}`;
    }

    const res = await apiCall('/foods/');
    grid.innerHTML = '';
    if (res.status === 'success') {
        let foods = res.data;
        if (filterRestaurant) {
            foods = foods.filter(f => f.restaurant_name === filterRestaurant);
        }

        foods.forEach(f => {
            const badgeClass = f.availability === 'Available' ? 'available' : 'out-of-stock';
            const img = f.image_url ? f.image_url : 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80';
            grid.innerHTML += `<div class="card food-card">
                <img src="${img}" class="card-img" alt="${f.food_name}">
                <div class="card-body">
                    <h3>${f.food_name}</h3>
                    <p><strong>${f.restaurant_name}</strong></p>
                    <p style="color:var(--text-muted)">${f.category}</p>
                    <h3 style="color:var(--primary); margin:10px 0;">₹${f.price}</h3>
                    <span class="badge ${badgeClass}">${f.availability}</span>
                    <div class="card-footer" style="margin-top:auto;">
                        ${f.availability === 'Available' ? `<button class="btn btn-primary" style="width:100%" onclick="addToCart('${f.food_name}', ${f.price}, 1)">Add to Cart</button>` : '<button class="btn" style="width:100%; background:#eee" disabled>Unavailable</button>'}
                    </div>
                </div>
            </div>`;
        });
    }
}

function searchFood() {
    const q = document.getElementById('search-food').value.toLowerCase();
    const cards = document.querySelectorAll('.food-card');
    cards.forEach(card => {
        const title = card.querySelector('h3').innerText.toLowerCase();
        card.style.display = title.includes(q) ? 'flex' : 'none';
    });
}

// ---------------------------------------------------------
// CART & PAYMENT (PhonePe Integration)
// ---------------------------------------------------------
let currentCartData = [];
let cartTotalAmount = 0;

async function loadCart() {
    const tbody = document.getElementById('cart-body');
    const totalEl = document.getElementById('cart-total');
    if (!tbody) return;
    const res = await apiCall('/cart/');
    tbody.innerHTML = '';
    cartTotalAmount = 0;
    currentCartData = [];

    if (res.status === 'success') {
        currentCartData = res.data;
        res.data.forEach(c => {
            cartTotalAmount += parseFloat(c.total_price);
            tbody.innerHTML += `<tr>
                <td style="font-weight:600">${c.food_name}</td>
                <td>₹${c.price}</td>
                <td>
                    <div style="display:flex; align-items:center; gap:10px">
                        <button class="btn" style="padding:0.3rem 0.8rem; background:#f0f0f0" onclick="updateCartQuantity(${c.cart_id}, ${c.quantity - 1}, ${c.price})">-</button>
                        <span style="font-weight:600; width:20px; text-align:center">${c.quantity}</span>
                        <button class="btn" style="padding:0.3rem 0.8rem; background:#f0f0f0" onclick="updateCartQuantity(${c.cart_id}, ${c.quantity + 1}, ${c.price})">+</button>
                    </div>
                </td>
                <td style="font-weight:700; color:var(--primary)">₹${c.total_price}</td>
                <td><button class="btn btn-danger" style="padding:0.5rem 1rem" onclick="removeFromCart(${c.cart_id})">Remove</button></td>
            </tr>`;
        });
        totalEl.innerText = `₹${cartTotalAmount.toFixed(2)}`;
    }
}

async function addToCart(food_name, price, quantity) {
    const body = { customer_name: 'Rahul Sharma', food_name: food_name, price: price, quantity: quantity };
    const res = await apiCall('/cart/add/', 'POST', body);
    if (res.status === 'success') {
        showToast(`${food_name} added to cart!`);
    } else {
        showToast('Failed to add to cart');
    }
}

async function updateCartQuantity(cart_id, newQty, price) {
    if (newQty < 1) { removeFromCart(cart_id); return; }
    await apiCall(`/cart/update/${cart_id}/`, 'PUT', { quantity: newQty });
    loadCart();
}

async function removeFromCart(cart_id) {
    await apiCall(`/cart/delete/${cart_id}/`, 'DELETE');
    loadCart();
}

// PhonePe Mock Integration
function initiateCheckout() {
    if (currentCartData.length === 0) {
        showToast('Your cart is empty!');
        return;
    }
    document.getElementById('phonepe-amount').innerText = `₹${cartTotalAmount.toFixed(2)}`;
    document.getElementById('phonepe-modal').style.display = 'flex';
}

function cancelPayment() {
    document.getElementById('phonepe-modal').style.display = 'none';
}

async function processPayment() {
    document.getElementById('qr-section').style.display = 'none';
    document.getElementById('loader-section').style.display = 'block';

    // Simulate API delay for payment gateway
    setTimeout(async () => {
        let items = [];
        currentCartData.forEach(c => items.push(`${c.food_name} (x${c.quantity})`));

        const orderBody = {
            customer_name: 'Rahul Sharma',
            restaurant_name: 'Multiple Restaurants',
            order_items: items.join(', '),
            total_amount: cartTotalAmount,
            payment_status: 'Paid',
            delivery_status: 'Preparing'
        };
        const orderRes = await apiCall('/orders/add/', 'POST', orderBody);

        if (orderRes.status === 'success') {
            // Clear cart
            for (let c of currentCartData) {
                await apiCall(`/cart/delete/${c.cart_id}/`, 'DELETE');
            }
            document.getElementById('phonepe-modal').style.display = 'none';
            showToast('Payment Successful! Order placed.');
            setTimeout(() => window.location.href = 'orders.html', 1500);
        }
    }, 2500);
}

// ---------------------------------------------------------
// ORDERS
// ---------------------------------------------------------
async function loadOrders() {
    const list = document.getElementById('orders-list');
    if (!list) return;
    const res = await apiCall('/orders/');
    list.innerHTML = '';
    if (res.status === 'success') {
        res.data.reverse().forEach(o => { // Show newest first
            list.innerHTML += `<div class="card" style="margin-bottom:20px">
                <div class="card-body">
                    <div style="display:flex; justify-content:space-between;">
                        <h3 style="color:var(--primary)">Order #${o.order_id}</h3>
                        <span class="badge ${o.payment_status === 'Paid' ? 'available' : 'out-of-stock'}">${o.payment_status}</span>
                    </div>
                    <p style="margin-top:10px"><strong>Items:</strong> ${o.order_items}</p>
                    <p><strong>Total Amount:</strong> ₹${o.total_amount}</p>
                    <div class="card-footer">
                        <strong>Status:</strong> 
                        <span style="font-weight:700; color:var(--text-main); margin-left:10px">${o.delivery_status}</span>
                    </div>
                </div>
            </div>`;
        });
    }
}

window.onload = () => {
    if (document.getElementById('register-form')) document.getElementById('register-form').addEventListener('submit', handleRegister);
    loadCustomers();
    loadRestaurants();
    loadMenu();
    loadCart();
    loadOrders();
};
