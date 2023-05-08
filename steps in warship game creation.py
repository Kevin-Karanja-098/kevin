import random
def fightzone():
    global board
    board = [[0]*10 for i in range(10)]
    return board
def display_gamekey():
    print('key')
    print('W=when you hit target')
    print('L=when you misses target')
    print('G=when opponent hit target')
    print('F=when opponent misses target')
def find_percentage_shipdestroyed_and_winner():
    p1=P1/20*100
    p2=P2/20*100
    print('percentage of player1 ship destroyed is',p1)
    print('percentage of player2 ship destroyed is',p2)
    if p1 > p2:
        print('opponent wins')
    elif p2 > p1:
        print('you  wins')
    else:
        print('you went draw')
def create_ships():
    ships_player=[]
    for i in range(20):
        ship=(random.randint(0,10-1),random.randint(0,10-1))
        ships_player.append(ship)
    return(ships_player)
def you_shoot():
    print('your turn')
    print('enter coordinates to shoot')
    global x
    global y
    x=int(input())
    y=int(input())
    global fire
    fire=(x,y)
    return fire
def opponent_shoot():
    global x
    global y
    x=random.randint(0,10-1)
    y=random.randint(0,10-1)
    global shoot
    shoot=(x,y)
    return shoot
P2=0
P1=0    
import time
import random
time_limit=300
start_time=time.time()
display_gamekey()
board=fightzone()
ships_player1=create_ships()
ships_player2=create_ships()
while True:
    you_shoot()
    if fire in ships_player2:
        board[x][y]='W'
        P1+=1
    else:
        board[x][y]='L'
    for i in board:
         print(*i)
    if time.time() -start_time  > time_limit:
        print("TIME'S UP")
        print('GAME OVER')
        break
    print("opponent's turn")
    time.sleep(2)
    opponent_shoot()
    if shoot in ships_player1:
        board[x][y]='G'
        P2+=1
    else:
        board[x][y]='F'
    for i in board:
         print(*i)
    if time.time() -start_time  > time_limit:
        print("TIME'S UP")
        print('GAME OVER')
        break
find_percentage_shipdestroyed_and_winner()

















    
         
