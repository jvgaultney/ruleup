# RuleUp module
# 2022.05.21 Initial version - VG
# Scale is 10 pixels per mm
# requires drawbot to be installed as module

from drawBot import *
import math

### BUILTINS

layouts = {
    'A4L': { 'page': { 'height' : 2100, 'width': 2970 }, 'frame': { 'top' : 200, 'right': 200, 'bottom': 200, 'left': 200 } },   # A4 portrait, 20mm frame margins
}

colblack = [0,0,0,1]
colgreen = [0,1,0,1]
colblue = [0,0,1,1]
colred = [1,0,0,1]

formats = {
    'A4 P basic': {
        'pageheight':  2970,
        'pagewidth': 2100,
        'frame':  { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [.3,.2,0,1] },
        'mat':    { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [0,.3,0,1] },
        'design': { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': [0,0,1,.2] }
    },    
    'A4 L basic' : {
        'pageheight':  2100,
        'pagewidth': 2970,
        'frame':  { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [.3,.2,0,1] },
        'mat':    { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [0,.3,0,1] },
        'design': { 'visible': False, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': [0,0,1,.2] }
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
        dleftx = self.frame['left'] + self.mat['left'] + self.design['left']
        drightx = self.pagewidth - self.frame['right'] - self.mat['right'] - self.design['right']
        dtopy = self.pageheight - self.frame['top'] - self.mat['top'] - self.design['top']
        dbottomy = self.frame['bottom'] + self.mat['bottom'] + self.design['bottom']
        dmidx = dleftx + (drightx - dleftx) / 2
        dmidy = dbottomy + (dtopy - dbottomy) / 2
        self.dwidth = drightx - dleftx
        self.dheight = dtopy - dbottomy
        self.dtopl = (dleftx, dtopy)
        self.dtopc = (dmidx, dtopy)
        self.dtopr = (drightx, dtopy)
        self.dmidl = (dleftx, dmidy)
        self.dmidc = (dmidx, dmidy)
        self.dmidr = (drightx, dmidy)
        self.dbottoml = (dleftx, dbottomy)
        self.dbottomc = (dmidx, dbottomy)
        self.dbottomr = (drightx, dbottomy)

    def setup(self):
        size(self.pagewidth, self.pageheight)
        
    def draw_frames(self):
        framewd = self.pagewidth - self.frame['left'] - self.frame['right']
        frameht = self.pageheight - self.frame['bottom'] - self.frame['top']
        matwd = self.pagewidth - self.frame['left'] - self.frame['right'] - self.mat['left'] - self.mat['right']
        math = self.pageheight - self.frame['bottom'] - self.frame['top'] - self.mat['bottom'] - self.mat['top']
        if self.frame['visible']:
            frame = Frame( revspecs = self.frame, framex = 0, framey = 0, framew = self.pagewidth, frameh = self.pageheight )
            frame.draw()
        if self.mat['visible']:
            mat = Frame( revspecs = self.mat, framex = self.frame['left'], framey = self.frame['bottom'], framew = framewd, frameh = frameht )
            mat.draw()
        if self.design['visible']:
            design = Frame( revspecs = self.design, framex = self.frame['left'] + self.mat['left'], framey = self.frame['bottom'] + self.mat['bottom'], framew = matwd, frameh = math )
            design.draw()

class Frame:
    def __init__(self, framex, framey, framew, frameh, revspecs):
        self.framex = framex
        self.framey = framey
        self.framew = framew
        self.frameh = frameh
        specs = {
            'top' : 0, 'right': 0, 'bottom': 0, 'left': 0, 'swidth': 0, 'color': [0,0,0,1], 'fill': [1,1,1,1], 'visible': True }
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
        settings = {
            #'height': 2970,
            #'width': 2100,
        }
        settings.update(kwargs)
        for key, value in settings.items():
            self.__setattr__(key, value)
        leftx = self.align[0] + self.offset[0]
        midx = leftx + (self.width/2)
        rightx = leftx + self.width
        topy = self.align[1] + self.offset[1]
        midy = topy - (self.height/2)
        bottomy = topy - self.height
        self.topl = (leftx, topy)
        self.topc = (midx, topy)
        self.topr = (rightx, topy)
        self.midl = (leftx, midy)
        self.midc = (midx, midy)
        self.midr = (rightx, midy)
        self.bottoml = (leftx, bottomy)
        self.bottomc = (midx, bottomy)
        self.bottomr = (rightx, bottomy) 

    def draw(self):
        if self.visible:
            if self.outline['visible']:
                draw_box(self.bottoml[0], self.bottoml[1], self.width, self.height, self.outline['swidth'], self.outline['color'])
            hpos = self.topl[0]
            vpos = self.topl[1]
            length = self.width
            indent = 0
            for s in self.sequences:
                indentcount = 0
                vpos = vpos - s['margintop']
                for lin in s['lines']:
                    if lin["changeindent"]:
                        indent = s['indents'][indentcount][0]
                        length = s['indents'][indentcount][1]
                        if indent + length > self.width:
                            print("Line", indentcount, "extends beyond design width:", indent + length)
                        indentcount = indentcount + 1
                    vpos = vpos - lin['spacing']
                    draw_line(hpos + indent, vpos, length, 0, lin['width'], lin['color'], lin['type'])
                    if lin["connectwt"] >0:
                        draw_line(hpos + indent, vpos, 0, lin['spacing'], lin['width'], lin['color'], 'solid')
                        draw_line(hpos + indent + length, vpos, 0, lin['spacing'], lin['width'], lin['color'], 'solid')
                vpos = vpos - s['marginbottom']
    


