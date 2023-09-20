letter_z = "z"
num_3 = "3.14"
a_space = " "

def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("Is Pi a Float?", isfloat(num_3))
