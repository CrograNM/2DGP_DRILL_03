from pico2d import *
import math

# 개발에 있어서 중요한 것은 실행 가능한 가장 큰 뼈대를 만드는 것.
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)

def run_bottom_right():
    print('bottom_right')
    for x in range(400, 750, 10):
        draw_boy(x, 50)
    pass

def run_bottom_left():
    print('bottom_left')
    for x in range(50, 400, 10):
        draw_boy(x, 50)
    pass

def run_right():
    print('right')
    for y in range(50, 550, 10):
        draw_boy(750, y)
    pass

def run_top():
    print('top')
    for x in range(750, 50, -10):
        draw_boy(x, 550)
    pass

def run_left():
    print('left')
    for y in range(550, 50, -10):
        draw_boy(50, y)
    pass

def run_rectangle():
    print('rectangle')
    run_bottom_right()
    run_right()
    run_top()
    run_left()
    run_bottom_left()
    pass # pass : 유보기능 - C로 따지면 아무것도 없는 빈 함수

def run_circle():
    print('Circle')
    r, cx, cy = 250, 800//2, 600//2

    for d in range(-90, 270):     # d = degree
        x = r * math.cos(math.radians(d)) + cx  
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x, y) 
    pass

while(1) :
    run_circle()
    run_rectangle()
    # break
    # **TOP-DOWN-DESIGN : 큰 틀을 잡고 내부를 채우는 하향식 설계 방식**

close_canvas()
