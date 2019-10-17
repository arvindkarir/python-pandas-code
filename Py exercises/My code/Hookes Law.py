import pylab
import csv

def getData(filename):
    forces, deformation1,deformation2, deformation3 = [], [], [], [] #initialize lists
    path = 'C:/Users/User/Desktop/MIT EdX programming course/Py exercises/data_dump/'
    dataFile = open( path +"exHooke.csv", "r")
    reader = csv.reader(dataFile) #just read the file
    next(reader, None) #this skips the header
    for line in reader:
        F = line[0]    
        d1 = line[1] # reads column 1
        d2 = line[2] # column 2
        d3 = line[3] # and 3
        forces.append(float(F))
        deformation1.append(float(d1))
        deformation2.append(float(d2))
        deformation3.append(float(d3))
    dataFile.close()
    return forces, deformation1, deformation2, deformation3
    
def plotData(inputFile):
    forces, deformation1, deformation2, deformation3 = getData(inputFile)
    forces = pylab.array(forces)
    deformation1 = pylab.array(deformation1)
    deformation2 = pylab.array(deformation2)
    deformation3 = pylab.array(deformation3)
    NewtonForce = forces*9.81
    pylab.title('Measured displacement of spring')
    pylab.xlabel('|Force| Newtons')
    pylab.ylabel('|Distance| Centimeters')    

# The lines below plot the data and line of best fit    
# ---------------------------------
    pylab.plot(NewtonForce, deformation1, 'bo') #raw data
    a,b = pylab.polyfit(NewtonForce, deformation1, 1) # polyfit line to power 1, straight line
    predictedDistances1 = a*pylab.array(NewtonForce) + b #equation of ax + b for a line
    k = 1.0/a
    pylab.plot(NewtonForce, predictedDistances1,label = 'Displacements predicted by\nlinear fit, k = ' + str(round(k, 5)))
#    pylab.legend(loc = 'best') # label for another line will not work if loc = best as here

# this is for cubic fit, beware of the perils of overfitting
# ---------------------------------
    pylab.plot(NewtonForce, deformation2, 'yo')
    a,b,c,d = pylab.polyfit(NewtonForce, deformation2, 3)
    predictedDistances2 = a*(NewtonForce**3) + b*NewtonForce**2 + c*NewtonForce + d
    pylab.plot(NewtonForce, predictedDistances2, 'b:', label = 'Quadratic fit') 
    pylab.legend() #allows multiple legends to work
# ---------------------------------    
#    pylab.plot(NewtonForce, deformation3, 'go')

    
plotData('exHooke.csv')    
    
#def fitData(inputFile):
    
