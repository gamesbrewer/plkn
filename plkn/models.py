import peewee
import datetime

database = peewee.MySQLDatabase("plkn", host="localhost", user="root", passwd="p4ssw0rd")

#---  Databases   ---------------------------------------------------------------

class Users(peewee.Model):
    email = peewee.CharField()
    password = peewee.CharField()
    full_name = peewee.CharField()
    phone_no = peewee.CharField()
    level = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Races(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Companies(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Religions(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Educations(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Relations(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class BloodGroups(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class ShirtSizes(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class PantSizes(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class ShoeSizes(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class BeretSizes(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class FreeSizes(peewee.Model):
    name = peewee.CharField()
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Trainees(peewee.Model):
    #trainee details
    camp = peewee.CharField(null=True) #system column
    name = peewee.CharField(null=True)
    ic_no = peewee.CharField(null=False)
    company = peewee.ForeignKeyField(Companies, null=True)
    index_no = peewee.CharField(null=True)
    blok_no = peewee.CharField(null=True)
    room_no = peewee.CharField(null=True)
    bed_no = peewee.CharField(null=True)
    gender = peewee.CharField(null=True)
    race = peewee.ForeignKeyField(Races, null=True)
    religion = peewee.ForeignKeyField(Religions, null=True)
    age = peewee.CharField(null=True)
    phone1 = peewee.CharField(null=True)
    phone2 = peewee.CharField(null=True)
    #address
    address1 = peewee.CharField(null=True)
    address2 = peewee.CharField(null=True)
    address3 = peewee.CharField(null=True)
    postcode = peewee.CharField(null=True)
    city = peewee.CharField(null=True)
    state = peewee.CharField(null=True)
    #training info
    is_married = peewee.BooleanField(null=True)
    education = peewee.ForeignKeyField(Educations, null=True)
    occupation = peewee.CharField(null=True)
    bsn_account_no = peewee.CharField(null=True)
    is_shooter = peewee.BooleanField(null=True)
    is_left_handed = peewee.BooleanField(null=True)
    is_registered = peewee.BooleanField(null=True)
    report_in_date = peewee.DateTimeField(null=True)
    #next of kin
    kin_name = peewee.CharField(null=True)
    relation = peewee.ForeignKeyField(Relations, null=True)
    kin_address = peewee.TextField(null=True)
    kin_phone = peewee.CharField(null=True)
    kin_occupation = peewee.CharField(null=True)
    #---------------------   Health   ----------------------------------------------
    #health info
    blood_group = peewee.ForeignKeyField(BloodGroups, null=True)
    height = peewee.CharField(null=True)
    weight = peewee.CharField(null=True)
    bmi = peewee.CharField(null=True)
    is_allergic = peewee.BooleanField(null=True)
    allergies = peewee.CharField(null=True)
    is_food_intolerant = peewee.BooleanField(null=True)
    food_intolerance = peewee.CharField(null=True)
    reference_no = peewee.CharField(null=True)
    is_declared = peewee.BooleanField(null=True)
    medicine_journal = peewee.TextField(null=True)
    #---------------------   Logistics   ----------------------------------------------
    #logistic info
    shirt_class_male = peewee.CharField(null=True)
    shirt_class_female = peewee.CharField(null=True)
    shirt_sport_male = peewee.CharField(null=True)
    shirt_sport_female = peewee.CharField(null=True)
    inner_male = peewee.CharField(null=True)
    inner_female = peewee.CharField(null=True)
    shoe_class_male = peewee.CharField(null=True)
    shoe_class_female = peewee.CharField(null=True)
    shirt_celoreng = peewee.CharField(null=True)
    track_bottom_black = peewee.CharField(null=True)
    shoe_sport = peewee.CharField(null=True)
    pants_celoreng = peewee.CharField(null=True)
    pants_class = peewee.CharField(null=True)
    shoe_spike = peewee.CharField(null=True)
    beret = peewee.CharField(null=True)
    #others
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class LastIndex(peewee.Model):
    camp = peewee.CharField(null=True) #system column
    male = peewee.IntegerField()
    female = peewee.IntegerField()

    class Meta:
        database = database

class GroupPlacement(peewee.Model):
    camp = peewee.CharField(null=True) #system column
    race = peewee.ForeignKeyField(Races, null=True)
    alpha = peewee.IntegerField(null=True)
    bravo = peewee.IntegerField(null=True)
    charlie = peewee.IntegerField(null=True)

    class Meta:
        database = database

class Dormitory(peewee.Model):
    camp = peewee.CharField(null=True) #system column
    room_no = peewee.CharField(null=True)
    occupancy = peewee.IntegerField(null=True)

    class Meta:
        database = database

class LastPrintCount(peewee.Model):
    camp = peewee.CharField(null=True) #system column
    no = peewee.IntegerField()

    class Meta:
        database = database

class Admittances(peewee.Model):
    #camp = peewee.CharField(null=True) #system column
    trainee = peewee.ForeignKeyField(Trainees, null=True)
    details = peewee.TextField(null=True)
    diagnosis = peewee.TextField(null=True)
    blood_pressure = peewee.CharField(null=True)
    temperature = peewee.CharField(null=True)
    pulse = peewee.CharField(null=True)
    respiration = peewee.CharField(null=True)
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = database

class InventoryCategories(peewee.Model):
    name = peewee.CharField(null=False)
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class Inventories(peewee.Model):
    item = peewee.CharField(null=False)
    category = peewee.ForeignKeyField(InventoryCategories, null=True)
    code = peewee.CharField(null=True)
    unit_price = peewee.DecimalField(null=True)
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = database

class Orders(peewee.Model):
    unit_from = peewee.CharField(null=True)
    unit_to = peewee.CharField(null=True)
    order_no = peewee.CharField(null=True)
    checkout_no = peewee.CharField(null=True)
    order_required_date = peewee.DateTimeField(null=True, default=datetime.datetime.now)
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

class OrderItems(peewee.Model):
    order = peewee.ForeignKeyField(Orders, null=False)
    inventory = peewee.ForeignKeyField(Inventories, null=False)
    quantity_ordered = peewee.IntegerField(null=True)
    quantity_approved = peewee.IntegerField(null=True)
    quantity_taken = peewee.IntegerField(null=True)
    unit_price = peewee.DecimalField(null=True)
    full_price = peewee.DecimalField(null=True)
    notes = peewee.TextField(null=True)
    is_deleted = peewee.BooleanField(default=False)
    created_by = peewee.ForeignKeyField(Users)
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = database
#------------ Database Creation & Initialization ---------------------------------------

if __name__ == "__main__":
    try:
        Users.create_table()
        Users.create(email = "admin@admin.com",
                     password = "password",
                     full_name = "administrator",
                     phone_no = "0123456789",
                     level = "1")
    except peewee.OperationalError:
        print "Users table already exists!"
   
    try:
        Races.create_table()
    except peewee.OperationalError:
        print "Races table already exists!"

    try:
        Companies.create_table()
    except peewee.OperationalError:
        print "Companies table already exists!"
    
    try:
        Religions.create_table()
    except peewee.OperationalError:
        print "Religions table already exists!"
  
    try:
        Educations.create_table()
    except peewee.OperationalError:
        print "Educations table already exists!"

    try:
        Relations.create_table()
    except peewee.OperationalError:
        print "Relations table already exists!"

    try:
        BloodGroups.create_table()
    except peewee.OperationalError:
        print "BloodGroups table already exists!"

    try:
        ShirtSizes.create_table()
    except peewee.OperationalError:
        print "ShirtSizes table already exists!"

    try:
        PantSizes.create_table()
    except peewee.OperationalError:
        print "PantSizes table already exists!"

    try:
        ShoeSizes.create_table()
    except peewee.OperationalError:
        print "ShoeSizes table already exists!"

    try:
        BeretSizes.create_table()
    except peewee.OperationalError:
        print "BeretSizes table already exists!"

    try:
        FreeSizes.create_table()
    except peewee.OperationalError:
        print "FreeSizes table already exists!"

########################################################################################################

    try:
        Trainees.create_table()
        print "Trainees table created"
    except peewee.OperationalError:
        print "Trainees table already exists!"

    try:
        LastIndex.create_table()
        new_index = LastIndex.create(camp="SW", no = 1)
        new_index = LastIndex.create(camp="SR", no = 1)
        new_index = LastIndex.create(camp="JP", no = 1)
        new_index = LastIndex.create(camp="BM", no = 1)
        new_index = LastIndex.create(camp="BS", no = 1)
        print "LastIndex table created"
    except peewee.OperationalError:
        print "LastIndex table already exists!"
        
    try:
        LastPrintCount.create_table()
        new_print = LastPrintCount.create(camp="SW", no = 0)
        new_print = LastPrintCount.create(camp="SR", no = 0)
        new_print = LastPrintCount.create(camp="JP", no = 0)
        new_print = LastPrintCount.create(camp="BM", no = 0)
        new_print = LastPrintCount.create(camp="BS", no = 0)
        print "LastPrintCount table created"
    except peewee.OperationalError:
        print "LastPrintCount table already exists!"

    try:
        GroupPlacement.create_table()
        new_races = Races.select()
        for looped_race in new_races:
            GroupPlacement.create(camp="SW", race=looped_race, alpha=0, bravo=0, charlie=0)
            GroupPlacement.create(camp="SR", race=looped_race, alpha=0, bravo=0, charlie=0)
            GroupPlacement.create(camp="JP", race=looped_race, alpha=0, bravo=0, charlie=0)
            GroupPlacement.create(camp="BM", race=looped_race, alpha=0, bravo=0, charlie=0)
            GroupPlacement.create(camp="BS", race=looped_race, alpha=0, bravo=0, charlie=0)
        print "GroupPlacement table created"
    except peewee.OperationalError:
        print "GroupPlacement table already exists!"
        
    try:
        Dormitory.create_table()
        for x in range(1, 9):
            Dormitory.create(camp="SW", room_no="BL" + str(x), occupancy=0)
            Dormitory.create(camp="SW", room_no="BP" + str(x), occupancy=0)
            Dormitory.create(camp="BM", room_no="BL" + str(x), occupancy=0)
            Dormitory.create(camp="BM", room_no="BP" + str(x), occupancy=0)
            Dormitory.create(camp="JP", room_no="BLOK " + str(x), occupancy=0)
            Dormitory.create(camp="JP", room_no="BLOK " + str(x) + "P", occupancy=0)
        for x in range(1, 13):
            Dormitory.create(camp="BS", room_no="WA" + str(x), occupancy=0)
            Dormitory.create(camp="BS", room_no="WA" + str(x), occupancy=0)
        for x in range(1, 9):    
            Dormitory.create(camp="SR", room_no="L" + str(x) + "A", occupancy=0)
            Dormitory.create(camp="SR", room_no="L" + str(x) + "B", occupancy=0)
            Dormitory.create(camp="SR", room_no="P" + str(x) + "A", occupancy=0)
            Dormitory.create(camp="SR", room_no="P" + str(x) + "B", occupancy=0)
        print "Dormitory table created"
    except peewee.OperationalError:
        print "Dormitory table already exists!"
########################################################################################################
    try:
        Admittances.create_table()
    except peewee.OperationalError:
        print "Admittances table already exists!"
        
    try:
        InventoryCategories.create_table()
    except peewee.OperationalError:
        print "InventoryCategories table already exists!"

    try:
        Inventories.create_table()
    except peewee.OperationalError:
        print "Inventories table already exists!"
    
    try:
        Orders.create_table()
    except peewee.OperationalError:
        print "Orders table already exists!"
    
    try:
        OrderItems.create_table()
    except peewee.OperationalError:
        print "OrderItems table already exists!"