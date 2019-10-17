class IntSet(object):
  def __init__(self):
    self.vals = []
  
  def insert(self, e):
    if not e in self.vals:
      self.vals.append(e)
      
  def member(self, e):
    return e in self.vals
    
  def remove(self, e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(str(e) + 'not found')
      
  def getMembers(self):
    return self.vals[:]
    
  def __str__(self):
    self.vals.sort()
    result = ''
    for e in self.vals:
      result = result + str(e) + ','
    return'{' + result[:-1] + '}'
    


s = IntSet()
s.insert(3)
s.insert(4)
s.insert(5)
print s.member(7)
s.insert(7)
print s.member(7)
s.insert(4)
print s.__str__()
IntSet.insert(s, 44)
print s
s.insert(55)
print s
