rand_string = "   this is a random string"

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

print(rand_string.capitalize())

print(rand_string.upper())

print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)
 
print("How many is :", rand_string.count("is"))

print("where is string :", rand_string.find("string"))

print(rand_string.replace("on ", "a kind of "))
