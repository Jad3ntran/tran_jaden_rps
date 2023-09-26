# This file was created by: Jaden Tran

'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

Sources:
https://www.geeksforgeeks.org/turtle-onclick-function-in-python/


'''
# import package
import turtle
from turtle import *
from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# Define the choices for rock-paper-scissors
rps_choices = ["rock", "paper", "scissors"]

# Setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# Setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 196
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170

# Setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# Canvas object
cv = screen.getcanvas()
# Hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# Setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# Instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# Setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# Instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# Setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# Instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

def show_rock(x, y):
    # Add the rock image as a shape
    screen.addshape(rock_image)
    # Attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # Remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # Set the position of the rock_instance
    rock_instance.setpos(x, y)

def show_paper(x, y):
    # Add the paper image as a shape
    screen.addshape(paper_image)
    # Attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # Remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # Set the position of the paper_instance
    paper_instance.setpos(x, y)

def show_scissors(x, y):
    # Add the scissors image as a shape
    screen.addshape(scissors_image)
    # Attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # Remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # Set the position of the scissors_instance
    scissors_instance.setpos(x, y)

# Instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# This function uses an x y value, an obj, and width and height 
def collide(x, y, obj, w, h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# Function to handle mouse click
def mouse_pos(x, y):
    if collide(x, y, rock_instance, rock_w, rock_h):
        # Display the user's choice
        text.clear()
        text.write("You chose rock!", False, "left", ("Arial", 24, "normal"))
        # Get the CPU's random choice
        cpu_choice = rps_choices[randint(0, len(rps_choices) - 1)]
        # Determine and display the result of the game
        result = evaluate("rock", cpu_choice)
        text.goto(0, -50)
        text.write(f"Result: {result}", False, "center", ("Arial", 24, "normal"))
        # Display the CPU's choice in interface
        text.goto(0, -100)
        text.write(f"CPU chose {cpu_choice}!", False, "center", ("Arial", 24, "normal"))
        # Hide the options that were not chosen (paper and scissors)
        paper_instance.hideturtle()
        scissors_instance.hideturtle()

    elif collide(x, y, paper_instance, paper_w, paper_h):
        # Display the user's choice
        text.clear()
        text.write("You chose paper!", False, "left", ("Arial", 24, "normal"))
        # Get the CPU's random choice
        cpu_choice = rps_choices[randint(0, len(rps_choices) - 1)]
        # Determine and display the result of the game
        result = evaluate("paper", cpu_choice)
        text.goto(0, -50)
        text.write(f"Result: {result}", False, "center", ("Arial", 24, "normal"))
        # Display the CPU's choice in interface
        text.goto(0, -100)
        text.write(f"CPU chose {cpu_choice}!", False, "center", ("Arial", 24, "normal"))
        # Hide the options that were not chosen (rock and scissors)
        rock_instance.hideturtle()
        scissors_instance.hideturtle()

    elif collide(x, y, scissors_instance, scissors_w, scissors_h):
        # Display the user's choice
        text.clear()
        text.write("You chose scissors!", False, "left", ("Arial", 24, "normal"))
        # Get the CPU's random choice
        cpu_choice = rps_choices[randint(0, len(rps_choices) - 1)]
        # Determine and display the result of the game
        result = evaluate("scissors", cpu_choice)
        text.goto(0, -50)
        text.write(f"Result: {result}", False, "center", ("Arial", 24, "normal"))
        # Display the CPU's choice
        text.goto(0, -100)
        text.write(f"CPU chose {cpu_choice}!", False, "center", ("Arial", 24, "normal"))

        # Hide the options that were not chosen (rock and paper)
        rock_instance.hideturtle()
        paper_instance.hideturtle()

    else:
        print("Choose something you fool!!")

text.setpos(0, 150)
text.write("Choose rock, paper, or scissors", False, "center", ("Arial", 24, "normal"))

# Function to evaluate the game result- whether user wins, loses, or ties with CPU
def evaluate(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and cpu_choice == "scissors")
        or (player_choice == "paper" and cpu_choice == "rock")
        or (player_choice == "scissors" and cpu_choice == "paper")
    ):
        return "Player wins!"
    else:
        return "CPU wins!"

# Use this to get mouse position
screen.onclick(mouse_pos)

# Runs mainloop for Turtle - required to be last
screen.mainloop()
