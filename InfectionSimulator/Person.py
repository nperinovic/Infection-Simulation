import random
import turtle

class Person():
    def __init__(self, infected = False, x = 0, y = 0):
        #initialize the person with update variables
        self.infected = infected
        self.x = x
        self.y = y

    def infection(self, i):
        #used to update a person's infected variable
        self.infected = i

    def getInfected(self):
        #returns infected value for each person T/F
        return self.infected

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def move(self, randomMovement, gathering):
        #Moves a person based on a random number and a specific gathering
        xy = int(random.uniform(0, 100)) % 2 == 0
        addToX = self.x + randomMovement
        addToY = self.y + randomMovement
        if(xy):
            self.setX(addToX)
        elif(not xy):
            self.setY(addToY)

    def inRangeToGetInfected(self, otherPerson, infectious):
        #checks to see if two people are in the range to get infected
        if (self.x - otherPerson.x) > -1*infectious and (self.x - otherPerson.x) < infectious and (self.y - otherPerson.y) > -1*infectious and (self.y - otherPerson.y) < infectious:
            return True
        else:
            return False


    def draw(self):
        #Draws each person
        turt = turtle
        turt.hideturtle()
        turt.penup()
        turt.setpos(self.x, self.y)
        turt.shape('turtle')
        if(self.infected == True):
            turt.color('red')
        else:
            turt.color('blue')
        turt.shapesize(0.5)
        turt.stamp()
