import os
import sqlite3

def main_function(sql):
    try:
        connection = sqlite3.connect("nothing.db")
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    except Exception as e:
        print(e)
        
def func1():
    a = input("Введите первое значение: ")
    b = input("Введите второе значение: ")
    sql = f"INSERT INTO table_name (`column2`, `column3`) VALUES ('{a}', '{b}');"
    main_function(sql)
    
def func3():
    #a = input("Введите первое значение: ")
    #connection = sqlite3.connect("nothing.db")
    #cursor = connection.cursor()
    sql = "SELECT * FROM table_name;"
    print(main_function(sql))


(main_function("SELECT * FROM table_name;"))

connection = sqlite3.connect("nothing.db")
while True:
    os.system("cls")
    print("1. нажмите для добавления")
    print("2. нажмите для того, чтобы обновить значение")
    print("3. нажмите для посмотреть")
    a = input()
    if a=="1":
        func1()
    elif a == "2":
        func2()
    elif a== "3":
        func3()
    else:
        print("нет")
    input("нажмите, чтобы...")
