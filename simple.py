from random import uniform, randint
from math import exp
import numpy as np
import csv
import ast
sig = lambda n: (1 + (exp(-n))) ** -1
sigderiv = lambda n: sig(n) * (1 - sig(n))
w1 = 0
w2 = 0
b1 = 0
b2 = 0
def forward_prop(input,w1,b1,w2,b2):
    l1 = np.array(list(map(sig, np.add(input.dot(w1), b1))))
    l2 = np.array(list(map(sig, np.add(l1.dot(w2),b2))))
    return l2
def back_prop(expected,input,w1,b1,w2,b2):
    yarray = np.zeros(26)
    yarray[expected] = 1

    l1 = np.add(input.dot(w1),b1)
    l1sig = np.array(list(map(sig, l1)))

    l2 = np.add(l1sig.dot(w2), b2)
    l2sig = np.array(list(map(sig, l2)))

    l1sigderiv = np.array(list(map(sigderiv, l1)))
    l2sigderiv = np.array(list(map(sigderiv, l2)))

    dc = 2 * (l2sig - yarray)

    dw2 = np.outer(l1sig, l2sigderiv * dc)
    db2 = l2sigderiv * dc

    dw1 = np.outer(input, l1sigderiv * (w2.dot(l2sigderiv * dc)))
    db1 = l1sigderiv * (w2.dot(l2sigderiv* dc))
    return dw1, db1, dw2, db2
def train(data):
    global w1, b1, w2, b2
    w1 = np.array([[uniform(-1,1) for _ in range(16)]for _ in range(4)])
    b1 = np.array([uniform(-1,1) for _ in range(16)])
    w2 = np.array([[uniform(-1,1) for _ in range(26)]for _ in range(16)])
    b2 = np.array([uniform(-1,1) for _ in range(26)])
    train_times = 500
    for training_amt in range(train_times):
        if training_amt % 5 == 0:
            print(str(training_amt / train_times * 100) + "% trained")
        for d in data:
            input = d["input"]
            expected = d["expected"]

            yarray = np.zeros(26)
            yarray[expected] = 1

            out = yarray * 999 # arbitrary

            i = 0
            while np.sum((out-yarray) ** 2)/len(out) > 0.001:
                dw1, db1, dw2,db2 = back_prop(expected, input,w1,b1,w2,b2)
                w1 = np.subtract(w1, np.multiply(dw1, 0.01))
                b1 = np.subtract(b1, np.multiply(db1, 0.01))
                w2 = np.subtract(w2, np.multiply(dw2, 0.01))
                b2 = np.subtract(b2, np.multiply(db2, 0.01))
                out = forward_prop(input,w1,b1,w2,b2)
                i+=1
def toLetter(out):
    return chr(97 + np.argmax(out))


with open('trainingdata.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydata = []
    for rows in reader:
        mydata.append(
            {
                "input": np.array(ast.literal_eval(rows[0])),
                "expected": int(rows[1])
            }
        )