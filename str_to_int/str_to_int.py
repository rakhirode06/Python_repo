
decimal_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str_to_int(text):
   
     if len (text)==0:
         return 0
     elif len (text)==1:
          if text in decimal_dict:
        
                 return  decimal_dict[text]
        
          else:
           raise ValueError(f"Invalid character: {text}")
           
     else:
      ''' # for the reverese the string      :: right to left 
          n=0
          for j, char in enumerate (text[::-1]):
           
             if char  not in decimal_dict:
                  raise ValueError (f"invalid char:{text}")
             n+= decimal_dict[char]*pow (10,j)
          return n'''
          
      #  for the left to right
     n=0
     for char in text:
             
                 if char not in decimal_dict:
                      raise ValueError (f"invalid char:{text}")
                      
                 n= n*10 + decimal_dict[char]
     return n
     
#print (str_to_int("123"))

# decimal subtraction add 
def decimal_sub(a_str,b_str):
    a_int = str_to_int(a_str)
    b_int= str_to_int(b_str)
    
    return  a_int-b_int
    
a= "123"
b="23"
print(decimal_sub(a,b))
    
     


