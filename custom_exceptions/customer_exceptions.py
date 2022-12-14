
class InvalidCustomerIDException(Exception):
    """InvalidCustomerIDException is derived class of Exception base class"""
    pass


class InvalidNameException(Exception):
    """InvalidNameException is derived class of Exception base class"""
    pass


class InvalidPhoneNumberFormat(Exception):
    """InvalidPhoneNumberFormat is derived class of Exception base class"""
    pass


class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        customer_id_range = range(1000, 9999, 1)
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        if not (customer_id_characters.issuperset(cid) and customer_id_range.__contains__(int(cid))):
            raise InvalidCustomerIDException
        if not (phone_number_characters.issuperset(pnumber)):
            raise InvalidPhoneNumberFormat

        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_characters.issuperset(name):
            raise InvalidNameException
        self.last_name = name

    def change_first_name(self, name):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_characters.issuperset(name):
            raise InvalidNameException
        self.first_name = name

    def change_phone_number(self, number):
        phone_number_characters = set("1234567890-()")
        if not (phone_number_characters.issuperset(number)):
            raise InvalidPhoneNumberFormat
        self.phone_number = number


#Driver code
# Valid customer
customer_one = Customer('2999', 'Duck', 'Donald', '(515)555-5555') # all required
print(str(customer_one))

# Invalid phone
try:
    customer_two = Customer('3000', 'Duck', 'Donald', '(515)555-5555P') # all required
except InvalidPhoneNumberFormat:
    print("Invalid Phone Number, customer not created")

# Invalid customer_id
try:
    customer_two = Customer('ABC', 'Duck', 'Donald', '(515)555-5555') # all required
except InvalidCustomerIDException:
    print("Invalid Customer ID, customer not created")

# Invalid first_name
try:
    customer_two = Customer('3000', 'Duck', '2', '(515)555-5555') # all required
except InvalidNameException:
    print("Invalid Name, customer not created")

# Invalid last_name
try:
    customer_two = Customer('3000', '123', 'Donald', '(515)555-5555') # all required
except InvalidNameException:
    print("Invalid Name, customer not created")



