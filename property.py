class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score>100 or score<0:
            raise ValueError('score must be 0-100!')
        self._score=score
panda=Student()
panda.set_score(99)
print(panda.get_score())

