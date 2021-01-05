import os

path = "/home/saumye/Documents/Vscode/snakecode/"

print("*********FILE CREATE UTILITY*********\n")
print("Enter the name of the to be created")
filename = input()

l1 = filename.split(" ")
l2 = []
for word in l1:
    word = word[0:1].upper() + word[1:]
    l2.append(word)

filename = "".join(l2)

filename += ".py"
bashcommand = "code {}".format(filename)

print("Enter the question code from codeforces")
code = input()

text = "'''\n Question Code: " + code +"\n'''"

with open (filename, 'w') as fp:
    fp.write(text)

os.system(bashcommand)    
fp.close()