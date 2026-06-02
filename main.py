from Scripts.Crud_operation.crud_operation import (
    new_student_record,
    read_data,
    update_data,
    delete_item
)
from Scripts.Crud_operation.all_operation import All_operation
from decimal import Decimal
from Scripts.Crud_operation.AdvanceTask import AdvancedOperations
# from Scripts.Crud_operation.Secondary_index import SecondaryIndex
def main():
    while True:

        print("\n1. Insert")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        k = int(input("Enter your choice: "))

        if k == 1:

            id = int(input("Enter the id: "))
            weekly_hour = Decimal(input("Enter the study hour: "))
            att = Decimal(input("Enter the attendance percentage: "))
            clas = Decimal(input("Enter the class participation: "))
            total = Decimal(input("Enter the total score: "))
            gr = input("Enter the performance category: ")
            grade = input("Enter the grade: ")

            new_student_record(
                id,
                weekly_hour,
                att,
                clas,
                total,
                gr,
                grade
            )

        elif k == 2:

            id = int(input("Enter the id: "))
            read_data(id)

        elif k == 3:

            id = int(input("Enter the id: "))

            print("\n1. Weekly Study Hours")
            print("2. Attendance Percentage")
            print("3. Class Participation")
            print("4. Total Score")
            print("5. Grade")

            choice = int(input("Select field to update: "))

            if choice == 1:
                value = Decimal(input("Enter new study hours: "))
                update_data(id, "weekly_self_study_hours", value)

            elif choice == 2:
                value = Decimal(input("Enter new attendance percentage: "))
                update_data(id, "attendance_percentage", value)

            elif choice == 3:
                value = Decimal(input("Enter new class participation: "))
                update_data(id, "class_participation", value)

            elif choice == 4:
                value = Decimal(input("Enter new total score: "))
                update_data(id, "total_score", value)

            elif choice == 5:
                value = input("Enter new grade: ")
                update_data(id, "grade", value)

        elif k == 4:

            id = int(input("Enter the id: "))
            delete_item(id)

        else:
            print("Thank You!!!!!")
            break


    at=All_operation()
    print(at)
    at.Retrieve_based_on_attendance_percentage()
    at.Retrieve_based_on_weely_hour()
    at.Retrieve_based_on_performance()

    # sc=SecondaryIndex()
    # sc.top_students_grade_a()
    # sc.highest_scores()


    op = AdvancedOperations()
    op.student_risk_detection()
    op.top_performers()
    op.validate_json("data/student_data.json")
    op.check_duplicate_student(101)

if __name__=='__main__':
    main()