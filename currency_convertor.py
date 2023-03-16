#take user input in dollars
#write a function to convert the usd to pkr
def convertor():
    print("This program converts USD to PKR.")
    usd=float(input("Enter USD : "))
    pkr=usd*226.72
    print("That is {} PKR".format(pkr))
convertor()