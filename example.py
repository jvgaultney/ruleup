# Example.py 

from drawBot import *
import ruleup

filename = "./test1.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(
    pageheight = 4200,
    pagewidth = 2970,
    frame = { 'visible': True, 'top' : 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [.3,.2,0,1] },
    mat = { 'visible': True, 'top' : 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 0, 'fill': [0,.3,0,1] },
    design = { 'visible': True, 'top' : 100, 'right': 100, 'bottom': 100, 'left': 100, 'swidth': 1, 'color': [0,0,1,.2] }
)

# Define individual tiles and their contents
tile_main = ruleup.Tile(
    visible = True,
    align = page.dtopl,
    offset = (200, -150),   # x, y in drawbot space
    height = 2000,
    width = 1500,
    # origin = (1200,1000),  # relative to ?
    outline = { 'visible': False, 'swidth': 4, 'color': [1,0,0,1] },
    clip = False,
    sequences = [
        {
            'margintop': 50,
            'lines': [
                dict(spacing=0,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=True),
                dict(spacing=63,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=50,   width=2, color=ruleup.colgreen, type='solid', connectwt=0, changeindent=False),
                dict(spacing=300,  width=2, color=ruleup.colgreen, type='dashed',  connectwt=2, changeindent=False),
                dict(spacing=125,  width=2, color=ruleup.colgreen, type='solid',  connectwt=2, changeindent=False),
                dict(spacing=50,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=50,  width=2, color=ruleup.colblue, type='solid',  connectwt=0, changeindent=True),
                dict(spacing=53,   width=1, color=ruleup.colblue, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=22,   width=2, color=ruleup.colblue, type='solid', connectwt=0, changeindent=False),
                ],
            'indents': [
                (175, 550), (0, 1300),
                ],
            'marginbottom': 100  # space between header and sequences
        },
        {
            'margintop': 50,
            'lines': [
                dict(spacing=0,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=True),
                dict(spacing=63,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=50,   width=2, color=ruleup.colgreen, type='solid', connectwt=0, changeindent=False),
                dict(spacing=300,  width=2, color=ruleup.colgreen, type='dashed',  connectwt=2, changeindent=False),
                dict(spacing=125,  width=2, color=ruleup.colgreen, type='solid',  connectwt=2, changeindent=False),
                dict(spacing=50,   width=1, color=ruleup.colblack, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=50,  width=2, color=ruleup.colblue, type='solid',  connectwt=0, changeindent=True),
                dict(spacing=53,   width=1, color=ruleup.colblue, type='dashed', connectwt=0, changeindent=False),
                dict(spacing=22,   width=2, color=ruleup.colblue, type='solid', connectwt=0, changeindent=False),
                ],
            'indents': [
                (175, 550), (0, 1300),
                ],
            'marginbottom': 100  # space between header and sequences
        }
    ]
)

# Draw page
newDrawing()

page.setup()
page.draw_frames()

tile_main.draw()

print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")