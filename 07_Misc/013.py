# Write a program that computes the value of a + aa + aaa + aaaa with a given digit as the value of a. E.g. input 9 → 9 + 99 + 999 + 9999 = 11106.

num = 9
result = 0

for i in range(1,5):
    x = str(num)*i
    result = result+int(x)


print(result)



