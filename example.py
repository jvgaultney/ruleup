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

# Define individual tiles and their contents

tile_trinity = ruleup.ShapesTile(
    visible = True,
    position = dict(valign='middle', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 6250,
    width = 1300,
    outline = dict(visible=True, swidth=4, color=ruleup.colred),
    clip = True,
    shapes = [
        dict(type='trinity', diameter=2000, spacing=850, hoffset=-250, voffset=50, swidth=60, color=ruleup.colgreen, fill=None),
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_eng = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-440, halign='left', hoffset=0),  # positive is right and up
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
    position = dict(valign='middle', voffset=-35, halign='right', hoffset=0),  # positive is right and up
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

tile_songs = ruleup.ShapesTile(
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
        dict(type='circle', diameter=1300, hoffset=-700, voffset=-1850, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1500, hoffset=-500, voffset=-2600, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=1400, hoffset=700, voffset=-2450, swidth=60, color=ruleup.colgreentrans, fill=None),
        dict(type='circle', diameter=5000, hoffset=-800, voffset=-400, swidth=60, color=ruleup.colgreentrans, fill=None),
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
tile_songs.draw()

print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")