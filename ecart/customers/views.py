from django.shortcuts import render,redirect

#User model
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

# Messages 
from django.contrib import messages

# Customer model
from . models import Customer

# Logout function but the keyword Sign_out is used to Exceptions Handling
def sign_out(request):
    logout(request)
    return redirect('home')

# Create your views here.
def show_account(request):
    # commen dictionary
    context={}

    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # Create user objects to user account
            user = User.objects.create_user( #for user password stored encrypted data (Hashing algorithms can be used to authenticate data )
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
            error_message="username already exists or invalid inputs"
            # to render the message to template
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username=request.POST.get('username')
        password=request.POST.get('password')
        # check user exciting
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credentials')

    return render(request,'account.html',context)