with open("artifacts.txt","r") as f:
    text= f.read()
    
with open("artifacts2.txt","w") as f:
    f.write(text +"added lines")
    
print("end of added")