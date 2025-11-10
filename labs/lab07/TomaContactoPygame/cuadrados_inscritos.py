from stddraw import *
from color import Color

setXscale(-4, 4)
setYscale(-4, 4)

setPenColor(RED)
filledSquare(0,0,2.5)
setPenColor(BLACK)
square(0,0,2.5)

setPenColor(YELLOW)
filledSquare(0,0,2)
setPenColor(BLACK)
square(0,0,2)

setPenColor(RED)
filledSquare(0,0,1.5)
setPenColor(BLACK)
square(0,0,1.5)

setPenColor(YELLOW)
filledSquare(0,0,1)
setPenColor(BLACK)
square(0,0,1)

setPenColor(RED)
filledSquare(0,0,0.5)
setPenColor(BLACK)
square(0,0,0.5)

show()