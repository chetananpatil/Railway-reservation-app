import mysql.connector 
mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="Chetu@12" ) 
c = mydb.cursor() 
c.execute("CREATE DATABASE railway_reservation")