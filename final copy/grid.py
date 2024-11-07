# button.py
from graphics import *
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
        self.win = win

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('white')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def isClicked(self, p):
        "Returns true if button active and p is inside"
        #print("clicked", p.getX(), p.getY(), self.xmin, self.xmax)
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def undraw(self):
        """undraws the entire butt-in"""
        self.rect.undraw()
        self.label.undraw()

    def setColor(self,color):
        """sets the rectangle color to be a user input"""
        self.rect.setFill(color)

    def setSize(self,size):
        """sets the font size of the text"""
        self.label.undraw()
        self.label.setSize(size)
        self.label.draw(self.win)

    def returnName(self):
        return self.label

  
class Grid:
    """A grid of squares/buttons"""
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, squareHeight):
        """initializes a 2D list of blank button objects
           startX, startY are the coordinates of the first button location
           squareWidth and squareHeight are the width and height of each button"""
        self.buttonMatrix=[]
        self.gwin=win
        self.columns=numCols
        self.rows=numRows
        self.squareWidth=squareWidth
        self.squareHeight=squareHeight
        self.tempX=startX
        self.tempY=startY
        for i in range(self.columns):
            tempXRow=[]
            for j in range(self.rows):
                butt=Button(self.gwin,Point(self.tempX,self.tempY),self.squareWidth,self.squareHeight,"")
                tempXRow.append(butt)
                self.tempX+=self.squareWidth
            self.tempY+=self.squareHeight
            self.buttonMatrix.append(tempXRow)
            self.tempX=startX


    def getClickPos(self, clickPt):
        """returns the column and row number of the button that was clicked
           assumes the point clickPt is in/on the grid"""
        clickpos=[clickPt.getX()//1,clickPt.getY()//1]
        return clickpos

                    


        
#def main():
    #SIZE = 20
    
    # create the application window
    #win = GraphWin("Fun with 2D lists", 600, 600)
    #win.setCoords(-3, -3, SIZE + 2, SIZE + 2)
    #win.setBackground("green2")

    ##add code here that creates a quitButton
    #quitb=Button(win,Point(20,21),2,1,"quit")
    #grid=Grid(win,0,0,20,20,1,1)
    #pt=win.getMouse()
    #while not quitb.clicked(pt):
        #print(grid.getClickPos(pt))
        #pt=win.getMouse()
    #getClickPos()



    
    ##check 4:  fill in the constructor for the Grid class above and then use it to create a Grid object here
    
 
    #pt = win.getMouse()

    ##check 3: add a while loop here that will keep taking mouse clicks until the quit button is clicked
  
    #win.close()
    
if __name__ == "__main__":
    main()
