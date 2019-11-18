import difflib
import codecs

cases=[('අනා', 'අණුක'),
       ('අණුවල', 'අණුකූල'),
       ('අණුකූලව', 'අණුකූලව'),
       ('අණුව', 'අණුව'),
       ('අඳ', 'අඬ')] 

g = codecs.open("testtxt.txt", "w+", encoding="utf-8")

for a,b in cases:     
    print('{} => {}'.format(a,b))  
    count=0
    for i,s in enumerate(difflib.ndiff(a, b)):
        g.write("i : "+str(i)+"\n")
        g.write("s : "+str(s)+"\n")
        if s[0]==' ':continue   
		#elif s[0]=='-':
            #g.write(u'Delete "{}" from position {}'.format(s[-1],i))
        #elif s[0]=='+':
            #g.write(u'Add "{}" to position {}'.format(s[-1],i)) 
        count=count+1
     
    g.write("count: "+str(count))
	