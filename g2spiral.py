#!/usr/bin/python
#
#       Copyright (C) 2015 Shawn Wilson
#       shawn@rj11.ca
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# Set the spiral dimensions, placement, and gap width
DIAMETER = 50
STARTX = 40
STARTY = 80 
DELTAX = 2


# Set the index values for Gcode parameter lists.
G2_X = 'X'
G2_Y = 'Y'
G2_I = 'I'
G2_J = 'J'


def genParams(d, x0, y0, dx):
    """This function generates the G2 g-code parameters (X,Y,I,J).
    Parameters are as follows:
        d = outer spiral diameter
        x0, y0 = starting x,y coordinates
        dx = the gap distance between spiral lines
    """

    paramList = []
    numSpirals = (DIAMETER / (2 * DELTAX))  

    for spiral in range(int(numSpirals)):

        # Calculate out the first half of the spiral arc
        params = {}
        params[G2_X] = x0 + (d - (spiral * dx))
        params[G2_Y] = y0
        params[G2_I] = (d - (2 * spiral * dx)) / 2
        params[G2_J] = 0 
        paramList.append(params)

        # Calculate out the second half of the spiral arc
        params = {}
        params[G2_X] = x0 + ((spiral + 1) * dx)
        params[G2_Y] = y0
        params[G2_I] = -1 * ((d / 2)) + ((spiral + 0.5) * dx)
        params[G2_J] = 0 
        paramList.append(params)

    return paramList

#### MAIN #####

# Generate the Gcode parameters.
gcodes = genParams(DIAMETER, STARTX, STARTY, DELTAX)

#
# Print out the Gcodes.
#

# Go to the start point.
print "G1 X{:.3f} Y{:.3f}".format(STARTX, STARTY) 

# Print out all the arcs.
for params in gcodes:
    
    G2code = "G2 X{X:.3f} Y{Y:.3f} I{I:.3f} J{J:.3f}".format(**params)
    print G2code



