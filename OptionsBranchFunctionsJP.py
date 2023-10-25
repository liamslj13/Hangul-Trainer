import random
import hangulcharacters
import menusandtextblocks


def initial_menu_loop_jp() -> None:
    print(len(menusandtextblocks.title) * "=")
    print(menusandtextblocks.title)
    print(len(menusandtextblocks.title) * "=")
    print(menusandtextblocks.project_info_jp)
    while True:
        # Start initial menu loop
        print(menusandtextblocks.main_menu_options_jp)
        choice = input("上の選択肢から選んでください: ").strip()
        # Create branch for learning characters
        if choice == "1":
            while True:
                print(menusandtextblocks.if_learn_hangul_menu_jp)
                choice = input("上の選択肢から選んでください: ").strip()
                if choice == "1":
                    hangul_vowels_jp()
                elif choice == "2":
                    hangul_combined_vowels_jp()
                elif choice == "3":
                    hangul_consonants_jp()
                elif choice == "4":
                    hangul_double_consonants_jp()
                elif choice == "5":
                    mixed_review_jp()
                elif choice == "6":
                    break
        elif choice == "2":
            print(menusandtextblocks.credit_text)
        elif choice == "3":
            break
        else:
            print(f"{choice}は無効な選択肢です。 "
                  "上の選択肢からお選びください。")


def hangul_vowels_jp() -> None:
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    print("やめたい場合は\"stop\"を入力することでやめることができます。")
    previous_character = 99
    while True:
        # 10 regular vowels, so we will set our interval as (0, 9)
        character_index = random.randint(0, 9)
        # Ensure user never gets the same character twice in a row
        while character_index == previous_character:
            character_index = random.randint(0, 9)
        previous_character = character_index
        character = hangulcharacters.vowels[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
        if hangul_guess == hangulcharacters.vowels_romanized[character_index]:
            print(f"{hangul_guess}は正解！")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"最終得点は{score}/{iterations}!"
                      f"約{float((score / iterations) * 100).__round__()}%です！")
                break
        else:
            print(f"{hangul_guess}は不正解！正解だったのは、"
                  f"{hangulcharacters.vowels_romanized[character_index]}！")
        print(menusandtextblocks.bar)
        print(f"スコア: {score}")
        iterations += 1


def hangul_combined_vowels_jp() -> None:
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    print("やめたい場合は\"stop\"を入力することでやめることができます。")
    previous_character = 99
    while True:
        # 11 combined vowels, so we will set our interval as (0, 10)
        character_index = random.randint(0, 10)
        # Ensure user never gets same character twice
        while character_index == previous_character:
            character_index = random.randint(0, 10)
        previous_character = character_index
        character = hangulcharacters.combined_vowels[character_index]
        print(menusandtextblocks.bar)
        print(" " * 19, character)
        print(menusandtextblocks.bar)
        hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
        if hangul_guess == hangulcharacters.combined_vowels_romanized[character_index]:
            print(f"{hangul_guess}は正解！")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"最終得点は{score}/{iterations}!"
                      f"約{float((score / iterations) * 100).__round__()}%です！")
                break
        else:
            print(f"{hangul_guess}は不正解！正解だったのは、"
                  f"{hangulcharacters.vowels_romanized[character_index]}！")
        print(menusandtextblocks.bar)
        print(f"スコア: {score}")
        iterations += 1


def hangul_consonants_jp() -> None:
    # Get jp bool to detect language
    # Used to calculate at final score at the end
    score = 0
    iterations = 0
    previous_character = 99
    print("やめたい場合は\"stop\"を入力することでやめることができます。")
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
        hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
        if hangul_guess in hangulcharacters.consonant_romanized[character_index]:
            print(f"{hangul_guess}は正解！")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            else:
                print(f"最終得点は{score}/{iterations}!"
                      f"約{float((score / iterations) * 100).__round__()}%です！")
                break
        else:
            if type(hangulcharacters.consonant_romanized[character_index]) == tuple:
                print(f"{hangul_guess}は不正解だった！正解だったのは、 "
                      f"{hangulcharacters.consonant_romanized[character_index][0]}か"
                      f"{hangulcharacters.consonant_romanized[character_index][1]}！")
            else:
                print(f"最終得点は{score}/{iterations}!"
                      f"約{float((score / iterations) * 100).__round__()}%です！")
        print(menusandtextblocks.bar)
        print(f"スコア: {score}")
        iterations += 1


def hangul_double_consonants_jp() -> None:
    score = 0
    iterations = 0
    print("やめたい場合は\"stop\"を入力することでやめることができます。")
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
        hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
        if hangul_guess == hangulcharacters.double_consonant_romanized[character_index]:
            print(f"{hangul_guess}は正解！")
            score += 1
        elif hangul_guess.strip().lower() == "stop":
            if score == 0:
                break
            print(f"最終得点は{score}/{iterations}!"
                  f"約{float((score / iterations) * 100).__round__()}%です！")
            break
        else:
            print(f"{hangul_guess}は不正解！正解だったのは、"
                  f"{hangulcharacters.vowels_romanized[character_index]}！")
        print(menusandtextblocks.bar)
        print(f"Score: {score}")
        iterations += 1


def mixed_review_jp() -> None:
    # 1 - Vowels, 2 - Combined Vowels, 3 - Consonants, 4 - Combined Consonants
    score = 0
    iterations = 0
    previous_character = 99
    print("やめたい場合は\"stop\"を入力することでやめることができます。")
    while True:
        # Get a new integer each iteration
        random_review = random.randint(1, 4)
        # Create vowels branch
        if random_review == 1:
            character_index = random.randint(0, 9)
            # Ensure user never gets the same character twice in a row
            while character_index == previous_character:
                character_index = random.randint(0, 9)
            previous_character = character_index
            #Process remains the same; lots of duplicate code
            character = hangulcharacters.vowels[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
            if hangul_guess == hangulcharacters.vowels_romanized[character_index]:
                print(f"{hangul_guess}は正解！")
                score += 1
            #Handle user exit request
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"最終得点は{score}/{iterations}!"
                          f"約{float((score / iterations) * 100).__round__()}%です！")
                    break
            #Tell user they are wrong, no point will be awarded (this is the same in every branch)
            else:
                print(f"{hangul_guess}は不正解! 正解だったのは、"
                      f"{hangulcharacters.vowels_romanized[character_index]}！")
        #Create branch to handle combined vowels
        elif random_review == 2:
            character_index = random.randint(0, 10)
            while character_index == previous_character:
                character_index = random.randint(0, 10)
            previous_character = character_index
            character = hangulcharacters.combined_vowels[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
            if hangul_guess == hangulcharacters.combined_vowels_romanized[character_index]:
                print(f"{hangul_guess}は正解！")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"最終得点は{score}/{iterations}!"
                          f"約{float((score / iterations) * 100).__round__()}%です！")
                    break
            else:
                print(f"{hangul_guess}は不正解！正解だったのは、"
                      f"{hangulcharacters.vowels_romanized[character_index]}！")
        elif random_review == 3:
            character_index = random.randint(0, 13)
            while character_index == previous_character:
                character_index = random.randint(0, 13)
            previous_character = character_index
            character = hangulcharacters.consonants[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
            if hangul_guess in hangulcharacters.consonant_romanized[character_index]:
                print(f"{hangul_guess}は正解！")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                else:
                    print(f"最終得点は{score}/{iterations}!"
                          f"約{float((score / iterations) * 100).__round__()}%です！")
                    break
            else:
                if type(hangulcharacters.consonant_romanized[character_index]) == tuple:
                    print(f"{hangul_guess}は不正解だった！正解だったのは、"
                          f"{hangulcharacters.consonant_romanized[character_index][0]}か"
                          f"{hangulcharacters.consonant_romanized[character_index][1]}！")
                else:
                    print(f"最終得点は{score}/{iterations}!"
                          f"約{float((score / iterations) * 100).__round__()}%です！")
        else:
            character_index = random.randint(0, 4)
            while character_index == previous_character:
                character_index = random.randint(0, 4)
            previous_character = character_index
            character = hangulcharacters.double_consonant[character_index]
            print(menusandtextblocks.bar)
            print(" " * 19, character)
            print(menusandtextblocks.bar)
            hangul_guess = input("このハングルのローマ字を入れてみよう: ").strip().lower()
            if hangul_guess == hangulcharacters.double_consonant_romanized[character_index]:
                print(f"{hangul_guess}は正解！")
                score += 1
            elif hangul_guess.strip().lower() == "stop":
                if score == 0:
                    break
                print(f"最終得点は{score}/{iterations}!"
                      f"約{float((score / iterations) * 100).__round__()}%です！")
                break
            else:
                print(f"{hangul_guess}は不正解！正解だったのは、"
                      f"{hangulcharacters.vowels_romanized[character_index]}！")
        print(menusandtextblocks.bar)
        print(f"スコア: {score}")
        iterations += 1
