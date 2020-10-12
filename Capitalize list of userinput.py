def alphabetize(original_list = []):
    sorted_list = original_list.copy()
    sorted_list.sort()
    
    final_list = ""
    for name in sorted_list:
        final_list += name+", "
    final_list = final_list[:-2]
    print (f"\nAll your students name are shown bellow:\n\n {final_list.upper()}")
students=[]
while True:
    try:
        members = input("Please type-in your name: ")
        students.append(members)
        if members == "unubi opaluwa": break
    except:
        exit()
alphabetize(students)