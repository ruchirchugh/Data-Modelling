# Ruchir Chugh
# 1001506316
import sys
import random
import math
from random import seed
random.seed(30)
def bernoulli(inputNumber,val):
    value = []
    p = float(val[0])
    if len(val) != 1:
        print("Wrong Arguments")
        sys.exit()
    else:
        if p < 0.0 and p > 1.0:
            print('value of P is wrong')
            sys.exit()
        else:
            for i in range(inputNumber):
                if random.random() >= p:
                    value.append(0)
                else:
                    value.append(1)
    return value

def binomial(inputNumber,val):
    value = []
    n = int(val[0])
    p = float(val[1])
    if len(val) != 2:
        print("Wrong Arguments")
        sys.exit()
    else:
        if p < 0.0 and p > 1.0:
            print('value of P is wrong')
            sys.exit()
        else:
            for i in  range(inputNumber):
                count = 0
                for j in range(n):
                    if random.random() < p:
                        count = count + 1
                value.append(count)
    return value

def geometric(inputNumber,val):
    value = []
    p = float(val[0])
    if len(val) != 1:
        print("Wrong Arguments")
        sys.exit()
    else:
        if p < 0.0 and p > 1.0:
            print('value of P is wrong')
            sys.exit()

        else:
            for i in range (inputNumber):
                count = 1
                while random.random() > p:
                    count = count + 1
                value.append(count)

    return value

def negbinomial(inputNumber,val):
    value = []
    k = int(val[0])
    p = val[1:len(val)]
    if len(val) > 2:
        print("Wrong Arguments")
        sys.exit()
    else:
        for i in range(inputNumber):
            value.append(sum(geometric(k,p)))
    return value

def poisson(inputNumber,val):
    values = []
    lambda1 = float(val[0])
    if len(val) >  1:
        print("Wrong Arguments")
        sys.exit()
    else:
        for i in range(inputNumber):
            count=0
            ran = random.random()
            e_lambda = math.exp(-lambda1)
            while ran >= e_lambda:
                count = count + 1
                ran = ran * random.random()
            values.append(count)
    return values

def cdf(p):
    table = []
    for i in range(len(p)):
        table.append(sum(p[0:i+1]))
    return table

def arbdiscrete(inputNumber,val):
    value = []
    p = []
    for i in val:
        p.append(float(i))
    cdf_P = cdf(p)
    if cdf_P[-1] != 1:
        print("total prob should be 1")
        sys.exit()
    else:
        for i in range(inputNumber):
            count = 0
            s = random.random()
            while cdf_P[count] <= s:
                count = count + 1
            value.append(count)
    return value

def uniform(inputNumber,val):
    value = []
    a = float(val[0])
    b = float(val[1])
    if len(val) != 2:
        print("worng paramenters")
        sys.exit()
    else:
        if a > b:
            x = a
            a = b
            b = x
        for i in range(inputNumber):
            value.append(a+((b-a)*random.random()))
    return value

def exponential(inputNumber,val):
    value = []
    lambda1 = float(val[0])
    if len(val) > 1:
        print("worng paramenters")
        sys.exit()
    else:
        for i in range(inputNumber):
            value.append((-(1/lambda1))*math.log(1-random.random()))
    return value

def gamma(inputNumber,val):
    value = []
    alpha1 = int(val[0])
    lambda1 = val[1:len(val)]
    for i in range(inputNumber):
        value.append(sum(exponential(alpha1,lambda1)))
    return value

def normal(inputNumber,val):
    value = []
    alpha1 = float(val[0])
    sigma = float(val[1])
    cen = int(math.ceil(float(inputNumber)/2))
    if len(val) > 2:
        print("wrong arguments")
        sys.exit()
    else:
        for i in range(cen):
            n1 = random.random()
            n2 = random.random()
            a1 = math.sqrt((-2)*math.log(n1))*math.cos(2*math.pi*n2)
            a2 = math.sqrt((-2)*math.log(n1))*math.sin(2*math.pi*n2)
            value.append(alpha1 + a1*sigma)
            value.append(alpha1 + a2*sigma)
        if inputNumber % 2 == 0:
            return value
        else:
            return value[0:len(value)-1]

inputNumber = int(sys.argv[1])
distName = sys.argv[2].lower()
argsval = sys.argv[3:len(sys.argv)]
if distName == 'bernoulli':
    result = bernoulli(inputNumber,argsval)
elif distName == 'binomial':
    result = binomial(inputNumber,argsval)
elif distName == 'geometric':
    result = geometric(inputNumber,argsval)
elif distName == 'neg-binomial':
    result = negbinomial(inputNumber,argsval)
elif distName == 'poisson':
    result = poisson(inputNumber,argsval)
elif distName == 'arb-discrete':
    result = arbdiscrete(inputNumber,argsval)
elif distName == 'uniform':
    result = uniform(inputNumber,argsval)
elif distName == 'exponential':
    result = exponential(inputNumber,argsval)
elif distName == 'gamma':
    result = gamma(inputNumber,argsval)
elif distName == 'normal':
    result = normal(inputNumber,argsval)
else:
    sys.exit(distName + 'Wrong distribution')

print('Values are:'+ str(result))