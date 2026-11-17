# This is a sample Python script.
import copy
from enum import IntEnum
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class spheres(IntEnum):
    EMPTY = 0
    RING = 1
    BLUE = 2
    RED = 3
    BUMPER = 4

class action(IntEnum):
    NOTHING = 0
    TURNLEFT = 1
    TURNRIGHT = 2
    JUMP = 3

class facing(IntEnum):
    UP=0
    RIGHT=1
    DOWN = 2
    LEFT = 3


player_position = [2, 30]

def setupArray():
    game_array_l = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 2, 4, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4, 2, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 4, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 4, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 2, 4, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4, 2, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 2, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 4, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 4, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 4, 4, 2, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 2, 4, 4, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    ]
    # TODO add more maps/better way of making maps (me)
    global rings_left
    rings_left = 64
    # Use a breakpoint in the code line below to debug your script.
    # make a 32x32 array, fill it with points
    # precalculate amount of rings needed for a perfect or just set it
    return game_array_l

def resolveCurrentSpace(affected_space):
    global game_array
    global rings_left
    xg = affected_space[0]
    yg = affected_space[1]
    if game_array[yg][xg] == spheres.RED:
        print("Touched a red sphere (dont do that)")
        quit()
    #print(f"current space {xg} {yg} {game_array[yg][xg]}")
    if game_array[yg][xg] == 2:
        game_array[yg][xg] = 3
        convertLoopsToRings(affected_space)
    if game_array[yg][xg] == spheres.RING:
        game_array[yg][xg] = spheres.EMPTY
        rings_left -= 1
    if game_array[yg][xg] == spheres.BUMPER:
        if player_facing == facing.UP:
            player_position[1]+=1
        elif player_facing == facing.DOWN:
            player_position[1]-=1
        elif player_facing == facing.LEFT:
            player_position[0] += 1
        elif player_facing == facing.RIGHT:
            player_position[0]-=1

def countSpheresRemaining():
    global game_array
    remaining = 0
    for i in game_array:
        for j in i:
            if j == spheres.BLUE or j == 2:
                remaining += 1
    return remaining


def spheresToRings(list):
    topleft = list[0]
    topright = list[0]
    botleft = list[0]
    botright = list[0]
    for i in list:
        if game_array[i[1]][i[0]] == spheres.BLUE:
            return

        if i[0] >= topright[0] and i[1] <= topright[1]:
            topright = i

        if i[0] <= topleft[0] and i[1] <= topleft[1]:
            topleft = i

        if i[0] >= botright[0] and i[1] >= botright[1]:
            botright = i

        if i[0] <= botleft[0] and i[1] >= botleft[1]:
            botleft = i


    #grab the highest 2/lowest 2 corners
    invertx = False
    inferty = False
    if abs(topleft[0]-topright[0]) <16:
        pass #check for blue spheres in specified areas
    else:
        invertx = True
    if abs(botleft[1] - topleft[1]) < 16:
        pass
    else:
        inverty = True#TODO fail ring check if blue spheres arent in any of the corners

    if invertx:
        pass
    else:
        if game_array[topleft[1]+1][topleft[0]+1] != spheres.BLUE:
            return
        if game_array[topright[1]+1][topright[0]-1] != spheres.BLUE:
            return
        if game_array[botleft[1]-1][botleft[0]+1] != spheres.BLUE:
            return
        if game_array[botright[1]-1][botright[0]-1] != spheres.BLUE:
            return

    floodstart = copy.deepcopy(topleft)
    floodstart[0]+= 1
    floodstart[1]+= 1
    floodFillRings(floodstart)

    #if the difference is more than 16,check opposite side for a blue sphere
    #look towards center to start flood filling blue spheres with rings
    #if we dont find one at EVERY corner, dont fill rings



    for i in list:
        game_array[i[1]][i[0]] = spheres.RING


def floodFillRings(start):
    newstart = start
    game_array[start[1]][start[0]] = spheres.RING
    if game_array[start[1]][start[0]+1] == spheres.BLUE:
        newstart[0]+=1
        floodFillRings(newstart)
        newstart[0]-=1
    if game_array[start[1]][start[0] - 1] == spheres.BLUE:
        newstart[0]-=1
        floodFillRings(newstart)
        newstart[0]+=1


    if game_array[start[1]+1][start[0]] == spheres.BLUE:
        newstart[1]+=1
        floodFillRings(newstart)
        newstart[1]-=1

    if game_array[start[1]-1][start[0]] == spheres.BLUE:
        newstart[1]-=1
        floodFillRings(newstart)
        newstart[1]+=1




def convertLoopsToRings(starting_space):
    points_in_loop.append(starting_space)
    start_copy = copy.deepcopy(starting_space)
    start_copy[1]-=1
    recursiveRingCheck(starting_space,start_copy,action.NOTHING,facing.UP)#UP

    start_copy = copy.deepcopy(starting_space)
    start_copy[1]+=1
    recursiveRingCheck(starting_space,start_copy,action.NOTHING,facing.DOWN)#DOWN

    start_copy = copy.deepcopy(starting_space)
    start_copy[0]+=1
    recursiveRingCheck(starting_space,start_copy,action.NOTHING,facing.RIGHT)#RIGHT

    start_copy = copy.deepcopy(starting_space)
    start_copy[0]-=1
    recursiveRingCheck(starting_space,start_copy,action.NOTHING,facing.LEFT)#LEFT



def recursiveRingCheck(starting_space,current_space,last_action,last_direction):
    if current_space == starting_space:
        spheresToRings(points_in_loop)
    if game_array[current_space[1]][current_space[0]] != spheres.RED:
        return
    if current_space in points_in_loop:
        #print(f"point already in loop {current_space}")
        return
    #print(f"new point: {current_space}")
    points_in_loop.append(current_space)
    # check direction
    if last_direction == facing.UP:

        if game_array[current_space[1]-1][current_space[0]] == 3:
            start_copy = copy.deepcopy(current_space)
            start_copy[1] -=1
            recursiveRingCheck(starting_space, start_copy, action.NOTHING, facing.UP)

        if game_array[current_space[1]][current_space[0]-1] == 3:
            if last_action != action.TURNLEFT:
                start_copy = copy.deepcopy(current_space)
                start_copy[0] -= 1
                recursiveRingCheck(starting_space, start_copy, action.TURNLEFT, facing.LEFT)

        if game_array[current_space[1]][current_space[0]+1] == 3:
            if last_action != action.TURNRIGHT:
                start_copy = copy.deepcopy(current_space)
                start_copy[0] += 1
                recursiveRingCheck(starting_space, start_copy, action.TURNRIGHT, facing.RIGHT)

    if last_direction == facing.DOWN:
        if game_array[current_space[1]+1][current_space[0]] == spheres.RED:
            start_copy = copy.deepcopy(current_space)
            start_copy[1] += 1
            recursiveRingCheck(starting_space, start_copy, action.NOTHING, facing.DOWN)

        if game_array[current_space[1]][current_space[0]-1] == spheres.RED:
            if last_action != action.TURNRIGHT:
                start_copy = copy.deepcopy(current_space)
                start_copy[0] -= 1
                recursiveRingCheck(starting_space, start_copy, action.TURNRIGHT, facing.LEFT)

        if game_array[current_space[1]][current_space[0]+1] == spheres.RED:
            if last_action != action.TURNLEFT:
                start_copy = copy.deepcopy(current_space)
                start_copy[0] += 1
                recursiveRingCheck(starting_space, start_copy, action.TURNLEFT, facing.RIGHT)

    if last_direction == facing.LEFT:
        if game_array[current_space[1]][current_space[0]-1] == spheres.RED:
            start_copy = copy.deepcopy(current_space)
            start_copy[0] -= 1
            recursiveRingCheck(starting_space, start_copy, action.NOTHING, facing.LEFT)

        if game_array[current_space[1]+1][current_space[0]] == spheres.RED:
            if last_action != action.TURNLEFT:
                start_copy = copy.deepcopy(current_space)
                start_copy[1] += 1
                recursiveRingCheck(starting_space, start_copy, action.TURNLEFT, facing.DOWN)

        if game_array[current_space[1]-1][current_space[0]] == spheres.RED:
            if last_action != action.TURNRIGHT:
                start_copy = copy.deepcopy(current_space)
                start_copy[1] -= 1
                recursiveRingCheck(starting_space, start_copy, action.TURNRIGHT, facing.UP)


    if last_direction == facing.RIGHT:
        if game_array[current_space[1]][current_space[0]+1] == spheres.RED:
            start_copy = copy.deepcopy(current_space)
            start_copy[0] += 1
            recursiveRingCheck(starting_space, start_copy, action.NOTHING, facing.RIGHT)

        if game_array[current_space[1]+1][current_space[0]] == spheres.RED:
            if last_action != action.TURNRIGHT:
                start_copy = copy.deepcopy(current_space)
                start_copy[1] += 1
                recursiveRingCheck(starting_space, start_copy, action.TURNRIGHT, facing.DOWN)


        if game_array[current_space[1]-1][current_space[0]] == spheres.RED:
            if last_action != action.TURNLEFT:
                start_copy = copy.deepcopy(current_space)
                start_copy[1] -= 1
                recursiveRingCheck(starting_space, start_copy, action.TURNLEFT, facing.UP)

    points_in_loop.pop()
    #print(f"removed point {current_space}")




def moveForward():
    global player_facing
    #global player_position
    match player_facing:
        case facing.UP:
            player_position[1] -=1
            player_position[1] %= 32
        case facing.RIGHT:
            player_position[0] += 1
            player_position[0] %= 32
        case facing.DOWN:
            player_position[1] +=1
            player_position[1] %= 32
        case facing.LEFT:
            player_position[0] -= 1
            player_position[0] %= 32

def decideAction():
    decision = input(f"SPHERES:{countSpheresRemaining()} RINGS:{rings_left} INPUT:")

    if "l" in decision:
        return action.TURNLEFT
    if "r" in decision:
        return action.TURNRIGHT
    if "j" in decision:
        return action.JUMP
    return action.NOTHING
    #TODO add AI that makes the descision
    # game_array is a 2d list of spheres enums with the format [Y,X] (because i coded it wrong)
    # player_facing is an enum
    # time_taken is for scoring the AI
    # rings_left for pefects

def mainLoop(wait_time, use_visuals, perfect_rings):
    #most inputs to this function are unused
    global game_array
    global player_facing
    #global player_position
    time_taken = 0 # turning + moving costs 2, going straight costs 1
    perfect = False
    completed = False
    jumping = 0
    # setup performance evaluators, ie steps moved/cost, ring/sphere amount
    while True:
        #print frame to console
        x = 0
        y = 0
        for i in game_array:
            for j in i:
                if x == player_position[0] and y == player_position[1]:
                    match player_facing:
                        case facing.UP:
                            print(f"{LBLUE}^", end="")
                        case facing.DOWN:
                            print(f"{LBLUE}v", end="")
                        case facing.RIGHT:
                            print(f"{LBLUE}>", end="")
                        case facing.LEFT:
                            print(f"{LBLUE}<", end="")
                        case _:
                            pass

                elif j == 3:
                    print(f"{RED}O", end="")
                elif j == 2:
                    print(f"{BLUE}O", end="")
                elif j == 1:
                    print(f"{YELLOW}o", end="")
                elif j == 4:
                    print(f"{WHITE}X", end="")

                else:
                    print(f" ", end="")
                x += 1
            y += 1
            x = 0

            print("")

        if jumping >0:
            moveForward()
            jumping -= 1
            if jumping != 0:
                continue
        else:# decide what to do based on current state (not my problem)
          match decideAction():
            case action.NOTHING:
                moveForward()
                time_taken += 1
            case action.TURNLEFT:
                player_facing -= 1
                if player_facing <0:
                    player_facing+=4
                moveForward()
                time_taken += 2
            case action.TURNRIGHT:
                player_facing += 1
                player_facing %= 4
                moveForward()
                time_taken += 2
            case action.JUMP:
                jumping = 1
                moveForward()
                continue
            case _:
                moveForward()
        # move player based on what was decided/force movement for jumping
        currentpos = player_position
        resolveCurrentSpace(currentpos)
        # check current map for things such as:
        # if not jumping:
        #   if on red, lose
        #   if on blue, turn it red
        #   if on ring, collect it
        #   bonus: if on yellow, set up jump x5
        #   if bumper, go back, im not implementing

        if countSpheresRemaining() == 0:
            completed = True
            break
        # check for spheres that need to turn into rings
        # check for victory (0 blue remaining)

        # process visuals if needed
        # vsync/wait
    if rings_left == 0:
        perfect = True
    return time_taken,perfect,completed

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global game_array
    rings_left = 0

    player_facing = facing.UP
    points_in_loop = []
    WHITE = "\033[37m"
    RED = "\033[31m"
    LBLUE= "\033[94m"
    BLUE = "\033[1;34m"

    YELLOW = "\033[33m"
    game_array = setupArray()
    mainLoop(0,True,12)

    #TODO cleanup or print more info here

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
