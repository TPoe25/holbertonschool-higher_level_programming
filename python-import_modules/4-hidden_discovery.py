#!/usr/bin/python3

with open("hidden_4.pyc", "rb") as f:
    code = f.read()
    
lines = code.split(b"\n")

names = set()
for line in lines:
    if b"STORE_NAME" in line and not line.startswith(b"__"):
        name = line.spilt(b" ")[-1].strip()
        names.add(name.decode("utf-8"))
        
for name in sorted(names):
    print(name)
