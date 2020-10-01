
from mycart.login import user_login,user_registration
from mycart.db_utility import make_connection
import sqlite3
from datetime import datetime
done = False


class ShoppingCart:
    def __init__(self):
        self.items = []

    def userCartDetails(self):
        cursor, connection = make_connection('MYCARTS.db')
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS MYCARTS (id INTEGER ,itemName TEXT ,price INTEGER ,quantity INTEGER,username TEXT,status TEXT )")
        connection.commit()

        try:

            status_temp = False
            list_item = []
            while (status_temp == False):
                input_type = input("Type S/s to view cart of user or ALL/all to view all user carts or X to exit.")
                if input_type.isdigit():
                    print('Wrong Input')
                else:

                    if input_type.upper() == 'S':
                        input_var = input('Please enter customer user name')
                        if input_var.isdigit():
                            print('Please enter valid customer user name')
                        else:

                            cursor,connection = make_connection('MYCARTS.db')
                            connection.commit()
                            records = cursor.execute("SELECT * from MYCARTS WHERE username='" + input_var + "'").fetchall()


                    if input_type.upper() == 'ALL':

                        cursor,connection = make_connection('MYCARTS.db')
                        records=cursor.execute('SELECT * FROM MYCARTS').fetchall()
                        connection.commit()
                    connection.close()
                    if len(records) > 0:

                        print('ItemId', end='   ')
                        print('Item', end='  ')
                        print('Price', end='  ')
                        print('Quantity', end='  ')
                        print('UserName', end='  ')
                        print('Status', end='  ')
                        print('\n')

                        for each_det in records:
                            print(each_det[0], end='  ')
                            print(each_det[1], end='  ')
                            print(each_det[2], end='  ')
                            print(each_det[3], end='  ')
                            print(each_det[4], end='  ')
                            print(each_det[5], end='  ')
                            print('\n')
                    else:
                        print('No items found.')

                    if input_type.upper() == 'X':
                        status_temp = True





        except IOError:
            pass
        finally:
            connection.close()








    def addToCart(self, item,uname,quantity):


        try:
            cursor, connection = make_connection('MYCARTS.db')
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS MYCARTS (id INTEGER ,itemName TEXT ,price INTEGER ,quantity INTEGER,username TEXT,status TEXT )")
            connection.commit()

            if item and uname:
                status='shipped'
                cursor.execute('INSERT INTO MYCARTS VALUES(?,?,?,?,?,?)',
                               (item[0], item[2], item[3],quantity, uname,status))
                connection.commit()
                connection.close()
                print('Added to cart')


                # connection.close()


        except:
            import traceback
            traceback.print_exc()
        finally:
            connection.close()



    def removeFromCart(self,uname):
        try:
            print('Your Cart Item')
            flag=cart1.listCart(uname)
            if flag:

                input_var = input("Please enter ItemId to remove")
                quantity_removed = input('Please enter quantity')

                if quantity_removed.isalpha():
                    print('Wrong Input')

                if not input_var:
                    print('Wrong input')

                else:
                    cursor,connection = make_connection('MYCARTS.db')
                    status = 'shipped'
                    records=cursor.execute("SELECT * from MYCARTS WHERE username='" + uname + "' AND id='" + str(input_var) + "' AND status='" + status + "'").fetchone()
                    if records:
                        print('You can only removed shipped item from cart')
                        db_quantity = records[3]

                        if int(quantity_removed)<db_quantity:

                            fquantity = db_quantity-int(quantity_removed)
                        if int(quantity_removed)>db_quantity:
                            print('Please enter valid quantity')

                        if int(quantity_removed)==db_quantity:
                            sql = "DELETE from  MYCARTS  WHERE username='" + uname + "' AND id='" + str(
                                input_var) + "' AND status='" + status + "'"
                            cursor.execute(sql)
                            connection.commit()
                        if quantity_removed<db_quantity:
                            sql = "UPDATE   MYCARTS set quantity='"+str(fquantity)+"'  WHERE username='" + uname + "' AND id='" + str(
                                input_var) + "' AND status='" + status + "'"
                            cursor.execute(sql)
                            connection.commit()


                    connection.close()
                    # connection.close()
                    print('Available item in cart')
                    flag=cart1.listCart(uname)





        except:
            import traceback
            traceback.print_exc()
        finally:
           connection.close()



    def saveInvoice(self,uname,final_amount,inv_date):
        try:
            cursor, connection = make_connection('INVOICE_DETAILS.db')
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS INVOICE_DETAILS (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT ,amount INTEGER ,invoicedDate TEXT)")
            connection.commit()
            cursor.execute('INSERT INTO INVOICE_DETAILS VALUES(?,?,?,?)',
                           (None,uname,final_amount,inv_date))
            connection.commit()
            connection.close()
            print('Order Placed')

        except:
            import traceback
            traceback.print_exc()
        finally:
            connection.close()

    def show_saved_invoice(self):
        try:
            cursor, connection = make_connection('INVOICE_DETAILS.db')
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS INVOICE_DETAILS (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT ,amount INTEGER ,invoicedDate TEXT)")
            connection.commit()
            input_var = input("Please enter customer name to view invoice details or type ALL/all to view all invoices")

            if input_var.isdigit():
                print('Wrong input')
            else:

                cursor,connection = make_connection('INVOICE_DETAILS.db')

                if input_var.upper()=='ALL':

                   records =  cursor.execute('select * from INVOICE_DETAILS').fetchall()
                   connection.commit()
                else:
                    records = cursor.execute("SELECT * from INVOICE_DETAILS WHERE name='" + input_var + "'").fetchall()
                    connection.commit()

                if len(records) > 0:
                    print('InvoiceId', end='   ')
                    print('Customer Name', end='   ')
                    print('Amount', end='  ')
                    print('Invoice Date', end='  ')
                    print('\n')
                    for each_det in records:
                        print(each_det[0], end='  ')
                        print(each_det[1], end='  ')
                        print(each_det[2], end='  ')
                        print(each_det[3], end='  ')
                        print('\n')

                else:
                    print('No Invoice found')
                connection.close()
        except:
            import traceback
            traceback.print_exc()
        finally:
            connection.close()

    def priceCart(self,uname):
        try:
            cursor,connection = make_connection('MYCARTS.db')
            status = 'shipped'

            records = cursor.execute("SELECT * from MYCARTS WHERE username='" + uname + "' AND status='" + status + "'").fetchall()
            connection.commit()
            # connection.close()

            price = 0
            if len(records)>0:
                inv_date = str(datetime.now())[:10]
                discount = 0
                print('***************** INVOICE *****************')
                print('                    ' +'Invoice Date:'+ inv_date)
                print('Invoice name:'+ ' '+uname)
                print('********************************************')
                print('Item', end='   ')
                print('Quantity', end='   ')
                print('Price', end='  ')
                for each_records in records:
                    price = price+(each_records[2]*each_records[3])
                    print(each_records[1] + ' '+ str(each_records[3]) + ' '+str(each_records[2]) )
                if price>10000:
                    discount = 500
                    print("Discount Applied in Rupee",discount)
                    final_amount = price-500
                else:
                    print("Discount Apllied in Rupee", discount)
                    final_amount = price
                print('Total amount to be paid in Rupee',final_amount)
                print('***************** END *****************')

                input_var = input("Please type 1 to place order")

                if input_var=='1':
                    ent_amount = input("Please enter amount")
                    if ent_amount.isalpha():
                        print('Wrong Input')
                    else:


                        if final_amount==int(ent_amount):

                            for each_records in records:
                                sql = "UPDATE MYCARTS set status='delivered'  WHERE username='" + uname + "' AND id='" + str(each_records[0]) + "'"
                                cursor.execute(sql)
                                connection.commit()
                            connection.close()

                            cart1.saveInvoice(uname,final_amount,inv_date)
                        else:
                            print('Please enter exact  amount')
                else:
                    print('Wrong input')
            else:
                print('No item found')

        except:
            import traceback
            traceback.print_exc()
        finally:
            connection.close()






    def listCart(self,uname):
        try:
            flag = False
            cursor, connection = make_connection('MYCARTS.db')
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS MYCARTS (id INTEGER ,itemName TEXT ,price INTEGER ,quantity INTEGER,username TEXT,status TEXT )")
            connection.commit()

            cursor, connection = make_connection('MYCARTS.db')

            records = cursor.execute("SELECT * from MYCARTS WHERE username='" + uname + "'").fetchall()
            connection.commit()

            if len(records) > 0:
                flag=True
                print('ItemId', end='   ')
                print('Item', end='  ')
                print('Price', end='  ')
                print('Quantity', end='  ')
                print('Name',end='  ')
                print('Staus',end='  ')
                print('\n')

                for each_det in records:
                    print(each_det[0], end='  ')
                    print(each_det[1], end='  ')
                    print(each_det[2], end='  ')
                    print(each_det[3], end='  ')
                    print(each_det[4], end='  ')
                    print(each_det[5], end='  ')
                    print('\n')
            else:
                print('Your cart is empty please add items in cart')
            return flag

        except:
            import traceback
            traceback.print_exc()
        finally:
            connection.close()

class HandlingInput:
    def __init__(self):
        pass

    def printInstructions(self):
        print("Type A/a to add items in your cart ")
        print("Type C/c to view your cart items")
        print("Type R/r to remove item from your cart")
        print("Type P/p to get the total cart price")
        print('Type L/l to get available item')
        print("Type X/x to exit")

    def printInstructionsAdmin(self):
        print("Type A to add items in store")
        print("Type L to view your store items")
        print("Type I to view Invoices")
        print("Type C to view User Carts Details")
        print("Type X to exit")

    def handleInputAdmin(self,in_var, cart, uname):

        if (in_var.upper() == "A"):
            store_obj.CreateStore()
        if (in_var.upper() == "L"):
           flag= store_obj.listStore()
        if (in_var.upper() == "I"):
            cart.show_saved_invoice()
        if (in_var.upper() == "C"):
            cart.userCartDetails()
        if (in_var.upper() == "X"):
            global done
            done = True

    def handleInput(self,in_var, cart, uname):
        char_inputs = ["C", "R", "P", "X", "L"]
        if (in_var.upper() == "C"):
            flag=cart.listCart(uname)
        if (in_var.upper() == "R"):
            cart1.removeFromCart(uname)
            # removeItem(cart,uname)
        if (in_var.upper() == "P"):
            print(cart.priceCart(uname))
        if (in_var.upper() == "L"):
            flag=store_obj.listStore()

        if (in_var.upper() == "X"):
            global done
            done = True
        if in_var.upper() == 'A':
            try:
                flag = store_obj.listStore()
                if flag:

                    input_var = input("choose an item to buy(type the item number)")

                    quantity = input("Please Enter quantity")
                    if not quantity:
                        quantity = 1

                    if quantity.isalpha():
                        print('Wrong Input')
                    else:

                        cursor, connection = make_connection('productTable.db')

                        records = cursor.execute("SELECT * from productTable WHERE id='" + input_var + "'").fetchone()
                        connection.commit()
                        connection.close()
                        if records:

                            cart.addToCart(records, uname, int(quantity))
                        else:
                            print('Item not available please wait until new item arrival ')





            except:
                import traceback
                traceback.print_exc()

class StoreItem:
    def __init__(self):
        pass

    def saved_category(self):
        cursor, connection = make_connection('CATEGORY_ITEMS.db')
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT,category TEXT ,itemName TEXT ,price INTEGER)")
        connection.commit()

    def listStore(self):
        try:
            flag = False
            input_var = input(
                "Type category name to view particular category list or type ALL/all to view all category list")
            connection = sqlite3.connect('productTable.db')
            cursor = connection.cursor()

            cursor.execute(
                "CREATE TABLE IF NOT EXISTS productTable (id INTEGER PRIMARY KEY AUTOINCREMENT,category TEXT NOT NULL,itemsName TEXT NOT NULL ,price INTEGER NOT NULL)")
            connection.commit()
            if input_var.upper() == 'ALL':

                cursor, connection = make_connection('productTable.db')
                # connection = sqlite3.connect('product.db')
                # cursor = connection.cursor()
                cursor.execute('SELECT * FROM productTable')
                records = cursor.fetchall()
                connection.commit()
            else:
                cursor, connection = make_connection('productTable.db')

                cursor.execute("SELECT * from productTable WHERE category='" + input_var + "'")
                records = cursor.fetchall()
                connection.commit()
            connection.close()

            if len(records) > 0:
                flag=True
                print('ItemId', end='   ')
                print('Category', end='   ')
                print('Item', end='  ')
                print('Price', end='  ')
                print('\n')

                for each_det in records:
                    print(each_det[0], end='  ')
                    print(each_det[1], end='  ')
                    print(each_det[2], end='  ')
                    print(each_det[3], end='  ')
                    print('\n')
            else:
                print('No items found.')
            return flag
        except:
            import traceback
            traceback.print_exc()

    def CreateStore(self):
        try:

            status_temp = False
            list_item = []
            while (status_temp == False):
                input_type = input("Type A to add new item to store and L to show store items X to exit.")

                if input_type.upper() == 'A':

                    category = input("Please enter category of item ")
                    name = input("Please enter item name")
                    price = int(input("Please enter price of item"))

                    if not category:
                        print('Please enter category of item ['']')
                        continue
                    if not name:
                        print('Please enter item name')
                        continue
                    if not price and isinstance(price, int):
                        print('Please enter price of item')
                        continue

                    # cursor,connection= make_connection('product.db')
                    connection = sqlite3.connect('productTable.db')
                    cursor = connection.cursor()

                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS productTable (id INTEGER PRIMARY KEY AUTOINCREMENT,category TEXT NOT NULL,itemsName TEXT NOT NULL ,price INTEGER NOT NULL)")
                    connection.commit()
                    if category and name and price:
                        cursor.execute('INSERT INTO productTable VALUES(?,?,?,?)',
                                       (None, category, name, price))

                        connection.commit()
                    connection.close()
                    print('Item Successfully added')
                    continue
                if input_type.upper() == 'L':
                    try:
                        # cursor, connection = make_connection('productTable.db')
                        connection = sqlite3.connect('productTable.db')
                        cursor = connection.cursor()
                        cursor.execute('SELECT * FROM productTable')
                        records = cursor.fetchall()
                        connection.commit()
                        connection.close()

                        if len(records) > 0:
                            print('ItemId', end='   ')
                            print('Category', end='   ')
                            print('Item', end='  ')
                            print('Price', end='  ')
                            print('\n')

                            for each_det in records:
                                print(each_det[0], end='  ')
                                print(each_det[1], end='  ')
                                print(each_det[2], end='  ')
                                print(each_det[3], end='  ')
                                print('\n')
                        else:
                            print('No records Found')
                    except:
                        import traceback
                        traceback.print_exc()

                if input_type.upper() == 'X':
                    status_temp = True





        except IOError:
            pass




if __name__ == '__main__':
    try:
        cart1 = ShoppingCart()
        input_obj = HandlingInput()
        store_obj = StoreItem()
    except:
        import traceback
        traceback.print_exc()

    done=False
    while(done==False):
        query = input('Welcome\nEnter "Log in" if you already have an account,else enter "Register". ')

        if query == 'Log in':
            status,uname,isAdmin= user_login()
            if status:
                print('Welcome'+' '+str(uname))
                done=True

        elif query == 'Register':
            status = user_registration()
            if status:
                print('Please Login....')
                status,uname,isAdmin = user_login()
                if status:
                    print('Welcome'+' '+uname)
                    done=True
        else:
            print('Incorrect Input.Please try again.')
            continue
    done=False
    while (done == False):

        if isAdmin in ['1',1]:
            input_obj.printInstructionsAdmin()
            input_var = input("Please enter your choice")

            input_obj.handleInputAdmin(input_var, cart1, uname)

        else:
            input_obj.printInstructions()
            input_var = input("Please enter your choice")

            input_obj.handleInput(input_var, cart1,uname)