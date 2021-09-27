import pygame
pygame.init() 

size = (400, 400)
screen = pygame.display.set_mode(size)

# Load the bedroom image location
bedroom=pygame.image.load("                  ").convert()
# Scale the bedroom image to size (600, 400) 
bedroom_scaled=pygame.transform.smoothscale(bedroom,(       ))
# Load the john_childhood image location 
john=pygame.image.load("                  ").convert_alpha()
# Scale john's image to size (100, 200) 
john_scaled=pygame.transform.smoothscale(john,(       ))

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
      
  # Display scaled bedroom image at (-15, 0)
  screen.blit(bedroom_scaled,(       ))
  # Display scaled john's image at (150, 100)
  screen.blit(john_scaled,(       ))
  
  pygame.display.flip()
pygame.quit()
