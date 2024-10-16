# 这是扫雷的源代码。
# 运行前请先安装pygame库，命令行运行pip install pygame。
# 作者：氢気氚 | qinch，邮箱：BlueRectS@outlook.com
# 版本：v1.0.1
# 最后编辑时间：2024年8月27日 14:05:16
import random
import pygame
import sys
from tkinter import *
from tkinter import messagebox
import pygame.locals


pygame.init()
ZOOM = (48, 48)
scores = 10
YaHei = pygame.font.match_font("Microsoft YaHei")
scores_F = pygame.font.Font(YaHei, 20)
List = []
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
def fill_s(map):
    for i in range(0, 10):
        for k in range(0, 10):
            if map[i][k] == -1:
                continue
            boom = 0
            for x in range(max(0, i-1), min(9, i+1)+1):
                for y in range(max(0, k-1), min(9, k+1)+1):
                    if map[x][y] == -1:
                        boom += 1
            map[i][k] = boom
# AI赞助编写
i=0
boom_itme = 10
while i < boom_itme:
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    print(x,y)
    if map[x][y] == -1:
        i -= 1
        continue
    else:
        map[x][y] = -1
        i += 1


fill_s(map)



for i in map:
    print(i)
    
pygame.init()
screen = pygame.display.set_mode((480, 600))
pygame.display.set_caption("扫雷")
Air = pygame.image.load(".\\N.png")
B_1 = pygame.image.load(".\\1.png")
B_2 = pygame.image.load(".\\2.png")
B_3 = pygame.image.load(".\\3.png")
B_4 = pygame.image.load(".\\4.png")
B_5 = pygame.image.load(".\\5.png")
B_6 = pygame.image.load(".\\6.png")
B_7 = pygame.image.load(".\\7.png")
B_8 = pygame.image.load(".\\8.png")
Line = pygame.image.load(".\\P.png")
Vacant = pygame.image.load(".\\None.png")
BOOM = pygame.image.load(".\\BOOM.png")

Air = pygame.transform.scale(Air, ZOOM)
B_1 = pygame.transform.scale(B_1, ZOOM)
B_2 = pygame.transform.scale(B_2, ZOOM)
B_3 = pygame.transform.scale(B_3, ZOOM)
B_4 = pygame.transform.scale(B_4, ZOOM)
B_5 = pygame.transform.scale(B_5, ZOOM)
B_6 = pygame.transform.scale(B_6, ZOOM)
B_7 = pygame.transform.scale(B_7, ZOOM)
B_8 = pygame.transform.scale(B_8, ZOOM)
Line = pygame.transform.scale(Line, ZOOM)
Vacant = pygame.transform.scale(Vacant, ZOOM)
BOOM = pygame.transform.scale(BOOM, ZOOM)
Air_rect = Air.get_rect()
One_rect = B_1.get_rect()
Two_rect = B_2.get_rect()
Three_rect = B_3.get_rect()
Four_rect = B_4.get_rect()
Five_rect = B_5.get_rect()
Six_rect = B_6.get_rect()
Seven_rect = B_7.get_rect()
Eight_rect = B_8.get_rect()
Line_rect = Line.get_rect()
block = [Air, Air, Air, Air, Air, Air, Air, Air, Air,
         B_1, B_2, B_3, B_4, B_5, B_6, B_7, B_8, 
         Line, Line, Line, Line, Line, Line, Line, Line, 
         Line, Line, BOOM, Vacant, Air]


win = 0
while True:
    # print(x-1, y-1)
    if win == 10:
        messagebox.showinfo("恭喜", "你赢了!")
        pygame.quit()
        sys.exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[1] // 48 + 1
        y = mouse_pos[0] // 48 + 1
        # print(mouse_pressed[0])
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pressed[0]:
                if map[x-1][y-1] >= 1 and map[x-1][y-1] <= 8:
                    map[x-1][y-1] = map[x-1][y-1] + 8
                # AI赞助编写
                if map[x-1][y-1] == 0:
                    map[x-1][y-1] = -2
                    stack = [(x-1, y-1)]
                    while stack:
                        cx, cy = stack.pop()
                        for i in range(-1, 2):
                            for k in range(-1, 2):
                                nx, ny = cx + i, cy + k
                                if 0 <= nx < 10 and 0 <= ny < 10:
                                    if map[nx][ny] == 0:
                                        map[nx][ny] = -2
                                        stack.append((nx, ny))
                                    elif 1 <= map[nx][ny] <= 8:
                                        map[nx][ny] += 8

                elif map[x-1][y-1] == -1:
                    messagebox.showinfo("HH...", "你寄了")
                    pygame.quit()
                    sys.exit()
            
            if mouse_pressed[2]:
                print(map[x-1][y-1])

                if map[x-1][y-1] >= 1 and map[x-1][y-1] <= 8 and scores > 0:
                    map[x-1][y-1] = map[x-1][y-1] + 18
                    scores -= 1
                elif map[x-1][y-1] >= 17 and map[x-1][y-1] <= 24:
                    map[x-1][y-1] = map[x-1][y-1] - 18
                    scores += 1
                if map[x-1][y-1] == -1 and scores > 0:
                    if f'{x}, {y}' in List:
                        map[x-1][y-1] = -4
                        scores -= 1
                        win += 1
                    else:
                        scores -= 1
                        win += 1
                        List.append((f"{x}, {y}"))
                        print(List)
                        map[x-1][y-1] = -4
                elif map[x-1][y-1] == -4:
                    map[x-1][y-1] = -1
                    scores += 1
                    win -= 1
                if map[x-1][y-1] == 0 and scores > 0:
                    map[x-1][y-1] = -5
                    scores -= 1
                elif map[x-1][y-1] == -5:
                    map[x-1][y-1] = 0
                    scores += 1
    screen.fill((0,0,0))
    for i in range(10):
        for k in range(10):
            screen.blit(block[map[k][i]], (0+i*Air_rect.width, 0+k*Air_rect.height))
    
    
    scores_S = scores_F.render(f"剩余雷数{scores}", True, "white")
    screen.blit(scores_S, (0, Air_rect.height * 10))
    pygame.display.update()