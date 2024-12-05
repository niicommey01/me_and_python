def get_names():
    names_dict = {}
    no_of_names = int(input("How many names? "))
    for i in range(no_of_names):
        name = input(f"Enter the name of person {i+1}: ")
        names_dict[f"Person {i+1}"] = name
    return names_dict


names = get_names()
print("Names:")
for key, value in names.items():
    print(f"{key}: {value}")


