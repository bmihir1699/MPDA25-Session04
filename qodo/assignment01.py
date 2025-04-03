<<<<<<< HEAD
         
import Rhino.Geometry as rg
import math         
from typing import List, Tuple, cast                                                        
pointList1 = []     # type: ignore          
pointList2 = []     # type: ignore
lineList = []       # type: ignore                  
allDivPts = []      # type: ignore
pointList3 = []     # type: ignore      

=======
from typing import cast, Any

import Rhino.Geometry as rg #type:ignore
import math
>>>>>>> e124991b982e8e4977e01390ffbe4000cbef2125

# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
x_points = cast(int, x_points)  # type: ignore          
y_points = cast(int, y_points)  # type: ignore

<<<<<<< HEAD
X_points = cast(int, X_points)  # type: ignore
Y_points = cast(int, Y_points)  # type: ignore      

#START CONDING HERE
for i in range(x_points):
    for j in range(y_points):
        point = rg.Point3d(i, j, 0)
        pointList1.append(point)
a = pointList1  


for i in range(x_points):       
    for j in range(y_points):
        point = rg.Point3d(i, j, 1)
        pointList2.append(point)
b = pointList2


for i in range(len(pointList1)):
    line = rg.Line(pointList1[i], pointList2[i])
    lineList.append(line)           
c = lineList    

for i in range(len(lineList)):
    divPts = lineList[i].DivideByCount(3, True)
    allDivPts.append(divPts)
    return allDivPts    
for i in range(len(allDivPts)):     
    for j in range(len(allDivPts[i])):
        point = allDivPts[i][j]
        pointList3.append(point)
        pointList3.append(point)
        pointList3.append(point)
    d = pointList3
    return d

for i in range(len(pointList3)):
    pointList3[i].Z = 0.5           
for i in range(len(pointList3)):
    pointList3[i].X = pointList3[i].X + 0.5 
for i in range(len(pointList3)):
    pointList3[i].Y = pointList3[i].Y + 0.5
for i in range(len(pointList3)):    
    pointList3[i].Z = pointList3[i].Z + 0.5
for i in range(len(pointList3)):
    pointList3[i].X = pointList3[i].X - 0.5
for i in range(len(pointList3)):
    pointList3[i].Y = pointList3[i].Y - 0.5
for i in range(len(pointList3)):
    pointList3[i].Z = pointList3[i].Z - 0.5
for i in range(len(pointList3)):
    pointList3[i].X = pointList3[i].X + 0.5
for i in range(len(pointList3)):
    pointList3[i].Y = pointList3[i].Y + 0.5
for i in range(len(pointList3)):                            
    pointList3[i].Z = pointList3[i].Z + 0.5
for i in range(len(pointList3)):
    pointList3[i].X = pointList3[i].X - 0.5                                                 
=======
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







>>>>>>> e124991b982e8e4977e01390ffbe4000cbef2125

