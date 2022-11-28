x = 0
y = 0
   
def init_c(a,b):
    global x
    global y
    x = a
    y = b

def c_devision():
    return  complex(x)/ complex(y)

def c_addition():
    return complex(x)+ complex(y)

def c_substraction():
    return complex(x)- complex(y)

def c_multiplication():
    return complex(x)* complex(y)