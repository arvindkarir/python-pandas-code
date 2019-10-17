ximport datetime
class Customer(object):
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RunTimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def setBirthday(self, birthdate):
        self.birthday = birthdate
        
    def setSchool(self, schoolname):
        self.schoolname = schoolname

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
      if self.birthday == None:
        raise ValueError
      return(datetime.date.today() - self.birthday).days
      
    def __str__(self):
      return self.name

class StudentCust(Customer):
  nextIdNum = 0 #identification number
  
  def __init__(self, name, balance):
    Customer.__init__(self, name, balance)
    self.idNum = StudentCust.nextIdNum
    StudentCust.nextIdNum += 1
  def getIdNum(self):
    return self.idNum
  def __lt__(self, other):
    return self.idNum < other.idNum
    
class TypeStudent(StudentCust):
  pass

class SchoolStudent(StudentCust):
  def __init__(self, name, balance):
    StudentCust.__init__(self, name, balance)

c1 = Customer('jeff', 1000.00)
c2 = Customer('mary', 1230.00)
c1.withdraw(100.00)
c1.setBirthday(datetime.date(1988, 8, 16))
c3 = Customer('charlie', 2000.00)
listC = [c1, c2]
print(c1.balance)
print(c1.name, c1.balance)
print(c1.birthday)
print(c1.name, 'is', c1.getAge(), 'days old.')
for n in listC:
    print(n.name, n.balance)
listC.append(c3)

p1 = StudentCust('aba', 250.00)
p2 = StudentCust('abur', 120.00)
p3 = StudentCust('jeff',90.00)

listD = [p1, p2, p3]
for n in listD:
    print(n.name, n.balance, n.idNum)

s1 = SchoolStudent('ammi', 300.00)
print(s1.name, s1.idNum, s1.balance)
c1.setSchool('harbored')
print(c1.schoolname)
