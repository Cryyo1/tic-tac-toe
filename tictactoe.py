import os

#class palyer
class Player():
    def __init__(self,name,XO):
        self.name=name
        self.XO=XO
# dictionnary for a board 
# each one represent (place : value)
board_dict={}
free_board=[]
def board():
    value=1;
    for i in range(3):    
        print('-------------')
        print('| {} | {} | {} |'.format(board_dict[str(value)],board_dict[str(value+1)],board_dict[str(value+2)]))
        value+=3
    print('-------------')

def input_X_O(XO):
    area=int(input("please enter the play area:"))
    while(area not in free_board):
        area=int(input("please enter the play area:"))
    board_dict[str(area)]=XO
    free_board.remove(area)

def check():
    if((board_dict['1'] == board_dict['2']) & (board_dict['2']==board_dict['3'])):
        return True
    if((board_dict['4'] == board_dict['5']) & (board_dict['5']==board_dict['6'])):
        return True
    if((board_dict['7'] == board_dict['8']) & (board_dict['8']==board_dict['9'])):
        return True
    if((board_dict['1'] == board_dict['4']) & (board_dict['4']==board_dict['7'])):
        return True
    if((board_dict['2'] == board_dict['5']) & (board_dict['5']==board_dict['8'])):
        return True
    if((board_dict['3'] == board_dict['6']) & (board_dict['6']==board_dict['9'])):
        return True
    if((board_dict['1'] == board_dict['5']) & (board_dict['5']==board_dict['9'])):
        return True
    if((board_dict['3'] == board_dict['5']) & (board_dict['5']==board_dict['7'])):
        return True
    return False


#My main  function u can say (for c devoloper)
   
print('***** welcome to TIC TAC TOE game *****')

#player 1 info
name=input('enter your name player1 :')
XO=input('enter your X or O :')
while(XO not in('X','O')):
    XO=input('enter your X or O :')
player1=Player(name,XO)

#player 2 info

name=input('enter your name player2 :')
player2=Player(name,XO)
if(player1.XO == 'O'):
    player2.XO='X'
else:
    player2.XO='O'

bool=True
while(bool):
    #intialize_board
    board_dict={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
    free_board=[1,2,3,4,5,6,7,8,9]
    os.system('cls')
    board()
    #the game start
    i=0
    while(i < 9 ):
        if(i % 2 == 0):
            player=player1
        else:
            player=player2
        print("it is {} turn:".format(player.name))
        input_X_O(player.XO)
        if(check()):
            print('congratulation {} won the game'.format(player.name))
            break
        os.system('cls')
        board()
        if((i==8) & (not check())):
            print('it is a draw between {} and {}'.format(player1.name,player2.name))
        i+=1
    rematch=input('would you like a rematch (yes/no):')
    if rematch in('y','Y','yes','YES','Yes'):
        bool=True
    else:
        bool=False 
        print('See you later, bye ')

    

