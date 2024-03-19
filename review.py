temp1 = 98.6
#temp1 = 98.6
class Person:

    def __init__(self, name, marks, studentNo):
        self.name = name
        self.marks = marks
        self.studentNo = studentNo
    def student(self):
        print(f"My name is {self.name}, i have {self.marks} marks and my student number is {self.studentNo} ")

person1 = Person('Simanga', 80, 1234 )
person1.student()

s = "Hello, "
t = "Simanga"
k = 3
print(s + t)
print()
print(k * s)
val = input("enter your character: ")
if val in s:
    print(f"Yes, val {val} is in the word")
else:
    print(f"The val {val} is not in the word")


multi = (5 + 2) * 3
print(multi)
# divsion
#n = float(input("enter you nmber: "))
#m = float(input("Enter your m number: "))
#div_me = n / m 
#print(f"ouch print integer {div_me}")