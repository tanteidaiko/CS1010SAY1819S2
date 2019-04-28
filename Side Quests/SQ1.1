#
# CS1010S --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(rune, count):
    def nxn(n, rune):
        return stackn(n, quarter_turn_right(stackn(n, quarter_turn_left(rune))))

    def centre_hollow(n):
        return nxn(n-2, blank_bb)

    def side_edge(n):
        return stackn(n-2, rune)

    def top_edge(n):
        return quarter_turn_left(stackn(n, quarter_turn_right(rune)))

    def middle_row_part1(n):
        return quarter_turn_left(stack_frac((n-2)/(n-1), centre_hollow(n), quarter_turn_right(side_edge(n))))

    def full_middle_row(n):
        return quarter_turn_left(stack_frac(1/n, quarter_turn_right(side_edge(n)), quarter_turn_right(middle_row_part1(n))))

    def part_pic(n):
        return stack_frac(1/(n-1), top_edge(n), full_middle_row(n))

    def main_pic(n):
        return stack_frac((n-1)/n, part_pic(n), top_edge(n))

    def hollow_add_in(n):
        return scale((n*(n-2))/n**2, rune)
    n = count
    if n <= 1:
        return rune
    else:
        return overlay_frac(0, hollow_add_in(n), main_pic(n))

# Test
#show(egyptian(make_cross(rcross_bb), 5))
#show(egyptian(make_cross(rcross_bb),9))
#show(egyptian(nova_bb, 9))
#show(egyptian(heart_bb, 15))
