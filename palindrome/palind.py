def count_palindromes(l):
   count=0
   
   for elements in l:
        
          if isinstance(elements,str):       # isinstance it is use for the check the object type..
              if check(elements):
              
                  count+=1
                  
          elif isinstance(elements, (list,tuple)):
               count_palindromes(elements)
               
   return count
   
def check (elements):
 
   if len(elements)% 5 == 0:         # check string is divisible by 5 or not..
   
       return elements==elements[::-1]
       
   return False
    
print(count_palindromes(["madam", '121', 'level', "deified", ["noon", "radar", "apple"]]))
               
