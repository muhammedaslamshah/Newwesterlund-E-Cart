from django.shortcuts import render,redirect

#User model
from django.contrib.auth.models import User

# Messages 
from django.contrib import messages

#Customer model
from . models import Customer

# Create your views here.
def show_account(request):

    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # Create user objects to user account
            user = User.objects.create(
                username=username,
                password=password,
                email=email
            )
            # Create Customer object to Customer account (Customer Profile)
            customer = Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message="Sucessfully registred sussessfully"
            messages.success(request,success_message)
            # return redirect('home')
        except Exception as e: 
            error_message="username already exists or invalid credentials"
            # to render the message to template
            messages.error(request,error_message)
    return render(request,'account.html')