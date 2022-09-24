def oldlicense(insurance):
    insurance= insurance /2
    print("Your insurance is: ",insurance)
def younglicense(insurance):
    insurance= insurance // 1.50
    print("Your insurance is: ",insurance)
def noteligible():
    print("Sorry, not eligible for insurance")
insurance=int(input("Please insert here your insurance value: "))
age=int(input("Please, insert here your age: "))
if(28<=age<=40):
    noteligible()
if(age>40):
    haslicense=input("Do you have license? ")
    if haslicense=='yes':
        oldlicense(insurance)
    else:
        noteligible()
if(age<=28):
    haslicense=input("Do you have license? ")
    if haslicense=='yes':
        younglicense(insurance)
    else:
        noteligible()