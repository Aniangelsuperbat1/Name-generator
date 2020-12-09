from faker import Faker

real = Faker()

# print(real.name())
# print(real.address())
# print(real.text())

print("Hello, my name is", real.name() + "and my address is", real.address())

