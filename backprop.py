from random import uniform
from math import exp

sig = lambda n: (1 + (exp(-n))) ** -1
sigderiv = lambda n: sig(n) * (1 - sig(n))


def forward_prop(inp,w1,b1,w2,b2):
    l1 = sig(inp * w1 + b1)
    l2 = sig(l1 * w2 + b2)
    return l2


def back_prop(inp, w1, b1, w2, b2, y):
    l1 = sig(inp * w1 + b1)
    l2 = sig(l1 * w2 + b2)
    
    dcost = 2 * (l2 - y)
    
    dsig2 = sigderiv(l2)
    dsig1 = sigderiv(l1)
    
    return ((l2 - y) ** 2), dcost * dsig2 * l1, dcost * dsig2, dsig1 * inp, dsig1


w1 = uniform(-0.1, 0.1)
b1 = uniform(-0.1, 0.1)
w2 = uniform(-0.1, 0.1)
b2 = uniform(-0.1, 0.1)
input = 1
output = 0.31415926535
loss=9999
while loss > 10 * 10**-27:
    out = forward_prop(input,w1,b1,w2,b2)
    loss, dw2, db2, dw1, db1 = back_prop(input, w1, b1,w2,b2,output)
    w1 -= dw1 * 0.01 
    b1 -= db1 * 0.01 
    w2 -= dw2 * 0.01 
    b2 -= db2 * 0.01 
print("Final Loss:", loss)
print("Output:", forward_prop(input,w1,b1,w2,b2))
