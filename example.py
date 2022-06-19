# Example.py 

from quopri import decodestring
from drawBot import *
import ruleup

filename = "./test1.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(format = 'Lit banner')

# Project-specific variables
textheight = 100
textspacing = 40

# Define individual tiles and their contents

tile_trinity = ruleup.ShapesTile(
    visible = True,
    position = dict(valign='middle', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 6250,
    width = 1300,
    outline = dict(visible=True, swidth=4, color=ruleup.colred),
    clip = False,
    shapes = [
        dict(type='circle', diameter=1000, hoffset=-270, voffset=1000, swidth=60, color=ruleup.colgreen, fill=None),
        dict(type='circle', diameter=1000, hoffset=-970, voffset=-386, swidth=60, color=ruleup.colgreen, fill=None),
        dict(type='circle', diameter=1000, hoffset=530, voffset=-386, swidth=60, color=ruleup.colgreen, fill=None),
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_eng = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-300, halign='left', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 16,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=False),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0, 200, 300],
            'lengths':  [600, 100, 150, 500, 700],
            'rindents': [  0, 100, 200,   0, 100],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_lat = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='middle', voffset=35, halign='right', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 16,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=False),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0, 200, 300],
            'lengths':  [600, 100, 150, 500, 700],
            'rindents': [  0, 100, 200,   0, 100],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_grk = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='bottom', voffset=370, halign='left', hoffset=0),  # positive is right and up
    height = 2500,
    width = 600,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 16,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='solid', connectwt=0, changehpos=False),
                dict(spacing=textheight, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [  0,   0,   0, 200, 300],
            'lengths':  [600, 100, 150, 500, 700],
            'rindents': [  0, 100, 200,   0, 100],
            'gap': textspacing,
            'marginbottom': 0  # space between header and sequences
        },
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

print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")