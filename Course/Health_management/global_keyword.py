var = 10
def inc_by_var(num):
    var = 15
    global var
    print(num + var)

res = inc_by_var(100)
