from django.urls import path

from . import views


urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('schedule_service/', views.schedule_service, name="schedule_service"),
	path('mechanic_page/', views.mechanic_page, name="mechanic_page"),
	path('mechanic_profile/', views.mechanic_profile, name="mechanic_profile"),
	path('contact/', views.contact, name="contact"),
	path('requests/', views.requests, name="requests"),

	path('blog/', views.blog, name='blog'),
    path('newPost/', views.newPost, name='newpost'),
    path('myPost/', views.myPost, name='mypost'),
    path('mechanic_home/', views.mechanic_home, name='mechanic_home'),
    path('confiramtion/', views.confiramtion, name="confiramtion"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
	

	
]