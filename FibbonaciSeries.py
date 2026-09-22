angka_Fibonacci = int(input("Input Fibonacchi Numbers: "))
z, x = 0, 1
for n in range(angka_Fibonacci):
    print(z, end=" ")
    z, x = x, z + x
