from stddraw import *
from color import Color

setXscale(-4, 4)
setYscale(-4, 4)

setPenColor(BLACK)
filledSquare(0,0,4)

setPenColor(MAGENTA)
filledCircle(-2,0,2)
setPenColor(CYAN)
filledCircle(1,0,1)
setPenColor(MAGENTA)
filledCircle(2.5,0,0.5)
setPenColor(CYAN)
filledCircle(3.25,0,0.25)

show()