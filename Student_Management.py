
import  random

def display_student_data(data_container):
    for index,data in enumerate(data_container):
        print(f"name: {data['name']}\n"
              f"Email: {data['Email']}\n"
              f"Roll No: {data['student_roll']}\n"
              f"Student id: {data['id']}\n")

def validate_id(student_id ,data_container):
    for index,data in enumerate(data_container):
        print(data)
        if student_id==data['id']:
            return False
        return True



def update_student_data(data_container):
    temp_id=int(input("Please Enter the Student id: "))

    is_validated=validate_id(temp_id,data_container)
    if not is_validated:
        student_name = input("Enter the student Name: ")
        student_email = input("Enter the student Email")
        student_roll = input("Enter the Student Roll Number")
        student_dict = {
            "name": student_name,
            "email": student_email,
            "student_roll": student_roll,
            "id": temp_id
        }
        index=-1
        for index, data in enumerate(data_container):
            if data['id']==temp_id:
                index=index
                break

        data_container[index]=student_dict
        print("Student Data updated...")




def register_student(data_container):
    student_name =input("Enter the student Name: ")
    student_email =input("Enter the student Email")
    student_roll =input("Enter the Student Roll Number")
    student_id =random.randint(0,100)
    while True:
        is_validated=validate_id(student_id, data_container)
        if is_validated:
            break
    student_dict ={
        "name" :student_name,
        "email" :student_email,
        "student_roll" :student_roll,
        "id" :student_id
    }
    data_container.append(student_dict)
    print("Student Registered...")
    display_student_data(data_container)



def main():
    data_container =[]
    while True:
        print("1. Register Student\n"
              "2. Update Student\n"
              "3. Delete Student\n"
              "4.View All Student\n"
              "5. Exit To the Program\n")

        choice =int(input("Please Choose above Choice: "))

        if choice==1:
            print(".....Adding student......\n\n")
            register_student(data_container)
        elif choice==2:
            print("...Editing Student...\n\n")
            update_student_data(data_container)
        elif choice==3:
            print("Deleting the student")
        elif choice==4:
            print("view data")
        elif choice==5:
            break
        else:
            print("Invalid Choice Please Enter the Valid Choice")


if __name__ == '__main__':
    main()
