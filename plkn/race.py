from flask import session
from models import *

def Create_Race(new_name):
    try:
        new_race = Races.select().where(Races.name==new_name).get()
    except Races.DoesNotExist:
        new_race = Races.create(name = new_name,
                                created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False