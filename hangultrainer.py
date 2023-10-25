import menusandtextblocks
import OptionsBranchFunctions
import OptionsBranchFunctionsJP

while True:
    print(menusandtextblocks.language_select)
    choice = input("Enter choice/一つを選んでください: ").strip()
    if choice == "1":
        OptionsBranchFunctions.initial_menu_loop()
    elif choice == "2":
        OptionsBranchFunctionsJP.initial_menu_loop_jp()
    elif choice == "3":
        print(menusandtextblocks.bar)
        print("Thank you for playing! See ya 👋\n遊んでいただいてありがとうございます！")
        print(menusandtextblocks.bar)
        break
    else:
        print("Please choose between 1 or 2. \n1か２のどちらかを選んでください。")
