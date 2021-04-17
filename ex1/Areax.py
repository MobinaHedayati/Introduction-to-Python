def Areax(A,B,C,D,ghotr):

    if D==0:
        p=(A+B+C)/2
        print ((p*(p-A)*(p-B)*(p-C))**0.5)
    elif B==0:
        p=(A+C+D)/2
        print ((p*(p-A)*(p-D)*(p-C))**0.5)
    elif C==0:
        p=(A+B+D)/2
        print ((p*(p-A)*(p-B)*(p-D))**0.5)
    elif A==0:
        p=(D+B+C)/2
        print ((p*(p-D)*(p-B)*(p-C))**0.5)

    else:
    pABghotr=(A+B+Di)/2
    pCDghotr=(C+D+Di)/2
    A1=((pABghotr*(pABghotr-A)*(pABghotr-B)*(pABghotr-ghotr))**0.5)
    A2=((pCDghotr*(pCDghotr-C)*(pCDghotr-D)*(pCDghotr-ghotr))**0.5)
    print (A1+A2)
