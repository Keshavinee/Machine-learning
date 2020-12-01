def partial_der(a,b,training_set):
    summation_1=summation_2=0
    for x,y in training_set:
        summation_1+=a+b*x-y
        summation_2+=(a+b*x-y)*x
    return summation_1,summation_2


def gradient_descent(a,b,learning_rate,training_set,sum1,sum2):
    a-=(learning_rate*sum1)
    b-=(learning_rate*sum2)
    return a,b
    
import random
import numpy as np
from matplotlib.pyplot import *

a=random.randrange(0,5)
b=random.randrange(0,5)

train_set=[(1,500),(3,600),(4,650),(8,700)]
alpha=0.01

sum1,sum2=partial_der(a,b,train_set)
while sum1!=0 and sum2!=0:
    a,b=gradient_descent(a,b,alpha,train_set,sum1,sum2)
    sum1,sum2=partial_der(a,b,train_set)

arr1=np.array([1,3,4,8])
arr2=a+b*arr1

plot(arr1,[500,600,650,700],"bo")
plot(arr1,arr2)

xlabel("area(in sq.ft)")
ylabel("price(in $")

show()


