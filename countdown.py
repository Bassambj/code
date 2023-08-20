# COUNTDOWN - BY Bassam Basil Junior
import os
import time

def clear(): os.system('cls')
def pause(): os.system('pause')

clear()

score = 0

try:
    def countdown():
        score = int(input("Set start above zero: "))
        if (score>0):
            for score in range(score,0,-1):
                clear()
                print("[",score,"]")
                time.sleep(1)
            clear()
            print("[",score-1,"]")
        else:
            print("Erro. Informed number: ",score)
            pause()
            clear()

except Exception:
    print("Exception.")

countdown()
