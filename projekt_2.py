"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Matela
email: lukas.matela@innogy.cz, Lukas.Matela@gmail.com
discord: Lukáš M., #8515
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
def main():
    introduction()
    display_board()
    while game_on:
        turn()
        check_end_game()
        change_player()


# Provedení tahu: vyzve hráče, aby zvolil pozici pro tah, rozsah 1 až 9, pozice musí být volná:
def turn():
    position = input(f" Player {actual_player} | Please enter your move number:")

    while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        position = input("Choose place between 1 and 9: ")

    if board[position] != " ":
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

    #vítěz řádku
    if board["1"] == board["2"] == board["3"] == actual_player != " " \
            or board["4"] == board["5"] == board["6"] == actual_player != " " \
            or board["7"] == board["8"] == board["9"] == actual_player != " ":

            print (f" Congratulations, the player {actual_player} WON!")
            winner = True
            game_on = False

    #vítěz sloupce
    if board["1"] == board["4"] == board["7"] == actual_player != " " \
            or board["2"] == board["5"] == board["8"] == actual_player != " " \
            or board["3"] == board["6"] == board["9"] == actual_player != " ":

        print(f" Congratulations, the player {actual_player} WON!")
        winner = True
        game_on = False

    #vítěz uhlopříčky
    if board["1"] == board["5"] == board["9"] == actual_player != " " \
            or board["3"] == board["5"] == board["7"] == actual_player != " ":

        print(f" Congratulations, the player {actual_player} WON!")
        winner = True
        game_on = False

    #remíza
    if board["1"] != " " and board["2"] != " " and board["3"] != " " and board["4"] != " " and board["5"] != " " \
            and ["6"] != " " and board["7"] != " " and board["8"] != " " and ["9"] != " " and winner == False:

        print("it's a tie, nobody wins")
        game_on = False


if __name__ == '__main__':
    main()
