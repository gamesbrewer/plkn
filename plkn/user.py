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

def camp_to_routes(camp):
    switcher = {
        "ALL": ".Allboard",
        "SW": ".Dashboard",
        "SR": ".Dashboard",
        "JP": ".Dashboard",
        "BM": ".Dashboard",
        "BS": ".Dashboard",
    }
    return switcher.get(camp, "")

def camp_full_name(camp):
    switcher = {
        "ALL": "ALL",
        "SW": "SIMILAJAU",
        "SR": "SUNGAI RAIT",
        "JP": "JUNACO PARK",
        "BM": "BUMIMAS",
        "BS": "BUKIT SABAN",
    }
    return switcher.get(camp, "")

def Log_User_In(email, camp): # goes to dashboard page
    user = Users.select().where(Users.email==email).get()
    session['email'] = email
    session['camp'] = camp
    session['campname'] = camp_full_name(camp)
    session['username'] = user.full_name
    session['level'] = user.level

    return camp_to_routes(camp)
    #return '.Dashboard'