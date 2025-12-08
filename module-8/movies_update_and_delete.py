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


    def show_films(cursor, title):




        #----------------------STANDARD OUTPUT----------------------

        stan_list = ("""SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film 
                               INNER JOIN genre ON film.genre_id = genre.genre_id
                               INNER JOIN studio ON film.studio_id = studio.studio_id""")

        cursor.execute(stan_list)
        standard_list = cursor.fetchall()

        print("\n == {} ==".format(title))

        for film in standard_list:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],film[3]))




            # ----------------------INSERT OUTPUT----------------------

        new_studio = ("INSERT INTO studio (studio_id, studio_name) VALUES ('4', 'Universal Pictures')")

        new_genre = ("INSERT INTO genre (genre_id, genre_name) VALUES ('4', 'Action')")


        new_film = ("""INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
                      
                      VALUES ('4', 'Jurassic Park', '1993', '127', 'Steven Spielberg', '3', '4')""")

        new_list = ("""SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film 
                                       INNER JOIN genre ON film.genre_id = genre.genre_id
                                       INNER JOIN studio ON film.studio_id = studio.studio_id""")





        cursor.execute(new_studio)
        cursor.execute(new_genre)
        cursor.execute(new_film)
        cursor.execute(new_list)
        new_filmlist = cursor.fetchall()

        print("\n == {} ==".format(title + " AFTER INSERT"))

        for film in new_filmlist:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))




        # ----------------------UPDATE OUTPUT----------------------

        genre_update = ("UPDATE genre SET genre_name = 'Horror' WHERE genre_name = 'SciFi'")


        up_list = ("""SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film 
                                               INNER JOIN genre ON film.genre_id = genre.genre_id
                                               INNER JOIN studio ON film.studio_id = studio.studio_id""")

        cursor.execute(genre_update)
        cursor.execute(up_list)


        updated_list = cursor.fetchall()

        print("\n == {} ==".format(title + " AFTER UPDATE- Changed Alien to Horror"))

        for film in updated_list:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))




            # ----------------------DELETE OUTPUT----------------------


        delete_row = ("DELETE FROM film WHERE film_name = 'Gladiator'")

        del_list = up_list


        cursor.execute(delete_row)
        cursor.execute(del_list)
        delete_list = cursor.fetchall()

        print("\n == {} ==".format(title + " AFTER DELETE"))

        for film in delete_list:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    show_films(cursor, "DISPLAYING FILMS")
















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


