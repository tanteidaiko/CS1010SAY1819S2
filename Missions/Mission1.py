#
# CS1010S --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(pic1, pic2, pic3, pic4):
    return stack_frac(1/2,
                      beside(pic4, pic1),
                      beside(pic3, pic2))


# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
#show(mosaic(heart_bb , pentagram_bb , circle_bb , ribbon_bb ))

##########
# Task 2 #
##########

def simple_fractal(pic):
    return beside(pic,
                  stack(pic, pic))

# Test
#show(simple_fractal(make_cross(rcross_bb)))
#show(simple_fractal(heart_bb )) 

