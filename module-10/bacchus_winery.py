""" Title: bacchus_winery.py
    Author: Colton Stone, Aysa Jordan, and Eric Brown
    Date: December 7, 2025,
    Description: This code is written to display a database which depicts the logistics of a wine company."""

import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
dotenv.load_dotenv()
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config)  # connect to the Bacchus database

    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))

    input("\nPress any key to continue...")

    cursor = db.cursor()

    # ----------------------EMPLOYEE RECORDS----------------------

    employee_list = ("""SELECT employee_name as Name, employee_title as Role, employee_department as Department,
                               annual_workhours as "Annual Hours" FROM employee""")

    cursor.execute(employee_list)
    employee_records = cursor.fetchall()

    print("\n------Employee Records-----: ")

    for emps in employee_records:
        print("\nName: {}\nRole: {}\nDepartment: {}\nAnnual Hours: {}\n".format(emps[0], emps[1], emps[2], emps[3]))
        print()

    # ----------------------SUPPLIER RECORDS----------------------

    supplier_list = ("""SELECT supplier_name as Name, supply_type as "Company Industry", items as "Company Material",
                               expected_monthly_deliverydates as "Expected Monthly Delivery Dates",
                               actual_monthly_deliverydates as "Actual Monthly Delivery Dates"
                        FROM supplier
                        WHERE supplier_name IN ('Green Glass & Packaging', 'Daily Express', 'G3 Industries')""")

    cursor.execute(supplier_list)
    supplier_records = cursor.fetchall()

    print("\n------Supplier Records-----: ")

    for sup in supplier_records:
        print("\nName: {}\nCompany Industry: {}\nCompany Material: {}\nExpected Monthly Delivery Dates: {}"
              "\nActual Monthly Delivery Dates: {}\n".format(sup[0], sup[1], sup[2], sup[3], sup[4]))
        print()

    # ----------------------WINE RECORDS----------------------

    wine_list = ("""SELECT wine_name as Name, wine_type as Type,
                           expected_gallonsales as "Expected Gallon Sales",
                           actual_gallonsales as "Actual Gallon Sales"
                    FROM wine
                    WHERE wine_name IN ('Cabernet', 'Chablis', 'Chardonnay', 'Merlot')""")

    cursor.execute(wine_list)
    wine_records = cursor.fetchall()

    print("\n------Wine Records-----: ")

    for drinks in wine_records:
        print("\nName: {}\nType: {}\nExpected Gallon Sales: {}\nActual Gallon Sales: {}\n".format(drinks[0], drinks[1], drinks[2], drinks[3]))
        print()

    # ----------------------Distributor RECORDS----------------------

    dis_list = ("""SELECT distributor_name as Name, wine_name as "Wine Name" FROM distributor
                                                                                      INNER JOIN wine ON distributor.wine_id = wine.wine_id
                   WHERE wine_name IN ('Cabernet', 'Chablis', 'Chardonnay', 'Merlot')""")

    cursor.execute(dis_list)
    distributor_records = cursor.fetchall()

    print("\n------Distributor Records-----: ")

    for dis in distributor_records:
        print("\nName: {}\nWine Name: {}".format(dis[0], dis[1]))

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

db.close()
