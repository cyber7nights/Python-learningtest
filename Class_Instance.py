class student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
panda=student("panda",99)
print(panda.name,":",panda.score)
#student is a class, panda is a instance.__init__ method
