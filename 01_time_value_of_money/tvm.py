import math

present_value = 1000
r = 0.05
n = 10
t = 5

# continuous methods
def future_value_continuos (pv, r, t) :
    return pv * math.exp(r*t)


def present_value_continuos (fv,r, t) :
    return fv * math.exp(-r*t)


print("####################### CONTINUOS METHODS ############################")

continuos_future_value = future_value_continuos(present_value, r, t)
continuos_present_value = present_value_continuos(continuos_future_value, r, t)

print(f"Future value of: {present_value} at {r} rate over {n} years is ${continuos_future_value:.2f}")
print(f"Future value of: ${continuos_future_value:.2f} at {r} rate over {n} years is ${continuos_present_value:.2f}")



# discrete methods
def future_value_discrete (pv, r, n) :
    return pv * (1+r) ** n

def present_value_discrete (fv, r, n) :
    return fv / (1+r) ** n




print("####################### DISCRETE METHODS ############################")

future_value_result = future_value_discrete(present_value, r, n)


print(f"Future value of: {present_value} at {r} rate over {n} years is ${future_value_result:.2f}")

present_value_result = present_value_discrete(future_value_result, r, n)

print(f"Present value of: ${future_value_result:.2f} at {r} rate over {n} years is ${present_value_result:.2f}")
