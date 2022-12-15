

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 10, 'd': 5}

diff = set(d1)-set(d2)
print('diff(d1-d2):', diff)


diff = set(d2)-set(d1)
print('diff(d2-d1)', diff)
