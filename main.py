'''
Muhammad Sidat
rock paper scissors meets conway's game of life
'''
#imports
import pygame
from random import randint
import glob

pygame.init()

#define screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway RPS")

#frame rate
clock = pygame.time.Clock()
FPS = 30

RPS = ("rock","paper","scissors")
#preload images
imageCache = {}
def get_image(key):
  #loads images and stores in dictionary
  if not key in imageCache:
    imageCache[key] = pygame.image.load(key)
  return imageCache[key]

images = glob.glob('*.png')
for image in images:
  get_image(image)

class cell(pygame.sprite.Sprite):
  #constructor
  def __init__(self, state, team, initX, initY):
    pygame.sprite.Sprite.__init__(self)
    self.state = state
    self.team = team
    self.velocityX = randint(-10,10)
    self.velocityY = randint(-10,10)
    self.image = imageCache[state+".png"]
    self.rect = self.image.get_rect()
    self.rect.center = (initX, initY)

  def update(self):
    #too jumpy and unpredictable maybe lock to framerate and move till it hits something
    #TODO bound to game window
    self.rect.center =(self.rect.centerx + self.velocityX , self.rect.centery + self.velocityY) 
    self.velocityX = randint(-10,10)
    self.velocityY = randint(-10,10)
        
#DELETE ME
testCell = cell(RPS[0],"a",500,300)
cells = pygame.sprite.Group()
cells.add(testCell)


#game loop
run = True
while run:

  clock.tick(FPS)

  #update background
  screen.fill("white")

  #update sprite group
  cells.update()

  #draw sprite group
  cells.draw(screen)
  

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.type == pygame.MOUSEBUTTONDOWN:
        print("click")
      elif event.type == pygame.MOUSEBUTTONUP:
        print("unclick")

  #update display
  pygame.display.flip()

pygame.quit()