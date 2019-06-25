def age_info(son_age):
    father_age = son_age + 30
    return father_age
son_age = float(input("Enter son age: "))

if son_age < 100:
    print(age_info(son_age))
else:
    print("How is that possible")