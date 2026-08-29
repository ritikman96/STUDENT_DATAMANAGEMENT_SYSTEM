import pandas as pd


# ---creating  intial student data----
students={
    "ID": [101, 102, 103, 104, 105],
    "NAME":["Max", "Messi", "Albert", "Fernandes", "Chris"],
    "AGE":[18, 19, 19, 22, 21],
    "COURSE": [ "AI", "CSE", "DS", "PHY", "CHE"],
    "MARKS": [87, 98, 84, 82, 90]
}
#---PYTHON DICTIONARY IS CREATED AND IT WILL CONVERTED IN PANDAS DATAFRAME
df=pd.DataFrame(students)
def add_student(sid,name,age,course,marks):
    global df
    
    
    if sid in df["ID"].values:
        return False,"student id already exits"
    
    new_student=pd.DataFrame({
        "ID":[sid],
        "NAME":[name],
        "AGE":[age],
        "COURSE":[course],
        "MARKS":[marks]
     })
        
    df=pd.concat([df,new_student],ignore_index=True)
    return True,"student Added Sucessfully"
    
    

        
#search student function
def search_Student():
    global df
    sid=int(input("enter the student ID \n"))
    
    
#making new tempory data  location
    student = df[df["ID"]== sid]
    #student=new_df.query("ID"==@sid) @ outside () for commands
    
    #adding error function if data is not there
    if student.empty:
        print("no data found")
        
    else:
        print(student)

#-----update the data of student----
def update_student():
    global df 
    #data frame was created outside the function are called global data frames
    
    sid= int(input("enter the id of student\n"))
    
    if sid not in df["ID"].values:
    #.values are use to convert in numpy array
     print("student not found ")
     return #immediately exit if not found not further loop
    name=input("Enter new name:")
    age=int(input("enter the age:"))
    course=(input("enter the course:"))
    marks=int((input("enter the marks:")))
    
    df.loc[df["ID"]==sid, "NAME"]=name
    df.loc[df["ID"]==sid, "AGE"]=age
    df.loc[df["ID"]==sid, "COURSE"]=course
    df.loc[df["ID"]==sid, "MARKS"]=marks
    
    return True,"student updated successfully"
   # print(df)
    
def delete_student():
    global df
    sid=int(input("enter the id want to delete: "))
    
    if sid not in df["ID"].values:
        print("not found")
        return
    df=df[df["ID"]!= sid]
    print("student deleted sucessfully")
    print(df)
    
def top_students():
    result=df.sort_values("MARKS", ascending=True)
    print(result.head(3))
    
    #ascending= highest to lowest
    #descending=lowest to highest
    
    
def average_marks():
    average= df["MARKS"].mean()
    print("Average marks is :",average)
    
def top_scorer():
    studentt=df.loc[df["MARKS"].idxmax()]
    print(studentt)
    
def search_course():
    course=input("Enter the name of the course")
    result=df.loc[df["COURSE"].str.upper()==course.upper()]
    
    if result.empty:
        print("student not found")
    else:
        print(result)
 
def main():   
    while True:
        print("........#>.......STUDENT MANGEMENT SYSTEM......#<....!")
        print("1.Display students")
        print("2.Search student")
        print("3.add students")
        print("4.Update student")
        print("5.Delete student")
        print("6.top students")
        print("7.average marks")
        print("7.EXIT")
    
        choice=input("enter the choice")
    
        if choice=="1":
         print(df) 
    
        elif choice=="2":
         search_Student()
         
        elif choice=="3":
         add_student()
        
        elif choice=="4":
         update_student()
        
        elif choice=="5":
         delete_student()
        
        elif choice=="6":
         top_scorer()
        
        elif choice=="7":
         average_marks()
        
        elif choice=="8":
         print("program ended")
         break
    
        else: print("invalid choice")
        
        

if __name__=="__main__":
    main()
    
    
    


       
       