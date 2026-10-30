import random
import string
import time
import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def green_text(text):
   return f"\033[92m {text} \033[0m"

def yellow_text(text):
   return f"\033[93m {text} \033[0m"

def red_text(text):
   return f"\033[91m {text} \033[0m"

def Letrdle_Conditioner(condition , code , trigger_turn) :
    if condition != "Normal" :
        print("⚠ System instability detected...")
        time.sleep(1.5)
        clear_screen()

    if condition == "swap_after_n_moves" :
        print(f" {trigger_turn} chances are over..... therefore swap occurs......")
        pos_1 , pos_2 = random.sample([i for i in range(7)] , 2)
        swap_list = list(code)
        item_1 = swap_list[pos_1] ; item_2 = swap_list[pos_2]
        swap_list[pos_1] = item_2 ; swap_list[pos_2] = item_1
        code = "".join(swap_list)

    elif condition == "shift_after_n":
        print(f" {trigger_turn} chances are over..... therefore shift occurs......")
        print("⚠ Re-indexing memory blocks...")
        if trigger_turn <= 4 :
            pos = random.randint(1,2)
        else :
            pos = 1
        code = code[pos:] + code[:pos]

    elif condition == "phantom_letter" :
        if trigger_turn == 3:
            letters = list(string.ascii_lowercase)
            for i in code : 
                letters.remove(i)
            phantom = random.choice(letters)
            code = [code , phantom]

    elif condition == "mirror_flip" :
        print("⚠ Reality inversion detected...")
        code = code[::-1]

    else :   
        # for normal conditions
        pass
    return code

def Letrdle_Logic(user = "User" ,condition = "Normal" ,counter = 0):
    print(f"{user}, you are playing under the {condition} condition..")
    lst = []
    phantom = " " #keeping phantom as a space for now since space aint allowed in guess
    phantom_used = False
    if condition == "phantom_letters" :
        random_condition_starter = random.randint(2,3)
    else :
        random_condition_starter = random.randint(3,5) 
    easy_code_string = "".join(random.sample(string.ascii_lowercase , 7))
        ## code to be used in the fn call itself.... cause umm at times we need specific codes to play ayy....

    while counter < 7 :
        state = ""
        guess = input("Enter a 7_lettered sequence : ").strip().lower()
        output_string = []
        if len(easy_code_string) == len(guess) :
            if guess.isalpha() == False :
                print(f"{user}, you really think i am gonna let that slide..? ") 
                value = bool(random.choice([0,1]))
                if value == True :
                    print("So you won the lottery for missing a chance cause of your little stunt....")
                    counter += 1
                    continue
                else :
                    print("You got off the hook this time..")
                    continue
            if guess == easy_code_string :
                if play == "random" :
                    print(f"You guessed it in {counter+1} moves..")
                else :
                    print(f"Congrats {user}, you found the right code")
                state = "guessed"
                break
            else :
                for i in range(len(easy_code_string)) :
                    if easy_code_string[i] == guess[i] :
                        output_string.append(green_text(guess[i]))
                    elif guess[i] == phantom and counter < 5 and not phantom_used:
                        #  Phantom interference
                        if random.choice([True, False]):
                            output_string.append(yellow_text(guess[i]))
                        else:
                            output_string.append(red_text(guess[i]))
                        phantom_used = True
                    elif guess[i] in easy_code_string :
                        output_string.append(yellow_text(guess[i]))
                    else :
                        output_string.append(red_text(guess[i]))
                if counter == random_condition_starter:
                    easy_code_string = Letrdle_Conditioner(condition , easy_code_string , random_condition_starter +1)
                    if isinstance(easy_code_string, list) :
                        easy_code_string , phantom = easy_code_string
                counter += 1
                clear_screen()
                lst.append("".join(output_string))
                for i,j in enumerate(lst):
                    print(f"Guess No {i+1}: {j}") 
        else :
            print(f"{user} try again...")
            time.sleep(1)
            clear_screen()
            for i,j in enumerate(lst):
                    print(f"Guess No {i+1}: {j}")
            continue
    if state == "guessed" :
        pass
    else :
        print(f"{user} was not succesful in cracking the code")
        print(f"The sequence was {easy_code_string}")

def Letrdle():
    print("Welcome to Letrdle")
    print("You have 7 chances to guess the 7 lettered sequence")
    print("The letters will be color coded as follows : ")
    print(green_text("Green") , " : Correct letter in correct position")
    print(yellow_text("Yellow") , " : Correct letter in wrong position")
    print(red_text("Red") , " : Incorrect letter")
    print("You can choose to play under different conditions which will make the game more challenging")
    print("The conditions are as follows : ")
    print("1. Normal : No special conditions")
    print("2. Swap after n moves : After n moves, two letters in the code will be swapped")
    print("3. Shift after n moves : After n moves, the code will be shifted by 1 or 2 positions")
    print("4. Phantom letter : A phantom letter will be added to the code which is not part of the code but can be guessed")
    print("5. Mirror flip : The code will be reversed after n moves")
    time.sleep(4)
    clear_screen()
    user = input("Enter your name : ").strip().capitalize()
    print(f"Hello {user} , welcome to Letrdle")
    try:
        condition_choice = input("Choose a condition to play under (1-5) : ").strip()
    except KeyboardInterrupt:
        print("\nExiting...")
        return
    except ValueError:
        print("Invalid input, defaulting to Normal condition")
        condition_choice = "1"
    if condition_choice not in ["1","2","3","4","5"] :
        print("Invalid input, defaulting to Normal condition")
        condition_choice = "1"
    else:
        if condition_choice == "1" :
            condition = "Normal"
        elif condition_choice == "2" :  
            condition = "swap_after_n_moves"
        elif condition_choice == "3" :
            condition = "shift_after_n"
        elif condition_choice == "4" :
            condition = "phantom_letter"
        elif condition_choice == "5" :
            condition = "mirror_flip"
    Letrdle_Logic(user , condition)
    
Letrdle()
