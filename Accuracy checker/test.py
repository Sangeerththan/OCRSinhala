import difflib

cases=[('අනා', 'අණුක'),
       ('අණුවල', 'අණුකූල'),
       ('අණුකූලව', 'අණුකූලව'),
       ('අණුව', 'අණුව'),
       ('අඳ', 'අඬ')] 


for a,b in cases:     
    print('{} => {}'.format(a,b))  
    count=0
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ':continue    
        count=count+1
     
    print("count: "+str(count))
	