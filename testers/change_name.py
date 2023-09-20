gbl_name = "Sally"

def change_name():
    global gbl_name
    gbl_name = "Sammy"
    
change_name()

print(gbl_name)
