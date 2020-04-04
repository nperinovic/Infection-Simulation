import turtle
from Person import *
import random


class Gathering():
    def __init__(self):
        #Initialize the gathering list. Will hold the Person objects
        self.gathering = []

    def initializeGathering(self, rateOfInfect, howPacked):
        #initialize the gathering
        #will initialize rateOfInfection and howPacked variables
        #will also intialize all the People objects in the list
        self.rateOfInfect = rateOfInfect
        self.howPacked = howPacked
        for i in range(25):
            for j in range(25):
                randomNum = random.uniform(0, 101)
                if(randomNum <= self.howPacked*10 + 50):
                    person = Person(False, i, j)
                    self.addToGathering(person)
                else:
                    self.addToGathering(None)

    def prompt(self):
        #Promp used to ask user how packed, and what the rate of infection is
        howpacked = int(input('How packed is the gathering? (please enter a value between 1 - 5 with 5 being very packed): '))
        rateofinfect = float(input('How infectious is the disease? (please enter a float value between 0 and 2 with 2 being very infectious): '))
        return rateofinfect, howpacked



    def initialInfectedPerson(self):
        #Sets the first infected person in the gathering list
        list = []
        count = 0
        for person in self.gathering:
            if person is not None:
                list+=[count]
            count += 1
        num = random.randint(0, len(list) - 1)
        infected = list[num]
        self.gathering[infected].infection(True)

    def samePosition(self, person):
        #checks to see if two people are in the same position
        #returns True if there are two in the same spot, False otherwise
        for p in self.gathering:
            if p != None and person != None:
                if p is person:
                    continue
                elif p.x == person.x and p.y == person.y:
                    return True
        return False

    def peopleMoving(self):
        #calls the move() function in Person to update the coordinates for each person
        for person in self.gathering:
            randomMovement = random.uniform(-1, 1)
            if person != None:
                person.move(randomMovement, self.gathering)

    def addToGathering(self, person):
        #function to add specified person to the gathering
        self.gathering.append(person)

    def getGathering(self):
        #function to return the gathering
        return self.gathering

    def everyoneInfected(self):
        #checks to see if everyone is infected. If so, the whole program will stop
        for person in self.gathering:
            if person != None and person.infected == False:
                return False
        return True

    def update(self):
        #checks to see if person is in range to get infected and updates the infection variable accordingly
        for person in self.gathering:
            if person != None and person.getInfected() == True:
                for w in self.gathering:
                    if w is not None and person.inRangeToGetInfected(w, self.rateOfInfect):
                        w.infection(True)



    def redraw(self):
        #used to draw the update gathering list
        turtle.clearstamps()
        turtle.tracer(0, 0)
        for person in self.gathering:
            if person != None:
                person.draw()
        turtle.update()
