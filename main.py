import psycopg2

connection = psycopg2.connect("dbname=sports_search_engine user=sports_search_engine")
cursor = connection.cursor()


def sort_by_name():
    cursor.execute("SELECT * FROM person_data ORDER BY name;")
    results = cursor.fetchall()
    for row in results:
        print(row)


def sort_by_age():
    cursor.execute("SELECT * FROM person_data ORDER BY age;")
    results = cursor.fetchall()
    for row in results:
        print(row)


def sort_by_number():
    cursor.execute("SELECT * FROM person_data ORDER BY player_number;")
    results = cursor.fetchall()
    for row in results:
        print(row)


def sort_by_position():
    cursor.execute("SELECT * FROM person_data ORDER BY position;")
    results = cursor.fetchall()
    for row in results:
        print(row)


def top_goal_scorers():
    cursor.execute("SELECT * FROM person_data ORDER BY goals DESC LIMIT 5;")
    results = cursor.fetchall()
    for row in results:
        print("{} - {} goals".format(row[0], row[4]))


def top_assists():
    cursor.execute("SELECT * FROM person_data ORDER BY assists DESC LIMIT 5;")
    results = cursor.fetchall()
    for row in results:
        print("{} - {} assists".format(row[0], row[5]))


def top_saves():
    cursor.execute("SELECT * FROM person_data ORDER BY saves DESC LIMIT 3;")
    results = cursor.fetchall()
    for row in results:
        print("{} - {}".format(row[0], row[6]))


def add_player():
    player_name = input("What is the player's name?\n>")
    player_age = input("Age?\n>")
    play_number = input("Number?\n>")
    player_position = input("Position?\n>")
    player_goals = input("Goals?\n>")
    player_assists = input("Assists?\n>")
    player_saves = input("Saves?\n>")
    team_name = "Manchester United"

    cursor.execute("""
    INSERT INTO person_data (name, age, player_number, position, goals, assists, saves, team
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (player_name, player_age, play_number, player_position, player_goals,
                                                   player_assists, player_saves, team_name))
    connection.commit()

response = ""

while response != "9":

    print ("2017 Manchester United Team Database")
    print ("""What would you like to view?
    1 - Player by name
    2 - Players by age
    3 - Players by number
    4 - Players by position
    5 - Top 5 goal scorers
    6 - Assists
    7 - Saves
    8 - Add Player
    9 - Exit
    """)
    response = input("")


if response == "1":
    sort_by_name()
if response == "2":
    sort_by_age()
if response == "3":
    sort_by_number()
if response == "4":
    sort_by_position()
if response == "5":
    top_goal_scorers()
if response == "6":
    top_assists()
if response == "7":
    top_saves()
if response == "8":
    add_player()


cursor.close()
connection.close()
