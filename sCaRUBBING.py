#Programmer's Note: This was one of my very first projects, written during my introduction to programming (2021 Pre-AI era).
# I'm keeping it as a milestone, a reminder of where I started.

import os
# Global variables to maintain state
matrix = []  # The drawing grid
size = 0  # Size of the NxN matrix
coordinates = [0, 0]  # Current position [row, column]
direction = "row+"  # Current direction: "row+" (right), "row-" (left), "column+" (down), "column-" (up)
brush = "up"  # Brush state: "up" (not drawing) or "down" (drawing)
finish = 0  # Flag to terminate the program

def turn_right():
    """Rotate the vehicle 90 degrees clockwise"""
    global direction
    if direction == "row+":
        direction = "column+"
    elif direction == "column+":
        direction = "row-"
    elif direction == "row-":
        direction = "column-"
    elif direction == "column-":
        direction = "row+"

def turn_left():
    """Rotate the vehicle 90 degrees counter-clockwise"""
    global direction
    if direction == "row+":
        direction = "column-"
    elif direction == "column-":
        direction = "row-"
    elif direction == "row-":
        direction = "column+"
    elif direction == "column+":
        direction = "row+"

def reverse():
    """Reverse the vehicle direction (180 degrees)"""
    global direction
    if direction == "row+":
        direction = "row-"
    elif direction == "column-":
        direction = "column+"
    elif direction == "row-":
        direction = "row+"
    elif direction == "column+":
        direction = "column-"

def move(direct, step, brush):
    """Move the vehicle in the current direction for a specified number of steps"""
    count = 0
    global matrix
    global coordinates
    global size
    
    # Optimize step count for large movements
    if step > size:
        step = (step % size) + size
    
    while count < step:
        # Mark current position if brush is down
        if brush == "down":
            matrix[coordinates[0]][coordinates[1]] = "*"
        
        # Move in the current direction
        if direct == "row+":
            coordinates[1] = coordinates[1] + 1
        if direct == "row-":
            coordinates[1] = coordinates[1] - 1
        if direct == "column+":
            coordinates[0] = coordinates[0] + 1
        if direct == "column-":
            coordinates[0] = coordinates[0] - 1
        
        # Handle wrapping (toroidal topology)
        if coordinates[0] == -1:
            coordinates[0] = size - 1
        if coordinates[0] == size:
            coordinates[0] = 0
        if coordinates[1] == -1:
            coordinates[1] = size - 1
        if coordinates[1] == size:
            coordinates[1] = 0
        
        count += 1
    
    # Mark final position if brush is down
    if brush == "down":
        matrix[coordinates[0]][coordinates[1]] = "*"

def jump(direct):
    """Jump 3 cells forward and automatically lift the brush"""
    global matrix
    global coordinates
    global brush
    
    # Automatically lift brush after jump
    brush = "up"
    
    # Jump 3 cells in the current direction
    if direct == "row+":
        coordinates[1] = coordinates[1] + 3
    if direct == "row-":
        coordinates[1] = coordinates[1] - 3
    if direct == "column+":
        coordinates[0] = coordinates[0] + 3
    if direct == "column-":
        coordinates[0] = coordinates[0] - 3
    
    # Handle wrapping for jump
    if coordinates[0] >= size:
        coordinates[0] = coordinates[0] - size
    if coordinates[1] >= size:
        coordinates[1] = coordinates[1] - size
    if coordinates[0] < 0:
        coordinates[0] = size + coordinates[0]
    if coordinates[1] < 0:
        coordinates[1] = size + coordinates[1]

def view(table, size):
    """Display the matrix with a border frame"""
    plus = ["+" for y in range(size)]
    table.insert(0, plus)  # Add top border
    table.append(plus)  # Add bottom border
    for s in table:
        print("+", *s, end="+\n", sep="")

def main():
    """Main program loop"""
    global coordinates
    global brush
    global direction
    global size
    global matrix
    global finish
    
    # Initialize global variables
    matrix = []
    size = 0
    finish = 0
    
    # Main program loop
    while finish == 0:
        # Reset initial state
        coordinates = [0, 0]
        direction = "row+"
        brush = "up"
        
        # Display instructions and get user input
        inputs = input("<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3.VEHICLE ROTATES RIGHT\n4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEW THE MATRIX\n0. EXIT\nPlease enter the commands with a plus sign (+) between them.\n")
        
        # Parse commands
        commands = inputs.split("+")
        size = int(commands[0])  # First value is the matrix size
        matrix = [[" "] * size for k in range(size)]  # Create NxN matrix filled with spaces
        commands.pop(0)  # Remove size from command list
        
        # Process each command
        for i in commands:
            if i == "1":
                # Command 1: Lower the brush
                brush = "down"
                matrix[coordinates[0]][coordinates[1]] = "*"
            elif i == "2":
                # Command 2: Lift the brush
                brush = "up"
            elif i == "3":
                # Command 3: Turn right
                turn_right()
            elif i == "4":
                # Command 4: Turn left
                turn_left()
            elif i[0] == "5":
                # Command 5_X: Move X steps forward
                stepal = i.split("_")
                move(direction, int(stepal[1]), brush)
            elif i == "6":
                # Command 6: Jump 3 cells
                jump(direction)
            elif i == "7":
                # Command 7: Reverse direction
                reverse()
            elif (i != "0") and (i != "8"):
                # Invalid command - clear screen and restart
                os.system("clear")
                print("You entered an incorrect command. Please try again!")
                main()
                break
            elif i == "8":
                # Command 8: Display the matrix
                view(matrix, size)
            elif i == "0":
                # Command 0: Exit program
                finish = 1
                break

# Start the program
main()