import sys
from mycart.db_utility import make_connection

def user_registration():
    print('******************* ADMIN REGISTRATION *********************')
    cursor, connection = make_connection('LOGINDB.db')
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS LOGINDB (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL,isAdmin BOOL)")
    connection.commit()
    while True:
        name = input("Enter your username. ")
        n = cursor.execute('SELECT name FROM LOGINDB').fetchone()
        n = str(n).strip("('',)'")
        if n == name:
            print('That username already exists,try another one!')
            continue
        else:
            while True:
                email = input("Enter your email. ")
                m = cursor.execute('SELECT email FROM LOGINDB').fetchone()
                m = str(m).strip("('',)'")
                if m == email:
                    print('That email is already in our database,enter another one!')
                    continue
                else:
                    while True:
                        password = input("Enter your password. ")
                        rpassword = input("Enter your password again. ")
                        if password == rpassword:
                            cursor.execute('INSERT INTO LOGINDB VALUES(?,?,?,?,?)',
                                           (None, name, email, password,True))
                            connection.commit()
                            print('You are now registered.')
                            sys.exit()

                        else:
                            print('Password does not match')
                            continue

user_registration()
