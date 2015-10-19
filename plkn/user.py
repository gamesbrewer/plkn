from flask import session
from models import *

def Register(new_full_name, new_email, new_password, new_phone_no):
    try:
        new_user = Users.select().where(Users.email==new_email).get()
    except Users.DoesNotExist:
        new_user = Users.create(email = new_email,
                                password = new_password,
                                full_name = new_full_name,
                                phone_no = new_phone_no,
                                level = "3")
        return True
    else:
        return False

def Authenticate(check_email, check_password):
    try:
        user = Users.select().where(Users.email==check_email).get()
    except Users.DoesNotExist:
        return False
    else:
        if user.password == check_password:
            return True
        else:
            return False

def Log_User_In(email): # goes to dashboard page
    user = Users.select().where(Users.email==email).get()
    session['email'] = email
    session['username'] = user.full_name
    session['level'] = user.level
    return '.Dashboard'