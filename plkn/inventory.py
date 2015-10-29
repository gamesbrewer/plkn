from flask import session
from models import *

def Create_Inventory_Category(new_name):
    try:
        new_category = InventoryCategories.select().where(InventoryCategories.name==new_name).get()
    except InventoryCategories.DoesNotExist:
        new_category = InventoryCategories.create(name = new_name,
                                created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False



def Create_Inventory(new_item, new_category_id, new_code, new_unit_price):
    try:
        new_inventory = Inventories.select().where(Inventories.item==new_item).get()
    except Inventories.DoesNotExist:
        new_inventory = Inventories.create(item = new_item,
                                           category = InventoryCategories.select().where(InventoryCategories.id==new_category_id).get(),
                                           code = new_code,
                                           unit_price = new_unit_price,
                                           created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False