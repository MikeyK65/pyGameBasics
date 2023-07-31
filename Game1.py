import pygame

def main():
    pygame.init()

    #logo = pygame.image.load("")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Basic Program")

    screen = pygame.display.set_mode((400,400))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running = False;



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()



