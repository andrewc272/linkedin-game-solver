'''
this is a script to capture the linked in puzzle solve it and then enter in the values
'''

sudoku_puzzle = {
        "og_puzzle" : None
        "cell_locations" : {
            (0,0) : (790, 166, 64, 64) # (left, top, width, height)
            (0,1) : (856, 165, 64, 64) # (left, top, width, height)
            (0,2) : (921, 165, 64, 64) # (left, top, width, height)
            (0,3) : (985, 166, 64, 64) # (left, top, width, height)
            (0,4) : (1050, 166, 64, 64) # (left, top, width, height)
            (0,5) : (1115, 166, 64, 64) # (left, top, width, height)
            
            (1,0) : (790, 230, 64, 64) 
            (1,1) : (856, 230, 64, 64) 
            (1,2) : (921, 230, 64, 64) 
            (1,3) : (985, 230, 64, 64) 
            (1,4) : (1050, 230, 64, 64) 
            (1,5) : (1115, 230, 64, 64) 
            
            (2,0) : (790, 295, 64, 64) 
            (2,1) : (856, 295, 64, 64) 
            (2,2) : (921, 295, 64, 64) 
            (2,3) : (985, 295, 64, 64) 
            (2,4) : (1050, 295, 64, 64) 
            (2,5) : (1115, 295, 64, 64)
            
            (3,0) : (790, 360, 64, 64)
            (3,1) : (856, 360, 64, 64)
            (3,2) : (921, 360, 64, 64)
            (3,3) : (985, 360, 64, 64)
            (3,4) : (1050, 360, 64, 64)
            (3,5) : (1115, 360, 64, 64)

            (4,0) : (790, 425, 64, 64)
            (4,1) : (856, 425, 64, 64)
            (4,2) : (921, 425, 64, 64)
            (4,3) : (985, 425, 64, 64)
            (4,4) : (1050, 425, 64, 64)
            (4,5) : (1115, 425, 64, 64)
            
            (5,0) : (790, 490, 64, 64)
            (5,1) : (856, 490, 64, 64)
            (5,2) : (921, 490, 64, 64)
            (5,3) : (985, 490, 64, 64)
            (5,4) : (1050, 490, 64, 64)
            (5,5) : (1115, 490, 64, 64)
            }
        }

# pause
import time
time.sleep(5)

# take a screenshot
from mss import mss
import mss.tools

filename = "test.png"

with mss.mss() as sct:
    monitor = {"top": 140, "left": 770, "width": 430, "height": 630}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    sct_img = sct.grab(monitor)
    mss.tools.to_png(sct_img.rgb,sct_img.size, output=output)
    print(output)


# get the original puzzle from the screen
for row in range(6):
    for column in range(6):
    with mss.mss() as sct:
        monitor = {"top": 140, "left": 770, "width": 430, "height": 630}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb,sct_img.size, output=output)
        print(output)
        
