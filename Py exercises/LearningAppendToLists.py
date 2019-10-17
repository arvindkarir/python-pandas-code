#about modifying lists using append
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
#Techs.append('RPI')
#Techs.append('UW')
#Univs.append('UW')
#Univs1.append('RPI')
Techs.append(Ivys)

for e in Univs:
  print 'Univs contains', e
  "which contain"
  for i in e:
    print ' -- ', i

#and some other commands....

L1 = [1,2,3,4]
L2 = [5,4,5,2,6]
L3 = L1 + L2
L3.sort()
print 'L3 =', L3
L1.extend(L2)
print 'L1 =', L1
print L1.pop(4), 'removed from index of 4'
print L3.pop(4), 'removed from index of 4 for L3'
L1.sort()
L1.reverse()
print 'L1 sorted/reversed', L1
print '2 occurs', L1.count(2), 'times'
for e in L1:
  print 'elements=', e
