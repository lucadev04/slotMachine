import random as rd
import time

def main():
    coins = 100
    while True:
        if coins == 0:
            print("You lost all your money, haha")
            exit()
        slotQuery = input(f"Do you want to play(1 coin per throw)? You have {coins} coins(y/n)")
        if slotQuery == "y":
            emojiList = ["🤠", "💀", "💩", "🤡", "👽", "👾", "💥", "🦫", "🐧", "🍆"]
            for n in range(100):
                randNum = rd.randint(0, 9)
                randNum2 = rd.randint(0, 9)
                randNum3 = rd.randint(0, 9)
                print(f"\r[ {emojiList[randNum]} | {emojiList[randNum2]} | {emojiList[randNum3]} ]  ", end="", flush=True)
                time.sleep(0.01+n/600)
            print("\n")
            randNums = [randNum, randNum2, randNum3]
            randNums_sorted = sorted(randNums)
            if randNum+randNum2+randNum3 == 27:
                coins += 1000
                print("Hot Ding Dong!🍆")

            if randNums_sorted[0] == randNums_sorted[1] == randNums_sorted[2]:
                coins += 100
                print("You won (three equal slots)")
            elif randNums_sorted[0] == randNums_sorted[1] or randNums_sorted[1] == randNums_sorted[2]:
                coins += 10
                print("You won half (two equal slots)")
            else:
                coins -= 1
                print("You lost")
        elif slotQuery == "n":
            print("Good bye")
            exit()
        else:
            print("You must put in y or n, lol")


if __name__ == "__main__":
    main()