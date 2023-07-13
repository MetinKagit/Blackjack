import functions
import logo

if __name__ == '__main__':
    print(logo.logo)
    functions.core_game()

    while input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
        print("""
        ================================
           ***** NEW GAME START *****
        ================================
        """)
        functions.core_game()