import pygame, sys
from pygame.locals import *

from maze_generator import generate_maze
from maze_solver import solve_maze



pygame.init()

###### 数值定义 ######
# 尺寸
WIDTH = 400
HEADER = 30
HEIGHT = WIDTH + HEADER
WINDOW = (WIDTH, HEIGHT)

# 标题
TITLE = "迷宫v1.0       by zzy"

# 颜色
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)

# 初始化界面与标题
SCREEN = pygame.display.set_mode(WINDOW)
pygame.display.set_caption(TITLE)

# 字体
FONT_SIZE = 16
FONT = pygame.font.Font("ext/fonts/msyh.ttf", FONT_SIZE)
FONTWIN = pygame.font.Font("ext/fonts/msyh.ttf", FONT_SIZE * 3)

# 迷宫flag
flag = 0
flag2 = 0

##### 函数定义 #####

# 绘制元素（方块）
def draw_rect(x, y, len, color):
    pygame.draw.rect(SCREEN, color, [x, y, len, len], 0)
# 绘制元素（圆形）
def draw_circle(x, y, r, color):
    pygame.draw.circle(SCREEN, color, [x, y], r, 0)

# 判断按钮按下
def dispatcher_click(pos):

    global flag, flag2, MAZE, POS_NOW, EXIT, ENTRANCE

    pos_x, pos_y = pos
    if 2 <= pos_x <= 52 and 2 <= pos_y <= 38:                           ### 简单

        MAZE, ENTRANCE, EXIT = generate_maze(11,11)                     # 生成迷宫0，1数组，出入口位置坐标
        pygame.draw.rect(SCREEN, COLOR_WHITE, [0, 30, 400, 400], 0)     # 屏幕涂白
        POS_NOW = ENTRANCE
        draw_maze(MAZE, ENTRANCE)                                                 # 绘制迷宫        
        flag = 1
        flag2 = 0

    elif 62 <= pos_x <= 112 and 2 <= pos_y <= 38:                       ### 困难

        MAZE, ENTRANCE, EXIT = generate_maze(23,23)                     # 生成迷宫0，1数组，出入口位置坐标
        pygame.draw.rect(SCREEN, COLOR_WHITE, [0, 30, 400, 400], 0)     # 屏幕涂白
        POS_NOW = ENTRANCE
        draw_maze(MAZE, ENTRANCE)                                                 # 绘制迷宫       
        flag = 1
        flag2 = 0

    elif 122 <= pos_x <= 172 and 2 <= pos_y <= 38:                      ### 答案
        if flag == 1:
            MAZE1 = solve_maze(MAZE, POS_NOW, EXIT)
            draw_solve(MAZE1, POS_NOW)                                                 # 绘制路径
            flag2 = 1
    
    
  
        
# 绘制路径
def draw_solve(maze, now):
    size = len(maze)
    cell_size = int(WIDTH / size)                             # 元素尺寸
    cell_padding = (WIDTH - (cell_size * size)) / 2           # 边距

    for y in range(size):
        for x in range(size):
            cell = maze[y][x]
            if cell == 2:
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_WHITE)
                draw_circle(int(cell_padding + (x + 0.5) * cell_size), int(HEADER + cell_padding + (y + 0.5) * cell_size), int(0.3 * cell_size) , COLOR_RED)
            elif cell == 3 or cell == 0:
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_WHITE)
    draw_rect(cell_padding + now[0] * cell_size, HEADER + cell_padding + now[1] * cell_size, cell_size - 1, COLOR_GREEN)




                



        


# 绘制按钮
def draw_button(x, y, len, height, text):
    pygame.draw.rect(SCREEN, COLOR_RED, [x, y, len, height], 1)
    text_surface = FONT.render(text, True, COLOR_RED)
    text_len = text.__len__() * FONT_SIZE
    # 文字居中
    SCREEN.blit(text_surface, (x + (len - text_len) / 2, y + 2))


# 绘制迷宫
def draw_maze(maze, ENTRANCE):
    size = len(maze)
    cell_size = int(WIDTH / size)                             # 元素尺寸
    cell_padding = (WIDTH - (cell_size * size)) / 2           # 边距
    for y in range(size):
        for x in range(size):
            cell = maze[y][x]
            color = COLOR_BLACK if cell == 1 else COLOR_WHITE
            draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, color)
    draw_rect(cell_padding + ENTRANCE[0] * cell_size, HEADER + cell_padding + ENTRANCE[1] * cell_size, cell_size - 1, COLOR_GREEN)                 # 起始点 绿色块


   

def draw_path(maze, now, next):
    size = len(maze)
    cell_size = int(WIDTH / size)                             # 元素尺寸
    cell_padding = (WIDTH - (cell_size * size)) / 2           # 边距
    
    maze[1][0] = 4

    x = next[0]
    y = next[1]
    x0 = now[0]
    y0 = now[1]
    if flag2 == 0:
        if 0 <= x <= size and 0 <= y <= size :
            if maze[y][x] == 0:                                                           # 按下答案前
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_GREEN)
                draw_rect(cell_padding + x0 * cell_size, HEADER + cell_padding + y0 * cell_size, cell_size - 1, COLOR_CYAN)
                maze[y][x] = 4
                now = next

            elif  maze[y][x] == 4:
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_GREEN)
                draw_rect(cell_padding + x0 * cell_size, HEADER + cell_padding + y0 * cell_size, cell_size - 1, COLOR_WHITE)
                maze[y0][x0] = 0
                now = next
    if flag2 == 1:                                                                         # 按下答案后
        if 0 <= x <= size and 0 <= y <= size :
            if maze[y][x] == 2:
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_GREEN)
                draw_rect(cell_padding + x0 * cell_size, HEADER + cell_padding + y0 * cell_size, cell_size - 1, COLOR_WHITE)
                maze[y][x] = 4
                now = next

            elif  maze[y][x] == 4 or maze[y][x] == 3 or maze[y][x] == 0:
                draw_rect(cell_padding + x * cell_size, HEADER + cell_padding + y * cell_size, cell_size - 1, COLOR_GREEN)
                draw_rect(cell_padding + x0 * cell_size, HEADER + cell_padding + y0 * cell_size, cell_size - 1, COLOR_WHITE)
                draw_circle(int(cell_padding + (x0 + 0.5) * cell_size), int(HEADER + cell_padding + (y0 + 0.5) * cell_size), int(0.3 * cell_size) , COLOR_RED)
                maze[y0][x0] = 2
                now = next
    return maze, now




##### 循环 #####
if __name__ == '__main__':

    SCREEN.fill(COLOR_WHITE)
    draw_button(2, 2, 50 , HEADER - 4, '简单')
    draw_button(62, 2, 50 , HEADER - 4, '困难')
    draw_button(122, 2, 50 , HEADER - 4, '答案') 
    
    

    while True:    
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            # 按下键盘
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if flag == 1:
                    if event.key == K_UP:
                        pos_next = [POS_NOW[0], POS_NOW[1] - 1]
                        MAZE, POS_NOW = draw_path(MAZE, POS_NOW, pos_next)
                    elif event.key == K_RIGHT:
                        pos_next = [POS_NOW[0] + 1, POS_NOW[1]]
                        MAZE, POS_NOW = draw_path(MAZE, POS_NOW, pos_next)
                    elif event.key == K_DOWN:
                        pos_next = [POS_NOW[0], POS_NOW[1] + 1]
                        MAZE, POS_NOW = draw_path(MAZE, POS_NOW, pos_next)
                    elif event.key == K_LEFT:
                        pos_next = [POS_NOW[0] - 1, POS_NOW[1]]
                        MAZE, POS_NOW = draw_path(MAZE, POS_NOW, pos_next)

            # 按下鼠标
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                dispatcher_click(mouse_pos)                     # 判断按钮按下
        
        if flag == 1:
            if POS_NOW == EXIT:
                draw_rect(0, 30, 400, COLOR_WHITE)              # 成功后的显示
                flag = 0
                


                text_win = FONTWIN.render('您已到达终点', True, COLOR_BLACK)
                text_len = len('您已到达终点') * FONT_SIZE * 3
                SCREEN.blit(text_win, ( (400 - text_len) / 2, 130))
                text_win = FONT.render("单击'简单'或'困难'再玩一次", True, COLOR_BLACK)
                text_len = (len("单击'简单'或'困难'再玩一次") - 4) * FONT_SIZE 
                SCREEN.blit(text_win, ( (400 - text_len) / 2, 250))
                text_win = FONT.render('或ESC键退出', True, COLOR_BLACK)
                text_len = (len('或ESC键退出') - 1 ) * FONT_SIZE 
                SCREEN.blit(text_win, ( (400 - text_len) / 2, 300))


        pygame.display.update()




