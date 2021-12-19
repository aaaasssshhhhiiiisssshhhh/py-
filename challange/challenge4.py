#Write a Python program to check if a number is a perfect square.
def powerOf4(n):
    while n and not (n & 3): #we can write 0b11 instead if writing 3
        n >>=2
    return n ==1
print(powerOf4(16))    