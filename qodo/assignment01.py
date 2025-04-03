         
import Rhino.Geometry as rg
import math         
from typing import List, Tuple, cast                                                        
pointList1 = []     # type: ignore          
pointList2 = []     # type: ignore
lineList = []       # type: ignore                  
allDivPts = []      # type: ignore
pointList3 = []     # type: ignore      


# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
x_points = cast(int, x_points)  # type: ignore          
y_points = cast(int, y_points)  # type: ignore

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

