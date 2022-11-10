import time
import math




a = ''
a = (input('choose your language (print "Eng" or "Rus") : '))
if a == 'Eng':
  

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
         
#----------------------------------------------------------------  
  
  ask_age()


elif a == 'Rus':
  def ask_age1():
    s = 1
    print('используйте "-" в знаке для вычитания')
    time.sleep(0.5)
    print('используйте "+" в знаке для сложения')
    time.sleep(0.5)
    print('используйте "*" в знаке для умножения')
    time.sleep(0.5)
    print('используйте "/" в знаке для деления')
    time.sleep(0.5)
    print('используйте "**" в знаке для возведения в степень')
    time.sleep(0.5)
    print('используйте "//" в знаке для вычисления квадратного корня')
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
  
  
           sign = input('введите знак:')
           if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '**' or sign == '//':
             print ()
           else:
             sign = ''
            
             raise ValueError
             
         
           if sign == '//':
                  num2 = num1 = int(input('Введите число:'))
                  print('')
                  sqrt = math.sqrt(num1)
                  print('квадратный корень из ', str(num1) , 'это' , str(sqrt))
          
           if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '**':
                 num1 = int(input('введите первое число:'))
                 if num1<= 999999 :
                   print()
                 else:
                   num1 > 999999
                 
          
          
                   raise ValueError
                  
                 if sign == '**' and num1 > 100 :
                   print('Ваше число слишком большое для "**"')
                   raise ValueError
          
                
                 
                 num2 = int(input('введите второе число:'))
                 if num2<= 999999 :
                   print()
                 else:
                   num2 > 999999
            
          
            
                   raise ValueError
                 if sign == '**' and num2 > 100 :
                   print('Ваше число слишком большое для "**"')
                   raise ValueError
      
                   
      
                
                 
               
  
  
            
         except ValueError:
              
        
            
               print('Вам нужно использовать числа или ваше число слишком большое !')
    
    
    
             
       if sign == '**' and num1 <= 100 and num2 <=100:
           print(num1,sign,num2, '=', num1**num2 )
          
           
           
     
       else:
          
             
         if sign == '+' and num2 <=999999:
           print(num1,sign,num2, '=',num1+num2)
          
           
        
    
         elif sign == '/'  and num2 <=999999:
           try:
               print(num1,sign,num2,'=', num1/num2)
              
           except:
     				          print('Вы неможете делить на ноль!')
         elif sign == '-' and num2 <=999999:
           print(num1,sign, num2, '=', num1-num2)
         
         elif sign == '*' and num2 <=999999:
           print(num1,sign,num2, '=', num1*num2)
           
  
           
       time.sleep(2)
  
       dr = 2
           
      
       
       while dr == 2:
           g = str(input('вы хотите продолжить в новом окне? (напишите "да" или "нет") :'))
         
           if g == 'да':
                print()
                dr = 1
      
           elif g == 'нет':
                 s = 2
                 print('программа была остановлена')
                 dr = 1
           else:
             print('пишите только "да" или "нет"')
             print('')
             time.sleep(1)
         
  
  
  ask_age1()


else:
  print('')
  print('you need to print just "Eng" or "Rus" ')
  

  