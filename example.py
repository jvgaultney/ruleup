# Example.py 

from drawBot import *
import ruleup

filename = "./test1.pdf"

# Define standard page, frame, mat, design
page = ruleup.Canvas(
    pageheight = 4000,
    frame = { 'visible': True, 'top' : 100, 'right': 100, 'bottom': 100, 'left': 100, 'width': 0, 'fill': [.3,.2,0,1] },
    mat = { 'visible': True, 'top' : 150, 'right': 250, 'bottom': 350, 'left': 450, 'width': 0, 'fill': [0,.3,0,1] },
    design = { 'top' : 100, 'right': 100, 'bottom': 100, 'left': 100 }
)

# Draw page
newDrawing()

page.setup()
page.draw_boxes()

print(page.frame)
print(page.frame['top'])

endDrawing()                      # advised by drawbot docs

saveImage(filename)                   # make sure to save your image

# Preview
#import os
#os.system(f"open --background -a Preview {filename}")