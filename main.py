import time

def fun(func):
  def wrapper():
    
		  func()
      
  return wrapper


def ask_age():
  s = 1
  print('use "-","+","*","/","**" in sign')
  while s == 1:
     num1 = ''
     sign = ''
     num2 = ''
     g = ''
     while num1 == '' or sign == '' or num2 == '' :
      
       try:


         sign = input('input your sign:')
         if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '**':
           print ()
         else:
           sign = ''
          
           raise ValueError
         
         num1 = int(input('Input your number 1:'))
         if num1<= 999999 :
           print()
         else:
           num1 >= 999999
  
  
           raise ValueError
  
        
         
         num2 = int(input('Input your number 2:'))
         if num2<= 999999 :
           print()
         else:
           num2 >= 999999
  
    
           raise ValueError

      
         
          
          
       except ValueError:
        
  
      
         print('You need to use digits or your number is too long!')
  
  
  
           
  
        
           
       if sign == '+':
         print(num1,sign,num2, '=',num1+num2)
       elif sign == '**':
         print(num1,sign,num2, '=', num1**num2)
  
       elif sign == '/':
         try:
             print(num1,sign,num2,'=', num1/num2)
         except:
   				          print('This is division by zero!!!')
       elif sign == '-':
         print(num1,sign, num2, '=', num1-num2)
       elif sign == '*':
         print(num1,sign,num2, '=', num1*num2)
     time.sleep(2)
     g = str(input('do you want to continue? (print "yes" or "no") :'))
   
     if g == 'yes':
          print()

     elif g == 'no':
           s = 2
           print('the program has been stopped')
     
  
    
     
    
       
     
  
     
        

   

ask_age()