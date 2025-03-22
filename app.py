import time, pet, budgeter 
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
currentPet = None
currentBudgeter = None
currentGoalWeekly = None
inLoop = True

@app.route("/")
def index():
     return render_template('index.html')

@app.route("/pet")
def start():
    if (currentPet is None):
            return redirect("/newpet")
            
    name = currentPet.getName()
    age = currentPet.getAge()
    points = currentPet.getHealthPoints()
    status = currentPet.getHealthStatus()
    species = currentPet.getSpecies()

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"HP: {points}")
    print(f"Your pet's status is: {status}")
    return render_template('pet.html', name=name, age=age, points=points, status=status, species=species)

@app.route("/newpet", methods=['GET'])
def newpet():
    data = request.form
    return render_template('newpet.html')


@app.route("/petForm", methods=['POST'])
def petForm():
     data = request.form
     global currentPet
     initName = data['name']
     initSpecies = data['species']
     currentPet = pet.Pet(initName, 0, 100, "" ,initSpecies )
     name = currentPet.getName()
     age = currentPet.getAge()
     points = currentPet.getHealthPoints()
     status = currentPet.getHealthStatus()
     species = currentPet.getSpecies()

     global currentBudgeter
     initGoal = data['savingsGoal']
     
     return render_template('pet.html', name=name, age=age, points=points, status=status, species=species)


if __name__ == '__main__':
    app.run()