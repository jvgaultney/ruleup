# RuleUp module
# 2022.05.21 Initial version - VG
# Scale is 10 pixels per mm
# requires drawbot to be installed as module

from drawBot import *
import math

### BUILTINS

colblack = [0,0,0,1]
colred = [1,0,0,1]
colbrown = [.3,.2,0,1]
colgreen = [0,1,0,1]
colgreendark = [0,.3,0,1]
colblue = [0,0,1,1]
colbluetrans = [0,0,1,.2]
colwhite = [1,1,1,1]

formats = {
    'A4 P basic': {
        'canvasheight':  2970,
        'canvaswidth': 2100,
        'frame':  { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': colbrown },
        'mat':    { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': colgreendark },
        'design': { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': colbluetrans },
        'paper': { 'visible': False, 'height': 2100, 'width': 2970, 'offsetx': 0, 'offsety': 0, 'swidth': 1, 'color': colred }
    },    
    'A4 L basic' : {
        'canvasheight':  2100,
        'canvaswidth': 2970,
        'frame':  { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': colbrown },
        'mat':    { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': colgreendark },
        'design': { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': colbluetrans },
        'paper': { 'visible': False, 'height': 2100, 'width': 2970, 'offsetx': 0, 'offsety': 0, 'swidth': 1, 'color': colred }
    },
    'Lit banner' : {
        'canvasheight':  7900,
        'canvaswidth': 2800,
        'frame':  { 'visible': True, 'top': 150, 'right': 150, 'bottom': 150, 'left': 150, 'swidth': 0, 'fill': colbrown },
        'mat':    { 'visible': True, 'top': 170, 'right': 170, 'bottom': 170, 'left': 170, 'swidth': 0, 'fill': colgreendark },
        'design': { 'visible': True, 'top': 480, 'right': 430, 'bottom': 530, 'left': 430, 'swidth': 1, 'color': colbluetrans },
        'paper': { 'visible': True, 'height': 7400, 'width': 2400, 'offsetx': 0, 'offsety': -310, 'swidth': 1, 'color': colred }
    },    
}

### FUNCTIONS

def draw_box(x, y, w, h, s, c): # stroke width, color
    with savedState():
        strokeWidth(s)
        stroke(c[0], c[1], c[2], c[3]) 
        fill(None)
        rect(x, y, w, h)

def draw_line(x, y, w, h, s, c, t):   # start x, start y, length, stroke width, color, type
    with savedState():
        fill(None)
        stroke(c[0], c[1], c[2], c[3]) 
        strokeWidth(s)
        lineCap("round")
        if t == 'dashed':
            lineDash(10, 6)
        else:
            lineDash(None)
        line((x, y), (x + w, y + h))

### CLASSES

class Canvas:
    def __init__(self, **kwargs):
        settings = formats['A4 P basic']     # set the default
        if kwargs['format']:
            settings.update(formats[kwargs['format']])
        settings.update(kwargs)
        for key, value in settings.items():
            self.__setattr__(key, value)

        # CALCULATED VALUES
        self.dleft = self.frame['left'] + self.mat['left'] + self.design['left']
        self.dright = self.canvaswidth - self.frame['right'] - self.mat['right'] - self.design['right']
        self.dtop = self.canvasheight - self.frame['top'] - self.mat['top'] - self.design['top']
        self.dbottom = self.frame['bottom'] + self.mat['bottom'] + self.design['bottom']
        #self.center = self.left + (self.right - self.left) / 2
        #self.middle = self.bottom + (self.top - self.bottom) / 2

        #self.dwidth = self.right - self.left
        #self.dheight = self.top - self.bottom
        #self.dtopl = (self.left, self.top)
        #self.dtopc = (self.center, self.top)
        #self.dtopr = (self.right, self.top)
        #self.dmidl = (self.left, self.middle)
        #self.dmidc = (self.center, self.middle)
        #self.dmidr = (self.right, self.middle)
        #self.dbottoml = (self.left, self.bottom)
        #self.dbottomc = (self.center, self.bottom)
        #self.dbottomr = (self.right, self.bottom)


    def setup(self):
        size(self.canvaswidth, self.canvasheight)
        
    def draw_frames(self):
        framewd = self.canvaswidth - self.frame['left'] - self.frame['right']
        frameht = self.canvasheight - self.frame['bottom'] - self.frame['top']
        matwd = self.canvaswidth - self.frame['left'] - self.frame['right'] - self.mat['left'] - self.mat['right']
        math = self.canvasheight - self.frame['bottom'] - self.frame['top'] - self.mat['bottom'] - self.mat['top']
        if self.frame['visible']:
            frame = Frame( revspecs = self.frame, framex = 0, framey = 0, framew = self.canvaswidth, frameh = self.canvasheight )
            frame.draw()
        if self.mat['visible']:
            mat = Frame( revspecs = self.mat, framex = self.frame['left'], framey = self.frame['bottom'], framew = framewd, frameh = frameht )
            mat.draw()
        if self.design['visible']:
            design = Frame( revspecs = self.design, framex = self.frame['left'] + self.mat['left'], framey = self.frame['bottom'] + self.mat['bottom'], framew = matwd, frameh = math )
            design.draw()
        if self.paper['visible']:  # aligned at top centre before applying offset
            draw_box( (self.canvaswidth - self.paper['width'])/2 + self.paper['offsetx'], self.canvasheight - self.paper['height'] + self.paper['offsety'], self.paper['width'], self.paper['height'], self.paper['swidth'], self.paper['color'] )

class Frame:
    def __init__(self, framex, framey, framew, frameh, revspecs):
        self.framex = framex
        self.framey = framey
        self.framew = framew
        self.frameh = frameh
        specs = { 'top' : 0, 'right': 0, 'bottom': 0, 'left': 0, 'swidth': 0, 'color': [0,0,0,1], 'fill': [1,1,1,1], 'visible': True }
        specs.update(revspecs)
        for key, value in specs.items():
            self.__setattr__(key, value)

    def draw(self):
        with savedState():
            # Draw full box
            strokeWidth(0)
            stroke(0, 0, 0, 1)
            fill(self.fill[0], self.fill[1], self.fill[2], self.fill[3])
            rect(self.framex, self.framey, self.framew, self.frameh)
            # Cut out center
            strokeWidth(self.swidth)
            stroke(self.color[0], self.color[1], self.color[2], self.color[3]) 
            fill(1, 1, 1, 1)
            rect(self.framex + self.left, self.framey + self.bottom, self.framew - self.left - self.right, self.frameh - self.bottom - self.top)

class Tile:
    def __init__(self, **kwargs):
        self.settings = {
            #'valign': 'top',
            #'halign': 'left',
            }
        self.settings.update(kwargs)
        for key, value in self.settings.items():
            self.__setattr__(key, value)
        
        if self.position['valign'] == 'top':
            self.vorigin = self.designbox['top'] + self.position['voffset']
        elif self.position['valign'] == 'middle':
            self.vorigin = self.designbox['bottom'] + (self.designbox['top'] - self.designbox['bottom'])/2 + (self.height/2) + self.position['voffset']
        elif self.position['valign'] == 'bottom':
            self.vorigin = self.designbox['bottom'] + self.height + self.position['voffset']
        else:
            print("Tile alignment is not set correctly")
        self.bottom = self.vorigin - self.height

        if self.position['halign'] == 'left':
            self.horigin = self.designbox['left'] + self.position['hoffset']
            self.left = self.horigin
        elif self.position['halign'] == 'center':
            self.horigin = self.designbox['left'] + (self.designbox['right'] - self.designbox['left'])/2 + self.position['hoffset']
            self.left = self.horigin - self.width/2
        elif self.position['halign'] == 'right':
            self.horigin = self.designbox['right'] + self.position['hoffset']
            self.left = self.horigin - self.width + self.position['hoffset']
        else:
            print("Tile alignment is not set correctly")

        #leftx = self.align[0] + self.offset[0]
        #midx = leftx + (self.width/2)
        #rightx = leftx + self.width
        #topy = self.align[1] + self.offset[1]
        #midy = topy - (self.height/2)
        #bottomy = topy - self.height
        #self.topl = (leftx, topy)
        #self.topc = (midx, topy)
        #self.topr = (rightx, topy)
        #self.midl = (leftx, midy)
        #self.midc = (midx, midy)
        #self.midr = (rightx, midy)
        #self.bottoml = (leftx, bottomy)
        #self.bottomc = (midx, bottomy)
        #self.bottomr = (rightx, bottomy)

    def draw(self):
        if self.visible:
            if self.outline['visible']:
                draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
            hpos = self.horigin
            vpos = self.vorigin
            length = self.width
            indent = 0
            for s in self.sequences:
                indentcount = 0
                lengthcount = 0
                vpos = vpos - s['margintop']
                for c in range(s['count']):
                    for lin in s['lines']:
                        if lin['changeindent']:
                            indent = s['indents'][indentcount]
                            indentcount = indentcount + 1
                            if indentcount == len(s['indents']):
                                indentcount = 0
                        if lin['changelength']:
                            length = s['lengths'][lengthcount]
                            lengthcount = lengthcount + 1
                            if lengthcount == len(s['lengths']):
                                lengthcount = 0
                        vpos = vpos - lin['spacing']
                        if self.position['halign'] == 'center':
                            hpos = self.horigin - self.width/2
                        elif self.position['halign'] == 'right':
                            hpos = self.horigin - self.width
                        draw_line(hpos + indent, vpos, length, 0, lin['width'], lin['color'], lin['type'])
                        if lin["connectwt"] >0:
                            draw_line(hpos + indent, vpos, 0, lin['spacing'], lin['width'], lin['color'], 'solid')
                            draw_line(hpos + indent + length, vpos, 0, lin['spacing'], lin['width'], lin['color'], 'solid')
                    if c < s['count'] - 1:
                        vpos = vpos - s['gap']
                vpos = vpos - s['marginbottom']
    