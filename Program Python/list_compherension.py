lis1=['hello','take']
lis2=['dear','sir']
a=lis1[0]+" "+lis2[0]
b=lis1[0]+" "+lis2[1]
c=lis1[1]+" "+lis2[0]
d=lis1[1]+" "+lis2[1]
new_lis=[a,b,c,d]
print(new_lis)
# another method
x=lis1+lis2
y=[x[0]+" "+x[2],x[0]+" "+x[3],x[1]+" "+x[2],x[1]+" "+x[3]]
print(y)