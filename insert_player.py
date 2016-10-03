import psycopg2

connection = psycopg2.connect("dbname=sports_search_engine user=sports_search_engine")
cursor = connection.cursor()

add_player = input("Add a player to the roster? Y/n\n>")
if add_player == "Y":
    player_name = input("What is the player's name?\n>")
    player_age = input("Age?\n>")
    play_number = input("Number?\n>")
    player_position = input("Position?\n>")
    player_goals = input("Goals?\n>")
    player_assists = input("Assists?\n>")
    player_saves = input("Saves?\n>")

    cursor.execute("""
    INSERT INTO person_data VALUES (player_name,
    player_age, play_number, player_position, player_goals,
    player_assists, player_saves, 'Manchester United')""")

cursor.close()
connection.close()
