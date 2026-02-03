"""
planet = "closest to sun"

print(planet[0])
print(planet[1])
print(planet[2])

# reverse order

print(planet[-1])
print(planet[-2])
print(planet[-3])

# slicing a string
print(planet[0:5])
print(planet[:7])
print(planet[11:])

# slicing tuple

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

print(devops[0])
print(devops[1])
print(devops[2])
print(devops[3])
print(devops[1:3])
print(devops[:3])
print(devops[2:])
print(devops[0:2][0])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-6:-1])

# slicing list

devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

print(devops[0])
print(devops[1])
print(devops[2])
print(devops[3])
print(devops[1:3])
print(devops[:3])
print(devops[2:])
print(devops[0:2][0])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-6:-1])
"""

# slicing in dict

skills = {
    "DevOps": ("AWS", "Jenkins", "Python", "Ansible"),
    "Development": [
        "C",
        "JS",
        "Rust",
        "Python",
    ],
}
print(skills)

print(skills["DevOps"])
print(skills["DevOps"][:])
print(skills["DevOps"][2][:7])
print(skills["DevOps"][:2][1][:7])
