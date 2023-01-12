import sqlite3 as sq
import pandas as pd

def main():
    conn = sq.connect("Postnummer.db") # Connect to database
    cursor = conn.cursor() # Create cursor
    data = pd.read_excel("Postnummerregister-Excel.xlsx") 
    data.to_sql("Kunder", conn, if_exists="replace", index=False) # Create table
    cursor.execute("SELECT * FROM Kunder") # Select all from table
    print(cursor.fetchall()) # Print all
    conn.commit
    conn.close()



main()

    
