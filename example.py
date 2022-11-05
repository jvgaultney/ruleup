# Example.py 

from quopri import decodestring
from drawBot import *
import ruleup

filename = "./test1.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(format = 'Lit banner')
page.frame['visible'] = False
page.mat['visible'] = False

# Project-specific variables
textheight = 100
textspacing = 40
arccolor=[0,.8,0,1]

# Define individual tiles and their contents

tile_trinity = ruleup.ShapesTile(
    visible = True,
    position = dict(valign='middle', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 6250,
    width = 1300,
    outline = dict(visible=True, swidth=4, color=ruleup.colred),
    clip = True,
    shapes = [
        dict(type='trinity', diameter=2000, spacing=860, hoffset=-240, voffset=-180, swidth=80,
            colora=[0,.9,0,1], colorb=[.5,1,0,1], colorc=[0,.7,.3,1], fill=None,
            showdot=True, dotfill=ruleup.colred, dotdia=20),
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_eng = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-450, halign='left', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 17,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=True),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'lengths':  [210, 210, 210, 400, 430, 480, 500, 440, 500, 600, 580, 550, 480, 530, 500, 500, 520],
            'rindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_lat = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='middle', voffset=-200, halign='right', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 17,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=True),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'lengths':  [360, 360, 360, 410, 220, 360, 500, 410, 540, 520, 500, 480, 410, 420, 300, 450, 370],
            'rindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_grk = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='bottom', voffset=60, halign='left', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 17,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=True),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'lengths':  [280, 280, 280, 330, 400, 380, 480, 520, 500, 540, 590, 600, 570, 500, 330, 620, 700],
            'rindents': [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_old_songs = ruleup.ShapesTile(
    visible = True,
    position = dict(valign='middle', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 6250,
    width = 1300,
    outline = dict(visible=True, swidth=4, color=ruleup.colred),
    clip = True,
    shapes = [
        dict(type='circle', diameter=7000, hoffset=800, voffset=-400, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1600, hoffset=-550, voffset=2000, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=2000, hoffset=800, voffset=1900, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=4000, hoffset=-1100, voffset=1200, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=7000, hoffset=-1000, voffset=-1200, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1200, hoffset=600, voffset=1000, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1500, hoffset=-750, voffset=300, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1200, hoffset=-850, voffset=-250, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1400, hoffset=-450, voffset=-900, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1500, hoffset=600, voffset=-800, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1100, hoffset=700, voffset=-1700, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1300, hoffset=-700, voffset=-1850, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1500, hoffset=-500, voffset=-2600, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1400, hoffset=700, voffset=-2450, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=5000, hoffset=-800, voffset=-400, swidth=60, color=ruleup.colgreentrans, fill=None),
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_songs = ruleup.ShapesTile(
    visible = True,
    position = dict(valign='bottom', voffset=0, halign='left', hoffset=0),  # positive is right and up
    height = 6250,
    width = 1300,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    shapes = [
        dict(type='arc', startx=0, starty=6235, endx=1300, endy=5200, radius=1800, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=270, starty=5900, endx=1300, endy=6235, radius=2500, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=0, starty=5950, endx=580, endy=4600, radius=870, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=270, starty=5430, endx=1300, endy=5950, radius=1800, ismajor=False, swidth=30, color=arccolor, fill=None),
        #dict(type='arc', startx=450, starty=5340, endx=1300, endy=5140, radius=2000, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=1300, starty=5700, endx=480, endy=5000, radius=2000, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=1300, starty=4800, endx=620, endy=4340, radius=1200, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=880, starty=3960, endx=1300, endy=5050, radius=700, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=880, starty=3390, endx=1300, endy=4400, radius=580, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=770, starty=3280, endx=320, endy=3400, radius=2200, ismajor=False, swidth=30, color=arccolor, fill=None),
        #dict(type='arc', startx=0, starty=3250, endx=500, endy=1800, radius=2000, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=0, starty=3000, endx=850, endy=3140, radius=2500, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=0, starty=2700, endx=850, endy=2430, radius=1800, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=840, starty=2270, endx=360, endy=2130, radius=1900, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=580, starty=1270, endx=1300, endy=1700, radius=1400, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=640, starty=1000, endx=1285, endy=0, radius=1300, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=1300, starty=950, endx=800, endy=1950, radius=650, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=1300, starty=750, endx=400, endy=540, radius=1800, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=1300, starty=420, endx=0, endy=15, radius=2200, ismajor=False, swidth=30, color=arccolor, fill=None),
        dict(type='arc', startx=980, starty=0, endx=1300, endy=1400, radius=960, ismajor=False, swidth=30, color=arccolor, fill=None),
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

# Draw page
newDrawing()

page.setup()
page.draw_frames()

tile_trinity.draw()
tile_eng.draw()
tile_lat.draw()
tile_grk.draw()
#tile_old_songs.draw()
tile_songs.draw()

print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")