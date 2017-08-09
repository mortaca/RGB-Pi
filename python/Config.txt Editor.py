import pygame, sys, os, math, time, random
from pygame.locals import*

## CONSTANTS, yo ## 

DISPLAYWIDTH  = 400
DISPLAYHEIGHT = 220
FPS          = 50
TEXTHEIGHT   = 13
STARTX       = 0
STARTY       = 0
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

## COLORS ##

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
DARKGREEN= (  0, 125,   0)
BLUE     = ( 66,  66, 231)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
COMBLUE  = (233, 232, 255)
BLUESWEET= (165, 165, 255)
ALPHA    = (  0,   0,   0,   0)

BGCOLOR = BLACK
TEXTCOLOR = WHITE

def main():
    global FPSCLOCK
    global loopCounter
    global loopList
    global directoryString
    pygame.init()
    pygame.joystick.init()
    FPSCLOCK = pygame.time.Clock()
    
    windowWidth  = 400
    windowHeight = 220 
    lineNumber   = 0
    newChar      = ''
    typeChar     = False
    textString   = " "
    mainList     = []
    deleteKey    = False
    returnKey    = False
    insertPoint  = 0
    camerax      = 0
    cameray      = 0
    mouseClicked = False
    mouseX       = 0
    mouseY       = 0
    loopList = ['-','0','1','2','3','4','5','6','7','8','9']
    loopCounter = [0]
    directoryString = ['/boot/config.txt']
    
    pygame.mouse.set_visible(0)
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)    
    displaySurf.fill(BGCOLOR)
    displaySurf.convert()
    pygame.display.update()
    
    pygame.display.set_caption('Notepad')
    mainFont = pygame.font.SysFont('Helvetica', TEXTHEIGHT)
    
    cursorRect = getCursorRect(STARTX, STARTY + (TEXTHEIGHT + (TEXTHEIGHT/4)), mainFont, camerax, cameray)
    
    mainList = LoadFile(mainList, windowWidth, windowHeight, displaySurf, mainFont)

    # 1ST JOYSTICK INIT
    joystick_one = pygame.joystick.Joystick(0)
    joystick_one.init()

## The main game loop detects user input, displays the text on the screen,
## displays the cursor on the screen, and adjusts the camera view if
## necessary.
    
    while True:
        
        camerax, cameray = adjustCamera(mainList, lineNumber, insertPoint, cursorRect, mainFont, camerax, cameray, windowWidth, windowHeight)

        newChar, typeChar, deleteKey, returnKey, directionKey, windowWidth, windowHeight, mouseX, mouseY, mouseClicked= getInput(windowWidth, windowHeight)
	

        if newChar == "escape":

	    os.system('mount -o remount,rw /boot')

            mainList = SaveFile(mainList, windowWidth, windowHeight, displaySurf, mainFont)

            newChar = False
            insertPoint = 0
            lineNumber = 0

	    os.system('mount -o remount,ro /boot')

	    pygame.quit()
            sys.exit()
		        
        mainList, lineNumber, insertPoint, cursorRect = displayText(mainFont, newChar, typeChar, mainList, deleteKey, returnKey, lineNumber, insertPoint, directionKey, camerax, cameray, cursorRect, windowWidth, windowHeight, displaySurf, mouseClicked, mouseX, mouseY)


        pygame.display.update()
        FPSCLOCK.tick(FPS)


## Interprets user input and changes mainList, lineNumber, insertPoint
## and cursorRect accordingly.  There is a function called blitAll()
## which blits all strings to the main surface.

def displayText(mainFont, newChar, typeChar, mainList, deleteKey, returnKey, lineNumber, insertPoint, directionKey, camerax, cameray, cursorRect, windowWidth, windowHeight, displaySurf, mouseClicked, mouseX, mouseY):
    if returnKey:
        firstString = getStringAtInsertPoint(mainList, lineNumber, insertPoint)
        secondString = getStringAfterInsertPoint(mainList, lineNumber, insertPoint)
        mainList[lineNumber] = firstString
        mainList.insert(lineNumber+1, secondString)
        lineNumber +=1
        returnKey = False
        insertPoint = 0
        cursorRect.x = STARTX
        stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
        cursorRect.y = stringRect.top
        
    elif mouseClicked:
        insertPoint, lineNumber, cursorRect = setCursorToClick(mainList, cursorRect, mainFont, camerax, cameray, mouseX, mouseY)

    elif directionKey:
        if directionKey == LEFT:
            if lineNumber == 0:
                if insertPoint > 0:
                    insertPoint -= 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = STARTY
                    
            elif lineNumber > 0:
                if insertPoint == 0:
                    lineNumber -= 1
                    insertPoint = len(mainList[lineNumber])
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                    
                elif insertPoint > 0:
                    insertPoint -= 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)

                    if insertPoint == 0:
                        cursorRect.x = STARTX
                        cursorRect.y = stringRect.top
                    else:
                        cursorRect.x = stringRect.right
                        cursorRect.y = stringRect.top
                    
        elif directionKey == RIGHT:
            if insertPoint < len(mainList[lineNumber]):
                insertPoint += 1
                stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                cursorRect.x = stringRect.right
                cursorRect.y = stringRect.top

            elif insertPoint >= len(mainList[lineNumber]):
                if len(mainList) > (lineNumber + 1):
                    lineNumber += 1
                    insertPoint = 0
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                    
        elif directionKey == UP:
            if lineNumber > 0:
                if insertPoint == 0:
                    lineNumber -= 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = STARTX
                    cursorRect.y = stringRect.top
                    
                elif insertPoint > len(mainList[lineNumber - 1]):
                    lineNumber -= 1
                    insertPoint = len(mainList[lineNumber])
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                      
                elif insertPoint <= len(mainList[lineNumber -1]):
                    lineNumber -= 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                    
        elif directionKey == DOWN:
            if lineNumber + 1 < len(mainList):
                if insertPoint == 0:
		    lineNumber += 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = STARTX
                    cursorRect.y = stringRect.top
                    
                elif insertPoint > len(mainList[lineNumber + 1]):
                    lineNumber +=1
                    insertPoint = len(mainList[lineNumber])
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                elif insertPoint <= len(mainList[lineNumber +1]):
                    lineNumber += 1
                    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
                    cursorRect.x = stringRect.right
                    cursorRect.y = stringRect.top
                    
    elif typeChar:
        string = mainList[lineNumber]
        stringList = list(string)
        stringList.insert(insertPoint, newChar)
        newString = ''.join(stringList)
        mainList[lineNumber] = newString
        
        typeChar = False

        if len(newString) > len(string) and newChar != '    ':   ## Prevents alteration keys like shifts from affecting the insertPoint ##
            insertPoint += 1
            stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
            cursorRect.x = stringRect.right
            cursorRect.y = stringRect.top
            
        elif newChar == '    ':
            insertPoint += 4
            stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
            cursorRect.x = stringRect.right
            cursorRect.y = stringRect.top

    elif deleteKey:
        
        if insertPoint > 0:
            firstString = getStringAtInsertPoint(mainList, lineNumber, insertPoint)
            secondString = getStringAfterInsertPoint(mainList, lineNumber, insertPoint)
            stringList = list(firstString)
            del stringList[insertPoint-1]
            string = ''.join(stringList)
            string += secondString
            mainList[lineNumber] = string

            deleteKey = False
            insertPoint -= 1
            stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
            cursorRect.x = stringRect.right
            cursorRect.y = stringRect.top
                                
        elif insertPoint <= 0:
            if lineNumber > 0:
                string = getStringAfterInsertPoint(mainList, lineNumber, insertPoint)
                del mainList[lineNumber]
                lineNumber -= 1
                mainList[lineNumber] += string
                
                deleteKey = False
                insertPoint = len(mainList[lineNumber]) - len(string)
                stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)                
                cursorRect.x = stringRect.right
                cursorRect.y = stringRect.top

    else:
        stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)

        if insertPoint == 0:
            cursorRect.x = STARTX
        elif insertPoint > 0:
            cursorRect.x = stringRect.right
        if lineNumber == 0:
            cursorRect.y = STARTY
        elif lineNumber > 0:
            cursorRect.y = stringRect.top
        else:
            cursorRect.x = stringRect.right

    if cursorRect.left >= STARTX:
        if cursorRect.right <= windowWidth:
            if cursorRect.top >= STARTY:
                if cursorRect.bottom <= (windowHeight - STARTY):
                    blitAll(mainList, mainFont, camerax, cameray, cursorRect, displaySurf)
    
    return mainList, lineNumber, insertPoint, cursorRect

##################################################################
## Blits all the strings in mainList to the main surface object 
##################################################################
##################################################################


def blitAll(mainList, mainFont, camerax, cameray, cursorRect, displaySurf):
    displaySurf.fill(BGCOLOR)
    i = 0
    
    for string in mainList:  ##blitting all the strings in the mainList by iterating through them
        stringRender = mainFont.render(string, True, TEXTCOLOR, BGCOLOR)
        stringRect = stringRender.get_rect()
        stringRect.x = STARTX - camerax
        stringRect.y = STARTY + (i * (TEXTHEIGHT + (TEXTHEIGHT/4))) - cameray
        displaySurf.blit(stringRender, stringRect)
        i += 1

    drawCursor(mainFont, cursorRect, displaySurf)


def adjustCamera(mainList, lineNumber, insertPoint, cursorRect, mainFont, camerax, cameray, windowWidth, windowHeight):

    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)
    
    if (stringRect.right + cursorRect.width) > windowWidth:
        camerax += (stringRect.right + cursorRect.width) - windowWidth  
    elif cursorRect.left < STARTX:
        camerax -= (-1)*(cursorRect.left)

    if stringRect.bottom > windowHeight:
        cameray += stringRect.bottom - windowHeight
    elif stringRect.top < 0:
        cameray -= (-1)*(stringRect.top)
               
    if insertPoint == 0:
        camerax = 0
    if lineNumber == 0:
        cameray = 0

    return camerax, cameray
    

def drawCursor(mainFont, cursorRect, displaySurf):
    cursor = mainFont.render("<<<", True, BLACK, WHITE)
    displaySurf.blit(cursor, cursorRect)
    



def getInput(windowWidth, windowHeight):
    newChar = False
    typeChar = False
    deleteKey = False
    returnKey = False
    directionKey = False
    mouseX = 0
    mouseY = 0
    mouseClicked = False
        
    for event in pygame.event.get():
	
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == JOYBUTTONDOWN:
		if event.button == 0:
			deleteKey = True
		elif event.button == 1:
			deleteKey = True
		elif event.button == 2:
			deleteKey = True
		elif event.button == 3:
			newChar = ' '
			typeChar = True
		elif event.button == 8:
			newChar = 'escape'
			

        elif event.type == JOYBUTTONUP:
		if event.button == 1:
			if loopCounter[0] < 10:
				loopCounter[0]+=1
			else:
				loopCounter[0]=0
			newChar = loopList[loopCounter[0]]
                	typeChar = True
		elif event.button == 2:
			if loopCounter[0] == 0:
				loopCounter[0]=10
			else:
				loopCounter[0]-=1
			newChar = loopList[loopCounter[0]]
                	typeChar = True
		


	elif event.type == JOYAXISMOTION:
		if event.axis == 1 and event.value > 0:
			directionKey = DOWN
		elif event.axis == 1 and event.value < 0:
			directionKey = UP
		elif event.axis == 0 and event.value > 0:
			directionKey = RIGHT
		elif event.axis == 0 and event.value < 0:
			directionKey = LEFT

            
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                deleteKey = True
            elif event.key == K_ESCAPE:
                newChar = 'escape'
            elif event.key == K_RETURN:
                returnKey = True
            elif event.key == K_TAB:
                newChar = '    '
                typeChar = True
            elif event.key == K_LEFT:
                directionKey = LEFT
            elif event.key == K_RIGHT:
                directionKey = RIGHT
            elif event.key == K_UP:
                directionKey = UP
            elif event.key == K_DOWN:
		directionKey = DOWN

	    else:
                newChar = event.unicode
                typeChar = True
			

        elif event.type == VIDEORESIZE:
            displaySurf = pygame.display.set_mode(event.dict['size'], RESIZABLE)
            windowWidth = event.dict['w']
            windowHeight = event.dict['h']
            displaySurf.fill(BLUE)
            displaySurf.convert()
            pygame.display.update()
            
           
            
        elif event.type == MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            #mouseClicked = True
	    directionKey = DOWN

    return newChar, typeChar, deleteKey, returnKey, directionKey, windowWidth, windowHeight, mouseX, mouseY, mouseClicked


## These functions involve the string the cursor happens to be on.
## By using the lineNumber, the program knows which string to
## manipulate.  lineNumber = 0 is the first line, and so on.
## The cursor's left position is always locked to the right of whatever
## stringRect it is next to.

def getStringRect(string, lineNumber, camerax, cameray):
    stringRect = string.get_rect()
    stringRect.x = STARTX - camerax
    stringRect.y = STARTY + (lineNumber * (TEXTHEIGHT + (TEXTHEIGHT/4))) - cameray

    return stringRect

def getStringAtInsertPoint(mainList, lineNumber, insertPoint):
    string = mainList[lineNumber]
    stringList = list(string)
    newStringList = stringList[0:insertPoint]
    newString = ''.join(newStringList)

    return newString

def getStringAfterInsertPoint(mainList, lineNumber, insertPoint):
    string = mainList[lineNumber]
    stringList = list(string)
    newStringList = stringList[insertPoint:]
    newString = ''.join(newStringList)

    return newString


def getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray):
    string = getStringAtInsertPoint(mainList, lineNumber, insertPoint)
    stringRender = mainFont.render(string, True, TEXTCOLOR, BGCOLOR)
    stringRect = getStringRect(stringRender, lineNumber, camerax, cameray)

    return stringRect


## Miscelaneous Functions.  getCursorRect is used to produce the
## cursors's rect object.


def getCursorRect(cursorX, cursorY, mainFont, camerax, cameray):
    cursor = mainFont.render('L', True, RED)
    cursorRect = cursor.get_rect()
    cursorRect.x = cursorX - camerax
    cursorRect.y = cursorY - cameray

    return cursorRect


## These three functions, setCursorToClick(), getLineNumberOfClick(), and
## get insertPointAtMouseX() allow the user to set the cursor location
## by clicking the mouse at the spot they want to go.


def setCursorToClick(mainList, cursorRect, mainFont, camerax, cameray, mouseX, mouseY):
    lineNumber = getLineNumberOfClick(mouseY, cameray, mainList)
    insertPoint = getInsertPointAtMouseX(mouseX, mouseY, lineNumber, mainList, mainFont, camerax, cameray)
    stringRect = getStringRectAtInsertPoint(mainList, lineNumber, insertPoint, mainFont, camerax, cameray)

    if insertPoint == 0:
        cursorRect.x = STARTX
    elif insertPoint > 0:
        cursorRect.x = stringRect.right
        
    cursorRect.y = stringRect.top

    return insertPoint, lineNumber, cursorRect


def getLineNumberOfClick(mouseY, cameray, mainList):
    clickLineNumber = (mouseY + cameray) / float(TEXTHEIGHT+ (TEXTHEIGHT/4))
    if clickLineNumber > len(mainList):
        lineNumber = (len(mainList)) - 1
    elif clickLineNumber <= len(mainList):
        floorLineNumber = math.floor(clickLineNumber)
        lineNumber = int(floorLineNumber)

    return lineNumber


def getInsertPointAtMouseX(mouseX, mouseY, lineNumber, mainList, mainFont, camerax, cameray):
    string = mainList[lineNumber]
    newInsertPoint = 0

    if (mouseY + cameray) > ((lineNumber + 1) * (TEXTHEIGHT + TEXTHEIGHT/4)):
        insertPoint = len(mainList[lineNumber])
        return insertPoint
    
    for insertPoint in string:
        stringRect = getStringRectAtInsertPoint(mainList, lineNumber, newInsertPoint, mainFont, camerax, cameray)
        if mouseX >= stringRect.left:
            if mouseX < stringRect.right:
                if newInsertPoint > 0:
                    return newInsertPoint - 1

        newInsertPoint += 1

    else:
        return newInsertPoint


def LoadFile(mainList, windowWidth, windowHeight, displaySurf, mainFont):
    

    loadDirectory = False

    loadDirectory, directoryString[0] = directoryInput(displaySurf, directoryString[0], mainFont, loadDirectory)
                
    newMainList = loadFromDisk(loadDirectory)
    return newMainList

    return mainList


def SaveFile(mainList, windowWidth, windowHeight, displaySurf, mainFont):
    

    saveDirectory = False
            
    saveDirectory, directoryString[0] = directoryInput(displaySurf, directoryString[0], mainFont, saveDirectory)
                
    saveToDisk(mainList, saveDirectory)

    
    return mainList
    
    

def directoryInput(displaySurf, directoryString, mainFont, saveOrLoadDirectory):
    directoryList = ''.join(directoryString)

    saveOrLoadDirectory = directoryString

    return saveOrLoadDirectory, directoryString


def saveToDisk(mainList, saveDirectory):
    saveFile = open(saveDirectory, 'w')

    for string in mainList:
        saveFile.write(string + '\n')

    saveFile.close()


def loadFromDisk(loadDirectory):
    mainList = []
    saveFile = open(loadDirectory, 'r')

    for line in saveFile:
        mainList.append(line)

    saveFile.close()

    i = 0
    while i < len(mainList):
        stringList = list(mainList[i])
        stringList.pop()
        mainList[i] = ''.join(stringList)
        i += 1

    return mainList



    
def getStringRenderAndRect(string, mainFont):
    stringRender = mainFont.render(string, True, TEXTCOLOR, BLUE)
    stringRect = stringRender.get_rect()

    return stringRender, stringRect


if __name__ == '__main__':
    main()


