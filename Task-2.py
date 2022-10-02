ans_y = ["Yes", "Y", "yes", "y"]
ans_n = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

a1 = input(">>")

if a1 in ans_y:
    print("\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. Will you say (Yes / No)\n")

    a2 = input(">>")

    if a2 in ans_y:
        print("\nYou are an honest person. He was a thief & You won the Game")

    elif a2 in ans_n:
        print("\nYou helped a thief. Now, go to Jail. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif a1 in ans_n:
    print("\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n")

    a3 = input(">>")

    if a3 in ans_y:
        print("\nCongrats! He was a thief & You helped the police to catch him with your bravery.")

    elif a3 in ans_n:
        print("\nSorry! You are dead. He was a thief & He killed you. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")