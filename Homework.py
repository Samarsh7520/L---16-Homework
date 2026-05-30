def is_power_of_eight(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0 and (n - 1) % 7 == 0

test_numbers = [1,8,64,512,16,0, -8]
for num in test_numbers:
    print(f"Is{num} a power of 8? {is_power_of_eight(num)}")