from random import uniform
from math import exp
import numpy as np
sig = lambda n: (1 + (exp(-n))) ** -1
sigderiv = lambda n: sig(n) * (1 - sig(n))

input = np.array([1,2,0,0])
expected = 3
w1 = np.array([[uniform(-0.1,0.1) for _ in range(4)]for _ in range(4)])
b1 = np.array([uniform(-0.1,0.1) for _ in range(4)])
w2 = np.array([[uniform(-0.1,0.1) for _ in range(26)]for _ in range(4)])
b2 = np.array([uniform(-0.1,0.1) for _ in range(26)])
def forward_prop(input,w1,b1,w2,b2):
    l1 = input.dot(w1)
    l1 = np.add(l1, b1)
    l1 = np.array(list(map(sig, l1)))
    l2 = l1.dot(w2)
    l2 = np.add(l2, b2)
    l2 = np.array(list(map(sig, l2)))
    return np.argmax(l2)
def back_prop(expected,input,w1,b1,w2,b2):
    yarray = np.zeros(26)
    yarray[expected] = 1
    l1 = np.add(input.dot(w1),b1)
    l1sig = np.array(list(map(sig, l1)))
    l2 = np.add(l1sig.dot(w2), b2)
    dw1 = np.zeros_like(w1)
    db1 = np.zeros_like(b1)
    dw2 = np.zeros_like(w2)
    db2 = np.zeros_like(b2)

    for j in range(len(l2)):
        zj = l2[j]
        aj = sig(zj)
        yj = yarray[j]
        dc = 2*(aj-yj)
        for k in range(len(l1)):
            dw = l1sig[k] * sigderiv(zj) * dc
            dw2[k][j] = dw
        db = sigderiv(zj) * dc
        db2[j] = db
    for k in range(len(l1)):
        dw = 0
        db = 0
        for j in range(len(l2)):
            zj = l2[j]
            aj = sig(zj)
            yj = yarray[j]
            dc = 2*(aj-yj)
            dw += w2[k][j] * sigderiv(zj) * dc
            db += sigderiv(zj) * dc
        dw1[k] = dw
        db1[k] = db
    return dw1, db1, dw2, db2


print(forward_prop(input,w1,b1,w2,b2))
for i in range(260):
    dw1, db1, dw2,db2 = back_prop(expected, input,w1,b1,w2,b2)
    w1 = np.subtract(w1, np.multiply(dw1, 0.001))
    b1 = np.subtract(b1, np.multiply(db1, 0.001))
    w2 = np.subtract(w2, np.multiply(dw2, 0.001))
    b2 = np.subtract(b2, np.multiply(db2, 0.001))
print(forward_prop(input,w1,b1,w2,b2))