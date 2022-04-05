def getdate():
    import time
    return time.asctime(time.localtime(time.time()))
while True:
    op=input("Do you want to Read or Write or Quit (r/w/q) ?\n")
    if op=='w':
        name=str(input("Whose File do you want to update: Harry, Rohan, Hammad\n"))
        if name=="Harry" or "harry":
            work=input("Do you want to update Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("harryfood.txt","a")
                inp=input("Please Enter the diet: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
            else:
                f=open("harryex.txt","a")
                inp=input("Please Enter the Workout: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
        elif name=="Rohan" or "rohan":
            work=input("Do you want to update Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("rohanfood.txt","a")
                inp=input("Please Enter the diet: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
            else:
                f=open("rohanex.txt","a")
                inp=input("Please Enter the Workout: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
        elif name=="Hamad" or "hamad":
            work=input("Do you want to update Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("hamadfood.txt","a")
                inp=input("Please Enter the diet: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
            else:
                f=open("hamadex.txt","a")
                inp=input("Please Enter the Workout: ")
                f.write("["+str(getdate())+"]: "+inp+"\n")
                f.close
        else:
            print("Please enter the correct name")
    elif op=='q':
        break
    else:
        name=str(input("Whose File do you want to read: Harry, Rohan, Hammad\n"))
        if name=="Harry" or "harry":
            work=input("Do you want to read Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("harryfood.txt")
                print(f.read())
                f.close
            else:
                f=open("harryex.txt")
                print(f.read())
                f.close
        elif name=="Rohan" or "rohan":
            work=input("Do you want to read Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("rohanfood.txt")
                print(f.read())
                f.close
            else:
                f=open("rohanex.txt")
                print(f.read())
                f.close
        elif name=="Hamad" or "hamad":
            work=input("Do you want to read Food or excercise (f/e) ?\n")
            if work=='f':
                f=open("hamadfood.txt")
                print(f.read())
                f.close
            else:
                f=open("hamadex.txt")
                print(f.read())
                f.close
        else:
            print("Please enter the correct name")
