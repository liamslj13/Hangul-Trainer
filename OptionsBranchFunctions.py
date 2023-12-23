import random
import hangulcharacters
import menusandtextblocks


#Create the loop that will display the user all of their options (eng)
def initial_menu_loop() -> None:
    print(len(menusandtextblocks.title) * "=")
    print(menusandtextblocks.title)
    print(len(menusandtextblocks.title) * "=")
    print(menusandtextblocks.project_info)
    while True:
        # Start initial menu loop
        print(menusandtextblocks.main_menu_options)
        choice = input("Enter your choice here: ").strip()
        # Create branch for learning characters
        if choice == "1":
            while True:
                print(menusandtextblocks.if_learn_hangul_menu)
                choice = input("Enter your choice here: ").strip()
                if choice == "1":
                    hangul_vowels()
                elif choice == "2":
                    hangul_combined_vowels()
                elif choice == "3":
                    hangul_consonants()
                elif choice == "4":
                    hangul_double_consonants()
                elif choice == "5":
                    mixed_review()
                elif choice == "6":
                    break
        elif choice == "2":
            print(menusandtextblocks.credit_text)
        elif choice == "3":
            break
        else:
            print("That is an invalid option. "
                  "Please choose from the select menu.")


#Define function that runs the vowels; returns nothing
def hangul_vowels() -> None:
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    print("Enter \"stop\" at anytime to quit.")
    previous_character = 99
    while True:
        # 10 regular vowels, so we will set our interval as (0, 9)
        character_index = random.randint(0, 9)
        #Ensure user never gets the same character twice in a row
        while character_index == previous_character:
            character_index = random.randint(0, 9)
        previous_character = character_index
        character = hangulcharacters.vowels[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
        if hangul_guess == hangulcharacters.vowels_romanized[character_index]:
            print(f"{hangul_guess} is correct!")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"Your final score was {score}/{iterations}, "
                      f"or about {float((score / iterations) * 100).__round__()}%!")
                break
        else:
            print(f"{hangul_guess} is wrong! The correct answer was "
                  f"{hangulcharacters.vowels_romanized[character_index]}.")
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1


#Define function that runs the combined vowels; returns nothing
def hangul_combined_vowels() -> None:
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    print("Enter \"stop\" at anytime to quit.")
    previous_character = 99
    while True:
        # 11 combined vowels, so we will set our interval as (0, 10)
        character_index = random.randint(0, 10)
        #Ensure user never gets same character twice
        while character_index == previous_character:
            character_index = random.randint(0, 10)
        previous_character = character_index
        character = hangulcharacters.combined_vowels[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
        if hangul_guess == hangulcharacters.combined_vowels_romanized[character_index]:
            print(f"{hangul_guess} is correct!")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"Your final score was {score}/{iterations}, "
                      f"or about {float((score / iterations) * 100).__round__()}%!")
                break
        else:
            print(f"{hangul_guess} is wrong! The correct answer was "
                  f"{hangulcharacters.combined_vowels_romanized[character_index]}.")
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1


#Define function that runs the consonants; returns nothing
def hangul_consonants() -> None:
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    previous_character = 99
    print("Enter \"stop\" at anytime to quit.")
    while True:
        # 14 regular consonants, so we will set our interval as (0, 13)
        character_index = random.randint(0, 13)
        while character_index == previous_character:
            character_index = random.randint(0, 13)
        previous_character = character_index
        character = hangulcharacters.consonants[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
        if hangul_guess in hangulcharacters.consonant_romanized[character_index]:
            print(f"{hangul_guess} is correct!")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"Your final score was {score}/{iterations}, "
                      f"or about {float((score / iterations) * 100).__round__()}%!")
                break
        else:
            if type(hangulcharacters.consonant_romanized[character_index]) == tuple:
                print(f"{hangul_guess} is wrong! the correct answer was "
                      f"{hangulcharacters.consonant_romanized[character_index][0]} or "
                      f"{hangulcharacters.consonant_romanized[character_index][1]}.")
            else:
                print(f"{hangul_guess} is wrong! The correct answer was "
                      f"{hangulcharacters.double_consonant_romanized[character_index]}.")
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1


#Define function that runs the double consonants; returns nothing
def hangul_double_consonants() -> None:
    # Get jp bool to detect language
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    print("Enter \"stop\" at anytime to quit.")
    previous_character = 99
    while True:
        # 5 double consonants, so we will set our interval as (0, 4)
        character_index = random.randint(0, 4)
        while character_index == previous_character:
            character_index = random.randint(0, 4)
        previous_character = character_index
        character = hangulcharacters.double_consonant[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
        if hangul_guess == hangulcharacters.double_consonant_romanized[character_index]:
            print(f"{hangul_guess} is correct!")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            print(f"Your final score was {score}/{iterations}, "
                  f"or about {float((score / iterations) * 100).__round__()}%!")
            break
        else:
            print(f"{hangul_guess} is wrong! The correct answer was "
                  f"{hangulcharacters.double_consonant_romanized[character_index]}.")
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1


#This function utilizes previous code with modifications, and allows the user to review everything at once
def mixed_review() -> None:
    #1 - Vowels, 2 - Combined Vowels, 3 - Consonants, 4 - Combined Consonants
    score = 0
    iterations = 0
    previous_character = 99
    while True:
        #Get a new integer each iteration
        random_review = random.randint(1, 4)
        #Create vowels branch
        if random_review == 1:
            character_index = random.randint(0, 9)
            # Ensure user never gets the same character twice in a row
            while character_index == previous_character:
                character_index = random.randint(0, 9)
            previous_character = character_index
            character = hangulcharacters.vowels[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
            if hangul_guess == hangulcharacters.vowels_romanized[character_index]:
                print(f"{hangul_guess} is correct!")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"Your final score was {score}/{iterations}, "
                          f"or about {float((score / iterations) * 100).__round__()}%!")
                    break
            else:
                print(f"{hangul_guess} is wrong! The correct answer was "
                      f"{hangulcharacters.vowels_romanized[character_index]}.")
        # Branch 2 corresponds to the RNG choosing combined vowels
        elif random_review == 2:
            character_index = random.randint(0, 10)
            while character_index == previous_character:
                character_index = random.randint(0, 10)
            previous_character = character_index
            character = hangulcharacters.combined_vowels[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
            if hangul_guess == hangulcharacters.combined_vowels_romanized[character_index]:
                print(f"{hangul_guess} is correct!")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"Your final score was {score}/{iterations}, "
                          f"or about {float((score / iterations) * 100).__round__()}%!")
                    break
            else:
                print(f"{hangul_guess} is wrong! The correct answer was "
                      f"{hangulcharacters.combined_vowels_romanized[character_index]}.")
        #Branch 3 corresponds to the RNG choosing regular consonants
        elif random_review == 3:
            character_index = random.randint(0, 13)
            while character_index == previous_character:
                character_index = random.randint(0, 13)
            previous_character = character_index
            character = hangulcharacters.consonants[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
            if hangul_guess in hangulcharacters.consonant_romanized[character_index]:
                print(f"{hangul_guess} is correct!")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"Your final score was {score}/{iterations}, "
                          f"or about {float((score / iterations) * 100).__round__()}%!")
                    break
            else:
                if type(hangulcharacters.consonant_romanized[character_index]) == tuple:
                    print(f"{hangul_guess} is wrong! the correct answer was "
                          f"{hangulcharacters.consonant_romanized[character_index][0]} or "
                          f"{hangulcharacters.consonant_romanized[character_index][1]}.")
                else:
                    print(f"{hangul_guess} is wrong! The correct answer was "
                          f"{hangulcharacters.double_consonant_romanized[character_index]}.")
        #This will be our branch for the double consonants, AKA the "4"th selection
        else:
            character_index = random.randint(0, 4)
            while character_index == previous_character:
                character_index = random.randint(0, 4)
            previous_character = character_index
            character = hangulcharacters.double_consonant[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("Enter the romanization of this hangul: ").strip().lower()
            if hangul_guess == hangulcharacters.double_consonant_romanized[character_index]:
                print(f"{hangul_guess} is correct!")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                print(f"Your final score was {score}/{iterations}, "
                      f"or about {float((score / iterations) * 100).__round__()}%!")
                break
            else:
                print(f"{hangul_guess} is wrong! The correct answer was "
                      f"{hangulcharacters.double_consonant_romanized[character_index]}.")
        #Unless the loop is broken, the score will be printed and an iteration added
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1
