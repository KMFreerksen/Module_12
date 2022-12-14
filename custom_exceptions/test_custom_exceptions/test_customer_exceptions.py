import unittest
from custom_exceptions import customer_exceptions as c

class TestExceptions (unittest.TestCase):
    def setUp(self):
        self.Customer1 = c.Customer('9001', 'Freerksen', 'Katie', '(515)776-0262')

    def tearDown(self):
        del self.Customer1

    def testValidID(self):
        self.assertEqual(self.Customer1.customer_id,'9001')

    def testValidLastName(self):
        self.assertEqual(self.Customer1.last_name, 'Freerksen')

    def testValidFirstName(self):
        self.assertEqual(self.Customer1.first_name, 'Katie')

    def testValidPhoneNumber(self):
        self.assertEqual(self.Customer1.phone_number, '(515)776-0262')

    def testInvalidCustomerID(self):
        with self.assertRaises(c.InvalidCustomerIDException):
            Customer2 = c.Customer('abc', 'Smith', 'Joe', '(515)864-3210')

    def testInvalidLastName(self):
        with self.assertRaises(c.InvalidNameException):
            Customer2 = c.Customer('1500', '123', 'Joe', '(515)864-3210')

    def testInvalidFirstName(self):
        with self.assertRaises(c.InvalidNameException):
            Customer2 = c.Customer('1500', 'Smith', '123', '(515)864-3210')

    def testInvalidPhone(self):
        with self.assertRaises(c.InvalidPhoneNumberFormat):
            Customer2 = c.Customer('1500', 'Smith', 'Joe', 'nada')

    def testString(self):
        self.assertEqual(str(self.Customer1), '9001: Freerksen, Katie Phone: (515)776-0262')
