import random
import sqlite3


def populate_athlete_db(x):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for i in range(x):
        first_name = "Athlete"+str(i+1)
        last_name = "Cycliste"
        weight = random.randint(50,100)
        age=random.randint(18,40)
        height=random.randint(150,195)
        c.execute(f"INSERT INTO Athlete ('first_name', 'last_name', 'weight', 'age', 'height' ) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, weight, age, height))
        conn.commit()
    conn.close()

def populate_performance_db(x):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for i in range(x):
        athlete_id = random.randint(1,10)
        power_max = random.randint(150,300)
        hr_max = random.randint(50,100)
        vo2_max=random.randint(18,40)
        cadence_max=random.randint(18,40)
        rf_max=random.randint(150,195)
        c.execute(f"INSERT INTO Performance ('athlete_id', 'power_max', 'hr_max', 'vo2_max', 'cadence_max','rf_max' ) VALUES (?, ?, ?, ?, ?, ?)", (athlete_id, power_max, hr_max, vo2_max, cadence_max, rf_max))
        conn.commit()
    conn.close()


if __name__=="__main__":
    populate_athlete_db(10)
    populate_performance_db(50)