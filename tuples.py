t1 = (1, 4, 2, 3)
print(sorted(t1))
print(sorted(t1, reverse=True))
t2 = ('hello', 'world')
t3 = [s.upper() for s in t2]
print(t3)
t3 = tuple(s.lower() for s in t2)
print(t3)
