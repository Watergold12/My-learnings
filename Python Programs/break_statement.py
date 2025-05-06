result = True
for marks in 65, 45, 89, 69, 48, 56:
    if marks < 35:
        result = False
        break
    print(marks)
if(not(result)):
    print("Fail")