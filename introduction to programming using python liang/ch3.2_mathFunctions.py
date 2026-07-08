import math      # Import the math module so we can use mathematical functions.

# =========================
# Algebraic Functions
# =========================

print("exp(1.0) =", math.exp(1))
# exp(x) = e^x
# 1 is chosen because e¹ = e, one of the most well known math constants.
# Expected result: about 2.718281828

print("log(e) =", math.log(math.e))
# log(x) is the natural logarithm (base e).
# math.e is used because ln(e) = 1 exactly.
# Expected result: 1.0

print("log10(10) =", math.log(10, 10))
# log(number, base)
# 10 is chosen for both values because log₁₀(10) = 1.
# Expected result: 1.0

print("sqrt(4.0) =", math.sqrt(4.0))
# sqrt(x) returns the square root.
# 4 is chosen because √4 = 2 exactly.
# Expected result: 2.0

# =========================
# Trigonometric Functions
# (Python uses RADIANS, not degrees.)
# =========================

print("sin(pi / 2) =", math.sin(math.pi / 2))
# π/2 radians = 90°
# sin(90°) = 1
# Expected result: 1.0

print("cos(pi / 2) =", math.cos(math.pi / 2))
# π/2 radians = 90°
# cos(90°) = 0
# Due to floating point rounding, Python may print a tiny number
# like 6.123233995736766e-17 instead of exactly 0.

print("tan(pi / 2) =", math.tan(math.pi / 2))
# π/2 radians = 90°
# tan(90°) is undefined because cosine is 0.
# Python returns a very large number instead of an error due to
# floating point approximation.

print("degrees(1.57) =", math.degrees(1.57))
# Converts radians to degrees.
# 1.57 is close to π/2 (about 1.5708).
# Expected result: about 90 degrees.

print("radians(90) =", math.radians(90))
# Converts degrees to radians.
# 90 degrees is chosen because it equals π/2 radians.
# Expected result: about 1.5707963267948966