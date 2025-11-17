# ---------------------------
# Basic Division in Python
# ---------------------------

# Dividend: the total amount we want to split
dividend = 17

# Divisor: the number of equal parts or groups we split into
divisor = 5

# Quotient: the result of division (how many full groups we can make)
quotient = dividend // divisor   # integer division

# Remainder: what is left over after making equal groups
remainder = dividend % divisor   # modulus operator

# Normal division (gives decimal)
division_result = dividend / divisor

print("Dividend:", dividend)
print("Divisor:", divisor)
print("Quotient (full groups):", quotient)
print("Remainder (left over):", remainder)
print("Division result (decimal):", division_result)
