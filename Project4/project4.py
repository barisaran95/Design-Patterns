from Arena import *

def main():
    game = Arena()

    while(len(game.gladiators)>1):
        game.round()

if(__name__ == "__main__"):
    main()