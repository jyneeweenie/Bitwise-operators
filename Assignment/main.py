num = int(input("Enter a number: "))

if num > 0 and (8 ** round(num.bit_length() / 3)) == num:
    print(f"{num} is a power of 8.")
else:
    print(f"{num} is NOT a power of 8.")
