from stddraw import *
from color import Color

setXscale(-5, 5)
setYscale(-5, 5)
setPenColor(ORANGE)

filledRectangle(-5,-5,10,2)
setPenColor(GREEN)
filledCircle(0,1,2.1)
setPenColor(YELLOW)
filledCircle(3,4,0.5)
setPenColor(BLACK)
filledRectangle(-0.5,-3,1,2)
circle(0,1,2.1)
circle(3,4,0.5)
show()