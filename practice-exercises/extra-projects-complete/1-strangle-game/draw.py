from colors import COLORS


class Draw:
    def image(self, attemps, hide_word):
        print("====================")
        print(f"Intentos: {attemps}")
        print("====================")
        if(attemps == 6):
            print(" ---------------------")
            for _ in range(16):
                print(" |")
            print("__________")
        elif(attemps == 5):
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | -  -  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            for _ in range(11):
                print(" |")
            print("__________")

        elif(attemps == 4):
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | -  -  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            print(" |                     |   ")
            print(" |                     |   ")
            print(" |                     |   ")
            print(" |                     |   ")
            print(" |                     |   ")
            for _ in range(6):
                print(" |")
            print("__________")

        elif(attemps == 3):
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | -  -  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            print(" |                     |   ")
            print(" |                   / |   ")
            print(" |                 /   |   ")
            print(" |                /    |   ")
            print(" |                     |   ")
            for _ in range(6):
                print(" |")
            print("__________")

        elif(attemps == 2):
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | -  -  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            print(" |                     |   ")
            print(" |                   / | \\ ")
            print(" |                  /  |   \\ ")
            print(" |                 /   |     \\ ")
            print(" |                     |   ")
            for _ in range(6):
                print(" |")
            print("__________")

        elif(attemps == 1):
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | -  -  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            print(" |                     |   ")
            print(" |                   / | \\ ")
            print(" |                  /  |   \\ ")
            print(" |                 /   |     \\ ")
            print(" |                     |   ")
            print(" |                    /  ")
            print(" |                   /      ")
            print(" |                  /       ")
            for _ in range(3):
                print(" |")
            print("__________")

        elif(attemps == 0):
            print(
                f"{COLORS['FAIL']}GAME OVER - La palabra oculta es \"{hide_word}\"{COLORS['ENDC']}")
            print(" ---------------------")
            print(" |                     |")
            print(" |                     |")
            print(" |                  -------")
            print(" |                 | X  X  |")
            print(" |                 |   o   |")
            print(" |                  -------")
            print(" |                     |   ")
            print(" |                   / | \\ ")
            print(" |                  /  |   \\ ")
            print(" |                 /   |     \\ ")
            print(" |                     |   ")
            print(" |                    / \\")
            print(" |                   /   \\  ")
            print(" |                  /     \\ ")
            for _ in range(3):
                print(" |")
            print("__________")

    def hide_word(hideword):
        print("Palabra a buscar: ")
        print(hideword)
