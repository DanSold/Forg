def name_processing(name_fun:str):
    while True:
        if len(name_fun) < 2:
            print("Your name is too short")
        elif len(name_fun) > 10:
            print("Your name is too long")
        elif not name_fun.isalpha():
            print("Your name can only contain letters")
        elif not name_fun[0].isupper() or name_fun[1:].islower():
            name_fun = name_fun[0].upper() + name_fun[1:].lower()
            break
        else:
            break
        name_fun = input("Please enter your name again: ")
    return name_fun

def age_processing(age_fun:str):
    while True:
        if age_fun.isdigit():
            age_fun = int(age_fun)
            if age_fun > 120:
                print("Your age is too high")
            else:
                break
        else:
            print("Your age isn't valid")
        age_fun = input("Please enter your age again: ")
    return age_fun

name = input("Please enter your name: ")
name_final = name_processing(name)
age = input("Please enter your age: ")
age_final = age_processing(age)
print(f"Hello {name_final}!")
print(f"You are {age_final} years old.")
