# made by Alemayhu Bersabeh Binyam, ИИКб-22-1

import pygame
import random

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
screen_width = screen_hight = 800
'''↑↑↑ YOUR CODE HERE ↑↑↑'''

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hight))
done = False

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
number_of_stars = 200
speed = 0.08
stars = []
'''↑↑↑ YOUR CODE HERE ↑↑↑'''


def new_star():
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    x = random.randint(0, screen_width) - screen_width // 2
    y = random.randint(0, screen_hight) - screen_hight // 2
    z = 256
    color = 0
    star = [x, y, z, color]
    '''↑↑↑ YOUR CODE HERE ↑↑↑'''

    return star


def move_and_check(star: list):
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    x = (star[0] * 256) / star[2]
    y = (star[1] * 256) / star[2]

    star[2] -= speed  # Change Z coordinate

    # If the coordinates go beyond the screen, we generate a new star.
    if star[2] <= 0 or x <= -screen_width // 2 or x >= screen_width // 2 or y <= -screen_hight // 2 or y >= screen_hight // 2:
        star = new_star()

    # If the color has not reached maximum brightness, increase the color.
    if star[3] < 150:
        star[3] += 0.15

    # If suddenly the color becomes more than acceptable, then set it to 255.
    if star[3] >= 150:
        star[3] = 255

    '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    return star


def draw_star(star: list):
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    x = (star[0] * 256) / star[2] + screen_width // 2
    y = (star[1] * 256) / star[2] + screen_hight // 2
    '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    pygame.draw.circle(screen, (150, star[3], star[3]), (x, y), 3)


for i in range(0, number_of_stars):
    stars.append(new_star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(0, number_of_stars):
        s = stars[i]

        '''↓↓↓ YOUR CODE HERE ↓↓↓'''
        # Move the star and check if it still appear
        s = move_and_check(s)
        '''↑↑↑ YOUR CODE HERE ↑↑↑'''

        stars[i] = s

        '''↓↓↓ YOUR CODE HERE ↓↓↓'''
        # draw the star on the screen
        draw_star(s)
        '''↑↑↑ YOUR CODE HERE ↑↑↑'''

    pygame.display.flip()

pygame.quit()