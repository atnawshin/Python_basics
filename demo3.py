#letter grade detectation
marks = 67

'''if marks >= 80 and marks <= 100:      #if 80>= marks <=100       can also be written
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")
else:
    print("A-")'''

if 80<= marks <=100:
    print("A+")
elif 75<= marks <=79:
    print("A")

elif 70<= marks <=74:
    print("A-")

elif 65<= marks <=69:
    print("B+")

elif 60<= marks <=64:
    print("B")

elif 55<= marks <=59:
    print("B-")

elif 50<= marks <=54:
    print("C+")

elif 45<= marks <=49:
    print("C")

elif 40<= marks <=44:
    print("D")

else:
    print("F")