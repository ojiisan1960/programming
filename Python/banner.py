# Program Name: banner
# Author: Lloyd Hugh Allen
# 4 July 2001

from Tkinter import *
import math

class Flag:
    def __init__(self, font_size=12):
        self.theHeight = 300
        self.theWidth = 1.9 * self.theHeight
        self.make_window( )
    
        self.drawflag( )

    def make_window(self):
        self.root = Tk( )
        self.root.title('Banner')

        self.cv = Canvas(self.root, width = self.theWidth, height = self.theHeight,
                         bg = 'white')
        self.cv.pack( )

    def stripes(self):
        self.theStripes = []
        for count in range(13):
            if count % 2 == 0:
                self.theStripes.append(self.cv.create_rectangle(0, count*self.theHeight/13.0,
                                                     self.theWidth, (count+1)*self.theHeight/13.0,
                                                     fill = 'red', outline = ''))
            else:
                self.theStripes.append(self.cv.create_rectangle(0, count*self.theHeight/13.0,
                                                     self.theWidth, (count+1)*self.theHeight/13.0,
                                                     fill = 'white', outline = ''))
    def star(self, x_loc, y_loc):
        return self.cv.create_polygon(
            x_loc + 0.0308*self.theHeight*math.cos(math.pi*198/180), y_loc + 0.0308*self.theHeight*math.sin(math.pi*198/180),
            x_loc + 0.0308*self.theHeight*math.cos(math.pi*54/180), y_loc + 0.0308*self.theHeight*math.sin(math.pi*54/180),
            x_loc + 0.0308*self.theHeight*math.cos(math.pi*270/180), y_loc + 0.0308*self.theHeight*math.sin(math.pi*270/180),
            x_loc + 0.0308*self.theHeight*math.cos(math.pi*126/180), y_loc + 0.0308*self.theHeight*math.sin(math.pi*126/180),
            x_loc + 0.0308*self.theHeight*math.cos(math.pi*342/180), y_loc + 0.0308*self.theHeight*math.sin(math.pi*342/180),
            fill = "white")
    def stars(self):
        self.theStars = []
        for acrossCount in range (6):
            self.theStars.append([])
            for downCount in range(5):
                self.theStars[acrossCount].append(self.star(self.theHeight*(.063 + .126*acrossCount),
                                                            self.theHeight*(.054 + .108*downCount)))
        self.theOtherStars = []
        for acrossCount in range(5):
            self.theOtherStars.append([])
            for downCount in range(4):
                self.theOtherStars[acrossCount].append(self.star(self.theHeight*(.126 + .126*acrossCount),
                                                                 self.theHeight*(.108 + .108*downCount)))
        pass
    def field(self):
	self.thefield = self.cv.create_rectangle( 0, 0,
                    0.4 * self.theWidth, (7. / 13) * self.theHeight,
                    fill = 'blue', outline = '')
    def drawflag(self):
        self.stripes( )
        self.field( )
        self.stars( )
        pass

if __name__ == '__main__':
	newFlag = Flag( )

