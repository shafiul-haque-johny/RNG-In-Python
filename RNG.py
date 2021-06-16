import math
import matplotlib.pyplot as plt

# Initial Z1 , Z2, Z3
Z1 = [12, 7]
Z2 = [3, 5]
Z3 = [2, 7]

# Random Numbers
N1 = 100
N2 = 1000
N3 = 5000

U1 = []
U2 = []
U3 = []


def g1(i):

    new_z1 = ((Z1[i - 1] * 13) + (Z1[i - 2] + 3)) % 16
    Z1.append(new_z1)
    return (new_z1 / 16)


def g2(i):

    new_z2 = (12 * (Z2[i - 1] ** 2) + (13 * Z2[i - 2])) % 17
    Z2.append(new_z2)
    return (new_z2 / 17)


def g3(i):

    new_z3 = ((Z3[i - 1] ** 3) + Z3[i - 2]) % 15
    Z3.append(new_z3)
    return (new_z3 / 15)


for i in range(2, N1+2):

    x1 = g1(i)
    y1 = g2(i)
    z1 = g3(i)
    d1 = (x1 + y1 + z1)

    fraction, whole = math.modf(d1)
    U1.append(fraction)

plt.figure(figsize=(8, 8))
plt.hist(U1, bins=20, rwidth=0.8)
plt.title("For 100 Random Numbers")
plt.show()

Z1 = [12, 7]
Z2 = [3, 5]
Z3 = [2, 7]

for i in range(2, N2+2):

    x2 = g1(i)
    y2 = g2(i)
    z2 = g3(i)
    d2 = (x2 + y2 + z2)

    fraction, whole = math.modf(d2)
    U2.append(fraction)

plt.figure(figsize=(8, 8))
plt.hist(U2, bins=20, rwidth=0.8)
plt.title("For 1000 Random Numbers")
plt.show()

Z1 = [12, 7]
Z2 = [3, 5]
Z3 = [2, 7]

for i in range(2, N3+2):

    x3 = g1(i)
    y3 = g2(i)
    z3 = g3(i)
    d3 = (x3 + y3 + z3)

    fraction, whole = math.modf(d3)
    U3.append(fraction)

plt.figure(figsize=(8, 8))
plt.hist(U3, bins=20, rwidth=0.8)
plt.title("For 5000 Random Numbers")
plt.show()
