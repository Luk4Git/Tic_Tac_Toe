"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Matela
email: lukas.matela@innogy.cz, Lukas.Matela@gmail.com
discord: Lukáš M., Lukáš#8477
"""

# Proměnné označující hráče
player_x = "X"
player_o = "O"

# Běžící hra = True
game_on = True

# Pokud není vítěz = False
winner = False

# Aktuální hráč na tahu je nastaven na začátek hry hráč "X"
actual_player = player_x

# Vytvoří datový typ slovník pro hrací plochu
board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "
         }


# Zobrazí úvodní text
def introduction():
    print("\n"
          "    Welcome to Tic Tac Toe\n"
          "========================================\n"
          "GAME RULES:\n"
          "Each player can place one mark (or stone)\n"
          "per turn on the 3x3 grid. The WINNER is\n"
          "who succeeds in placing three of their\n"
          "marks in a:\n"
          "* horizontal,\n"
          "* vertical or\n"
          "* diagonal row\n"
          "========================================\n"
          "Let's start the game\n"
          "    ")


# Funkce pro zobrazení hrací plochy
def display_board():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# Spoustí hru po jednotlivých krocích:
def play():
    introduction()
    display_board()
    while game_on:
        turn()
        change_player()
        check_end_game()


# Provedení tahu: vyzve hráče, aby zvolil pozici pro tah, rozsah 1 až 9, pozice musí být volná:
def turn():
    position = input(f" Player {actual_player} | Please enter your move number:")

    while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        position = input("Choose place between 1 and 9: ")

    while board[position] != " ":
        position = input("This space isn't free, chose another place: ")

    board[position] = actual_player
    display_board()


# funkce změní hráče na druhého:
def change_player():
    global actual_player
    if actual_player == player_x:
        actual_player = player_o
    elif actual_player == player_o:
        actual_player = player_x


# Zkontrolu zda nastal konec hry (došlo k vítězství/ k remíze) vypíše vítěze a nastaví globalní proměnnou
def check_end_game():
    global winner
    global game_on
    # řádky X
    if board["1"] == board["2"] == board["3"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    if board["4"] == board["5"] == board["6"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    if board["7"] == board["8"] == board["9"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    # sloupce X
    if board["1"] == board["4"] == board["7"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    if board["2"] == board["5"] == board["8"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    if board["3"] == board["6"] == board["9"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    # uhlopricka X
    if board["1"] == board["5"] == board["9"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    if board["3"] == board["5"] == board["7"] == "X" != " ":
        print("Congratulations, the player X WON!")
        winner = True
        game_on = False
    # řádky O
    if board["1"] == board["2"] == board["3"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    if board["4"] == board["5"] == board["6"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    if board["7"] == board["8"] == board["9"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    # sloupce O
    if board["1"] == board["4"] == board["7"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    if board["2"] == board["5"] == board["8"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    if board["3"] == board["6"] == board["9"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    # uhlopricka X
    if board["1"] == board["5"] == board["9"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    if board["3"] == board["5"] == board["7"] == "O" != " ":
        print("Congratulations, the player O WON!")
        winner = True
        game_on = False
    # remíza
    if board["1"] != " " and board["2"] != " " and board["3"] != " " and board["4"] != " " and board["5"] != " " \
            and ["6"] != " " and board["7"] != " " and board["8"] != " " and ["9"] != " " and winner == False:
        print("it's a tie, nobody wins")
        game_on = False


play()
