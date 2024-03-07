def twice(f):
     def result(x):
        return f(f(x))
     return result

plus_three = lambda i: i + 3

g = twice(plus_three)
g(7)
