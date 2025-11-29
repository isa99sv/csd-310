""" import statements """
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

    db = mysql.connector.connect(**config)  # connect to the movies database

    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))

    input("\nPress any key to continue...")

    cursor = db.cursor()

    cursor.execute("SELECT studio_name FROM studio")
    studio = cursor.fetchall()



    cursor.execute("SELECT genre_name FROM genre")
    genre = cursor.fetchall()




    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_id IN ('2', '3')")
    short_film = cursor.fetchall()


    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_releaseDate DESC")
    director = cursor.fetchall()



    print("\n-- DISPLAYING Studio RECORDS --")

    for stu_id,studio_name in enumerate(studio, start=1):
            print(f"\nStudio ID: {stu_id}")
            print(f"Studio Name: {studio_name[0]}")



    print()
    print("\n-- DISPLAYING Genre RECORDS --")

    for gen_id, genre_names in enumerate(genre, start=1):
            print(f"\nGenre ID: {gen_id}")
            print(f"Genre Name: {genre_names[0]}")




    print()
    print("\n-- DISPLAYING Short Film RECORDS --")

    for film_name, film_runtime in short_film:
        print(f"\nFilm Name: {film_name}")
        print(f"Runtime: {film_runtime}")




    print()
    print("\n-- DISPLAYING Director RECORDS in Order --")

    for film_name, film_director in director:
        print(f"\nFilm Name: {film_name}")
        print(f"Director: {film_director}")




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






