import os  # perform os task

# print(os.system("df -h"))


def sys__info(command):
    return os.system(command)


sys__info(input("Enter the sys command: "))
