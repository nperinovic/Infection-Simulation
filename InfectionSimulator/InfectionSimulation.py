from Gathering import *
from Person import *
import turtle

def main():
    turt = turtle
    gather = Gathering()
    infectious, packed = gather.prompt()
    gather.initializeGathering(infectious, packed)
    gather.initialInfectedPerson()
    turtle.setworldcoordinates(0, 0, 20, 20)
    gather.redraw()

    while True:
        gather.update()
        gather.peopleMoving()
        gather.redraw()
        first = gather.getGathering()
        first_person = first[1]
        if gather.everyoneInfected():
            break


main()
