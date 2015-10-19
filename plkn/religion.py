from flask import session
from models import *

def Create_Religion(new_name):
    try:
        new_religion = Religions.select().where(Religions.name==new_name).get()
    except Religions.DoesNotExist:
        new_religion = Religions.create(name = new_name,
                                        created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False