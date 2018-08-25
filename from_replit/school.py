class School(object):
  def __init__(self,money,equipment):
    self.money = money
    self.students =[]
    self.equipment = equipment
  
  def enroll(self,stud_obj):
    self.students.append(stud_obj)
    
    
  def close_for_summer(self):
    print('Students go home!')
    self.students =[]
    print('Reducing budget')
    self.money /= 2
    print ('Current balance: ' +str (self.money) + ' USD')
    print('Repairing equipment')
    self.repair()
    
    
  def repair(self):
    self.money -= 100
    self.equipment = 1
    print ('Equipment is repaired. Current balance: ' +str (self.money) + ' USD')
    
  def open_for_studies(self):
    print('Students came back!')
    print('Breaking equipment!')
    self.equipment = self.equipment*0.5
    # print('Getting more money.')
    # self.money = 2000
    
  def count_money(self):
    for i in self.students:
      self.money += i.tuition
      print(self.money)
    print 'total: ',self.money,"USD"
    
    

s = School(money=2000,equipment=1)    
s.close_for_summer()
s.open_for_studies()


class Student (object):
  def __init__(self,tuition):
   self.tuition = tuition
  
class Nonfunded(Student):
  pass
  
class Funded(Student):
  pass
full_tuition = 1000
part_tuition = 500
n = Nonfunded(full_tuition)
f = Funded(part_tuition)
print (n.tuition,f.tuition,s.students)
s.enroll(n)
s.enroll(f)
print(s.students)
for i in range(100):
  s.enroll(n)

for i in range(50):
  s.enroll(f)


print(s.students) 

s.count_money()  
