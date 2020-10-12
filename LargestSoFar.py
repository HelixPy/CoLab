largest_weight = 0
while (True):
    try:
        fish_weight = float(input("Enter fish weight: "))
        if fish_weight > largest_weight:
            largest_weight = fish_weight
        elif fish_weight == "end":
            print (f"The largest fish weight is: {largest_weight}Kg")
    except ValueError as e:
        print (f"The largest fish weight is: {largest_weight}Kg")
        break