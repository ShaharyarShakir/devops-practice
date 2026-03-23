# String buildin
intro = "corona virus vaccine are becoming effective"
print(intro.capitalize())
# as strings are immutable
print(intro)
# display build-in functions for str dict list tuple
"""
print(dir(""))
print(dir(()))
print(dir([]))
print(dir({}))
"""
print(intro.upper())
print(intro.upper().isupper())
print(intro.islower())
print(intro.find("are"))

# editing a list
skills = ["jenkins", "linux"]
print(skills)
skills.append("ansible")
print(skills)
skills.insert(2, "teraform")
print(skills)
skills.extend(["bash scripting"])
print(skills)
skills.pop()
print(skills)
skills.pop(2)
print(skills)
squ1 = ["192", "168", "100", "4"]
print(".".join(squ1))
