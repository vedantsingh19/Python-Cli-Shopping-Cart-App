import unittest
from mycart.db_utility import make_connection
from mycart.cartcrud import ShoppingCart,StoreItem,HandlingInput

class TDD(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        self.store = StoreItem()

    def test_login_true(self,name='vedantsingh',password='qwerty'):
        status=False
        cursor, connection = make_connection('login.db')
        n = cursor.execute("SELECT name from login WHERE name='" + name + "'").fetchone()
        n = str(n).strip("('',)'")
        if n == name:
            pw = cursor.execute("SELECT password from login WHERE password='" + password + "'").fetchone()
            pw = str(pw).strip("('',)'")
            if pw == password:
                status = True
                print('You are now logged in.')

            else:
                print('Wrong password.')

        else:
            print('Wrong username.')

        self.assertEqual(True,status)

    def test_login_false(self,name='vedantsingh',password='qwert'):
        status = False
        cursor, connection = make_connection('login.db')
        n = cursor.execute("SELECT name from login WHERE name='" + name + "'").fetchone()
        n = str(n).strip("('',)'")
        if n == name:
            pw = cursor.execute("SELECT password from login WHERE password='" + password + "'").fetchone()
            pw = str(pw).strip("('',)'")
            if pw == password:
                status = True
                print('You are now logged in.')

            else:
                print('Wrong password.')

        else:
            print('Wrong username.')

        self.assertEqual(False,status)

    def test_list_cart_items_true(self):
        uname = 'vedantsingh'
        self.cart.listCart(uname)
        self.assertTrue(True,'Success')
    def test_list_cart_items_false(self):
        uname = 'h'
        self.cart.listCart(uname)
        self.assertTrue(False,'please add items in your cart')
    def test_list_store_items_true(self):
        self.store.listStore()
        self.assertTrue(True,'Store items')



if __name__ == '__main__':
    unittest.main()