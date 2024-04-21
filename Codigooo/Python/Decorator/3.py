def fun(a):
    def wrap(*args, **kwargs):
        print("argument",*args, **kwargs)
        
        
        
        result = a(*args, **kwargs)
        return result
    return wrap
@fun
def mul(x, y):
    return x * y
result = mul(10, 20)
print("Result:", result, type(result))

