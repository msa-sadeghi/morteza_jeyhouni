def greet(name=""):
    return f"Hello {name}"


print(greet())
print(greet("sara"))

def mul(*args):
    res = 1
    for number in args:
        res *= number
        
    return res

print(mul(2,10,100, 5432))