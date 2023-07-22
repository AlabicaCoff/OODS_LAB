height, weight = input("Enter your High and Weight : ").split(" ")
bmi = float(weight) / (float(height) * float(height))

if bmi < 18.50:
    print("Less Weight")
elif bmi >= 18.50 and bmi < 23:
    print("Normal Weight")
elif bmi >= 23 and bmi < 25:
    print("More than Normal Weight")
elif bmi >= 25 and bmi < 30:
    print("Getting Fat")
else:
    print("Fat")