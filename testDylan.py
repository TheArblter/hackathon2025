from flask import Flask
from random import randint
import time
import asyncio

# This mess will be cleaned soon enough
class Tama:

    def __init__(self, n):

        self.name = 'New Pet' if n == None else n
        self.age = 0
        self.score = 0
        self.life = 100
        self.species = ('cat', 'dog', 'fish')[randint(0, 2)] # <- nullified; too lazy to remove this

    def setScore(n):

        score = n
        return

app = Flask('Tamagotchi')


async def live(obj):

    while obj.life > 0:
        await record(obj)
        time.sleep(10_000)
        obj.life -= 1

    if obj.score > -1: # TODO! Find a way to store objects on the user's device, then compare scores
        return obj
    
    print(f'New pet! Care to name it? (Leave blank if no)')
    return Tama(input())

#@app.route("/")
async def record(obj):
    print(f'<p>Pet stats: </br>Name: {obj.name} </br>Age: {obj.age} </br>species: {obj.species} </br>Score: {obj.score}</p>') #print() for now; should reroute to the site later

def main():

    current = Tama(str(input()))
    best = live(current)
    record(current)
    record(best)
    
    main()

print('New Pet! Care to name it? (Leave blank if no)')   
asyncio.run(main())