def test():
    
    yield 1
    yield 2
    yield 3
g = test()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
