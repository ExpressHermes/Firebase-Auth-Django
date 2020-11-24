import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyChADR3W98xLnX8tQc4Sl4a1qvRJZJa8Co",
    "authDomain": "django-auth-179cc.firebaseapp.com",
    "databaseURL": "https://django-auth-179cc.firebaseio.com",
    "projectId": "django-auth-179cc",
    "storageBucket": "django-auth-179cc.appspot.com",
    "messagingSenderId": "693986128290",
    "appId": "1:693986128290:web:3659590c844f6a667e82fb"
  }

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)