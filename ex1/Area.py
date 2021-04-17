def Area(A,B,C,D,ghotr):

    if D==0:
        p=(A+B+C)/2
        print ((p*(p-A)*(p-B)*(p-C))**0.5)
    if D!=0:
        pABDi=(A+B+ghotr)/2
        pCDDi=(C+D+ghotr)/2
        A1=((pABghotr*(pABghotr-A)*(pABghotr-B)*(pABghotr-ghotr))**0.5)
        A2=((pCDghotr*(pCDghotr-C)*(pCDghotr-D)*(pCDghotr-ghotr))**0.5)
        print (A1+A2)
