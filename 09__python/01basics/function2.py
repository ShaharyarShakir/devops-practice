def vac_feedback(name, effeciency):
    print(f"{name} Vaccine is having a {effeciency} % effeciency")
    if 50 < effeciency <= 75:
        print("Low effeciency need more trail")
    elif 75 < effeciency <= 95:
        print("Good effeciency ready to use")
    else:
        print("Need more more trail")


vac_feedback("Pfizer", 95)

