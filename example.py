# Example.py 

from quopri import decodestring
from drawBot import *
import ruleup

filename = "./test1.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(format = 'Lit banner')

# Project-specific variables
textheight = 100
textspacing = 50

# Define individual tiles and their contents

tile_eng = ruleup.Tile(
    visible = True,
    position = dict(valign='top', voffset=-100, halign='left', hoffset=0),  # positive is right and up
    height = 2500,
    width = 700,
    outline = dict(visible=True, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 16,
            'lines': [
                dict(spacing=0, width=1, color=ruleup.colblack, type='solid', connectwt=0, changeindent=True, changelength=True),
                dict(spacing=textheight, width=1, color=ruleup.colblack, type='solid', connectwt=1, changeindent=False, changelength=False),
                ],
            'indents': [0, 0, 0, 200, 300],
            'lengths': [600, 100, 150, 500, 700],
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

tile_eng.draw()

print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")