import time
import random
import sys
from snake import snake_position
from ladder import ladder_position
max_val= 100
adding_delay= 0.2
dice=6

def roll_dice():
    time.sleep(adding_delay)
    dice_value = random.randint(1,dice)
    print('Its a ' + str(dice_value))
    return dice_value

def snake(old_val,new_val,player_name):
    print('* * S N A K E * *')
    print(player_name.title() + ' got bite by the snake.Therefore going down from ' + str(old_val) + ' to ' + str(new_val))

def ladder(old_val,new_val,player_name):
    print('- - L A D D E R - -')
    print(player_name.title() + ' climbed the ladder from ' + str(old_val) + ' to ' + str(new_val))

def snake_ladder(new_val,dice_value,player):
    time.sleep(adding_delay)
    old_val = new_val
    new_val = new_val + dice_value

    if new_val > max_val:
        print('You just need ' + str(max_val - old_val) + ' to win this game.')
        return old_val

    print('\n' + player+ ' moved from ' + str(old_val) + ' to ' + str(new_val))
    if new_val in snake_position:
        final_position = snake_position.get(new_val)
        snake(new_val, final_position, player)

    elif new_val in ladder_position:
        final_position = ladder_position.get(new_val)
        ladder(new_val, final_position,player)

    else:
        final_position = new_val

    return final_position

def check_win(player_name,pos):
    time.sleep(adding_delay)
    if max_val== pos:
        print(f' ***** Congratulations ***** \n {player_name.title()} won the game.')
        print('thank u for playing the game')
        sys.exit()

def name():
    player1= None
    while not player1:
        player1=input('Enter Player 1\'s Name : ')

    player2 = None
    while not player2:
        player2= input('Enter Player 2\'s Name : ')

    print(f'Welcome {player1.title()} and {player2.title()} to the \'SNAKE AND LADDER\' Game')
    return player1, player2

def play():
    name1, name2 = name()
    time.sleep(adding_delay)

    player1_loc= 0
    player2_loc= 0

    while True:
        time.sleep(adding_delay)
        x= input('\n' + name1.title() + '---> Press enter to roll the dice: ')
        print('---Dice Rolling---')
        dice = roll_dice()
        player1_loc = snake_ladder(player1_loc,dice,name1)
        check_win(name1, player1_loc)

        y= input('\n' + name2.title()+ '---> Press enter to roll the dice: ')
        print('---Dice Rolling---')
        dice= roll_dice()
        player2_loc = snake_ladder(player2_loc,dice,name2)
        check_win(name2, player2_loc)


if __name__ == '__main__':
    play()