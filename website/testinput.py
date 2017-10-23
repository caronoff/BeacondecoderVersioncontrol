#!/usr/bin/python
print("Content-Type: text/html\n")
#print()

def input():
    f = '<form action="runme.py">Enter hexidecimal code: <input type="text" name="hex" value=""><br><input type="submit" value="Submit"></form>'
    print(f)


if __name__ == "__main__":
     input()


