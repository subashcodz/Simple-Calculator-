print("choose 1 for numerical calucations\nchoose 2 for temperature converter")
q=int(input("choose method :"))
if q==1:
    c=input("calucation:")
    if(c.__contains__("+")):
       num1,num2=c.split("+")
       num1=int(num1)
       num2=int(num2)
       print(num1+num2)
    if(c.__contains__("-")):
       num1,num2=c.split("-")
       num1=int(num1)
       num2=int(num2)
       print(num1-num2)    
    if(c.__contains__("*")):
       num1,num2=c.split("*")
       num1=int(num1)
       num2=int(num2)
       print(num1*num2)
    if(c.__contains__("/")):
       num1,num2=c.split("/")
       num1=int(num1)
       num2=int(num2)
       print(num1/num2)
    if(c.__contains__("%")):
       num1,num2=c.split("%")
       num1=int(num1)
       num2=int(num2)
       print(num1%num2)
elif q==2:
    temp=int(input("enter temperature:"))
    unit=input("\nenter units of entered temperature\n c if celsius\n f if farenheit\n k if kelvin")
    if unit=="c":
       print("fahrenheit:",(temp*9/5)+32)
       print("kelvin:",temp+273)
    elif unit=="k":
       print("fahrenheit:",((temp-273)*18)+32)
       print("celsius:",temp-273)
    elif unit=="f":
       print("kelvin:",((temp-32)*5/9)+273)
       print("celsius:",(temp-32)*5/9)
else:
    print("invalid method")

   

     


     


 