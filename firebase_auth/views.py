from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib import messages
import pyrebase
from .pyrebase_settings import firebase

from pprint import pprint as pp

auth = firebase.auth()
db = firebase.database()

# Create your views here.
def profile(request):
    pp(dict(request.session))
    try:
        user_id = dict(request.session)['token_id']
        response = db.child("users").get(user_id).val()
        for item in response.items():
            user_info = list(item)
        user = user_info[1]
    except Exception as e:
        pp(e)
        messages.info(request, "You need to login to view this page")
        return redirect('firebase_auth:signin')
    
    if request.method == "POST":
        form = request.POST
        place_of_birth = form.get('place_of_birth')
        user['place_of_birth'] = place_of_birth
        try:
            # Pass the user's idToken to the push method
            db.child("users").child(user_info[0]).update(user)
        except Exception as e:
            pp(e)
            pass
    return render(request, 'auth/profile.html', {'user': user})

def signup(request, *args, **kwargs):
    if request.method == "POST":
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        password = form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            # add user to db
            data = {
                "name": name, 
                "email": email,
                "place_of_birth": None,
                "status": 1
            }
            # Pass the user's idToken to the push method
            results = db.child("users").push(data, user['idToken'])
            messages.success(request, 'Signed up successfully! Signin now')
            return redirect('firebase_auth:signin')
        except Exception as e:
            pp(e)
            messages.error(request, 'Signup Failed')
    return render(request, 'auth/signup.html')

def signin(request, *args, **kwargs):
    if request.method == "POST":
        form = request.POST
        email = form.get('email')
        password = form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            pp(dict(request.session))
            request.session['token_id'] = str(user['idToken'])
            pp(dict(request.session))
            messages.success(request, 'Signed In!')
            return redirect('firebase_auth:profile')
        except Exception as e:
            pp(e)
            messages.error(request, 'Signin Failed')
    return render(request, 'auth/signin.html')

def logout_view(request):
    try:
        pp(dict(request.session))
        del request.session['token_id']
        pp(dict(request.session))
        messages.success(request, "Logged out successfully")
    except Exception as e:
        pp(dict(request.session))
        print(e)
        messages.error(request, "Logout Failed")
        return redirect('firebase_auth:profile')
    return redirect('firebase_auth:signin')
