from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame=random.randint(0, 7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.r = random.randint(1, 2) * 10
        if self.r == 10:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.v = random.randint(0, 20) + 5

    def update(self):
        self.y -= self.v
        if self.y - self.r + 1 < 60:
            self.y = 60 + self.r - 1

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




def reset_world():
    global running
    global grass
    global team
    global world
    global ball

    running = True
    world=[]

    grass = Grass() # 클래스를 이용해서 객체를 찍어냄.
    world.append(grass)

    team = [Boy() for i in range(11)]
    ball = [Ball() for i in range(20)]
    world+=team + ball


def update_world():
    for o in world:
        o.update()




def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()



open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world() # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.05)

# finalization code

close_canvas()
