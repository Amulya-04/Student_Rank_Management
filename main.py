import Student
q=[]
ch=1
while ch==1:
    print("1.Enter student details")
    print("2.Overall performence of a student")
    print("3.Ranking")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        Name=input("Enter name:")
        clas=input("Enter class:")
        Roll_no=int(input("Enter Roll_no:"))
        DOB=input("Enter DOB:")
        Phy_marks=int(input("Enter physics marks:"))
        Mat_marks=int(input("Enter maths marks:"))
        Che_marks=int(input("Enter chemistry marks:"))
        Comp_marks=int(input("Enter computer marks:"))
        A=Phy_marks+Mat_marks
        B=Che_marks+Comp_marks
        Total=A+B
        Average=Total/4
        Percentage=Total*100/400
        
        print("Name-",Name)
        print("Class-",clas)
        print("Roll_no-",Roll_no)
        print("Date Of Birth-",DOB)
        print("Physics marks-",Phy_marks)
        print("Maths marks-",Mat_marks)
        print("Chemistry marks-",Che_marks)
        print("Computer marks-",Comp_marks)
        print("Total-",Total)
        print("Average-",Average)
        print("Percentage-",Percentage)
        Student.save_student_details(Roll_no, Name, clas, DOB, Phy_marks, Mat_marks, Che_marks, Comp_marks, Total, Average, Percentage)
    elif choice==2:
        Roll_no=int(input("Enter Roll_no:"))
        Student.get_student_details(Roll_no)
    elif choice==3:
        Student.get_student_rank_list()
    elif choice==4:
        print("Thank you")
        ch=0
