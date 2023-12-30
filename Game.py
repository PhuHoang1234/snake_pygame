import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rec = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rec)
        #pygame.draw.rect(screen,(126,166,114),fruit_rec)
    
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        self.crunch_sound = pygame.mixer.Sound("Sound/crunch.wav")

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x*cell_size),int(block.y*cell_size),cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),block_rect)
    
    def move_snake(self):
        if self.new_block == True:
         body_copy = self.body[:]
         body_copy.insert(0,body_copy[0]+self.direction)
         self.body = body_copy[:]
         self.new_block = False
        else:
         body_copy = self.body[:-1]
         body_copy.insert(0,body_copy[0]+self.direction)
         self.body = body_copy[:]


    def add_block(self):
        self.new_block=True

    def play_crunch_sound(self):
        self.crunch_sound.play()


class MAIN:
    def __init__(self):
        self.fruit = FRUIT()
        self.snake = SNAKE()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.check_fail()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()


    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size*cell_number-60)
        score_y = int(cell_size*cell_number-40)
        score_rect = score_surface.get_rect(center=(score_x,score_y))
        screen.blit(score_surface,score_rect)


        

         
                


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
game_font = pygame.font.Font(None,25)
apple = pygame.image.load("Graphics/apple.png").convert_alpha()

fruit = FRUIT()
snake = SNAKE()
main = MAIN()
while True:
    #draw all our elements
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==SCREEN_UPDATE:
            main.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                if main.snake.direction.y!=1:
                 main.snake.direction = Vector2(0,-1)
            if event.key==pygame.K_d:
                if main.snake.direction.x!=-1:
                 main.snake.direction = Vector2(1,0)
            if event.key==pygame.K_a:
                if main.snake.direction.x!=1:
                 main.snake.direction = Vector2(-1,0)
            if event.key==pygame.K_s:
                if main.snake.direction.y!=-1:
                 main.snake.direction = Vector2(0,1)

    screen.fill((175,215,70))
    main.draw_elements()
    pygame.display.update()
    clock.tick(60)


