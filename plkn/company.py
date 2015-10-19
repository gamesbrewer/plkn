from flask import session
from models import *

def Create_Company(new_name):
    try:
        new_company = Companies.select().where(Companies.name==new_name).get()
    except Companies.DoesNotExist:
        new_company = Companies.create(name = new_name,
                                       created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False