# Example.py 
# 

from drawBot import *             # requires drawbot to be first installed as module
import ruleup

newDrawing()                      # required by drawbot module

testc = ruleup.Canvas(
    frame={ 'top' : 50, 'right': 100, 'bottom': 200, 'left': 300 }
)

size(testc.pagewidth, testc.pageheight)

print(testc.frame)

endDrawing()                      # advised by drawbot docs

path = "./test1.pdf"      # set the path as a variable
saveImage(path)                   # make sure to save your image

# not required, but functions as an instant preview
import os
os.system(f"open --background -a Preview {path}")