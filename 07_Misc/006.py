# Calculate Q = sqrt(2*C*D/H) where C=50, H=30. D values are supplied as a comma-separated sequence. Round each result to the nearest integer. E.g. input: 100,150,180 → output: 18,22,24.


D = [100,150,180]
C = 50
H = 30

result = []

for num in D:
    result.append(((2*C*num)/H)**0.5)

for num in result:
    print(int(num))

