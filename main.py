import random as rd
import time

def main():
    coins = int(100)
    while True:
        if coins <= 0:
            print("You lost all your money, haha")
            exit()

        slotQuery = input(f"Do you want to play? You have {int(coins)} coins(y/n)[y] ").strip().lower()
        if slotQuery == "" or slotQuery == "y":
            try:
                betAmount = int(input(f"How much do you want to bet?"))
                if betAmount > coins:
                    print("You can't bet more then you have, fucking cheater")
                    continue
            except ValueError:
                print("You must put a number in")
                continue

            emojiList = ["🤠", "💀", "💩", "🤡", "👽", "👾", "💥", "🦫", "🐧", "🍆"]
            for n in range(100):
                randNum = rd.randint(0, 9)
                randNum2 = rd.randint(0, 9)
                randNum3 = rd.randint(0, 9)
                print(f"\r╔--------------------╗\n|    \033[91m*     *    *\033[0m    |\n|  [ {emojiList[randNum]} | {emojiList[randNum2]} | {emojiList[randNum3]} ]  |\n╚--------------------╝", end="")
                print("\033[3A", end="")  # Cursor 3 Zeilen nach oben (für die Rahmenhöhe)
                time.sleep(0.01 + n/600)

            # Nach der Schleife: Rahmen und Ergebnis anzeigen
            print(f"\r╔--------------------╗\n|    \033[91m*     *    *\033[0m    |\n|  [ {emojiList[randNum]} | {emojiList[randNum2]} | {emojiList[randNum3]} ]  |\n╚--------------------╝")
            randNums = [randNum, randNum2, randNum3]
            randNums_sorted = sorted(randNums)

            if randNum + randNum2 + randNum3 == 27:
                coins += betAmount *3
                print("Hot Ding Dong! 🍆")
            elif randNums_sorted[0] == randNums_sorted[1] == randNums_sorted[2]:
                coins += betAmount * 2
                print("You won (three equal slots)")
            elif randNums_sorted[0] == randNums_sorted[1] or randNums_sorted[1] == randNums_sorted[2]:
                coins += betAmount / 2
                print("You won half (two equal slots)")
            else:
                coins -= betAmount
                print("You lost")
        elif slotQuery == "n":
            print("Good bye")
            exit()
        else:
            print("You must put in y/enter or n, lol")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGood bye")