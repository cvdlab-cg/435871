from pyplasm import *

#Homework 1 - exercise1
#Author: Davide Violante

#function for custom colors with 0:255 numbers
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]

#custom colors
OCRA0 = rgb([140, 90, 0.0])
OCRA1 = rgb([160, 110, 0.0])
OCRA2 = rgb([180, 130, 0.0])
OCRA3 = rgb([200, 150, 0.0])
OCRA3A = rgb([220, 170, 0.0])
OCRA4 = rgb([240, 190, 0.0])

#def heights of the floors
H1 = 1
H2 = 2
H3 = 3
H3col = 3.001 #prevent glittering
H3int = 3.002 #prevent glittering
H4 = 13

#floor0: sand
pts0 = [[0,0],[0,50],[50,50],[50,0]]
floor0 = COLOR(OCRA0)(JOIN(AA(MK)(pts0)))

#floor1: 1st stair
pts1 = [[0,0],[0,20],[40,20],[40,0]]
floor1 = COLOR(OCRA1)(JOIN(AA(MK)(pts1)))
floor1 = T([1,2,3])([5,15,H1])(floor1)

#floor2: 2nd stair
pts2 = [[0,0],[0,19],[39,19],[39,0]]
floor2 = COLOR(OCRA2)(JOIN(AA(MK)(pts2)))
floor2 = T([1,2,3])([5.5,15.5,H2])(floor2)

#floor3: interior and columns
pts3 = [[0,0],[0,18],[38,18],[38,0]]
floor3base = COLOR(OCRA3)(JOIN(AA(MK)(pts3)))
floor3base = T([1,2,3])([6,16,H3])(floor3base)

#column
column = COLOR(OCRA3A)(JOIN(CIRCUMFERENCE(0.8)(10)))
column = T([1,2,3])([7,17,H3col])(column)

#cloning and positioning columns
columns_x = STRUCT([column, T(1)(3.28)]*12)
columns_y = STRUCT([column, T(2)(3.2)]*6)
columns_xcopy = STRUCT([columns_x, T(2)(16)]*2)
columns_ycopy = STRUCT([columns_y, T(1)(36.08)]*2)
column2fronta = T([1,2])([5.5,6])(column)
column2frontb = T([1,2])([5.5,9.5])(column)
columns_front = STRUCT([column2fronta, column2frontb])
columns_rear = STRUCT([columns_front, T(1)(22)]*2)

columnsTOT = STRUCT([columns_x, columns_y, columns_xcopy, columns_ycopy, columns_front, columns_rear])

interior1 = CUBOID([23,0.5])
interior1 = T([1,2,3])([12,20,H3int])(interior1)
interior2 = CUBOID([2,3])
interior2 = T([1,2,3])([15,20.5,H3int])(interior2)
interior3 = CUBOID([0.5,9])
interior3 = T([1,2,3])([31,20.5,H3int])(interior3)

interior1b = T([2])([9])(interior1)
interior2b = T([2])([5.5])(interior2)

interiorTOT = COLOR(OCRA3A)(STRUCT([interior1, interior2, interior3, interior1b, interior2b]))

floor3 = STRUCT([floor3base,columnsTOT,interiorTOT])

#floor4: top of the columns (roof)
floor4a = T([1,2])([2,2])((CUBOID([34,14])))
floor4b = CUBOID([38,18])
floor4 = DIFFERENCE([floor4b,floor4a])
floor4 = T([1,2,3])([6,16,H4])(floor4)

floor4int = T([3])([H4-H3])(interiorTOT)
floor4coltop = CUBOID([2,8.5])
floor4coltopfront = T([1,2,3])([12,20.5,H4])(floor4coltop)
floor4coltoprear = T([1,2,3])([33,20.5,H4])(floor4coltop)
floor4 = COLOR(OCRA4)((STRUCT([floor4,floor4int,floor4coltopfront,floor4coltoprear])))

two_and_half_model = STRUCT([floor0,floor1,floor2,floor3,floor4])

#final view
VIEW(two_and_half_model)
VIEW(SKELETON(1)(two_and_half_model))


exit()