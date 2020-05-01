import pygame, sys, random
from pygame.locals import *

#variables
FPS=15
WINDOWWIDTH=1000
WINDOWHEIGHT=600

WHITE= (255, 255, 255)
BLACK= (  0,   0,   0)
GREEN= (  0, 255,   0)
YELLOW=(255, 225,   0)
RED=   (255,   0,   0)
CYAN=  (  0, 255, 255)

#this procedure will display the message to press any button
def drawPressAnyKey():
    pressEnterKeySurf=BASICFONT.render("Press Any Key To Continue.", True, GREEN)
    pressEnterKeyRect=pressEnterKeySurf.get_rect()
    pressEnterKeyRect.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT-40))
    DISPLAYSURF.blit(pressEnterKeySurf, pressEnterKeyRect)
# end drawPressAnyKey

# this function will check for any key press
#return : list : the list of key up events
def checkForAnyKeyPress():
    if len(pygame.event.get(QUIT))>0:
        sys.exit()
        pygame.quit()
    #end if len(pygame.event.get(QUIT))
    
    keyUpEvents= pygame.event.get(KEYUP)
    if len(keyUpEvents)==0:
        return None
    #end if len(keyUpEvents)
    
    if keyUpEvents[0].key==K_ESCAPE:
        sys.exit()
        pygame.quit()
    #end if keyUpEvents[0].key
    
    return keyUpEvents[0].key
# end checkForAnyKeyPress

# this procedure will display the score to the screen
#currentScore : int : keeps track of the score
# x, y : int : the x and y coordinates of the the score
def showScore(currentScore, x, y):
    scoreText = BASICFONT.render("Score: "+str(currentScore), True, CYAN)
    scoreRect=scoreText.get_rect()
    scoreRect.center=(x, y)
    DISPLAYSURF.blit(scoreText, scoreRect)
#end showScore

#this procedure will display the real time user input to te screen
#userInput : string : this is what the user is typing
#chosenWord: string : the chosen word at the moment
def realTimeUserInput(userInput):
    userInputSurf = BASICFONT.render(userInput, True, WHITE)
    userInputRect = userInputSurf.get_rect()
    userInputRect.center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2+225))
    DISPLAYSURF.blit(userInputSurf, userInputRect) 
# end realTimeUserInput

# this procedure will draw the instructions
def drawInstructions():
    instructionsSurf1=BASICFONT.render("Type the falling words and press Enter", True, GREEN)
    instructionsRect1=instructionsSurf1.get_rect()
    instructionsRect1.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2+50))
    DISPLAYSURF.blit(instructionsSurf1, instructionsRect1)
    
    instructionsSurf2=BASICFONT.render("after each correct word, the words will fall faster", True, GREEN)
    instructionsRect2=instructionsSurf2.get_rect()
    instructionsRect2.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2+80))
    DISPLAYSURF.blit(instructionsSurf2, instructionsRect2)
    
    instructionsSurf3=BASICFONT.render("if you miss a word, game over!", True, GREEN)
    instructionsRect3=instructionsSurf3.get_rect()
    instructionsRect3.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2+110))
    DISPLAYSURF.blit(instructionsSurf3, instructionsRect3)   
#end drawInstructions()

#this procedure will draw the game over screen
def showGameOverScreen(currentScore):
    DISPLAYSURF.fill(BLACK)
    
    gameOverSurf=FONT.render("Game Over", True, CYAN)
    gameOverRect=gameOverSurf.get_rect()
    gameOverRect.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2))
    DISPLAYSURF.blit(gameOverSurf, gameOverRect)
    
    showScore(currentScore, 500, 360)
    drawPressAnyKey()
    
    pygame.time.wait(500)
    checkForAnyKeyPress()
    while True:
        if checkForAnyKeyPress():
            pygame.event.get() #this clears the event queue
            main()
        pygame.display.update()
        FPSCLOCK.tick(FPS)        
        #end if checlForAnyKeyPress()
    #end while True
#end showGameOverScreen

#this procedure will open the word.txt file and store them in a list
# currentScore           : int : keeps track of the score
#fallingWordsSpeed: int : the speed at which the words are falling
def runFallingWordsGame(currentScore, fallingWordsSpeed, words):
    
    userInput=""
    chosenWord=random.choice(words)
    text_x=random.randint(0, 800)
    text_y=-25
    
    pygame.key.set_repeat(150,50) 
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
            #end if event.type            
            if event.type == KEYDOWN:
                if event.unicode.isalpha(): #checks for uppercase letters when shift is used
                    userInput += event.unicode
                elif event.key == K_BACKSPACE:
                    userInput = userInput[:-1]
                elif event.key == K_RETURN:
                    if userInput==chosenWord:
                        currentScore+=1
 
                        chance=random.randint(1, 3)
                        if chance ==1 or chance ==2:
                            fallingWordsSpeed+=1
                        else:
                            pass
                        #end if chance
                        
                        runFallingWordsGame(currentScore, fallingWordsSpeed, words)
                    #end if userInput
                elif event.key == K_ESCAPE:
                    sys.exit()
                    pygame.quit()                    
                #end if event.unicode.isalpha()            
        #end for event
        
        DISPLAYSURF.fill(BLACK)
        text=BASICFONT.render(chosenWord, True, GREEN)
        DISPLAYSURF.blit(text, (text_x, text_y)) 
        
        if text_y>WINDOWHEIGHT:
            showGameOverScreen(currentScore)
        elif text_y>(2*WINDOWHEIGHT/3):
            DISPLAYSURF.fill(BLACK)
            text=BASICFONT.render(chosenWord, True, RED)
            DISPLAYSURF.blit(text, (text_x, text_y))           
        elif text_y>(WINDOWHEIGHT/3):
            DISPLAYSURF.fill(BLACK)
            text=BASICFONT.render(chosenWord, True, YELLOW)
            DISPLAYSURF.blit(text, (text_x, text_y)) 
        #end if text_y
        
        text_y= text_y+ fallingWordsSpeed
        
        showScore(currentScore, 500, 560)
        realTimeUserInput(userInput)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)  
#end runFallingWordsGame

#this procedure will draw the starting screen
def showStartScreen():
    titleSurf=FONT.render("Typing Maniac", True, CYAN)
    titleRect=titleSurf.get_rect()
    titleRect.center=(int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2-30))
    
    pygame.time.wait(500)
    while True:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(titleSurf, titleRect)   
        
        drawPressAnyKey()
        drawInstructions()
        

        if checkForAnyKeyPress():
            pygame.event.get() #this clears the event queue
            return
        #end if checkForAnyKeyPress()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    #end while True
# end showStartScreen

#this procedure  is the main proceudre that will initiate the game and also set global variables
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, FONT
    
    pygame.init()
    
    currentScore=0
    fallingWordsSpeed=1
    
    FPSCLOCK=pygame.time.Clock()
    BASICFONT= pygame.font.SysFont("Consolas", 25)
    FONT= pygame.font.SysFont("Consolas", 20*4)
    
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    DISPLAYSURF.fill(BLACK)
    pygame.display.set_caption("Typing Maniac")
    
    file = open('words.txt', 'r') # 'r' is for reading mode
    words = file.read().split()
    file.close()

    showStartScreen()
    runFallingWordsGame(currentScore, fallingWordsSpeed, words)
    showGameOverScreen(currentScore)     
#end main

if __name__ == "__main__":
    main()
#end if __name__