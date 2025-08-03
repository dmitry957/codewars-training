class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self._attributes = []
    
    def setAge(self, age):
        if self.age is None:
            self._attributes.append('age')
        self.age = age
        return self
        
    def setSex(self, sex):
        if self.sex is None:
            self._attributes.append('sex')
        self.sex = sex
        return self
        
    def setName(self, name):
        if self.name is None:
            self._attributes.append('name')
        self.name = name
        return self
        
    def hello(self):
        result = ['Hello.']
        for attr in self._attributes:
            if attr == 'name' and self.name is not None:
                result.append(f'My name is {self.name}.')
            if attr == 'age' and self.age is not None:
                result.append(f'I am {self.age}.')
            if attr == 'sex' and self.sex is not None:
                result.append(f"I am {'male' if self.sex == 'M' else 'female'}.")
        return ' '.join(result)