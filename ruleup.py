# RuleUp module
# 2022.05.21 Initial version - VG
# Scale is 10 pixels per mm
# requires drawbot to be installed as module

from drawBot import *
import math

layouts = {
    'A4L': { 'page': { 'height' : 2100, 'width': 2970 }, 'frame': { 'top' : 200, 'right': 200, 'bottom': 200, 'left': 200 } },   # A4 portrait, 20mm frame margins
}

class Box:
    def __init__(self, boxx, boxy, boxw, boxh, revspecs):
        self.boxx = boxx
        self.boxy = boxy
        self.boxw = boxw
        self.boxh = boxh
        specs = {
            'top' : 0, 'right': 0, 'bottom': 0, 'left': 0, 'width': 0, 'color': [0,0,0,1], 'fill': [1,1,1,1], 'visible': True }
        specs.update(revspecs)
        for key, value in specs.items():
            self.__setattr__(key, value)

    def draw_box(self):
        with savedState():
            # Draw full box
            strokeWidth(0)
            stroke(0, 0, 0, 1)
            fill(self.fill[0], self.fill[1], self.fill[2], self.fill[3])
            rect(self.boxx, self.boxy, self.boxw, self.boxh)
            # Cut out center
            strokeWidth(self.width)
            stroke(self.color[0], self.color[1], self.color[2], self.color[3]) 
            fill(1, 1, 1, 1)
            rect(self.boxx + self.left, self.boxy + self.bottom, self.boxw - self.left - self.right, self.boxh - self.bottom - self.top)


class Canvas:
    def __init__(self, **kwargs):
        settings = {
            'pageheight': 2970,
            'pagewidth': 2100,
        }
        settings.update(kwargs)
        for key, value in settings.items():
            self.__setattr__(key, value)

    def setup(self):
        size(self.pagewidth, self.pageheight)
        
    def draw_boxes(self):
        if self.frame['visible']:
            frame = Box( revspecs = self.frame, boxx = 0, boxy = 0, boxw = self.pagewidth, boxh = self.pageheight )
            frame.draw_box()
        if self.mat['visible']:
            mat = Box( revspecs = self.mat, boxx = self.frame['left'], boxy = self.frame['bottom'], boxw = self.pagewidth - self.frame['left'] - self.frame['right'], boxh = self.pageheight - self.frame['bottom'] - self.frame['top'] )
            mat.draw_box()


