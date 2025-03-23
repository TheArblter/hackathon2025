import numpy
import pygame
import asyncio
import pygame.sndarray



#initializing pygame
pygame.init()
clock = pygame.time.Clock()

async def main():
    Asset_Path = "C:\\Users\\nikwi\\Documents\\GitHub\\hackathon2025\\images\\"

    #Misc
    Window_Width, Window_Height = 1000, 800
    Movement = 0.05
    Pinguin_list = [
        (239, 175, 340, 382),
        (673, 677, 437, 382),
        (1138, 178, 427, 382)
    ]


    #animation sheet
    class Animation_Sheet():
        def __init__ (self, pinguin_sheet_path, pinguin_positions):
            image = pygame.image.load(pinguin_sheet_path).convert_alpha()
            self.pinguins = [] #list
            for position in pinguin_positions:
                pinguin = image.subsurface(pygame.Rect(position))
                self.pinguins.append(pinguin)



    #pet
    class Pet():

        def __init__(self, position):

            #loading animation sheet
            self.pet_animations = Animation_Sheet(Asset_Path + "PinguinsSheet.png", Pinguin_list)

            self.current_animation = self.pet_animations.pinguins
            #Pet_picture = pygame.image.load(Asset_Path + "PinguinsSheet.png").convert_alpha()
            self.image = self.pet_animations.pinguins[0]
            self.rect = self.image.get_rect(bottomleft = position)
            self.animation_action = 0
            self.idle_state = "Move Hands"

        def update(self):
            
            #animations
            self.Animations()
        
            #animating (telling code that after it reaches last image cycle back to first)
            self.animation_action += self.animation_speed
            if self.animation_action >= len(self.current_animation):
                self.animation_action = 0

            #use int to round down from to integers since only have 3 animations (animation_action is set to 0 and animation_speed is set to .05 so it naturally goes up in increments of .2 and dont have .2 of an image) 
            self.image = self.current_animation[int(self.animation_action)]    


        def draw(self, displaySurface):
            displaySurface.blit(self.image, self.rect)

        def Animations(self):
            self.animation_speed = Movement
        # if self.idle_state == "Move Hands":
                #self.current_animation = self.Amimation_Sprite_sheet.get_sprite()




    #background 
    class Screen():
        def __init__(self, displaySurface):
            #loading background and scalling up
            self.wallpaper = pygame.image.load(Asset_Path + "IcyWallpaper.png").convert()
            self.wallpaper = pygame.transform.scale(self.wallpaper, (Window_Width, Window_Height))

            #loading pet
            self.penguin = Pet((300, 650))

            self.displaySurface = displaySurface
        #might not need update
        def update(self):
            self.penguin.update()

        def draw(self):
            #draws the background image every frame btw ((0,0) top left coordinate)
            
            displaySurface.blit(self.wallpaper, (0,0))
            self.penguin.draw(self.displaySurface)

        def run(self):
            self.update()
            self.draw()





    #dispay 
    displaySurface = pygame.display.set_mode((Window_Width, Window_Height))
    pygame.display.set_caption("MyFinancePet")
    Background = Screen(displaySurface)




    #game loop
    Game_running = True
    while Game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game_running = False

        Background.run()            
    #setting fps
        pygame.display.flip()
        clock.tick(60)

    
    await asyncio.sleep(0)

asyncio.run(main())    
pygame.quit()            










