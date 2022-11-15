import pygame
import random
import os

from pygame.locals import *
from Settings import *

if Record:
    try:
        file = open('matchrecord.txt','a')
    except:
        file = open('matchrecord.txt','w')

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Attack')
#Values
#use pygame.image.load('./image/') to load images
b1=pygame.image.load('./image/background1.png')
b2=pygame.image.load('./image/background2.png')
R =pygame.image.load('./image/Rule.png')
S =pygame.image.load('./image/Start.png')
P =pygame.image.load('./image/PVP.png')
C =pygame.image.load('./image/Confirm.png')
RB=pygame.image.load('./image/RedBlock.png')
BB=pygame.image.load('./image/BlueBlock.png')
num = [pygame.image.load('./image/number/0.png'),\
       pygame.image.load('./image/number/1.png'),\
       pygame.image.load('./image/number/2.png'),\
       pygame.image.load('./image/number/3.png'),\
       pygame.image.load('./image/number/4.png'),\
       pygame.image.load('./image/number/5.png'),\
       pygame.image.load('./image/number/6.png'),\
       pygame.image.load('./image/number/7.png'),\
       pygame.image.load('./image/number/8.png'),\
       pygame.image.load('./image/number/9.png')]
T = [pygame.image.load('./image/tutorial/t0.png'),\
     pygame.image.load('./image/tutorial/t1.png'),\
     pygame.image.load('./image/tutorial/t2.png'),\
     pygame.image.load('./image/tutorial/t3.png'),\
     pygame.image.load('./image/tutorial/t4.png'),\
     pygame.image.load('./image/tutorial/t5.png'),\
     pygame.image.load('./image/tutorial/t6.png'),\
     pygame.image.load('./image/tutorial/t7.png'),\
     pygame.image.load('./image/tutorial/t8.png'),\
     pygame.image.load('./image/tutorial/t9.png'),\
     pygame.image.load('./image/tutorial/t10.png'),\
     pygame.image.load('./image/tutorial/t11.png'),\
     pygame.image.load('./image/tutorial/t12.png'),\
     pygame.image.load('./image/tutorial/t13.png'),\
     pygame.image.load('./image/tutorial/t14.png'),\
     pygame.image.load('./image/tutorial/t15.png'),\
     pygame.image.load('./image/tutorial/t16.png'),\
     pygame.image.load('./image/tutorial/t17.png'),\
     pygame.image.load('./image/tutorial/t18.png'),\
     pygame.image.load('./image/tutorial/t19.png'),\
     pygame.image.load('./image/tutorial/t20.png'),\
     pygame.image.load('./image/tutorial/t21.png'),\
     pygame.image.load('./image/tutorial/t22.png'),\
     pygame.image.load('./image/tutorial/t23.png'),\
     pygame.image.load('./image/tutorial/t24.png'),\
     pygame.image.load('./image/tutorial/t25.png'),\
     pygame.image.load('./image/tutorial/t26.png'),\
     pygame.image.load('./image/tutorial/t27.png'),\
     pygame.image.load('./image/tutorial/t28.png'),\
     pygame.image.load('./image/tutorial/t29.png'),\
     pygame.image.load('./image/tutorial/t30.png'),\
     pygame.image.load('./image/tutorial/t31.png'),\
     pygame.image.load('./image/tutorial/t32.png'),\
     pygame.image.load('./image/tutorial/t33.png'),\
     pygame.image.load('./image/tutorial/t34.png'),\
     pygame.image.load('./image/tutorial/t35.png'),\
     pygame.image.load('./image/tutorial/t36.png'),\
     pygame.image.load('./image/tutorial/t37.png'),\
     pygame.image.load('./image/tutorial/t38.png'),\
     pygame.image.load('./image/tutorial/t39.png'),\
     pygame.image.load('./image/tutorial/t40.png'),\
     pygame.image.load('./image/tutorial/t41.png'),\
     pygame.image.load('./image/tutorial/t42.png'),\
     pygame.image.load('./image/tutorial/t43.png'),\
     pygame.image.load('./image/tutorial/t44.png'),\
     pygame.image.load('./image/tutorial/t45.png'),\
     pygame.image.load('./image/tutorial/t46.png'),\
     pygame.image.load('./image/tutorial/t47.png'),\
     pygame.image.load('./image/tutorial/t48.png'),\
     pygame.image.load('./image/tutorial/t49.png'),\
     pygame.image.load('./image/tutorial/t50.png'),\
     pygame.image.load('./image/tutorial/t51.png'),\
     pygame.image.load('./image/tutorial/t52.png'),\
     pygame.image.load('./image/tutorial/t53.png')]
Pt= [pygame.image.load('./image/tutorial/PVP/P1.png'),\
     pygame.image.load('./image/tutorial/PVP/P2.png'),\
     pygame.image.load('./image/tutorial/PVP/P3.png'),\
     pygame.image.load('./image/tutorial/PVP/P4.png'),\
     pygame.image.load('./image/tutorial/PVP/P5.png'),\
     pygame.image.load('./image/tutorial/PVP/P6.png'),\
     pygame.image.load('./image/tutorial/PVP/P7.png'),\
     pygame.image.load('./image/tutorial/PVP/P8.png')]
Arrowr = pygame.image.load('./image/tutorial/leftdownarrow.png')
Arrowb = pygame.image.load('./image/tutorial/rightuparrow.png')

Map = [[0,0,0,0,2],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [1,0,0,0,0],\
       [0,0,0,0,0]]
# 存储城市所属
QwQ = [[0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0]]
# 存储即将出的兵数
QAQ = [[0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0],\
       [0,0,0,0,0]]
DC  = [[1,1,1,1,1],\
       [1,1,1,1,1],\
       [1,1,1,1,1],\
       [1,1,1,1,1],\
       [1,1,1,1,1]]

RArmy = BArmy = 1 # 双方军队
RMaxn = BMaxn = 4 # 双方最大容兵数量
RDispatch = BDispatch = False # 上一回合双方是否出兵
I=1 # 回合数
opening = random.randint(0,2)

#functions
def DeadCityUpdate(y,x,c):
    if DC[y][x]:
        DC[y][x] = 0
        if x>0:
            if Map[y][x-1] == c:
                DeadCityUpdate(y,x-1,c)
        if x<4:
            if Map[y][x+1] == c:
                DeadCityUpdate(y,x+1,c)
        if y>0:
            if Map[y-1][x] == c:
                DeadCityUpdate(y-1,x,c)
        if y<4:
            if Map[y+1][x] == c:
                DeadCityUpdate(y+1,x,c)

def decide(): # update QAQ
    global opening
    if Difficulty == 0:
        if I == 1:
            pass
        elif I == 2:
            QAQ[0][3] = QAQ[1][4] = 1
        elif I == 3:
            pass
        elif I == 4:
            QAQ[0][2] = QAQ[2][4] = 1
            if random.randint(0,9) == 0:
                QAQ[1][3] = 1
        elif I == 5:
            QAQ[0][1] = QAQ[3][4] = 1
        elif I == 6:
            pass
        elif I == 7:
            if Map[1][1] == 0:
                QAQ[1][1] = 1
            if Map[3][3] == 0:
                QAQ[3][3] = 1
            if Map[0][0] == 1:
                QAQ[4][4] = 1
            elif Map[4][4] == 1:
                QAQ[0][0] = 1
            else:
                QAQ[1][1] = QAQ[3][3] = 0
                if BArmy > 4:
                    d = random.randint(0,11)
                    if d<2:
                        QAQ[0][0] = 2
                        QAQ[4][4] = 3
                    elif d<4:
                        QAQ[0][0] = 3
                        QAQ[4][4] = 2
                    elif d<6:
                        QAQ[0][0] = 4
                        QAQ[4][4] = 1
                    elif d<8:
                        QAQ[0][0] = 1
                        QAQ[4][4] = 4
                    elif d==8:
                        QAQ[0][0] = 3
                    elif d==9:
                        QAQ[4][4] = 3
                    elif d==10:
                        QAQ[0][0] = 4
                    else:
                        QAQ[4][4] = 4
                else:
                    d = random.randint(0,9)
                    if d<4:
                        QAQ[0][0] = QAQ[4][4] = 2
                    elif d<6:
                        QAQ[0][0] = 3
                        QAQ[4][4] = 1
                    elif d<8:
                        QAQ[0][0] = 1
                        QAQ[4][4] = 3
                    elif d==8:
                        QAQ[0][0] = 3
                    else:
                        QAQ[4][4] = 3
        elif I == 8:
            pass
        elif I == 9:
            if Map[0][0] == 0 and Map[4][4] == 0:
                d = random.randint(0,1)
                if d:
                    QAQ[0][0] = BArmy//2
                    QAQ[4][4] = BArmy-BArmy//2
                else:
                    QAQ[4][4] = BArmy//2
                    QAQ[0][0] = BArmy-BArmy//2
            elif Map[0][0] == 0:
                QAQ[0][0] = BArmy
            elif Map[4][4] == 0:
                QAQ[4][4] = BArmy
            else:
                pass
        else:
            if Map[0][0] == 0 and Map[4][4] == 0:
                d = random.randint(0,7)
                if d<4:
                    QAQ[0][0] = QAQ[4][4] = 2
                elif d<6:
                    QAQ[0][0] = 3
                    QAQ[4][4] = 1
                else:
                    QAQ[0][0] = 1
                    QAQ[4][4] = 3
            elif Map[0][0] == 0:
                QAQ[0][0] = BArmy
            elif Map[4][4] == 0:
                QAQ[4][4] = BArmy
            else:
                if (Map[0][3] == 1 or Map[1][4] == 1) and RArmy > 2:
                    QAQ[0][4] = random.randint(0,RArmy)
                    if QAQ[0][4] > (RArmy+1)//2:
                        QAQ[0][4] = (RArmy+1)//2
                    if RArmy == 3 and QAQ[0][4] == 2:
                        QAQ[0][4] = 1
                    if BArmy - QAQ[0][4] > 2:
                        if Map[0][3] == 1:
                            QAQ[0][3] = 2
                        else:
                            QAQ[1][4] = 2
                    QAQ[0][4] = min(QAQ[0][4],BArmy)
                else:
                    if Map[0][0] == 2:
                        if Map[1][0] == 2:
                            if Map[2][0] == 2:
                                if Map[3][0] == 2:
                                    if BArmy > 2:
                                        if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                            pass
                                        elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                            QAQ[3][0] = 1
                                        else:
                                            QAQ[4][0] = random.randint(3,BArmy)
                                            if QAQ[4][0] > 5 and QAQ[4][0] % 2 == 0:
                                                QAQ[4][0] -= 1
                                    else:
                                        if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                            QAQ[3][0] = 1
                                else:
                                    if BArmy > 2:
                                        if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                            pass
                                        elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                            QAQ[2][0] = 1
                                        else:
                                            QAQ[3][0] = random.randint(2,min(BArmy,4))
                                    else:
                                        if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                            QAQ[2][0] = 1
                                    if Map[3][0] == 0:
                                        QAQ[2][0] = 0
                                        if QAQ[3][0] > 1:
                                            QAQ[3][0] = 1
                            else:
                                if BArmy > 2:
                                    if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                        pass
                                    elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                        QAQ[1][0] = 1
                                    else:
                                        QAQ[2][0] = random.randint(2,min(BArmy,4))
                                else:
                                    if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                        QAQ[1][0] = 1
                                if Map[2][0] == 0:
                                    QAQ[1][0] = 0
                                    if QAQ[2][0] > 1:
                                        QAQ[2][0] = 1
                        else:
                            if BArmy > 2:
                                if random.randint(0,1)==0 and BMaxn-BArmy >= 4:
                                    pass
                                else:
                                    QAQ[1][0] = random.randint(2,min(BArmy,4))
                                    if Map[1][0] == 0:
                                        QAQ[1][0] = 1
                    elif Map[4][4] == 2:
                        if Map[4][3] == 2:
                            if Map[4][2] == 2:
                                if Map[4][1] == 2:
                                    if BArmy > 2:
                                        if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                            pass
                                        elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                            QAQ[4][1] = 1
                                        else:
                                            QAQ[4][0] = random.randint(3,BArmy)
                                            if QAQ[4][0] > 5 and QAQ[4][0] % 2 == 0:
                                                QAQ[4][0] -= 1
                                    else:
                                        if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                            QAQ[4][1] = 1
                                else:
                                    if BArmy > 2:
                                        if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                            pass
                                        elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                            QAQ[4][2] = 1
                                        else:
                                            QAQ[4][1] = random.randint(2,min(BArmy,4))
                                    else:
                                        if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                            QAQ[4][2] = 1
                                    if Map[4][1] == 0:
                                        QAQ[4][2] = 0
                                        if QAQ[4][1] > 1:
                                            QAQ[4][1] = 1
                            else:
                                if BArmy > 2:
                                    if random.randint(0,2)==0 and BMaxn-BArmy >= 4:
                                        pass
                                    elif random.randint(0,2)==1 and RArmy > 1 and BArmy > 0:
                                        QAQ[4][3] = 1
                                    else:
                                        QAQ[4][2] = random.randint(2,min(BArmy,4))
                                else:
                                    if random.randint(0,5) == 0 and RArmy > 1 and BArmy > 0:
                                        QAQ[4][3] = 1
                                    if Map[4][2] == 0:
                                        QAQ[4][3] = 0
                                        if QAQ[4][2] > 1:
                                            QAQ[4][2] = 1
                        else:
                            if BArmy > 2:
                                if random.randint(0,1)==0 and BMaxn-BArmy >= 4:
                                    pass
                                else:
                                    QAQ[4][3] = random.randint(2,min(BArmy,4))
                                    if Map[4][3] == 0:
                                        QAQ[4][3] = 1
                    else:
                        QAQ[0][4] = BArmy
    elif Difficulty == 2:
        if I == 1:
            if QwQ[3][0] == 1:
                opening = 1
            elif QwQ[4][1] == 1:
                opening = 2
            else:
                opening = 0
    if Difficulty:
        if opening == 0:
            if I == 1:
                pass
            elif I == 2:
                QAQ[0][3] = QAQ[1][4] = 1
            elif I == 3:
                pass
            elif I == 4:
                QAQ[0][2] = QAQ[2][4] = 1
                if random.randint(0,9) == 0:
                    QAQ[1][3] = 1
            elif I == 5:
                QAQ[0][1] = QAQ[3][4] = 1
            elif I == 6:
                pass
            elif I == 7:
                if Map[1][1] == 0:
                    QAQ[1][1] = 1
                if Map[3][3] == 0:
                    QAQ[3][3] = 1
                if Map[0][0] == 1:
                    QAQ[4][4] = 1
                elif Map[4][4] == 1:
                    QAQ[0][0] = 1
                else:
                    QAQ[1][1] = QAQ[3][3] = 0
                    if BArmy > 4:
                        d = random.randint(0,11)
                        if d<2:
                            QAQ[0][0] = 2
                            QAQ[4][4] = 3
                        elif d<4:
                            QAQ[0][0] = 3
                            QAQ[4][4] = 2
                        elif d<6:
                            QAQ[0][0] = 4
                            QAQ[4][4] = 1
                        elif d<8:
                            QAQ[0][0] = 1
                            QAQ[4][4] = 4
                        elif d==8:
                            QAQ[0][0] = 3
                        elif d==9:
                            QAQ[4][4] = 3
                        elif d==10:
                            QAQ[0][0] = 4
                        else:
                            QAQ[4][4] = 4
                    else:
                        d = random.randint(0,9)
                        if d<4:
                            QAQ[0][0] = QAQ[4][4] = 2
                        elif d<6:
                            QAQ[0][0] = 3
                            QAQ[4][4] = 1
                        elif d<8:
                            QAQ[0][0] = 1
                            QAQ[4][4] = 3
                        elif d==8:
                            QAQ[0][0] = 3
                        else:
                            QAQ[4][4] = 3
        elif opening == 1:
            if I == 1:
                QAQ[0][3] = 1
            elif I == 2:
                pass
            elif I == 3:
                QAQ[0][2] = QAQ[1][4] = 1
            elif I == 4:
                pass
            elif I == 5:
                QAQ[0][1] = QAQ[2][4] = 1
            elif I == 6:
                if Map[0][0]:
                    QAQ[1][1] = QAQ[3][4] = 1
                else:
                    QAQ[0][0] = QAQ[3][4] = 1
            elif I == 7:
                if Map[0][0] == 1:
                    QAQ[4][4] = 1
        else:
            if I == 1:
                QAQ[1][4] = 1
            elif I == 2:
                pass
            elif I == 3:
                QAQ[2][4] = QAQ[0][3] = 1
            elif I == 4:
                pass
            elif I == 5:
                QAQ[3][4] = QAQ[0][2] = 1
            elif I == 6:
                if Map[4][4]:
                    QAQ[3][3] = QAQ[0][1] = 1
                else:
                    QAQ[4][4] = QAQ[0][1] = 1
            elif I == 7:
                if Map[4][4] == 1:
                    QAQ[0][0] = 1
    if Difficulty == 1 and I > 7:
        if BArmy == 0:
            return None
        if not (Map[0][0] or Map[4][4]):
            if BArmy != 4:
                d=random.randint(0,min(BArmy,RArmy))
                QAQ[0][0] = d
                QAQ[4][4] = BArmy - d
            else:
                d=random.randint(0,7)
                if d<4:
                    QAQ[0][0] = QAQ[4][4] = 2
                elif d<6:
                    QAQ[0][0] = 3
                    QAQ[4][4] = 1
                else:
                    QAQ[0][0] = 1
                    QAQ[4][4] = 3
        elif Map[0][0] == 0:
            QAQ[0][0] = BArmy
        elif Map[4][4] == 0:
            QAQ[4][4] = BArmy
        else:
            if Map[3][0]-2 and Map[4][1]-2 and Map[0][3]-1 and Map[1][4]-1:
                if random.randint(0,1) and BArmy > 2:
                    Sum = 0
                    Maxn = min(8,BArmy-1)
                    for i in range(5):
                        for j in range(5):
                            if Map[j][i] == 2 and not DC[j][i]:
                                if i > 0:
                                    if Map[j][i-1] == 1:
                                        QAQ[j][i-1] = random.randint(0,2) + random.randint(0,2)
                                        if QAQ[j][i-1] == 1:
                                            QAQ[j][i-1] = 0
                                        if RArmy < 2 and QAQ[j][i-1] == 4:
                                            QAQ[j][i-1] = 3
                                        if RArmy < 1 and QAQ[j][i-1] == 3:
                                            QAQ[j][i-1] = 2
                                    if Map[j][i-1] == 0:
                                        QAQ[j][i-1] = random.randint(0,1)
                                    QAQ[0][0] = QAQ[4][4] = QAQ[2][2] = 0
                                    Sum += QAQ[j][i-1]
                                    if Sum > Maxn:
                                        Sum -= QAQ[j][i-1]
                                        QAQ[j][i-1] = 0
                                if i < 4:
                                    if Map[j][i+1] == 1:
                                        QAQ[j][i+1] = random.randint(0,2) + random.randint(0,2)
                                        if QAQ[j][i+1] == 1:
                                            QAQ[j][i+1] = 0
                                        if RArmy < 2 and QAQ[j][i+1] == 4:
                                            QAQ[j][i+1] = 3
                                        if RArmy < 1 and QAQ[j][i+1] == 3:
                                            QAQ[j][i+1] = 2
                                    if Map[j][i+1] == 0:
                                        QAQ[j][i+1] = random.randint(0,1)
                                    QAQ[0][0] = QAQ[4][4] = QAQ[2][2] = 0
                                    Sum += QAQ[j][i+1]
                                    if Sum > Maxn:
                                        Sum -= QAQ[j][i+1]
                                        QAQ[j][i+1] = 0
                                if j > 0:
                                    if Map[j-1][i] == 1:
                                        QAQ[j-1][i] = random.randint(0,2) + random.randint(0,2)
                                        if QAQ[j-1][i] == 1:
                                            QAQ[j-1][i] = 0
                                        if RArmy < 2 and QAQ[j-1][i] == 4:
                                            QAQ[j][i-1] = 3
                                        if RArmy < 1 and QAQ[j-1][i] == 3:
                                            QAQ[j-1][i] = 2
                                    if Map[j-1][i] == 0:
                                        QAQ[j-1][i] = random.randint(0,1)
                                    QAQ[0][0] = QAQ[4][4] = QAQ[2][2] = 0
                                    Sum += QAQ[j-1][i]
                                    if Sum > Maxn:
                                        Sum -= QAQ[j-1][i]
                                        QAQ[j-1][i] = 0
                                if j < 4:
                                    if Map[j+1][i] == 1:
                                        QAQ[j+1][i] = random.randint(0,2) + random.randint(0,2)
                                        if QAQ[j+1][i] == 1:
                                            QAQ[j+1][i] = 0
                                        if RArmy < 2 and QAQ[j+1][i] == 4:
                                            QAQ[j][i-1] = 3
                                        if RArmy < 1 and QAQ[j+1][i] == 3:
                                            QAQ[j+1][i] = 2
                                    if Map[j+1][i] == 0:
                                        QAQ[j+1][i] = random.randint(0,1)
                                    QAQ[0][0] = QAQ[4][4] = QAQ[2][2] = 0
                                    Sum += QAQ[j+1][i]
                                    if Sum > Maxn:
                                        Sum -= QAQ[j+1][i]
                                        QAQ[j+1][i] = 0
                else:
                    Maxn = 3
                    if RArmy < 2:
                        return None
                    if Map[1][1] == 2 and\
((Map[0][1] == 1 and not DC[0][1]) or (Map[1][0] == 1 and not DC[1][0]) or \
(Map[2][1] == 1 and not DC[2][1]) or (Map[1][2] == 1 and not DC[1][2])):
                        QAQ[1][1] = random.randint(0,1)
                    if Map[3][3] == 2 and\
((Map[3][2] == 1 and not DC[3][2]) or (Map[2][3] == 1 and not DC[2][3]) or \
(Map[3][4] == 1 and not DC[3][4]) or (Map[4][3] == 1 and not DC[4][3])):
                        QAQ[3][3] = random.randint(0,1)
                    if Map[0][0] == 2:
                        if Map[1][0] == 2:
                            if Map[2][0] == 2:
                                QAQ[2][0] = random.randint(0,1)
                            else:
                                QAQ[1][0] = random.randint(0,1)
                    elif Map[4][4] == 2:
                        if Map[4][3] == 2:
                            if Map[4][2] == 2:
                                QAQ[4][2] = random.randint(0,1)
                            else:
                                QAQ[4][3] = random.randint(0,1)
                    QAQ[random.randint(0,4)][random.randint(0,4)] = random.randint(0,1)
                    if Map[0][2] == 1 and not DC[0][2]:
                        QAQ[0][3] += random.randint(0,1)
                        Maxn += 1
                    if Map[1][3] == 1 and not DC[1][3]:
                        QAQ[0][3] += random.randint(0,1)
                        QAQ[1][4] += random.randint(0,1)
                        Maxn += 1
                    if Map[2][4] == 1 and not DC[2][4]:
                        QAQ[1][4] += random.randint(0,1)
                        Maxn += 1
                    Sum = 0
                    for i in range(5):
                        for j in range(5):
                            if Map[j][i] != 2:
                                QAQ[j][i] = 0
                            Sum += QAQ[j][i]
                    if Sum > min(Maxn,BArmy):
                        for i in range(5):
                            for j in range(5):
                                QAQ[j][i] = 0
            else:
                if not((Map[3][0]-2 and Map[4][1]-2) or (Map[0][3]-1 and Map[1][4]-1)):
                    if BArmy > 2*RArmy:
                        if (Map[1][2]-2 or DC[1][2]) and (Map[2][1]-2 or DC[2][1]) and (Map[2][3]-2 or DC[2][3]) and (Map[3][2]-2 or DC[3][2]):
                            QAQ[4][0] = 2*RArmy+1
                            QAQ[2][2] = BArmy - QAQ[4][0]
                        else:
                            QAQ[4][0] = BArmy
                    elif RArmy > max(2*BArmy,2):
                        if random.randint(0,1):
                            QAQ[0][4] = BArmy
                        else:
                            QAQ[4][0] = BArmy
                    else:
                        if RArmy < 3:
                            if BArmy < 3:
                                pass
                            else:
                                if random.randint(0,2):
                                    pass
                                else:
                                    QAQ[4][0] = BArmy
                        else:
                            if BArmy < 3:
                                QAQ[0][4] = min((RArmy+1)//2,random.randint(0,max(RArmy,BArmy)))
                            else:
                                if random.randint(0,2):
                                    QAQ[0][4] = min((RArmy+1)//2,random.randint(0,max(RArmy,BArmy)))
                                elif not random.randint(0,2):
                                    if Map[0][3] == 1:
                                        QAQ[0][3] = random.randint(2,3)
                                    if Map[1][4] == 1 and BArmy-QAQ[0][3] > 3:
                                        QAQ[1][4] = random.randint(2,3)
                                else:
                                    QAQ[4][0] = random.randint(3,BArmy+2)
                                    if QAQ[4][0] > BArmy:
                                        QAQ[4][0] = BArmy
                                    if QAQ[4][0] > 5 and QAQ[4][0]%2 == 0:
                                        QAQ[4][0] -= 1
                elif not(Map[3][0]-2 and Map[4][1]-2):
                    if random.randint(0,2):
                        if BArmy:
                            if Map[3][0] == 2:
                                QAQ[3][0] = random.randint(0,1)
                        if BArmy-QAQ[3][0]:
                            if Map[4][1] == 2:
                                QAQ[4][1] = random.randint(0,1)
                    else:
                        if BArmy > 2:
                            QAQ[4][0] = random.randint(3,BArmy)
                else:
                    if random.randint(0,2) and RArmy > 2:
                        QAQ[0][4] = min((RArmy+1)//2,random.randint(0,max(RArmy,BArmy)))
                    elif random.randint(0,2) and BArmy > 2:
                        if Map[0][3] == 1:
                            QAQ[0][3] = 2+random.randint(0,2)%2
                        if Map[1][4] == 1 and BArmy-QAQ[0][3] > 3:
                            QAQ[1][4] = 2+random.randint(0,2)%2
    elif Difficulty == 2 and I > 7:
        d=1
        Sum = 0
        for i in range(5):
            for j in range(5):
                if i == 4 and j == 0:
                    if QwQ[j][i] > 2:
                        d=0
                        QAQ[j][i] = min(QwQ[j][i]-2,(QwQ[j][i]+1)//2,BArmy-Sum)
                if QwQ[j][i] == 2 and Map[j][i] == 2 and BArmy - Sum > 1:
                    d=0
                    Sum += 1
                    QAQ[j][i] = 1
                if QwQ[j][i] > 2 and Map[j][i] == 2:
                    if BArmy - Sum > RArmy:
                        d=0
                        QAQ[j][i] = min(QwQ[j][i]//2+1,QwQ[j][i]-1)
        if d:
            if Map[1][3] == 0 and BArmy > 4:
                Sum += 1
                QAQ[1][3] = 1
            if Map[1][2] == 0 and BArmy - Sum > 4:
                Sum += 1
                QAQ[1][2] = 1
            if Map[2][3] == 0 and BArmy - Sum > 4:
                Sum += 1
                QAQ[2][3] = 1
            if Map[0][0] == 2:
                if Map[1][0] == 2:
                    if Map[2][0] == 2:
                        if Map[3][0] == 2:
                            if BArmy - Sum > max(QwQ[4][0]+2,QwQ[4][0]*2):
                                QAQ[4][0] = BArmy - Sum
                        else:
                            if BArmy - Sum > max(QwQ[3][0]+2,QwQ[3][0]*2):
                                if Map[3][0] == 0:
                                    QAQ[3][0] = 1
                                else:
                                    QAQ[3][0] = max(QwQ[3][0]+2,QwQ[3][0]*2)
                    else:
                        if BArmy - Sum > max(QwQ[2][0]+2,QwQ[2][0]*2):
                            if Map[2][0] == 0:
                                QAQ[2][0] = 1
                            else:
                                QAQ[2][0] = max(QwQ[2][0]+2,QwQ[2][0]*2)
                else:
                    if BArmy - Sum > max(QwQ[1][0]+2,QwQ[1][0]*2):
                        if Map[1][0] == 0:
                            QAQ[1][0] = 1
                        else:
                            QAQ[1][0] = max(QwQ[1][0]+2,QwQ[1][0]*2)
            elif Map[4][4] == 2:
                if Map[4][3] == 2:
                    if Map[4][2] == 2:
                        if Map[4][1] == 2:
                            if BArmy - Sum > max(QwQ[4][0]+2,QwQ[4][0]*2):
                                QAQ[4][0] = BArmy - Sum
                        else:
                            if BArmy - Sum > max(QwQ[4][1]+2,QwQ[4][1]*2):
                                if Map[4][1] == 0:
                                    QAQ[4][1] = 1
                                else:
                                    QAQ[4][1] = max(QwQ[4][1]+2,QwQ[4][1]*2)
                    else:
                        if BArmy - Sum > max(QwQ[4][2]+2,QwQ[4][2]*2):
                            if Map[4][2] == 0:
                                QAQ[4][2] = 1
                            else:
                                QAQ[4][2] = max(QwQ[4][2]+2,QwQ[4][2]*2)
                else:
                    if BArmy - Sum > max(QwQ[4][3]+2,QwQ[4][3]*2):
                        if Map[4][3] == 0:
                            QAQ[4][3] = 1
                        else:
                            QAQ[4][3] = max(QwQ[4][3]+2,QwQ[4][3]*2)
            else:
                if Map[0][0] == 0 and Map[4][4] == 0:
                    if QwQ[0][0] > QwQ[4][4]:
                        QAQ[4][4] = QwQ[4][4] + 1
                    else:
                        QAQ[0][0] = QwQ[0][0] + 1
                elif Map[0][0] == 1:
                    QAQ[4][4] = QwQ[4][4] + 1
                else:
                    QAQ[0][0] = QwQ[0][0] + 1

def tutorial():
    global RArmy,BArmy,RMaxn,BMaxn,RDispatch,Map,QwQ
    t=1
    while True:
        if t>53:
            RArmy = BArmy = 1
            RMaxn = BMaxn = 4
            Map = [[0,0,0,0,2],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [1,0,0,0,0],\
                   [0,0,0,0,0]]
            QwQ = [[0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0]]
            QAQ = [[0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0]]
            break
        window.blit(b2,(0,0))
        if RArmy//10:
            window.blit(num[RArmy//10],(549,62))
        window.blit(num[RArmy%10],(609,62))
        if BArmy//10:
            window.blit(num[BArmy//10],(549,366))
        window.blit(num[BArmy%10],(609,366))
        if RMaxn//10:
            window.blit(num[RMaxn//10],(680,160))
            window.blit(num[RMaxn%10],(740,160))
        else:
            window.blit(num[RMaxn%10],(680,160))
        if BMaxn//10:
            window.blit(num[BMaxn//10],(680,465))
            window.blit(num[BMaxn%10],(740,465))
        else:
            window.blit(num[BMaxn%10],(680,465))
        for i in range(5):
            for j in range(5):
                if Map[j][i] == 1:
                    window.blit(RB,(45+100*i,45+100*j))
                if Map[j][i] == 2:
                    window.blit(BB,(45+100*i,45+100*j))
                if QwQ[j][i]:
                    if QwQ[j][i] < 10:
                        window.blit(num[QwQ[j][i]],(i*100+65,j*100+50))
                    else:
                        window.blit(num[QwQ[j][i]//10],(i*100+25,j*100+50))
                        window.blit(num[QwQ[j][i]% 10],(i*100+85,j*100+50))
        window.blit(T[t],(0,550))
        if t==2:
            window.blit(Arrowr,(150,390))
        elif t==3:
            window.blit(Arrowb,(390,150))
        elif t==4 or t==8:
            window.blit(Arrowr,(669,12))
        elif t==5:
            window.blit(Arrowb,(569,466))
        elif t==9:
            window.blit(Arrowr,(740,110))
            window.blit(Arrowr,(740,415))
        elif t==14:
            window.blit(Arrowr,(120,20))
            window.blit(Arrowr,(520,420))
        elif t==16:
            window.blit(Arrowr,(320,220))
        elif t==18:
            window.blit(RB,(145,345))
            window.blit(RB,(145,45))
            window.blit(RB,(245,45))
            window.blit(RB,(145,145))
            window.blit(RB,(45,245))
        elif t==20:
            window.blit(Arrowr,(220,420))
        elif t==26:
            window.blit(Arrowr,(120,320))
            window.blit(Arrowr,(320,420))
        elif t==29:
            window.blit(Arrowr,(120,220))
            window.blit(Arrowr,(420,420))
        elif t==30:
            window.blit(Arrowr,(120,120))
            window.blit(Arrowr,(520,420))
        elif t==43:
            window.blit(Arrowr,(120,120))
        elif t==44:
            window.blit(Arrowr,(520,320))
        elif t==45:
            window.blit(Arrowr,(520,220))
        elif t==46:
            window.blit(Arrowr,(520,120))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if t==20:
                    x,y = pygame.mouse.get_pos()
                    if x<245 and x>145 and y>445 and y<545:
                        QwQ[4][1]=1
                        t+=1
                    continue
                elif t==21 or t==24 or t==27 or t==28 or t==32 or t==42:
                    continue
                elif t==26:
                    x,y = pygame.mouse.get_pos()
                    if x<145 and x>45 and y>345 and y<445 and QwQ[3][0]==0:
                        QwQ[3][0]=1
                        if QwQ[4][2] == 1:
                            t+=1
                    if x<345 and x>245 and y>445 and y<545 and QwQ[4][2]==0:
                        QwQ[4][2]=1
                        if QwQ[3][0] == 1:
                            t+=1
                    continue
                elif t==29:
                    x,y = pygame.mouse.get_pos()
                    if x<145 and x>45 and y>245 and y<345 and QwQ[2][0]==0:
                        QwQ[2][0]=1
                    if x<445 and x>345 and y>445 and y<545 and QwQ[4][3]==0:
                        QwQ[4][3]=1
                    continue
                elif t==30:
                    x,y = pygame.mouse.get_pos()
                    if x<145 and x>45 and y>145 and y<245 and QwQ[1][0]==0:
                        QwQ[1][0]=1
                    if x<545 and x>445 and y>445 and y<545 and QwQ[4][3]==0:
                        QwQ[4][4]=1
                    continue
                elif t==43:
                    x,y = pygame.mouse.get_pos()
                    if x<145 and x>45 and y>145 and y<245 and QwQ[1][0]==0:
                        QwQ[1][0]=1
                    continue
                elif t==44:
                    x,y = pygame.mouse.get_pos()
                    if x<545 and x>445 and y>345 and y<445 and QwQ[3][4]<2:
                        QwQ[3][4]+=1
                    continue
                elif t==45:
                    x,y = pygame.mouse.get_pos()
                    if x<545 and x>445 and y>245 and y<345 and QwQ[2][4]<2:
                        QwQ[2][4]+=1
                    continue
                elif t==46:
                    x,y = pygame.mouse.get_pos()
                    if x<545 and x>445 and y>145 and y<245 and QwQ[1][4]<3:
                        QwQ[1][4]+=1
                    continue
                elif t==47:
                    x,y = pygame.mouse.get_pos()
                    if x>45 and x<545 and y>45 and y<545:
                        if pygame.mouse.get_pressed()[0]:
                            Sum = 0
                            for i in range(5):
                                for j in range(5):
                                    Sum += QwQ[j][i]
                            if Sum < RArmy and not( \
(x<145 or Map[(y-45)//100][(x-145)//100]-1)and \
(x>445 or Map[(y-45)//100][(x+55)//100]-1) and \
(y<145 or Map[(y-145)//100][(x-45)//100]-1)and \
(y>445 or Map[(y+55)//100][(x-45)//100]-1) and \
Map[(y-45)//100][(x-45)//100]-1 ):
                                QwQ[(y-45)//100][(x-45)//100] += 1
                        if pygame.mouse.get_pressed()[2]:
                            if QwQ[(y-45)//100][(x-45)//100]:
                                QwQ[(y-45)//100][(x-45)//100] -= 1
                    continue
                t+=1
            if event.type == KEYUP:
                if event.key == K_RETURN or K_KP_ENTER:
                    if t==21:
                        QwQ[4][1] = 0
                        RArmy = 0
                        BArmy = 3
                        RMaxn = 5
                        Map[4][1] = 1
                        t+=1
                    elif t==24:
                        RArmy = 3
                        BArmy = 1
                        BMaxn = 6
                        Map[0][3] = Map[1][4] = 2
                        t+=1
                    elif t==27:
                        QwQ[4][2] = QwQ[3][0] = 0
                        Map[4][2] = Map[3][0] = 1
                        RArmy = 1
                        BArmy = 5
                        RMaxn = 7
                        t+=1
                    elif t==28:
                        RArmy = 5
                        BArmy = 3
                        BMaxn = 8
                        Map[0][2] = Map[2][4] = 2
                        t+=1
                    elif t==29:
                        if QwQ[2][0] == 1 and QwQ[4][3] == 1:
                            QwQ[2][0] = QwQ[4][3] = 0
                            Map[2][0] = Map[4][3] = 1
                            Map[0][1] = Map[3][4] = 2
                            RArmy = 3
                            BArmy = 1
                            RMaxn = 9
                            BMaxn = 10
                            t+=1
                    elif t==30:
                        if QwQ[1][0] == 1 and QwQ[4][4] == 1:
                            QwQ[1][0] = QwQ[4][4] = 0
                            Map[1][0] = Map[4][4] = 1
                            RArmy = 1
                            BArmy = 5
                            RMaxn = 12
                            t+=1
                    elif t==32:
                        Map[0][0] = Map[1][1] = Map[3][3] = 2
                        RArmy = 5
                        BArmy = 2
                        BMaxn = 14
                        t+=1
                    elif t==42:
                        RArmy = 9
                        BArmy = 6
                        t+=1
                    elif t==43:
                        if QwQ[1][0] == 1:
                            QwQ[1][0] = 0
                            RArmy = 12
                            BArmy = 4
                            t+=1
                    elif t==44:
                        if QwQ[3][4] == 2:
                            QwQ[3][4] = 0
                            Map[3][4] = 1
                            RArmy = 10
                            BArmy = 8
                            RMaxn = 13
                            BMaxn = 13
                            t+=1
                    elif t==45:
                        if QwQ[2][4] == 2:
                            QwQ[2][4] = 0
                            Map[2][4] = 1
                            Map[1][0] = Map[2][1] = 2
                            RArmy = 8
                            BArmy = 5
                            BMaxn = 14
                            t+=1
                    elif t==46:
                        if QwQ[1][4] == 3:
                            QwQ[1][4] = 0
                            Map[1][4] = 1
                            RArmy = 5
                            BArmy = 8
                            BMaxn = 13
                            t+=1
                    elif t==47:
                        for i in range(5):
                            for j in range(5):
                                if QwQ[j][i]:
                                    RArmy -= QwQ[j][i]
                                    if Map[j][i] != 1:
                                        RDispatch = True
                                        if i == 4 and j == 0:
                                            if QwQ[0][4] > 2:
                                                Map[0][4] = 1
                                                t+=2
                                            else:
                                                BArmy = 4
                                                t+=1
                                if Map[j][i] == 2:
                                    if QwQ[j][i] >= 2 and not(i == 4 and j == 0):
                                        Map[j][i] = 1
                                else:
                                    if QwQ[j][i] > 0:
                                        Map[j][i] = 1
                        QwQ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                        Map[2][2] = 0
                        RMaxn = BMaxn = 4
                        if Map[4][4] == 1:
                            RMaxn += 1
                        if Map[4][4] == 2:
                            BMaxn += 1
                        for i in range(5):
                            for j in range(5):
                                if Map[j][i] == 1:
                                    RMaxn += 1
                                elif Map[j][i] == 2:
                                    BMaxn += 1
                        if not RDispatch:
                            RArmy += min(4,RMaxn-RArmy)
                        BArmy += min(4,BMaxn-BArmy)
                        RDispatch = False

        pygame.display.update()
        pygame.event.pump()

def start():
    end = False
    DeadCityUpdate(0,4,2)
    DeadCityUpdate(4,0,1)
    while True:
        window.blit(b1,(0,0))
        window.blit(R,(238,360))
        window.blit(S,(238,240))
        window.blit(P,(238,480))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                if Record:
                    file.close()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 238 and x < 548:
                    if y > 240 and y < 330:
                        end = True
                    if y > 360 and y < 450:
                        tutorial()
                    if y > 480 and y < 570:
                        PVP()
        pygame.display.update()
        pygame.event.pump()
        if end:
            break
    

def game():
    global RArmy,BArmy,RMaxn,BMaxn,RDispatch,BDispatch,I,QwQ,QAQ,DC
    ENDING = ''
    while True:
        window.blit(b2,(0,0))
        if RArmy//10:
            window.blit(num[RArmy//10],(549,62))
        window.blit(num[RArmy%10],(609,62))
        if BArmy//10:
            window.blit(num[BArmy//10],(549,366))
        window.blit(num[BArmy%10],(609,366))
        if RMaxn//10:
            window.blit(num[RMaxn//10],(680,160))
            window.blit(num[RMaxn%10],(740,160))
        else:
            window.blit(num[RMaxn%10],(680,160))
        if BMaxn//10:
            window.blit(num[BMaxn//10],(680,465))
            window.blit(num[BMaxn%10],(740,465))
        else:
            window.blit(num[BMaxn%10],(680,465))
        for i in range(5):
            for j in range(5):
                if Map[j][i] == 1:
                    window.blit(RB,(45+100*i,45+100*j))
                if Map[j][i] == 2:
                    window.blit(BB,(45+100*i,45+100*j))
        for i in range(5):
            for j in range(5):
                if QwQ[j][i]:
                    if QwQ[j][i] < 10:
                        window.blit(num[QwQ[j][i]],(i*100+65,j*100+50))
                    else:
                        window.blit(num[QwQ[j][i]//10],(i*100+25,j*100+50))
                        window.blit(num[QwQ[j][i]% 10],(i*100+85,j*100+50))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x>45 and x<545 and y>45 and y<545:
                    if event.button == 1 or event.button == 4:
                        Sum = 0
                        for i in range(5):
                            for j in range(5):
                                Sum += QwQ[j][i]
                        if Sum < RArmy and not( \
(x<145 or Map[(y-45)//100][(x-145)//100]-1 or DC[(y-45)//100][(x-145)//100])and \
(x>445 or Map[(y-45)//100][(x+55)//100]-1  or DC[(y-45)//100][(x+55)//100]) and \
(y<145 or Map[(y-145)//100][(x-45)//100]-1 or DC[(y-145)//100][(x-45)//100])and \
(y>445 or Map[(y+55)//100][(x-45)//100]-1  or DC[(y+55)//100][(x-45)//100]) and \
Map[(y-45)//100][(x-45)//100]-1 ):
                            QwQ[(y-45)//100][(x-45)//100] += 1
                    if event.button == 3 or event.button == 5:
                        if QwQ[(y-45)//100][(x-45)//100]:
                            QwQ[(y-45)//100][(x-45)//100] -= 1
            if event.type == KEYUP:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    Rrec = ' '
                    Brec = ' '
                    decide()
                    I += 1
                    # fight
                    for i in range(5):
                        for j in range(5):
                            if QwQ[j][i]:
                                RArmy -= QwQ[j][i]
                                if Map[j][i] != 1:
                                    RDispatch = True
                                if Rrec != ' ':
                                    Rrec += '-'
                                if QwQ[j][i] > 1:
                                    Rrec += str(QwQ[j][i])
                                if i==0:
                                    Rrec += 'A'
                                elif i==1:
                                    Rrec += 'B'
                                elif i==2:
                                    Rrec += 'C'
                                elif i==3:
                                    Rrec += 'D'
                                else:
                                    Rrec += 'E'
                                Rrec += str(5-j)
                            if QAQ[j][i]:
                                BArmy -= QAQ[j][i]
                                if Map[j][i] != 2:
                                    BDispatch = True
                                if Brec != ' ':
                                    Brec += '-'
                                if QAQ[j][i] > 1:
                                    Brec += str(QAQ[j][i])
                                if i==0:
                                    Brec += 'A'
                                elif i==1:
                                    Brec += 'B'
                                elif i==2:
                                    Brec += 'C'
                                elif i==3:
                                    Brec += 'D'
                                else:
                                    Brec += 'E'
                                Brec += str(5-j)
                            if (i == 0 and j == 0) or (i == 4 and j == 4):
                                if Map[j][i] == 0:
                                    if QwQ[j][i] > QAQ[j][i]:
                                        Map[j][i] = 1
                                    elif QwQ[j][i] < QAQ[j][i]:
                                        Map[j][i] = 2
                            elif (i == 0 and j == 4):
                                if QAQ[j][i] > max(QwQ[j][i]+2,QwQ[j][i]*2):
                                    ENDING = 'lost'
                            elif (i == 4 and j == 0):
                                if QwQ[j][i] > max(QAQ[j][i]+2,QAQ[j][i]*2):
                                    ENDING = 'won'
                            else:
                                if Map[j][i] == 1:
                                    if max(QwQ[j][i]+2,QwQ[j][i]*2) <= QAQ[j][i]:
                                        Map[j][i] = 2
                                elif Map[j][i] == 2:
                                    if max(QAQ[j][i]+2,QAQ[j][i]*2) <= QwQ[j][i]:
                                        Map[j][i] = 1
                                else:
                                    if QwQ[j][i] > QAQ[j][i]:
                                        Map[j][i] = 1
                                    elif QwQ[j][i] < QAQ[j][i]:
                                        Map[j][i] = 2
                    # clear lists
                    QwQ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                    QAQ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                    Map[2][2] = 0
                    # update Maxn
                    RMaxn = BMaxn = 3
                    if Map[0][0] == 1:
                        RMaxn += 1
                    if Map[0][0] == 2:
                        BMaxn += 1
                    if Map[4][4] == 1:
                        RMaxn += 1
                    if Map[4][4] == 2:
                        BMaxn += 1
                    for i in range(5):
                        for j in range(5):
                            if Map[j][i] == 1:
                                RMaxn += 1
                            elif Map[j][i] == 2:
                                BMaxn += 1
                    # update Army
                    if not RDispatch:
                        RArmy += min(I,4,RMaxn-RArmy)
                    if not BDispatch:
                        BArmy += min(I,4,BMaxn-BArmy)
                    RDispatch = BDispatch = False
                    if Rrec == ' ':
                        Rrec += '0'
                    if Brec == ' ':
                        Brec += '0'
                    print(str(I-1)+'.'+Rrec+Brec)
                    if Record:
                        file.write(str(I-1)+'.'+Rrec+Brec+'\n')
                    if ENDING != '':
                        end(ENDING)

                    DC  = [[1,1,1,1,1],\
                           [1,1,1,1,1],\
                           [1,1,1,1,1],\
                           [1,1,1,1,1],\
                           [1,1,1,1,1]]
                    DeadCityUpdate(0,4,2)
                    DeadCityUpdate(4,0,1)
                    if Map[0][0]:
                        DeadCityUpdate(0,0,Map[0][0])
                    if Map[4][4]:
                        DeadCityUpdate(4,4,Map[4][4])
        pygame.display.update()
        pygame.event.pump()

def PVP():
    if PVPtutorial:
        pygame.time.delay(100)
        for p in Pt:
            while True:
                Next = False
                window.blit(p,(0,0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        if Record:
                            file.close()
                        exit()
                    if event.type == KEYUP or event.type == MOUSEBUTTONUP:
                        Next = True
                        break
                if Next:
                    break
                pygame.display.update()
    global RArmy,BArmy,RMaxn,BMaxn,RDispatch,BDispatch,I,QwQ,QAQ,DC,Map
    ENDING = ''
    R_C = B_C = False # 双方是否已确认
    while True:
        window.blit(b2,(0,0))
        if RArmy//10:
            window.blit(num[RArmy//10],(549,62))
        window.blit(num[RArmy%10],(609,62))
        if BArmy//10:
            window.blit(num[BArmy//10],(549,366))
        window.blit(num[BArmy%10],(609,366))
        if RMaxn//10:
            window.blit(num[RMaxn//10],(680,160))
            window.blit(num[RMaxn%10],(740,160))
        else:
            window.blit(num[RMaxn%10],(680,160))
        if BMaxn//10:
            window.blit(num[BMaxn//10],(680,465))
            window.blit(num[BMaxn%10],(740,465))
        else:
            window.blit(num[BMaxn%10],(680,465))
        for i in range(5):
            for j in range(5):
                if Map[j][i] == 1:
                    window.blit(RB,(45+100*i,45+100*j))
                if Map[j][i] == 2:
                    window.blit(BB,(45+100*i,45+100*j))
        if R_C:
            window.blit(C,(40,550))
        if B_C:
            window.blit(C,(490,550))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                for x in range(5):
                    for y in range(5):
                        if event.key == RK[y][x] and not R_C:
                            Sum = 0
                            for i in range(5):
                                for j in range(5):
                                    Sum += QwQ[j][i]
                            if Sum < RArmy and not( \
(x==0 or Map[y][x-1]-1 or DC[y][x-1]) and (x==4 or Map[y][x+1]-1 or DC[y][x+1]) and \
(y==0 or Map[y-1][x]-1 or DC[y-1][x]) and (y==4 or Map[y+1][x]-1 or DC[y+1][x]) and \
Map[(y-45)//100][(x-45)//100]-1 ):
                                QwQ[y][x] += 1
                        if event.key == BK[y][x] and not B_C:
                            Sum = 0
                            for i in range(5):
                                for j in range(5):
                                    Sum += QAQ[j][i]
                            if Sum < BArmy and not( \
(x==0 or Map[y][x-1]-2 or DC[y][x-1]) and (x==4 or Map[y][x+1]-2 or DC[y][x+1]) and \
(y==0 or Map[y-1][x]-2 or DC[y-1][x]) and (y==4 or Map[y+1][x]-2 or DC[y+1][x]) and \
Map[(y-45)//100][(x-45)//100]-1 ):
                                QAQ[y][x] += 1
            if event.type == KEYUP:
                if event.key == RConfirm:
                    R_C = True
                if event.key == BConfirm:
                    B_C = True
                if event.key == RClear:
                    for i in range(5):
                        for j in range(5):
                            QwQ[j][i] = 0
                    R_C = False
                if event.key == BClear:
                    for i in range(5):
                        for j in range(5):
                            QAQ[j][i] = 0
                    B_C = False
        if R_C and B_C:
            Rrec = ' '
            Brec = ' '
            I += 1
            # fight
            for i in range(5):
                for j in range(5):
                    if QwQ[j][i]:
                        RArmy -= QwQ[j][i]
                        if Map[j][i] != 1:
                            RDispatch = True
                        if Rrec != ' ':
                            Rrec += '-'
                        if QwQ[j][i] > 1:
                            Rrec += str(QwQ[j][i])
                        if i==0:
                            Rrec += 'A'
                        elif i==1:
                            Rrec += 'B'
                        elif i==2:
                            Rrec += 'C'
                        elif i==3:
                            Rrec += 'D'
                        else:
                            Rrec += 'E'
                        Rrec += str(5-j)
                    if QAQ[j][i]:
                        BArmy -= QAQ[j][i]
                        if Map[j][i] != 2:
                            BDispatch = True
                        if Brec != ' ':
                            Brec += '-'
                        if QAQ[j][i] > 1:
                            Brec += str(QAQ[j][i])
                        if i==0:
                            Brec += 'A'
                        elif i==1:
                            Brec += 'B'
                        elif i==2:
                            Brec += 'C'
                        elif i==3:
                            Brec += 'D'
                        else:
                            Brec += 'E'
                        Brec += str(5-j)
                    if (i == 0 and j == 0) or (i == 4 and j == 4):
                        if Map[j][i] == 0:
                            if QwQ[j][i] > QAQ[j][i]:
                                Map[j][i] = 1
                            elif QwQ[j][i] < QAQ[j][i]:
                                Map[j][i] = 2
                    elif (i == 0 and j == 4):
                        if QAQ[j][i] > max(QwQ[j][i]+2,QwQ[j][i]*2):
                            ENDING = 'lost'
                    elif (i == 4 and j == 0):
                        if QwQ[j][i] > max(QAQ[j][i]+2,QAQ[j][i]*2):
                            ENDING = 'won'
                    else:
                        if Map[j][i] == 1:
                            if max(QwQ[j][i]+2,QwQ[j][i]*2) <= QAQ[j][i]:
                                Map[j][i] = 2
                        elif Map[j][i] == 2:
                            if max(QAQ[j][i]+2,QAQ[j][i]*2) <= QwQ[j][i]:
                                Map[j][i] = 1
                        else:
                            if QwQ[j][i] > QAQ[j][i]:
                                Map[j][i] = 1
                            elif QwQ[j][i] < QAQ[j][i]:
                                Map[j][i] = 2
            # clear lists
            QwQ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            QAQ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
            Map[2][2] = 0
            # update Maxn
            RMaxn = BMaxn = 3
            if Map[0][0] == 1:
                RMaxn += 1
            if Map[0][0] == 2:
                BMaxn += 1
            if Map[4][4] == 1:
                RMaxn += 1
            if Map[4][4] == 2:
                BMaxn += 1
            for i in range(5):
                for j in range(5):
                    if Map[j][i] == 1:
                        RMaxn += 1
                    elif Map[j][i] == 2:
                        BMaxn += 1
            # update Army
            if not RDispatch:
                RArmy += min(I,4,RMaxn-RArmy)
            if not BDispatch:
                BArmy += min(I,4,BMaxn-BArmy)
            RDispatch = BDispatch = False
            if Rrec == ' ':
                Rrec += '0'
            if Brec == ' ':
                Brec += '0'
            print(str(I-1)+'.'+Rrec+Brec)
            if Record:
                file.write(str(I-1)+'.'+Rrec+Brec+'\n')

            DC  = [[1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1]]
            DeadCityUpdate(0,4,2)
            DeadCityUpdate(4,0,1)
            if Map[0][0]:
                DeadCityUpdate(0,0,Map[0][0])
            if Map[4][4]:
                DeadCityUpdate(4,4,Map[4][4])

            R_C = B_C = False
        pygame.display.update()
        pygame.event.pump()
        if ENDING != '':
            print('Red %s.\n' % ENDING)
            if Record:
                file.write('Red %s.\n\n' % ENDING)
            Map = [[0,0,0,0,2],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [1,0,0,0,0],\
                   [0,0,0,0,0]]
            QwQ = [[0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0]]
            QAQ = [[0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0],\
                   [0,0,0,0,0]]
            DC  = [[1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1],\
                   [1,1,1,1,1]]
            RArmy = BArmy = 1
            RMaxn = BMaxn = 4
            RDispatch = BDispatch = False
            I=1
            break

def end(ENDING):
    pygame.quit()
    if Record:
        file.write('Red %s.\n\n' % ENDING)
        file.close()
    print('You %s.\n' % ENDING)
    os.system('pause')
    exit()

if __name__ == '__main__':
    start()
    game()
