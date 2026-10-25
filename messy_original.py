import sys
def f(l):
    t=0
    for i in range(0,len(l)):
        t=t+l[i]
    a=t/len(l)
    return a
def g(l):
    m=l[0]
    for x in l:
        if x>m:
            m=x
    return m
def h(a):
    if a>=90:
        return "A"
    else:
        if a>=75:
            return "B"
        else:
            if a>=50:
                return "C"
            else:
                return "F"
d={"amit":[88,92,79],"riya":[45,60,52],"sam":[70,81,77]}
for k in d:
    x=f(d[k]);y=g(d[k])
    print(k+" avg:"+str(round(x,2))+" best:"+str(y)+" grade:"+h(x))
