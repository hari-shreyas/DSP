class cricketer:
    def __init__(self,name,runs):
        self.name=name
        self.runs=runs
    def display(self):
        print ('cricketer info:')
        print ('name:',self.name)
        print ('runs:',self.runs)
c1=cricketer('virat kholi','100000')
c2=cricketer('ms dhoni','3829240')

c1.display()
print()
c2.display()