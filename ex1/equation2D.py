def equation2D (a,b,c):
    delta=(b**2)-(4*a*c)
    x1=(-b-(delta**0.5))/2*a
    x2=(-b+(delta**0.5))/2*a
    
    if delta>0 :
        print ('x1={} and x2={}'.format(x1,x2))
      
    elif delta==0 :
        print ('x1=x2={}'.format(x1))
      
    elif delta<0 :
        print ('none')
