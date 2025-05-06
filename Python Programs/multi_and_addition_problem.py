"""Problem: Calculate the Multiplication and Sum of Two Numbers
   Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

   For example:
   - Given `number1 = 20` and `number2 = 30`, the result should be the product: `The result is 600`.
   - Given `number1 = 40` and `number2 = 30`, the result should be the sum: `The result is 70`.

   Feel free to give it a try, and I'll be here to evaluate your solution!

   Hint: You can use an `if` statement to check whether the product exceeds 1000."""

# def multi_divi_problem():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     multi = num1 * num2

#     if multi > 1000:
#         return num1 + num2
#     else:
#         return multi
    
# ans = multi_divi_problem()

# print(ans)

def multi_divi_problem():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    multi = num1 * num2

    if multi > 1000:
        result = num1 + num2
        print(f"The result is {result} (sum).")
    else:
        print(f"The result is {multi} (product).")

multi_divi_problem()
