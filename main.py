import os
import time
import math
import random



 		

dr = 1
t = ''
r = ''
ran1 = ''
ran2 = ''
a = ''

a = (input('choose your language (print "Eng" or "Rus") : '))


if a == 'Eng' or a == 'eng':
      
    print('')
    r = (input('Do you want to use program like a calculator or random? (print "Cal" or "Rand") : '))
    if r == 'Rand' or r == 'rand': 
     try:
      ran1 = int(input('input where the countdown starts:'))
      if ran1 > 0 or ran1 < 0:
        print('')
      else:
        raise ValueError
      ran2 = int(input('input where the countdown stopped:'))
      if ran2 > 0 or ran2 < 0:
        print('')
      else:
        raise ValueError
      print('')
      t =   random.randint(ran1,ran2)
      print('random number from', ran1, 'to', ran2, 'is', t) 
      print('')
      print('The program has been stopped')

      


      
     except ValueError:
       print('use only numbers! ')
        
       

    elif r == 'Cal' or r == 'cal':
    
      
    
 
  

                
     
     
       
  
  
      
      def ask_age():
        s = 1

        
        while s == 1:

           num1 = ''
           sign = ''
           num2 = ''
           g = ''
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
               
               g = str(input('do you want to continue in a new window? (print "yes" or "no") :'))
             
               if g == 'yes' or g == 'Yes':
                    print()
                    dr = 1
                    os.system('cls||clear')
          
               elif g == 'no' or g == 'No':
                     s = 2
                     print('The program has been stopped')
                     dr = 1
               else:
                 print('print just "yes" or "no"')
                 print('')
                 time.sleep(1)
             
 
  
      ask_age()
#-----------------------------------------------------------------------
    
    
elif a == 'Rus' or a == 'rus':
    print('')
    op = (input('Вы хотите использовать программу как калькулятор или рандомайзер? (напишите "Кал" или "Ранд") : '))
    if op == 'Ранд' or op == 'ранд': 
     try:
      ran1 = int(input('введите начало отсчета:'))
      if ran1 > 0 or ran1 < 0:
        print('')
      else:
        raise ValueError
      ran2 = int(input('введите окончание отсчета:'))
      if ran2 > 0 or ran2 < 0:
        print('')
      else:
        raise ValueError
      print('')
      t =   random.randint(ran1,ran2)
      print('рандомное число от', ran1, 'до', ran2, 'это', t) 
      print('')
      print('Программа была остановлена')


      
     except ValueError:
       print('используйте только числа! ')
       

    elif op == 'Кал' or op =='кал': 
      
      def ask_age1():
        s = 1

        
        while s == 1:
           num1 = ''
           sign = ''
           num2 = ''
           g = ''
           dr = 1
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
             
               if g == 'да' or g == 'Да':
                    print()
                    dr = 1
                    os.system('cls||clear')
               elif g == 'нет' or g == 'Нет':
                     s = 2
                     print('программа была остановлена')
                     dr = 1
               else:
                 print('пишите только "да" или "нет"')
                 print('')
                 time.sleep(1)
             
          
      
      ask_age1()
    
    else:
      
     print()


else:
  print('')
  print('you need to print just "Eng" or "Rus" ')
  

  