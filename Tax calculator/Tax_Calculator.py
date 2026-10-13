salary = int(input("What is your salary : "))


a = 12450 * 0.19
b = (20199 - 12450) * 0.24
c = (35200 - 20199) * 0.30
d = (60000 - 35200) * 0.37
e = (300000 - 60000) * 0.45
f = (salary - 300000) * 0.47


tax = 0

if salary <= 12450:
    tax += salary  * 0.19
elif salary <= 20199:
    tax += a
    tax += (salary - 12450) * 0.24
elif salary <= 35200:
    tax += a
    tax += b
    tax += (salary - 20199) * 0.30
elif salary <= 60000:
    tax += a
    tax += b
    tax += c
    tax += (salary - 35200) * 0.37
elif salary <= 300000:
    tax += a
    tax += b
    tax += c
    tax += d
    tax += (salary - 60000) * 0.45
elif salary > 300000:
    tax += a
    tax += b
    tax += c
    tax += d
    tax += f

print(f"Salary before tax is {salary}, Gross tax amount is {tax:.2f} and "
      f"{"\n"}Salary after tax is {salary - tax:.2f}")


