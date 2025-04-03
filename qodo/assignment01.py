from typing import cast, Any

import Rhino.Geometry as rg #type:ignore
import math

# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
x_points = cast(int, x_points)  # type: ignore
y_points = cast(int, y_points)  # type: ignore

#START CONDING HERE 

pointList1 = []

#using Rhino Geometry, start by initializing an empty list and fill it with points 
#by creating points with a for loop. The number of points should come
# from a slider called x_points

for i in range(x_points):
    pointList1.append(rg.Point3d(i, 0, 0))

a= pointList1

pointList2 = []

# make another list where all points are displaced in the y direction
# by y_points amount

for i in range(x_points):
    pointList2.append(rg.Point3d(i, y_points, 0))

b= pointList2

# connect points of both lists with a line and store them in a list
lineList = []
for i in range(x_points):
    lineList.append(rg.LineCurve(pointList1[i], pointList2[i]))
    
c= lineList


# divide those lines into n amount of points and store them in a list of list
# called allDivPts








