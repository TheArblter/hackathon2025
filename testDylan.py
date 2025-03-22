from flask import Flask
from random import randint
import time

# This mess will be cleaned soon enough

class Tama:

    def __init__(self, n):

        self.name = 'New Pet' if n == None else n
        self.age = 0
        self.score = 0
        self.life = 100

    def setScore(n):

        score = n
        return

app = Flask('Tamagotchi')


def live(obj):

    while obj.life > 0:
        record(obj) # this is why the program doesn't work, for anybody who is more experienced with asyncio than I (probably everybody)
        time.sleep(10_000)
        obj.life -= 1
        obj.age += 1

    if obj.score > -1: # TODO! Find a way to store objects on the user's device, then compare scores (change -1 to the actual score)
        return obj
    
    print(f'New pet! Care to name it? (Leave blank if no)')
    return Tama(input())

#@app.route("/")
def record(obj):

    print(f'<p>Pet stats: </br>Name: {obj.name} </br>Age: {obj.age} </br>Score: {obj.score}</p>')

def main():

    current = Tama(str(input()))
    best = live(current)
    record(current)
    record(best)
    
    main()

print('New Pet! Care to name it? (Leave blank if no)')   
main()