## memory game

import random
import tabulate
import os
import sys 
import time 
import emoji
from string import ascii_uppercase

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

def memory_game():
    TIME_SLEEP = 3
    print("You get {} seconds to remember".format(TIME_SLEEP))

    max_rows = 8
    actual_board = {}
    emoji_list = ['🔥', '😎', '👑', '🏆', '💥', '⭐', '🚀', '🥳', '😀', '✨', '🥇', '💀', '☠', '🤡', '😭', '😩', '😤', '👀' ]

    temp_count = 0

    def take_row_input():
        while True:
            try:
                row_no = int(input("Enter no. of rows(3-8): "))
            except ValueError:
                    pass
            except KeyboardInterrupt:
                print("\nExiting...")
                return 0
            else:
                if row_no in range(3, 9):
                    return row_no
            print("Enter a valid integer between 3 and 8.")
            clear_screen()


    row_count = take_row_input()
    letters = ascii_uppercase[:row_count]

    if row_count == 0:
        pass
        ## gotta exit properly otherwise data can be corrupted
    else :
        emojis = random.sample(emoji_list , row_count)
        
        if row_count %2 != 0:
            #temp_count += 1 
            emojis = emojis * (row_count-1)
            temp_list = emoji_list[:row_count//2] * 2
            emojis.extend(temp_list)
            emojis.append('X')
        else:
            if (row_count//2)%2 == 0 :
                emojis = emojis * (row_count//2)
                emojis_2 = random.sample(emoji_list , row_count)
                emojis_2 = emojis_2 * (row_count//2)
                emojis.extend(emojis_2)
            else:
                emojis = emojis * row_count
                ## will maybe make a proper thing for that later i think
        random.shuffle(emojis)
        
        for i in letters:
            for j in range(1,row_count +1):
                key = i+str(j)
                if temp_count < len(emojis):
                    actual_board[key] = emojis[temp_count]
                    temp_count += 1 
        #print(actual_board)
        
    game_board = actual_board.copy()
    for i in game_board:
        game_board[i] = i
    
    counter = 0
    while True:
        print_list = list(game_board.values())
        temp_count_2 = 0 
        printable_list = []
        for i in range(row_count):
            temp_list = []
            for j in range(row_count):
                temp_list.append(print_list[temp_count_2])
                temp_count_2 += 1
            printable_list.append(temp_list)

        print(tabulate.tabulate((printable_list), tablefmt="grid"))
        if counter == (row_count**2)//2 :
            break

        while True:
            input_1 = input("Enter grid_1 position: ").strip().upper()
            input_2 = input("Enter grid_2 position: ").strip().upper()
            if input_1 in actual_board and input_2 in actual_board:
                break
            else:
                print("Key Error found. Pls input valid grid_name")
        print(f"Grid_1: {actual_board[input_1]} | Grid_2: {actual_board[input_2]}")
        if actual_board[input_1] == actual_board[input_2]:
            print("Match found!")
            game_board[input_1] = actual_board[input_1]
            game_board[input_2] = actual_board[input_2]
            counter += 1

        time.sleep(TIME_SLEEP)
        clear_screen()
        
    print("Board Cleared..")

if __name__ == "__main__":
    if "win" in sys.platform:
        print("⚠️ CMD may not display emojis correctly")
        print("⚠️ For best experience, use Windows Terminal (CMD may not show emojis)")
        time.sleep(1.5)
        clear_screen()
    memory_game()
