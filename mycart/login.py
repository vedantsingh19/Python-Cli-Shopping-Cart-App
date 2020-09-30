import sys
from mycart.db_utility import make_connection


def user_login():
    cursor, connection = make_connection('login.db')
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL)")
    connection.commit()
    while True:
        name = input("Enter your username. ")
        password = input("Enter your password. ")
        n = cursor.execute("SELECT name from login WHERE name='" + name + "'").fetchone()
        n = str(n).strip("('',)'")
        if n == name:
            pw = cursor.execute("SELECT password from login WHERE password='" + password + "'").fetchone()
            pw = str(pw).strip("('',)'")
            if pw == password:
                print('You are now logged in.')
                return True,n
            else:
                print('Wrong password.')
                continue
        else:
            print('Wrong username.')
            continue

def user_registration():
    cursor, connection = make_connection('login.db')
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,password TEXT NOT NULL)")
    connection.commit()
    while True:
        name = input("Enter your username. ")
        n = cursor.execute('SELECT name FROM login').fetchone()
        n = str(n).strip("('',)'")
        if n == name:
            print('That username already exists,try another one!')
            continue
        else:
            while True:
                email = input("Enter your email. ")
                m = cursor.execute('SELECT email FROM login').fetchone()
                m = str(m).strip("('',)'")
                if m == email:
                    print('That email is already in our database,enter another one!')
                    continue
                else:
                    while True:
                        password = input("Enter your password. ")
                        rpassword = input("Enter your password again. ")
                        if password == rpassword:
                            cursor.execute('INSERT INTO login VALUES(?,?,?,?)',
                                           (None, name, email, password))
                            connection.commit()
                            print('You are now registered.')
                            sys.exit()

                        else:
                            print('Password does not match')
                            continue


