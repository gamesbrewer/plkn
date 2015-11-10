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

def category_to_checkout_no(category_id):
    switcher = {
        "1": "CIV/SIMI/PN/______/______",
        "3": "CIV/SIMI/AT/______/______",
        "4": "CIV/SIMI/SUKAN/______/______",
    }
    return switcher.get(category_id, "")

def Create_Order(new_unit_from, new_unit_to, new_order_no, new_order_required_date, new_category_id):
    try:
        new_order = Orders.select().where(Orders.order_no==new_order_no).get()
    except Orders.DoesNotExist:
        new_checkout_no = category_to_checkout_no(new_category_id)

        new_order = Orders.create(order_no = new_order_no,
                                  unit_from = new_unit_from,
                                  unit_to = new_unit_to,
                                  order_required_date = "" if new_order_required_date == "" else datetime.datetime.now,
                                  checkout_no = new_checkout_no,
                                  created_by = Users.select().where(Users.email==session['email']).get())

        #after create order, create order items
        inventories = Inventories.select().where(Inventories.category==new_category_id)
        for item in inventories:
            OrderItems.create(order = new_order, 
                              inventory=item, 
                              quantity_ordered = 0, 
                              quantity_approved = 0, 
                              quantity_taken = 0, 
                              unit_price = item.unit_price, 
                              full_price = 0, 
                              notes = "",
                              created_by = Users.select().where(Users.email==session['email']).get())
        return True
    else:
        return False