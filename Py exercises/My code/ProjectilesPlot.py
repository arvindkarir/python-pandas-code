'''By comparing the estimation errors (the numerator) with the variability of the original values (the denominator), R2 is intended to capture the proportion of variability in a data set that is accounted for by the statistical model provided by the fit. When the model being evaluated is produced by a linear regression, the value of R2 always lies between 0 and 1. If R2 = 1, the model explains all of the variability in the data. If R2 = 0, there is no relationship between the values predicted by the model and the actual data. def rSquared below'''

import pylab
import csv

def rSquared(measured, predicted):
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/float(len(measured))
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability

def getFlightData(filename):
    distances, heights1,heights2, heights3, heights4 = [], [], [], [], [] #initialize lists
    path = 'C:/Users/User/Desktop/MIT EdX programming course/Py exercises/data_dump/'
    dataFile = open( path + filename, "r")
    reader = csv.reader(dataFile) #just read the file
    next(reader, None) #this skips the header
    for line in reader:
        d = line[0]    
        h1 = line[1] # reads column 1
        h2 = line[2] # column 2
        h3 = line[3] # and 3
        h4 = line[4] # and 4
        
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
        
    dataFile.close()
    return (distances, [heights1, heights2, heights3, heights4])
   
def plotPath(inputFile):
    distances, heights = getFlightData(inputFile)
    numTrials = len(heights)
    distances = pylab.array(distances)
    
    totHeights = pylab.array([0]*len(distances)) #do not understand this line, are we defining an array of [0]null times len(distances)? Possible
    for h in heights: #loop thru heights
        totHeights = totHeights + pylab.array(h) #for each row
    meanHeights = totHeights/numTrials #average of each of the four trial rows for a particular distance
    
    pylab.title('Trajectory of Projectile (Mean of ' + str(numTrials) + ' Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    pylab.plot(distances, meanHeights, 'bo')
    pylab.legend()
  
    a,b = pylab.polyfit(distances, meanHeights, 1) # for LINE of best fit
    altitudes = a*distances + b
    pylab.plot(distances, altitudes, 'b', label = 'Linear Fit')
# ----------------------------
# Either run the line below for linear fit to calculate the Rsquared of linear
# print('RSquare of linear fit =', rSquared(meanHeights, altitudes))
# -----------------------------
    a,b,c = pylab.polyfit(distances, meanHeights, 2) # for CURVE of best fit
    altitudes = a*(distances**2) + b*distances + c
    pylab.plot(distances, altitudes, 'b:', label = 'Quadratic Fit')
# Or the line below for quadratic fit - which is better in this case as it explains 98% of variations of values by this model 
    print('RSquare of quadratic fit =', rSquared(meanHeights, altitudes))
    
plotPath('Projectiles.csv')    
    

    
