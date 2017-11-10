file=open("devices.txt","a")

while True:
    newitem=input("Enter device name: ")
    if newitem=="exit":
        print("All done!")
        file.close()
        break
    else:
        file.write(newitem + "\n")
    
