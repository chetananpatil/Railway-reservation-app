import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="train_sys"
)
c = mydb.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS User(Train_No int, name TEXT, Train_Type TEXT, Source TEXT, Destination TEXT,Availability TEXT)')

def add_data(Train_No, name, Train_Type, Source, Destination,Availability):
    c.execute('INSERT INTO User(Train_No, name, Train_Type, Source, Destination,Availability) VALUES (%s,%s,%s,%s,%s,%s)',(Train_No, name, Train_Type, Source, Destination,Availability))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM User')
    data = c.fetchall()
    return data

def view_only_names():
    c.execute('SELECT Train_No FROM User')
    data = c.fetchall()
    return data

def get_data(Train_no):
    c.execute('SELECT * FROM User  WHERE Train_No="{}"'.format(Train_no))
    data = c.fetchall()
    return data

def edit_data(new_Train_No, new_name, new_Train_Type, new_Source, new_Destination, new_Availability, Train_No, name, Train_Type, Source,Destination,Availability):
    c.execute("UPDATE User SET Train_no=%s,Name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s WHERE Train_no=%s and name=%s and Train_Type=%s and Source=%s and Destination=%s and Availability=%s" , (new_Train_No, new_name, new_Train_Type, new_Source, new_Destination, new_Availability,Train_No, name, Train_Type, Source,Destination,Availability))
    '''sql="UPDATE Data SET Train_no=%s,name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s WHERE Train_no=%s,name=%s, Train_Type=%s, Source=%s, Destination=%s, Availability=%s"
    val= (new_Train_No, new_name, new_Train_Type, new_Source, new_Destination, new_Availability, Train_No, name, Train_Type, Source,Destination,Availability)
    c.execute(sql,val)'''
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data(Train_No):
    c.execute('DELETE FROM User WHERE name="{}"'.format(Train_No))
    mydb.commit()
    data = c.fetchall()
    return data
