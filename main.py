import time
import math




def ask_age():
  s = 1
  print('use "-" in sign to subtract')
  time.sleep(0.5)
  print('use "+" in sign to fold')
  time.sleep(0.5)
  print('use "*" in sign to multiply')
  time.sleep(0.5)
  print('use "/" in sign to devision')
  time.sleep(0.5)
  print('use "**" in sign to exponentiation')
  time.sleep(0.5)
  print('use "//" in sign to take the square root')
  time.sleep(0.5)
  print('')
  print('')
  
  while s == 1:
     num1 = ''
     sign = ''
     num2 = ''
     g = ''
     dr = 1
     
     
     
     while num1 == '' or sign == '' or num2 == '' :
      
       try:


         sign = input('input your sign:')
         if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '**' or sign == '//':
           print ()
         else:
           sign = ''
          
           raise ValueError
           
       
         if sign == '//':
                num2 = num1 = int(input('Input your number:'))
                print('')
                sqrt = math.sqrt(num1)
                print('the square root of ', str(num1) , 'this' , str(sqrt))
        
         if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '**':
               num1 = int(input('Input your number 1:'))
               if num1<= 999999 :
                 print()
               else:
                 num1 > 999999
               
        
        
                 raise ValueError
                
               if sign == '**' and num1 > 100 :
                 print('your number is too big for "**"')
                 raise ValueError
        
              
               
               num2 = int(input('Input your number 2:'))
               if num2<= 999999 :
                 print()
               else:
                 num2 > 999999
          
        
          
                 raise ValueError
               if sign == '**' and num2 > 100 :
                 print('your number is too big for "**"')
                 raise ValueError
    
                 
    
              
               
             


          
       except ValueError:
            
      
          
             print('You need to use digits or your number is too long!')
  
  
  
           
     if sign == '**' and num1 <= 100 and num2 <=100:
         print(num1,sign,num2, '=', num1**num2 )
        
         
         
   
     else:
        
           
       if sign == '+' and num2 <=999999:
         print(num1,sign,num2, '=',num1+num2)
        
         
      
  
       elif sign == '/'  and num2 <=999999:
         try:
             print(num1,sign,num2,'=', num1/num2)
            
         except:
   				          print('This is division by zero!!!')
       elif sign == '-' and num2 <=999999:
         print(num1,sign, num2, '=', num1-num2)
       
       elif sign == '*' and num2 <=999999:
         print(num1,sign,num2, '=', num1*num2)
         

         
     time.sleep(2)

     dr = 2
         
    
     
     while dr == 2:
         g = str(input('do you want to continue in NEW window? (print "yes" or "no") :'))
       
         if g == 'yes':
              print()
              dr = 1
    
         elif g == 'no':
               s = 2
               print('the program has been stopped')
               dr = 1
         else:
           print('say only "yes" or "no"')
           print('')
           time.sleep(1)
       


ask_age()