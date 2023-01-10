import sqlite3 as sq
import pandas as pd

def main():
    conn = sq.connect("Kunder.db")
    cursor = conn.cursor()
    data = pd.read_csv("randoms.csv") 
    data.to_sql("Kunder", conn, if_exists="replace", index=False)
    cursor.execute("SELECT * FROM Kunder")
    print(cursor.fetchall())
    conn.close()
main()
    
