import math



# discrete methods
def future_value_discrete (pv, r, n) :
    return pv * (1+r) ** n

def present_value_discrete (fv, r, n) :
    return fv / (1+r) ** n

present_value = 1000
r = 0.05
n = 10


future_value_result = future_value_discrete(present_value, r, n)

print(f"Future value of: {present_value} at {r} rate over {n} years is ${future_value_result:.2f}")

present_value_result = present_value_discrete(future_value_result, r, n)

print(f"Present value of: ${future_value_result:.2f} at {r} rate over {n} years is ${present_value_result:.2f}")
