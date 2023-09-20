samp_string = "This is a very important string"

print("Length :", len(samp_string))

for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])


print ("Hello " * 5)

num_string = str(4)

print(num_string)

print(type(num_string))


for char in samp_string:
    print(char)

# A - Z 65 - 90
# a - z 97 - 122

print("A =", ord("A"))
print("65 =", chr(65))
