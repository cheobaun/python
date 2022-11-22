cartoon_names = []
cartoon_number = input("How many cartoons do you want to add?: ")
cartoon_number = int(cartoon_number)
for i in range(cartoon_number):
    name = input("Enter the name of the cartoon: ")
    cartoon_names.append(name)
print(cartoon_names)
