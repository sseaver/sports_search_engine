import psycopg2
import csv
connection = psycopg2.connect("dbname=sports_search_engine user=sports_search_engine")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS person_data;")

create_table_command = """
CREATE TABLE person_data (
    name VARCHAR(50),
    age SMALLINT(50),
    player_number SMALLINT(3),
    position VARCHAR(50),
    goals SMALLINT(3),
    assists SMALLINT(3),
    saves SMALLINT(3),
    team VARCHAR(50)
);
"""

cursor.execute(create_table_command)

with open("playerinfo.csv") as player_stats:
    stats = csv.reader(player_stats)
    for row in stats:
        cursor.execute("INSERT INTO person_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


connection.commit()
cursor.close()
connection.close()
