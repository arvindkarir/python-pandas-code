nameHandle = open('kids', 'r')
for line in nameHandle:
    print (nameHandle.readlines())
nameHandle.close()

ageHandle = open('ages', 'r')
for line in ageHandle:
    print (ageHandle.readlines())
ageHandle.close()
