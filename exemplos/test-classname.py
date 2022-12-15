

class MyClass:
  def __init__(self):
    self.attr1 = 'oi'
    self.attr2 = 22
  
  def __str__(self):
    msg = f'''
    MyClass:
    -- attr1: {self.attr1}
    -- attr2: {self.attr2}
    '''
    return msg


OutraClasse = MyClass

tst = MyClass()
print(tst)
print(OutraClasse.__name__)
print(OutraClasse.__class__)
