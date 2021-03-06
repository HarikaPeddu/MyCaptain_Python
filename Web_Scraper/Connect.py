# SQL
import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname) # to connect with database or create file, if not exist # returns connection object

    # create table
    conn.execute(" CREATE TABLE IF NOT EXISTS PRODUCTS (NAME TEXT, PRICE INT, REVIEW TEXT, SCREEN_SIZE INT, PROCESSOR TEXT, RAM TEXT, ROM TEXT)")

    print("Table created successfully!!")

    conn.close()

def insert_into_table(dbname,values):
    conn = sqlite3.connect(dbname)

    print("Inserted values in table: " + str(values))    # print values to be inserted
    # inserting data
    insert_data = "INSERT INTO PRODUCTS  (NAME, PRICE, REVIEW, SCREEN_SIZE, PROCESSOR, RAM, ROM) VALUES (?,?,?,?,?,?,?)"
    conn.execute(insert_data, values)

    conn.commit() # commit the changes
    conn.close() 


def get_product_info(dbname):
    conn = sqlite3.connect(dbname) # to connect with database or create file, if not exist # returns connection object

    # select query
    cur = conn.cursor() # object
    cur.execute("SELECT * FROM PRODUCTS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)

    conn.close() 
	
