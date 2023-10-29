from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    users = User.objects.all()
    query=""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            User.objects.create(
                name=name,
                username=username,
                email=email
            )
            messages.success(request, "Successfully Added User...")

        elif "update" in request.POST:
            id = request.POST.get("id")   
            name = request.POST.get("name")   
            username = request.POST.get("username")   
            email = request.POST.get("email")

            update_user = User.objects.get(id=id)
            update_user.name = name   
            update_user.username = username   
            update_user.email = email
            update_user.save()
            
            messages.success(request, "User Information Updated Successfully....")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            User.objects.get(id=id).delete()

            messages.success(request, "Successfully Deleted....")


        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            users = User.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(username__icontains=query))          

    context = {"Users": users, "query": query}
    return render(request, "index.html", context=context)
