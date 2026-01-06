student= []
def add_student():
    name= input("name")
    marks= int (input("Marks"))
    grade = "Pass" if marks >= 50 else "Fail"

    student.append({"name":name,"marks":marks,"grade":grade})
    print("Successfuly added student detail")
    
def show_student():
    for s in student:
        print(f"{s['name']}|{s['marks']}|{s['grade']}")
        
def save_file():
        with open("student.txt",'w')as f:
            for s in student:
                f.write(f"{s['name']}|{s['marks']}|{s['grade']}")

                #menu 
while True:
        print("\n1.Add  2.View  3.Save  4.Exit")
        ch=input("Choice")
        
        if ch== "1":
                add_student()
        elif ch== "2":
                show_student()
        elif ch== "3":
                save_file()
        elif ch=="4":
           break
                
    
  

    