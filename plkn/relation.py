from flask import session
from models import *

def Create_Relation(new_name):
    try:
        new_relation = Relations.select().where(Relations.name==new_name).get()
    except Relations.DoesNotExist:
        new_relation = Relations.create(name = new_name,
                                created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False