from flask import session
from models import *

def Create_Education(new_name):
    try:
        new_education = Educations.select().where(Educations.name==new_name).get()
    except Educations.DoesNotExist:
        new_education = Educations.create(name = new_name,
                                     created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False