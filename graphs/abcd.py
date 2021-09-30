count_names = 0
given_names, result = "abc", ""
while given_names != "":
    given_names = input("Enter a name: ")
    result += f"{given_names}, "
    count_names += 1 
    
print(f"Name count {count_names}\n")
print(result.rstrip(", "))