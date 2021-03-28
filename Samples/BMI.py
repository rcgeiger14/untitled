x=input("What is your name?")
print("Hello"+" "+x)
y=int(input(x+", What is your weight?"))
z=int(input(x+" , What about your height?"))
b=y*703/(z**2);
if b<18.5:
    print("Your BMI is:"+str(b)+". "+x+" you are underweight.")
elif 18.5<b<24.9:
    print("Your BMI is:"+str(b)+". "+x+" you are normal.")
elif 24.9<=b<=29.9:
    print("Your BMI is:"+str(b)+". "+x+" you are overweight.")
else:
    print("Your BMI is:"+str(b)+". "+x+" you are super fat...")
dic={
    x:b}
