import random
import sqlite3


def populate_athlete_db(x):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for i in range(x):
        first_name = "Athlete"+str(i)
        last_name = "Cycliste"
        weight = random.randint(50,100)
        age=random.randint(18,40)
        height=random.randint(150,195)
        c.execute(f"INSERT INTO Athlete ('first_name', 'last_name', 'weight', 'age', 'height' ) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, weight, age, height))
        conn.commit()
    conn.close()

if __name__=="__main__":
    populate_athlete_db(10)