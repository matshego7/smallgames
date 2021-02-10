print("Welcome to tictactoe")
print("By Matshego")
print("This is how you play")
print('''
 0 | 1 | 2  
---+---+---
 3 | 4 | 5  
---+---+---
 6 | 7 | 8
''')
print("""
Each block is represented by an integer 
from 0 to 8. When it is your turn to play
press the number on the keyboard and your
respective symbol ('x' or 'o') will go into 
that block. 

Please do not use any integers smaller than 0
or any integers larger than 8 as this will cause
an error and the game will crash. 
    """)
print("let the games begin")
#array to handle the game
game_array = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        
def gameOverveiw():
    
    print(' ') 
    print(' ')
    print('Game Board Positions') 
    print(' 0 | 1 | 2 ') 
    print('---+---+---')
    print(' 3 | 4 | 5 ') 
    print('---+---+---') 
    print(' 6 | 7 | 8 ') 
    
#function to determine who has to play next 
def nextplay(num): 
    if num % 2 == 0 or num % 2 == 2: 
        return "make a play 'x'"
    else:
        return "make a play 'o'"
    
#function to check there is no invalid entry
def isLegal(num):
    if num < 0 or num > 8:
        return False  
    else: 
        return True
           
#function to handle who wins the game
def win(game): 
    
    #checking for winner in horizontal rows
    if game[0] == 'x' and game[1] == 'x' and game[2] == 'x': 
        return 'Hooray x is the winner!!!'
    elif game[0] == 'o' and game[1] == 'o' and game[2] =='o': 
        return 'Hooray o is the winner!!!' 
    elif game[3] == 'x' and game[4] == 'x' and game[5] == 'x': 
        return 'Hooray x is the winner!!!' 
    elif game[3] == 'o' and game[4] == 'o' and game[5] == 'o':
        return 'Hooray o is the winner!!!' 
    elif game[6] == 'x' and game[7] == 'x' and game[8] == 'x':
        return 'Hooray x is the winner!!!' 
    elif game[6] == 'o' and game[7] == 'o' and game[8] == 'o':
        return 'Hooray o is the winner!!!' 
    
    #checking for winner in vertical rows
    elif game[0] == 'x' and game[3] == 'x' and game[6] == 'x':
        return 'Hooray x is the winner!!!' 
    elif game[0] == 'o' and game[3] == 'o' and game[6] == 'o':
        return 'Hooray o is the winner!!!' 
    elif game[1] == 'x' and game[4] == 'x' and game[7] == 'x':
        return 'Hooray x is the winner!!!' 
    elif game[1] == 'o' and game[4] == 'o' and game[7] == 'o':
        return 'Hooray o is the winner!!!' 
    elif game[2] == 'x' and game[5] == 'x' and game[8] == 'x': 
        return 'Hooray x is the winner!!!' 
    elif game[2] == 'o' and game[5] == 'o' and game[8] == 'o':
        return 'Hooray o is the winner!!!' 
    
    #checking for winner in diagonal 
    elif game[0] == 'x' and game[4] == 'x' and game[8] == 'x': 
        return 'Hooray x is the winner!!!'
    elif game[0] == 'o' and game[4] == 'o' and game[8] == 'o': 
        return 'Hooray o is the winner!!!'    
    elif game[2] == 'x' and game[4] == 'x' and game[6] == 'x': 
        return 'Hooray x is the winner!!!' 
    elif game[2] == 'o' and game[4] == 'o' and game[6] == 'o': 
        return 'Hooray o is the winner!!!'    
    
    else: 
        return False
    
#function to handle the gameboard         
def gameboard(game):
    print(' ')
    print(' ' + game[0] + ' ' + '|' + ' ' + game[1] + ' ' + '|' + ' ' + game[2] + ' ') 
    print('---+---+---') 
    print(' ' + game[3] + ' ' + '|' + ' ' + game[4] + ' ' + '|' + ' ' + game[5] + ' ')
    print('---+---+---') 
    print(' ' + game[6] + ' ' + '|' + ' ' + game[7] + ' ' + '|' + ' ' + game[8] + ' ')
    print(' ') 

def main(): 
    count = 0   
    while win(game_array) == False: 
        if nextplay(count) == "make a play 'x'":
            play = input("Enter a play 'x' \n")
            if isLegal(eval(play)): 
                if game_array[eval(play)] == ' ':
                    game_array[eval(play)] = 'x'
                    count+=1
                    gameboard(game_array)
                    gameOverveiw()
                    
                else: 
                    print("ooops can't play there")
                
            else: 
                print("Invalid play")
        else:
            play = input("Enter a play 'o' \n")
            if isLegal(eval(play)):
                if game_array[eval(play)] == ' ': 
                    game_array[eval(play)] = 'o' 
                    gameboard(game_array)
                    gameOverveiw() 
                    count+=1
                else:
                    print("ooops can't play there")
            else:
                print("Invalid play")
                
    winner = win(game_array) 
    print(winner)
        
                    
if __name__ == '__main__': 
    main() 
    

        
    











