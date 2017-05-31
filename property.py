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

class Student(object):
    @property
    def score (self):
        return self.scores
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise TypeError('score must be a int')
        if score>100 or score<0:
            raise ValueError('score must 1~100')
        self.scores=score
panda=Student()
panda.score=98  #注意变化
print(panda.score)

#作业
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('wrong Typle')
        if value<0:
            raise ValueError('width must be >0')
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('wrong Typle')
        if value<0:
            raise ValueError('width must be >0')
        self._height=value
    @property
    def resolution(self):
        return self._height*self._width

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution