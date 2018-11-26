"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Valeria Paiz.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
turtle = rg.SimpleTurtle('turtle')
circle = rg.SimpleTurtle('circle')
turtle.pen = rg.Pen('green',10)
circle.pen = rg.Pen('red',7)
turtle.speed = 10
circle.speed = 10

for k in range (100):
    circle.forward(10 + k)
    circle.left(10)
    circle.go_to(rg.Point(0, 0))

for k in range (80):
    turtle.forward(10 + k)
    turtle.left(10)
    turtle.go_to(rg.Point(0, -110))