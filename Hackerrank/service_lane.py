n,t=map(int,raw_input().split())
width = raw_input().split()
while t:
    i,j = map(int,raw_input().split())
    sm = width[i] # Entry section
    for item in range(i,j+1):
        if width[item] < sm:
            sm = width[item] # update the smallest
    print sm
    t=t-1
