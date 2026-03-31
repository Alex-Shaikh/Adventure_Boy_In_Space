# A game where adventure boy climbs his way into space.
__author__ = "Alex Shaikh"
__version__ = "3.30.2026"

__User__ = "Alex" # this is what is displayed on the leaderboard
# Flint Link https://app.flintk12.com/activities/platform-jumper-cc84ca/sessions/4071c560-6196-4202-9f55-de36a9fe367a


# definition of a Foddian game: Foddian video game
# A subgenre of video games characterized by their anger-inducing, monotonous nature.
# The subgenre is named after Bennett Foddy, creator of hugely popular game Getting Over It.
# Although not the first of its kind, this game largely popularized the subgenre and brought it into the mainstream.


# My extras for this game is that the camera follows the player and the timer
import pygame
from player import Player
from JumpPlatform import JumpPlatform
from NormalPlatform import NormalPlatform
from TemporaryPlatform import TemporaryPlatform
from DayPlatform import DayPlatform
from NightPlatform import NightPlatform

#This function spawns in all the platforms and puts them into a sprite group
# It returns the group
def spawnPlatforms():
    platforms = []
    platforms.append(NormalPlatform(250, 15, 200, 720))
    platforms.append(NormalPlatform(350, 80, 700, 660))
    platforms.append(NormalPlatform(250, 50, 200, 410))
    platforms.append(NormalPlatform(250, 50, 355, -10))
    platforms.append(NormalPlatform(150, 50, 85, 220))
    platforms.append(NormalPlatform(150, 50, 775, -10))
    platforms.append(NormalPlatform(350, 50, 475, -240))
    platforms.append(NormalPlatform(350, 500, 945, -530))
    platforms.append(NormalPlatform(200, 50, 545, -830))
    platforms.append(NormalPlatform(200, 50, 345, -930))
    platforms.append(NormalPlatform(200, 250, 85, -1230))
    platforms.append(NormalPlatform(150, 50, 465, -1330))
    platforms.append(NormalPlatform(150, 90, 865, -1620))
    platforms.append(NormalPlatform(470, 50, 85, -1620))
    platforms.append(NormalPlatform(100, 50, 85, -1850))
    platforms.append(NormalPlatform(100, 50, 85, -1850))
    platforms.append(NormalPlatform(100, 50, 390, -2050))
    platforms.append(NormalPlatform(100, 50, 690, -2250))
    platforms.append(NormalPlatform(140, 75, 950, -2450))
    platforms.append(NormalPlatform(100, 305, 1030, -2750))
    platforms.append(NormalPlatform(100, 75, 750, -2700))
    platforms.append(NormalPlatform(50, 75, 1000, -2940))
    platforms.append(NormalPlatform(100, 75, 680, -2960))
    platforms.append(JumpPlatform(100, 75, 350, -2560))
    platforms.append(NormalPlatform(100, 75, 185, -2950))
    platforms.append(NormalPlatform(100, 45, 350, -3235))
    platforms.append(NormalPlatform(140, 35, 570, -3425))
    platforms.append(TemporaryPlatform(100, 35, 920, -3565))
    platforms.append(TemporaryPlatform(100, 35, 580, -3725))
    platforms.append(TemporaryPlatform(100, 35, 370, -3855))
    platforms.append(NormalPlatform(100, 55, 700, -4025))
    platforms.append(JumpPlatform(100, 25, 450, -4225))
    platforms.append(NormalPlatform(120, 55, 125, -4300))
    platforms.append(NormalPlatform(60, 205, 95, -4500))
    platforms.append(TemporaryPlatform(180, 25, 740, -4475))
    platforms.append(NormalPlatform(70, 35, 315, -4820))
    platforms.append(TemporaryPlatform(70, 35, 575, -4990))
    platforms.append(TemporaryPlatform(70, 35, 870, -5230))
    platforms.append(TemporaryPlatform(70, 35, 575, -5290))
    platforms.append(TemporaryPlatform(70, 35, 385, -5490))
    platforms.append(DayPlatform(170, 35, 85, -5620))
    platforms.append(NightPlatform(85, 35, 455, -5820))
    platforms.append(NightPlatform(125, 35, 745, -6020))
    platforms.append(NightPlatform(85, 35, 385, -6220))
    platforms.append(DayPlatform(110, 25, 705, -6420))
    platforms.append(NightPlatform(110, 25, 975, -6520))
    platforms.append(NightPlatform(155, 25, 675, -6720))
    platforms.append(JumpPlatform(75, 15, 375, -6500))
    platforms.append(DayPlatform(75, 25, 95, -6750))
    platforms.append(NightPlatform(385, 25, 395, -7030))
    platforms.append(DayPlatform(65, 35, 880, -7220))
    platforms.append(TemporaryPlatform(65, 35, 525, -7420))
    platforms.append(NightPlatform(65, 35, 225, -7520))
    platforms.append(NightPlatform(5, 85, 155, -7840))
    platforms.append(NightPlatform(120, 15, 285, -7800))
    platforms.append(NightPlatform(90, 15, 555, -7880))
    platforms.append(DayPlatform(90, 35, 775, -8020))
    platforms.append(TemporaryPlatform(90, 15, 405, -8080))
    platforms.append(NightPlatform(90, 15, 105, -8300))
    platforms.append(TemporaryPlatform(90, 15, 275, -8520))
    platforms.append(NightPlatform(80, 15, 550, -8400))
    platforms.append(TemporaryPlatform(90, 15, 805, -8620))
    platforms.append(DayPlatform(70, 45, 955, -8820))
    platforms.append(NightPlatform(100, 15, 755, -8980))
    platforms.append(NightPlatform(90, 15, 555, -9120))
    platforms.append(NightPlatform(80, 15, 305, -9250))
    platforms.append(NightPlatform(70, 15, 85, -9440))
    platforms.append(DayPlatform(90, 35, 355, -9620))
    platforms.append(NightPlatform(60, 15, 715, -9800))
    platforms.append(NightPlatform(50, 15, 915, -10000))
    platforms.append(NightPlatform(40, 15, 615, -10200))
    platforms.append(NormalPlatform(100, 45, 915, -10420))
    sprite_group = pygame.sprite.Group()
    for platform in platforms:
        sprite_group.add(platform)
    return sprite_group

# This draws helpful information such as hits onto the screen based on the camera position
def drawText(camera,screen):
    if camera == 0:
        font = pygame.font.Font(None, 30)
        text_surface = font.render("Use arrow Keys to walk.", True,(0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.x = 550
        text_rect.y = 300
        screen.blit(text_surface, text_rect)
        text_surface = font.render("Press R to restart a jump.", True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 550
        text_rect.y = 200
        screen.blit(text_surface, text_rect)
        font = pygame.font.Font(None, 18)
        text_surface = font.render(
            "Hold space or up arrow to jump. Hold arrows while jumping to jump that direction(release the jump before releasing direction).The longer you press, the higher you go!",
            True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 10
        text_rect.y = 500
        font = pygame.font.Font(None, 52)
        text_surface2 = font.render(
            "EASY SECTION", True,
            (0, 255, 0))
        text_rect2 = text_surface.get_rect()
        text_rect2.x = 510
        text_rect2.y = 400
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)

    if camera == -800:
        font = pygame.font.Font(None, 30)
        text_surface = font.render(
            "To pass this jump, lightly press jump. Jump into walls to bounce off them.", True,
            (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 210
        text_rect.y = 500
        screen.blit(text_surface, text_rect)
    if camera == -2400:
        font = pygame.font.Font(None, 52)
        text_surface = font.render(
            "MEDIUM SECTION", True,
            (250, 200, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 210
        text_rect.y = 500
        screen.blit(text_surface, text_rect)
    if camera == -3200:
        font = pygame.font.Font(None, 23)
        text_surface = font.render(
            "These are bouncy Platforms. You bounce you when you jump on them. Higher jump = higher bounce ", True,
            (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 110
        text_rect.y = 400
        screen.blit(text_surface, text_rect)
    if camera == -4000:
        font = pygame.font.Font(None, 24)
        text_surface = font.render(
            "These are Temporary Platforms. Don't stand on them for too long or they will break!", True,
            (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 110
        text_rect.y = 520
        screen.blit(text_surface, text_rect)
    if camera == -5600:
        font = pygame.font.Font(None, 52)
        text_surface = font.render(
            "HARD SECTION", True,
            (255, 20, 20))
        text_rect = text_surface.get_rect()
        text_rect.x = 110
        text_rect.y = 400
        screen.blit(text_surface, text_rect)
    if camera == -6400:
        font = pygame.font.Font(None, 30)
        text_surface = font.render(
            "These are Day and Night platforms. You can only see Night Platforms when on Day Platforms.", True,
            (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.x = 110
        text_rect.y = 320
        screen.blit(text_surface, text_rect)


# This draws the background based on the camera position
def drawBG(screen,camera,groundBG,skyBG,spaceBG):
    if camera <= -5600:
        screen.blit(spaceBG,screen.get_rect())
    elif camera <= -2400:
        screen.blit(skyBG,screen.get_rect())
    else:
        screen.blit(groundBG,screen.get_rect())

# This reads the top times from the file and stores it in a list and returns it
def readTimes():
    handle = open('Leaderboard_Times', 'r')
    times = []
    for line in handle:
        line = line.strip()
        times.append({"User":line[:line.find('#')], "time_ms":int(line[line.find("#")+1:line.find("%")]), "time_str":line[line.find("%")+1:]})
    handle.close()
    return times

# This adds your score to the file
# This adds the username the time in ms and in text
def writeTime(time,timestr):
    times = readTimes()
    times.append({"User":__User__, "time_ms":time, "time_str": timestr})
    times.sort(key=lambda x: x["time_ms"])
    handle = open('Leaderboard_Times', 'w')
    for record in times:
        handle.write(record["User"]+"#" + str(record["time_ms"])+"%"+record["time_str"]+"\n")
    handle.close()

# This draws the Leaderboard with the top 10 times
def drawLeaderboard(screen):
    font = pygame.font.Font(None, 32)
    y = 120
    times = readTimes()
    for i in range(10):
        if len(times) <= i:
            break
        text_surface = font.render(str(i+1)+" "+times[i]["User"] + "  " + times[i]["time_str"], True, (255, 255, 255),0)
        text_rect = text_surface.get_rect()
        text_rect.y = y
        text_rect.x = 400
        y += 50
        screen.blit(text_surface, text_rect)

def main():
    running = True
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1040, 800))
    min_height = 690  # Controls the minimum height so the player can't go off-screen
    character = Player(min_height) # spawns in the player
    jumping = 0 # Controls how many frames the player is jumping
    #These are all self-explanatory
    velocityY = 0
    jumpingRight = False
    jumpingLeft = False
    walkingLeft = False
    walkingRight = False
    # Whether the player has bounced off of a wall
    rebounded = False
    #Whether on a day platform so can make night platforms visible
    onDayPlatform = False
    # Amount of jumps completed out of 65 (throughout the whole playtime)
    platformsCompleted = 0
    # loads in the sounds
    jumpSound = pygame.mixer.Sound('adventure_boy/Jump2.wav')
    bounceSound = pygame.mixer.Sound('adventure_boy/Blip.wav')
    # Load in BG images
    groundBG = pygame.transform.scale(pygame.image.load("adventure_boy/sprites/GroundBG.jpg"), (1040, 800))
    skyBG = pygame.transform.scale(pygame.image.load("adventure_boy/sprites/SkyBG.png"), (1040, 800))
    spaceBG = pygame.transform.scale(pygame.image.load("adventure_boy/sprites/spaceBG.jpg"), (1040, 800))
    # Dictionary that has all the platform y positions so when r is pressed it will got to the highest one
    playback = {
        "690": 0
    }
    jumpCounter = 0 # how long the player has held down jump
    velocityX = 6 # velocity when jumping
    collisions = [] # a list of all the collisions present
    platform_group = spawnPlatforms() # makes the platform group
    character.Stand() # start the player standing
    grounded = False # whether the player is standing on something
    camera = 0 # the camera y position
    submittedTime =False # whether the player has submitted their time this run so it won't get added multiple times
    pygame.mixer.init() # init mixer
    while running: # main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed() # get inputs

        if key[pygame.K_r]: # teleports the player to the highest platform they have reached
            playbackList = list(playback.items())
            playbackListCopy = []
            for position in playbackList:
                playbackListCopy.append([int(position[0]),int(position[1])])
            playbackListCopy.sort()
            velocityY = 0
            velocityX = 0
            character.rect.y = playbackListCopy[0][0]
            character.rect.x = playbackListCopy[0][1]

        if (key[pygame.K_SPACE] or key[pygame.K_UP]) and grounded: # if on the ground and pressing space
            # start charging up the jump
            jumpCounter += 1
            character.Stand()
            if jumpCounter > 60:
                jumpCounter = 60

        else:
            if jumpCounter > 0 and grounded:
                # On letting go of the jump button, jump
                jumpSound.play()
                if key[pygame.K_LEFT]:
                    jumpingLeft = True
                elif key[pygame.K_RIGHT]:
                    jumpingRight = True
                jumping = int(jumpCounter/2)
                velocityY = 10 + (0.27 * jumpCounter)
                jumpCounter = 0
            # Jumping in a direction
            if jumpingRight:
                character.JumpRight()
            if jumpingLeft:
                character.JumpLeft()

        squish = 110 - jumpCounter # how much the character is squished based on how charged the jump is
        if not key[pygame.K_SPACE] and not key[pygame.K_UP]:
            # handles walking left and right
            if key[pygame.K_LEFT]:
                if grounded:
                    walkingLeft = True
            elif key[pygame.K_RIGHT]:
                if grounded:
                    walkingRight = True
            else:
                if grounded:
                    character.Stand()
        # if hit your head, stop going up
        if 4 in collisions:
            velocityY = 0
            bounceSound.play()
        character.rect.move_ip(0, -velocityY) # move the character based on y velocity
        collisions = []
        for plat in platform_group: # updates all collisions
            collisions.append(plat.collisions(character))

        if (1 in collisions or 6 in collisions) or character.rect.y >= min_height: # if on top on platform
            grounded = True
        else:
            grounded = False
        if 6 in collisions: # on day platform
            onDayPlatform = True
        else:
            onDayPlatform = False
        if 5 in collisions: # on a bouncy platform
            bounceSound.play()
            if velocityY >=0: # stops getting stuck on the platform
                velocityY = -5
            if not (jumpingLeft or jumpingRight) and not(walkingLeft or walkingRight): # stops getting stuck on the platform
                jumpingRight = True
            velocityY = - 1.1*velocityY # reverse velocity and increase it a bit
            velocityX = 5 # slow x velocity a tad

        if walkingLeft and not jumpingRight and not jumpingLeft: # moves to the left if walking left
            character.WalkLeft() #play anim
            character.rect.move_ip(-velocityX, 0)
        elif walkingRight and not jumpingRight and not jumpingLeft: # moves to the right if walking right
            character.Walk() # play anim
            character.rect.move_ip(velocityX, 0)

        # Moves the camera with the character position
        if character.rect.y - camera < -110:
            camera -= 800
        if character.rect.y - camera > screen.get_height():
            camera += 800

        # Stops the player going out of bounds
        if character.rect.y > min_height:
            character.rect.y = min_height
        if character.rect.x + character.rect.width > 1040 :
            character.rect.x = 1040 - character.rect.width
        if character.rect.x < 0 :
            character.rect.x = 0

        if not grounded: #applies gravity acceleration
            velocityY -= 1
            if velocityY < -40:
                velocityY = -40
            jumpCounter = 0
        else:
            if not playback.__contains__(str(character.rect.y)): # If on a new platform, add it to the list of teleportable platforms
                playback[str(character.rect.y)]=character.rect.x
            velocityY = 0
            jumpingRight = False
            jumpingLeft = False
            rebounded = False
            walkingLeft = False
            walkingRight = False
            velocityX = 6
        if jumpingRight:
            if 2 in collisions: # turns player around if bounced of platform
                jumpingRight = False
                jumpingLeft = True
                rebounded = True
                bounceSound.play()
            else:
                if not rebounded: # moves player
                    character.rect.move_ip(8, 0)
                else:
                    character.rect.move_ip(4, 0)
        if jumpingLeft:
            if 3 in collisions:# turns player around if bounced of platform
                jumpingLeft = False
                jumpingRight = True
                rebounded = True
                bounceSound.play()
            else:
                if not rebounded: # moves player
                    character.rect.move_ip(-8, 0)
                else:
                    character.rect.move_ip(-4, 0)

        drawBG(screen,camera,groundBG,skyBG,spaceBG)# draw BG

        for plat in platform_group: #draws all the sprites
            if plat.platformType == "night": # tell the night platforms if they are on a day platforms to know whether they should be visible
                plat.update_sprite(screen,camera,onDayPlatform)
            else:
                plat.update_sprite(screen, camera)
        drawText(camera,screen)# draw the hints
        if camera == -11200:# if at the end of the game, draw the Leaderboard
            drawLeaderboard(screen)
        character.draw(screen,squish,camera) # draw player

        platformsCompleted = playback.__len__() #update completed platforms

        # Draws the text for completed platforms
        font = pygame.font.SysFont("Arial", 20)
        text_surface = font.render(
            "Platforms Completed: %d/65" % platformsCompleted, True,
            (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.y =30
        screen.blit(text_surface, text_rect)

        # updates the clock
        if platformsCompleted < 65: # don't update if finished the level
            elapsed_time = pygame.time.get_ticks()
        milliseconds = elapsed_time % 1000
        seconds = (elapsed_time // 1000) % 60
        minutes = (elapsed_time // 60000) % 60
        hours = elapsed_time // 3600000
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
        font = pygame.font.SysFont("Arial", 20) # draws the timer to the screen
        text_surface = font.render(
            "Your Time:  "+str(time_string), True,
            (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.x = 800
        screen.blit(text_surface, text_rect)

        if platformsCompleted >= 65 and not submittedTime: # write the time to file if completed
            submittedTime = True
            writeTime(elapsed_time,time_string)
        jumping -= 1
        pygame.display.flip() # draw the display
        clock.tick(60)#framerate

if __name__ == "__main__":# main entry point
    main()

