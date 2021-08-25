import pygame
pygame.init() 

size = (400, 400)
screen = pygame.display.set_mode(size)
#Load and scale the images




pygame.display.set_caption("Project C9")
#Create "carryOn" variable and set to true
carryOn = True
#Begin the while loop
while carryOn:
  #Iterate through each event
  for event in pygame.event.get():
    #Identify is user has quit 
    if event.type == pygame.QUIT: 
      #change "carryOn" to False
      carryOn = False 
  #Display the images
  
  
  
  pygame.display.flip()
pygame.quit()
