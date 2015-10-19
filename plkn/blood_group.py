from flask import session
from models import *

def Create_Blood_Group(new_name):
    try:
        new_blood_group = BloodGroups.select().where(BloodGroups.name==new_name).get()
    except BloodGroups.DoesNotExist:
        new_blood_group = BloodGroups.create(name = new_name,
                                             created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False