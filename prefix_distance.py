import math


def slice_prefix_distance(pattern, text):
    m=len(pattern)
    n=len(text)
   
   
    insertions, matches = 0, 0
    
    for i in range(m): 
       
        while pattern[i+insertions] != text[i]:
          insertions += 1
          if (i+insertions == m) : 
           return insertions, matches
        
        matches += 1
        if (matches+insertions == m): 
         return insertions, matches
    
    
def test_match(pattern, text , L  , verbose):
    
    if verbose:
        #print('pattern: %s\n text: %s'%(pattern,text))
     print "pattern:", pattern
     print "text   :", text
    ins, mat = slice_prefix_distance(pattern,text)
    
    m = float(len(pattern))
    if verbose:
     print "length of pattern        :", m
     print "matching characters      :", mat
     print "required ins or d_prefix :", ins


###############################main#########################3

patterns = ['matchme']
print "DB has signatures:", patterns
text= raw_input("Please enter source string:")


for pattern in patterns:
 test_match(pattern, text, 2, True)




