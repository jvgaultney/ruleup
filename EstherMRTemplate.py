# Example.py 

from quopri import decodestring
from drawBot import *
import ruleup
import datetime

filename = "EstherMR01.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(format = 'Esther')
page.frame['visible'] = False
page.mat['visible'] = False

# Project-specific variables
captionsize = 18
# Define individual tiles and their contents

tile_header = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 30,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                dict(spacing=30, swidth=1, color=ruleup.colblack, type='dashed', connectwt=1, changehpos=False),
                ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_header = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=0, halign='center', hoffset=0),  # positive is right and up
    height = 30,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                dict(spacing=30, swidth=1, color=ruleup.colblack, type='dashed', connectwt=1, changehpos=False),
                ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_top = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-130, halign='center', hoffset=0),  # positive is right and up
    height = 900,
    width = 900,
    outline = dict(visible=True, swidth=1, color=ruleup.colblack),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_text = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-1130, halign='left', hoffset=0),  # positive is right and up
    height = 360,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 45,
            'count': 4,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=True),
                dict(spacing=45, swidth=1, color=ruleup.colblack, type='solid', connectwt=1, changehpos=False),
                ],
            'lindents': [ 130, 220,   0, 160 ],
            'lengths':  [ 540, 540, 540, 740 ],
            'rindents': [   0,   0,   0,   0 ],
            'gap': 45,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_reference = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-1385, halign='right', hoffset=0),  # positive is right and up
    height = 15,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=True),
                dict(spacing=15, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                ],
            'lindents': [   0 ],
            'lengths':  [ 280 ],
            'rindents': [  30 ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_bottom = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-1630, halign='center', hoffset=0),  # positive is right and up
    height = 900,
    width = 900,
    outline = dict(visible=True, swidth=1, color=ruleup.colblack),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_footer = ruleup.SequencesTile(
    visible = True,
    position = dict(valign='top', voffset=-2630, halign='left', hoffset=0),  # positive is right and up
    height = 30,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    clip = False,
    sequences = [
        {
            'margintop': 0,
            'count': 1,
            'lines': [
                dict(spacing=0, swidth=1, color=ruleup.colblack, type='dashed', connectwt=0, changehpos=False),
                dict(spacing=30, swidth=1, color=ruleup.colblack, type='dashed', connectwt=1, changehpos=False),
                ],
            'gap': 0,
            'marginbottom': 0  # space between header and sequences
        },
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)

tile_info = ruleup.TextTile(
    visible = True,
    position = dict(valign='top', voffset=100, halign='left', hoffset=0),  # positive is right and up
    height = 100,
    width = 900,
    outline = dict(visible=False, swidth=4, color=ruleup.colred),
    #clip = False,
    textprop = dict(fontname='Andika', fontsize=captionsize, lineheight=(captionsize*1.15), color=ruleup.colblack, align='left'),
    texts = [
        filename + ' produced by RuleUp ' + page.datetime + ' • Print at 28.3% for accurate sizing',
        'Design W ' + str(page.dwidth) + ' H ' + str(page.dheight) + ' • Paper W ' + str(page.paper['width']) + ' H ' + str(page.paper['height'])
    ],
    designbox = { 'left': page.dleft, 'right': page.dright, 'top': page.dtop, 'bottom': page.dbottom }  # required do not modify
)


# Draw page
newDrawing()

page.setup()
page.draw_frames()

tile_header.draw()
tile_top.draw()
tile_text.draw()
tile_reference.draw()
tile_bottom.draw()
tile_footer.draw()
tile_info.draw()

#print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")