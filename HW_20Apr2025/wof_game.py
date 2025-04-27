#Wheel of Fortune Game
from random import randint


debugging = True
def game():
    global debugging
    player = 1
    #Ask how many players will play the game. 
    try:
        number_of_players = int(input("Please enter the number of players for this game (Max Players 10):  "))
        if number_of_players>10:
            print("Invalid number of players entered (Max 10)");print(f"Number of players : {number_of_players}")
    except TypeError:
        print("Enter a number")
    except Exception as e:
        print(f"Error exception={e}")


    #Create a list with the name of the players or contestants 
    player_list = ["Player"+str(i) for i in range(number_of_players)]
    print(f"Player list :{player_list}")

    #And another list that contains the money they have in the game. 
    #Their money should be set to 0 at the start of the game.
    player_money = [0 for i in range(number_of_players)]
    print(f"Player money: {player_money}")

    #Create a list of the values in the wheel
    wheel_values = [-10000000000000000000000000000,32,45,34,53,45,3,4,35,53,65,97,100]

    #Create a list of categories and list of words per category. There should be one list per category.
    categories = ["Sports","Computers","Food"]
    spo_words = ["Tennis","Baseball","Cricket","Racket","Bat","Pitcher"]
    com_words = ["Display","MotherBoard","Software","Hardware","Laptop","Malware","PC"]
    foo_words = ["Apple","Orrange","Pear","Blue Berry","Cran Berry","Black Berry","Gold Berry","Appricot","Mango","Banana"]
    print(f"Categories: {categories}")

    #To start the game, choose a random category and then pick a random word from the list of the chosen category. 
    #Create a blank list and add blanks (‘_’) with the same number of letters from the random word. 
    #Print the blank list.

    catogery = categories[randint(0,2)]
    cat = catogery
    if cat == "Sports":
        word = spo_words[randint(0,len(spo_words)-1)]
    elif cat == "Computers":
        word = com_words[randint(0,len(com_words)-1)]
    elif cat == "Food":
        word = foo_words[randint(0,len(foo_words)-1)]

    if debugging:
        print(f"word={word}") 
    word_list = list(word)


    blank_list = ["_" for i in range(len(word))]
    print(" ".join(blank_list))
    while True:
        #In the main game, contestants have three options: 
        # 1. spin the wheel and call a consonant
        # 2. buy a vowel for a specific amount (example: $50),
        # or 3. solve the puzzle
        try:
            choice = int(input("Pick an option, enter 1, 2, or 3:"+
                            "\n1. Spin the wheel and call a consonant "+
                            "\n2. Buy a vowel for a specific amount (example: $50), "+
                            "\n3. Solve the puzzle : "))
        except:
            print("Invalid choice")
        print(f"Selected option is {choice}")

        #When spinning the wheel, pick a random item from the wheel list. 
        #Each consonant is worth the cash value of the selected value from the wheel list. 
        #Contestants can continue spinning the wheel until they miss a letter or spin/get Bankrupt or Lose a Turn.
        if choice == 1:
            while player_money > 0:
                prize=wheel_values[randint(0,len(wheel_values)-1)]
                print("You landed on",prize)
                player_list=player_money+prize
        elif choice == 2:
            if player_money >= 50:
                vowel = input("Wich Vowel")
                player_money = player_money-50
                for i in range(len(word_list)):
                    if vowel == word_list[i]:
                        blank_list[i]=word_list[i]
            else:
                print("You dont have $50")
        elif choice == 3:
            geuss_word = input("Word:  ")
            if geuss_word == word:
                print("YOU WON")
                print("Word: ",word)
                break
            else:
                print("You Lost")
            
while True:
    game()