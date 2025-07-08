import time

# nested for loop
diseases = ("smallpox", "cowpox", "malaria", "HIV")

for disease in diseases:
    print("Name of the disease is: ", disease)
    print("Give me the test of:")
    for i in disease:
        print(i)
x = 2
while True:
    print("The value of x is:", x)
    print("Looping")
    x *= 2
    time.sleep(3)
