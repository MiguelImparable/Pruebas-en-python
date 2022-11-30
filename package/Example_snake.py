# Un programa sobre jugar al SNAKE
import os
import random
import readchar


def Example_snake():
    os.system("cls")
    print("\nExercise for Example snake")
    print("let's play snake")
    enter = input("\nPresiona ENTER para continuar: ")
    os.system("cls")

    # Constants
    POS_X = 0
    POS_Y = 1
    MAP_WIDTH = 20
    MAP_HEIGHT = 15
    NUM_MAP_OBJECTS = 11

    # Variables
    my_position = [3, 1]
    tail_length = 0
    map_objects = []
    tail = []
    end_game = False
    died = False
    score = 0

    # Create obstacle map
    obstacle_definition = """\
########   #########
                    
###   ########   ###
                    
###########       ##
                    
#######            #
                    
####       #########
                    
                    
#                ###
                    
#                  #
########   #########\
"""
    obstacle_definition = [list(row)for row in obstacle_definition.split("\n")]

    # Min Loop
    while not end_game:

        # Generate random objects on the map
        while len(map_objects) < NUM_MAP_OBJECTS:
            new_position = [random.randint(
                0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
            map_objects.append(new_position)

            if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y][POS_X] != "#"]:
                map_objects.append(new_position)

        # Generate map
        print("+" + ("-"*(MAP_WIDTH*3)) + "+")
        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")
            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = "   "
                object_in_cell = None
                tail_in_cell = None

                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = " * "
                        object_in_cell = map_object

                for tail_piece in tail:
                    if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                        char_to_draw = "|||"
                        tail_in_cell = tail_piece

                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "|||"

                    if object_in_cell:
                        map_objects.remove(object_in_cell)
                        tail_length += 1
                        score += 10

                    if tail_in_cell:
                        end_game = True
                        died = True

                    if obstacle_definition[coordinate_y][coordinate_x] == "#":
                        char_to_draw = "###"

                # Draw
                print(f"{char_to_draw}", end="")

            print("|")
        print("+" + ("-"*(MAP_WIDTH*3)) + "+")

        print("")
        print(f"SCORE: {score} - MY POSITION {my_position}")

    # Buttons=
        new_position = None
        # Ask user where he wants to move
        direction = (readchar.readchar().decode())
        os.system("cls")

        if direction == "w":
            new_position == [my_position[POS_X],
                             (my_position[POS_Y] - 1) % MAP_WIDTH]

        elif direction == "s":
            new_position == [my_position[POS_X],
                             (my_position[POS_Y] + 1) % MAP_WIDTH]

        elif direction == "a":
            new_position == [(my_position[POS_X] - 1) %
                             MAP_WIDTH, my_position[POS_Y]]

        elif direction == "d":
            new_position == [(my_position[POS_X] + 1) %
                             MAP_WIDTH, my_position[POS_Y]]

        elif direction == "q":
            end_game = True

        if new_position:
            if obstacle_definition[new_position[POS_Y], new_position[POS_X]] != "#":
                tail.insert(0, my_position.copy())
                tail = tail[:tail_length]
                my_position = new_position
                score += 1

    if died:
        print("W  A  S  T  E  D")
        print(f"SCORE: {score}")

    print("\nEnd of program\n")


if __name__ == "__main__":
    Example_snake()
