import pygame
import time
import math
import random

pygame.init()

windown_size = width, height = 800, 400
screen = pygame.display.set_mode(windown_size)
ingame = True

class Explosion():

    def __init__(self, position):
        self.position_initial = position
        self.frame = 1
        self.running = True
        self.color = (255,255,255)

    def increment_postion(self, increment_position):
        return tuple(y+x for y, x in zip(self.position_initial, increment_position))

    def draw_circle(self, position, size):
        pygame.draw.circle(screen, self.color, position, size)

    def defrag_circle(self, num_circles, position_distance, size):
        for i in range(num_circles):
            distance = random.randint(position_distance[0],position_distance[1])
            angle = (360/num_circles)*(i+1)           
            position = (int(math.cos(angle)*distance), int(math.sin(angle)*distance))
            self.draw_circle(self.increment_postion(position), size)
       

    def draw(self):
        
        if self.frame == 1:
            
            self.defrag_circle(num_circles = 1, position_distance = (0,2), size = 2)
            self.frame += 1
        elif self.frame == 2:
            self.defrag_circle(num_circles = 2, position_distance = (0,2), size = 5)
            self.frame += 1
        elif self.frame == 3:
            self.defrag_circle(num_circles = 3, position_distance = (2,5), size = 10)
            self.frame += 1   

        elif self.frame == 4:
            self.defrag_circle(num_circles = 4, position_distance = (5,15), size = 15)
            self.frame += 1   

        elif self.frame == 5:
            self.defrag_circle(num_circles = 5, position_distance = (15,25), size = 20)
            self.frame += 1   

        elif self.frame == 6:
            self.defrag_circle(num_circles = 6, position_distance = (25,35), size = 15)
            self.frame += 1    

        elif self.frame == 7:
            self.defrag_circle(num_circles = 7, position_distance = (35,45), size = 10)
            self.frame += 1   

        elif self.frame == 8:
            self.defrag_circle(num_circles = 8, position_distance = (45,55), size = 5)
            self.frame += 1   

        elif self.frame == 9:
            self.defrag_circle(num_circles = 9, position_distance = (55,65), size = 2)
            self.frame += 1   
        else:
            if self.frame > 9:
                self.running = False

explosions = []

while ingame:
    screen.fill((0,0,0))
    time.sleep(0.03)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            explosions.append(Explosion(pos))

    for explosion in explosions:
        if explosion.running:
            explosion.draw()

    pygame.display.update()

    for key, explosion in enumerate(explosions):
        if not explosion.running:
            del(explosions[key])