# RuleUp module
# 2022.05.21 Initial version - VG
# Scale is 10 pixels per mm
# Print PDFs at 28.3% for accurate sizing
# requires drawbot to be installed as module

from drawBot import *
from datetime import datetime
import math

### BUILTINS

colblack = [0,0,0,1]
colgray = [0,0,0,.5]
colgrayverylight = [0,0,0,.1]
colgraylight = [0,0,0,.2]
colgraydark = [0,0,0,.8]
colred = [1,0,0,1]
colreddark = [.3,0,0,1]
colbrown = [.3,.2,0,1]
colbrownlight = [.6,.5,0,1]
colgreen = [0,1,0,1]
colgreendark = [0,.3,0,1]
colgreentrans = [0,1,0,.2]
colblue = [0,0,1,1]
colbluelight = [0,0,1,.5]
colbluetrans = [0,0,1,.2]
colwhite = [1,1,1,1]

formats = {
    'A4 P basic': {
        'canvasheight':  2970,
        'canvaswidth': 2100,
        'frame':  { 'visible': False, 'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'swidth': 0, 'fill': colbrown },
        'mat':    { 'visible': False, 'top': 0, 'right': 0, 'bottom': 0, 'left': 0, 'swidth': 0, 'fill': colgreendark },
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
    'Esther' : {
        'canvasheight': 4300,
        'canvaswidth': 2500,
        'frame':  { 'visible': True, 'top': 200, 'right': 200, 'bottom': 200, 'left': 200, 'swidth': 0, 'fill': colbrown },
        'mat':    { 'visible': True, 'top': 250, 'right': 250, 'bottom': 250, 'left': 250, 'swidth': 0, 'fill': colgreendark },
        'design': { 'visible': True, 'top': 370, 'right': 350, 'bottom': 370, 'left': 350, 'swidth': 1, 'color': colbluetrans },
        'paper': { 'visible': True, 'height': 3900, 'width': 2100, 'offsetx': 0, 'offsety': -200, 'swidth': 1, 'color': colred }
    },    
    'Wall' : {  # dimensions shrunk 1:10 for ease
        'canvasheight': 1200,  # include wrap around each 2 cm pole plus radius = 2 x 65 + 2 x 10
        'canvaswidth': 1800,
        'frame':  { 'visible': False, 'top': 55, 'right': 0, 'bottom': 55, 'left': 0, 'swidth': 0, 'fill': colreddark },
        'mat':    { 'visible': False, 'top': 20, 'right': 0, 'bottom': 20, 'left': 0, 'swidth': 0, 'fill': colbrownlight },
        'design': { 'visible': True, 'top': 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': colbluetrans },
        'paper': { 'visible': True, 'height': 1050, 'width': 1800, 'offsetx': 0, 'offsety': -75, 'swidth': 1, 'color': colred }
    },    
}

### FUNCTIONS

def getarcinfo(xs, ys, xe, ye, r, ismajor):
    # assumes clockwise order
    # based on algorithm from
    # https://math.stackexchange.com/questions/1781438/finding-the-center-of-a-circle-given-two-points-and-a-radius-algebraically
    xhalf = (xs - xe) / 2
    yhalf = (ys - ye) / 2
    lenhalf = sqrt(xhalf ** 2 + yhalf ** 2)
    if r < lenhalf:
        raise ValueError("Arc error - radius must be greater than " + str(int(lenhalf)))
    else:
        lenperp = sqrt(r ** 2 - lenhalf ** 2)
        if ismajor:
            xc = (xe + xhalf) + (lenperp * yhalf) / lenhalf
            yc = (ye + yhalf) - (lenperp * xhalf) / lenhalf
        else:
            xc = (xe + xhalf) - (lenperp * yhalf) / lenhalf
            yc = (ye + yhalf) + (lenperp * xhalf) / lenhalf
        centerpoint = xc, yc
        angs = degrees(atan2(yc - ys, xc - xs)) + 180
        ange = degrees(atan2(yc - ye, xc - xe)) + 180
        return centerpoint, angs, ange

def draw_box(x, y, w, h, s, c): # stroke width, color
    with savedState():
        strokeWidth(s)
        stroke(c[0], c[1], c[2], c[3]) 
        fill(None)
        rect(x, y, w, h)

def draw_oval(cpx, cpy, vdia, hdia, s, c, f, dot, dotc, dotdia): # center point, vertical diameter, horiz diameter, stroke width, color, fill
    with savedState():
        strokeWidth(s)
        stroke(c[0], c[1], c[2], c[3])
        if f == None:
            fill(None)
        else:
            fill(f[0], f[1], f[2], f[3]) 
        oval(cpx - hdia/2, cpy - vdia/2, hdia, vdia)
        if dot:
            strokeWidth(0)
            stroke(1,1,1,1)
            fill(dotc[0], dotc[1], dotc[2], dotc[3])
            oval(cpx - dotdia/2, cpy - dotdia/2, dotdia, dotdia)

def draw_arc(xs, ys, xe, ye, rad, ismajor, s, c, f, h, dot, dotc, dotdia): # start x, start y, end x, end y, radius, is major, stroke width, color, fill, hollow
    with savedState():
        strokeWidth(s)
        stroke(c[0], c[1], c[2], c[3])
        if f == None:
            fill(None)
        else:
            fill(f[0], f[1], f[2], f[3])
        arcpath = BezierPath()
        try:
            centerpt, angs, ange = getarcinfo(xs, ys, xe, ye, rad, ismajor)
        except ValueError as e:
            print(str(e))
        else:
            if h:
                strokeWidth(2)
                arcpath.arc(centerpt, rad + s/2, angs, ange, True)
                drawPath(arcpath)
                arcpathaddl = BezierPath()                
                arcpathaddl.arc(centerpt, rad - s/2, angs, ange, True)
                drawPath(arcpathaddl)
            else:
                arcpath.arc(centerpt, rad, angs, ange, True)
                drawPath(arcpath)
        if dot:
            strokeWidth(0)
            stroke(1,1,1,1)
            fill(dotc[0], dotc[1], dotc[2], dotc[3])
            oval(centerpt[0] - dotdia/2, centerpt[1] - dotdia/2, dotdia, dotdia)


def draw_line(x, y, w, h, s, c, t):   # start x, start y, width, height, color, type
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

def draw_text(x, y, w, h, c, fn, fs, lh, t, a): #
    with savedState():
        font(fn)
        fontSize(fs)
        lineHeight(lh)
        strokeWidth(0)
        if c == None:
            fill(0)
        else:
            fill(c[0], c[1], c[2], c[3]) 
        textBox(t, (x, y, w, h), align=a)

def draw_image(x, y, p, a): #
    with savedState():
        image(p, (x, y), alpha=a)

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

        self.dwidth = self.dright - self.dleft
        self.dheight = self.dtop - self.dbottom

        now = datetime.now()
        self.datetime = now.strftime("%-d %b %Y, %H:%M:%S")

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
            #'sequences': [],
            #'shapes': [],
            }
        self.settings.update(kwargs)
        for key, value in self.settings.items():
            self.__setattr__(key, value)
        
        if self.position['valign'] == 'top':
            self.vorigin = self.designbox['top'] + self.position['voffset']
            self.top = self.vorigin
            self.bottom = self.vorigin - self.height
        elif self.position['valign'] == 'middle':
            self.vorigin = self.designbox['bottom'] + (self.designbox['top'] - self.designbox['bottom'])/2 + self.position['voffset']
            self.top = self.vorigin + (self.height/2)
            self.bottom = self.vorigin - (self.height/2)
        elif self.position['valign'] == 'bottom':
            self.vorigin = self.designbox['bottom'] + self.position['voffset']
            self.top = self.vorigin + self.height
            self.bottom = self.vorigin
        else:
            print("Tile alignment is not set correctly")

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

        # save design boundaries for use as clipping path but do not draw
        self.clippath = BezierPath()
        self.clippath.moveTo((self.left, self.bottom))
        self.clippath.lineTo((self.left + self.width, self.bottom))
        self.clippath.lineTo((self.left + self.width, self.bottom + self.height))
        self.clippath.lineTo((self.left, self.bottom + self.height))
        self.clippath.closePath()
        #drawPath(sqpath)
    
class SequencesTile(Tile):
    def draw(self):
        if self.visible:
            with savedState():
                if self.outline['visible']:
                    draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
                if self.clip:
                    clipPath(self.clippath)
                hpos = self.horigin
                vpos = self.top
                lindent = 0
                length = self.width
                rindent = 0
                for sq in self.sequences:
                    poscount = 0
                    vpos = vpos - sq['margintop']
                    for c in range(sq['count']):
                        for lin in sq['lines']:
                            vpos = vpos - lin['spacing']
                            if lin['changehpos']:
                                lindent = sq['lindents'][poscount]
                                rindent = sq['rindents'][poscount]
                                length = sq['lengths'][poscount]
                                poscount = poscount + 1
                                if poscount == len(sq['lindents']):
                                    poscount = 0
                            if self.position['halign'] == 'left':
                                hpos = self.horigin + lindent
                            elif self.position['halign'] == 'center':
                                hpos = self.horigin - (length/2) + lindent - rindent
                            elif self.position['halign'] == 'right':
                                hpos = self.horigin - length - rindent
                            draw_line(hpos, vpos, length, 0, lin['swidth'], lin['color'], lin['type'])
                            if lin["connectwt"] >0:
                                draw_line(hpos, vpos, 0, lin['spacing'], lin["connectwt"], lin['color'], 'solid')
                                draw_line(hpos + length, vpos, 0, lin['spacing'], lin["connectwt"], lin['color'], 'solid')
                        if c < sq['count'] - 1:
                            vpos = vpos - sq['gap']
                    vpos = vpos - sq['marginbottom']

class ShapesTile(Tile):
    def draw(self):
        if self.visible:
            with savedState():
                if self.outline['visible']:
                    draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
                if self.clip:
                    clipPath(self.clippath)
                hpos = self.horigin
                vpos = self.vorigin
                for sh in self.shapes:
                    if sh['type'] == 'circle':
                        draw_oval(hpos + sh['hoffset'], vpos + sh['voffset'], sh['diameter'], sh['diameter'], sh['swidth'], sh['color'], sh['fill'], sh['showdot'], sh['dotfill'], sh['dotdia'])
                    if sh['type'] == 'trinity':
                        draw_oval(hpos + sh['hoffset'], vpos + sh['voffset'] + sh['spacing'], sh['diameter'], sh['diameter'], sh['swidth'], sh['colora'], sh['fill'], sh['showdot'], sh['dotfill'], sh['dotdia'])
                        draw_oval(hpos + sh['hoffset'] + (sh['spacing'] * 0.866), vpos + sh['voffset'] - (sh['spacing'] * 0.5), sh['diameter'], sh['diameter'], sh['swidth'], sh['colorb'], sh['fill'], sh['showdot'], sh['dotfill'], sh['dotdia'])
                        draw_oval(hpos + sh['hoffset'] - (sh['spacing'] * 0.866), vpos + sh['voffset'] - (sh['spacing'] * 0.5), sh['diameter'], sh['diameter'], sh['swidth'], sh['colorc'], sh['fill'], sh['showdot'], sh['dotfill'], sh['dotdia'])
                    if sh['type'] == 'arc':
                        draw_arc(hpos + sh['startx'], vpos + sh['starty'], hpos + sh['endx'], vpos + sh['endy'], sh['radius'], sh['ismajor'], sh['swidth'], sh['color'], sh['fill'], sh['hollow'], sh['showdot'], sh['dotfill'], sh['dotdia'])

class TextTile(Tile):
    def draw(self):
        if self.visible:
            with savedState():
                if self.outline['visible']:
                    draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
                #if self.clip:
                #    clipPath(self.clippath)
                hpos = self.horigin
                vpos = self.vorigin - self.height
                txp = self.textprop
                for txt in self.texts:
                    draw_text(hpos, vpos, self.width, self.height, txp['color'], txp['fontname'], txp['fontsize'], txp['lineheight'], txt, txp['align'])
                    vpos = vpos - txp['lineheight']

class ImageTile(Tile):
    def draw(self):
        if self.visible:
            with savedState():
                if self.outline['visible']:
                    draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
                if self.clip:
                    clipPath(self.clippath)
                hpos = self.horigin
                vpos = self.vorigin
                for img in self.images:
                    draw_image(hpos + img['hoffset'], vpos + img['voffset'], img['path'], img['alpha'])

class GridTile(Tile):  # angle specified clockwise from vertical, can be negative to tilt to left
    def draw(self):
        if self.visible:
            with savedState():
                if self.outline['visible']:
                    draw_box(self.left, self.bottom, self.width, self.height, self.outline['swidth'], self.outline['color'])
                if self.clip:
                    clipPath(self.clippath)
                hpos = self.left
                vpos = self.bottom
                hposdiff = self.horigin - self.left
                vposdiff = self.vorigin - self.bottom
                print(hpos, vpos)
                #length = math.sqrt( self.width * self.width + self.height * self.height )
                #print(length)
                for hl in self.hlines:
                    hlcount = int(self.height / hl['spacing']) + 1
                    for c in range(hlcount):
                        draw_line(hpos, vpos + hl['offset'] + (c * hl['spacing']), self.width, 0, hl['swidth'], hl['color'], hl['type'],)
                for vl in self.vlines:
                    hang = self.height * math.tan(math.radians(vl['angle']))
                    hposhangadj = vl['spacing'] * int(abs(hang) / vl['spacing'])
                    #print(hang)
                    hposhalignadj = hposdiff - (vl['spacing'] * int(hposdiff / vl['spacing']))
                    hposvalignadj = hang * (vposdiff / self.height)
                    hstart = hpos - hposhangadj + hposhalignadj - hposvalignadj + vl['offset']
                    vlcount = int((self.width + abs(hang) * 2) / vl['spacing']) + 2
                    for c in range(vlcount):
                        draw_line(hstart + (c * vl['spacing']), vpos, hang, self.height, vl['swidth'], vl['color'], vl['type'],)

