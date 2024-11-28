class student:
    def __init__(self,name,branch,rollno,sem):
        self.name=name
        self.branch=branch
        self.rollno=rollno
        self.sem=sem
    def display(self):
        print ('name:',self.name)
        print ('branch:',self.branch)
        print ('rollno:',self.rollno)
        print ('sem:',self.sem)

student1 = student("hari", "mechanical", "160123736050", 3)
student2 = student("hari", "mechanical", "160123736043", 3)
student1.display()
print()
student2.display()
