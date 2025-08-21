import os, platform

# print host name

host_name = os.uname()


print("####################################################################")
print("########################## Printing Host Info ######################")
print("####################################################################")
print(f"Host Name: {host_name.nodename}")

print(f"OS Name: {host_name.sysname}")

print(f"Python Version: {platform.python_version()}")



