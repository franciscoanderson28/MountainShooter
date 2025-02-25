import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('setup end')

print('loop start')
while True:
    # cheek for all events
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:# otaro
            pygame.quit() # close window
            quit() # end pygame
