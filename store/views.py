from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from django.contrib.auth.models import User


# Create your views here.



def home(request):
    
    context = {}
    return render(request, 'home.html', context)



def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
        cartItems = order['get_cart_item']

    products = Product.objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store.html', context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
        cartItems = order['get_cart_item']   
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
        cartItems = order['get_cart_item']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)




def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)





def schedule_service(request):
    
    context = {}
    return render(request, 'schedule_service.html', context)


def mechanic_page(request):
    
    context = {}
    return render(request, 'mechanic_page.html', context)

def mechanic_profile(request):
    
    context = {}
    return render(request, 'mechanic_profile.html', context)



def contact(request):
    
    if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            user_message = request.POST.get("user_message")
            contact = Message(name=name, email=email, subject=subject, user_message=user_message)
            contact.save()
    
    return render(request,"contact.html" )



def requests(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        b_model = request.POST.get('b_model')
        b_reg_no = request.POST.get('b_reg_no')
        s_type = request.POST.get('s_type')
        desc = request.POST.get('desc')
        request = Request(name=name, address=address, contact=contact, b_model=b_model, b_reg_no=b_reg_no, s_type=s_type, desc=desc)
        request.save()         
    return render(request,"requests.html")



def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog.html', context)



def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/blog')
    
    return render(request, 'newpost.html')



def confiramtion(request):
    
    context = {}
    return render(request, 'confiramtion.html', context)




def myPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'mypost.html', context)


def mechanic_home(request):
   
    get_data = Request.objects.all()
    context = {'get_data': get_data}
    return render(request, 'mechanic_home.html', context)


# products = Product.objects.all()
# context = {'products': products, 'cartItems':cartItems}


def login(request):
    
    context = {}
    return render(request, 'login.html', context)



def signup(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        upassword=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        my_user = User.objects.create_user(uname, email, upassword)
        my_user.save()

    context = {}
    return render(request, 'signup.html', context)
