def convert(temp):
    return (temp * 9/5) + 32

celsius_temperatures = [0, 20, 37, 100]
a = list(map(convert, celsius_temperatures))
print(a)