import sys
import turtle
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def pythagorean_tree(turtle, length, angle, level):
    if level == 0:
        turtle.forward(level)
    else:
        turtle.forward(length)
        turtle.left(angle)
        pythagorean_tree(turtle, length * 0.7, angle, level - 1)
        turtle.right(2 * angle)
        pythagorean_tree(turtle, length * 0.7, angle, level - 1)
        turtle.left(angle)
        turtle.backward(length)

def get_recursion_level():
    while True:
        try:            
            recursion_level = int(input("\nEnter the level of recursion (an integer): "))
            return recursion_level
        
        except ValueError:
            print("\nPlease enter an integer")
        except KeyboardInterrupt:
            logging.info("\nProgram finished\n")
            sys.exit()
        
def main():

    recursion_level = get_recursion_level()

    turtle.speed(0)
    turtle.up()
    turtle.left(90)
    turtle.backward(200)
    turtle.down()
    turtle.color("purple")
    turtle.pensize(2)

    pythagorean_tree(turtle, 150, 35, recursion_level)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
