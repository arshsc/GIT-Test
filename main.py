# Holds user interface, runs the program

from Creator import char_Creator



def main():
    choice = input("\n1. Create a Character\n\n2. Exit\n\n")

    if choice == "1":
        char_Creator()
    else:
        pass


main()