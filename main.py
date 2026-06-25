class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total = sum(marks)
        self.percentage = (self.total / (len(marks) * 100)) * 100

    def get_grade(self):
        if self.percentage >= 90: return "A+"
        elif self.percentage >= 80: return "A"
        elif self.percentage >= 70: return "B"
        elif self.percentage >= 60: return "C"
        elif self.percentage >= 50: return "D"
        else: return "Fail"

def main():
    all_students = []
    num_subjects = 3  # You can change this number as needed
    
    while True:
        print(f"\n--- Entering Details for Student {len(all_students) + 1} ---")
        name = input("Enter student name: ")
        
        # Issue 1 Fix: Input Validation Loop
        while True:
            marks_input = input(f"Enter marks for {num_subjects} subjects (separated by space): ")
            marks = [int(m) for m in marks_input.split()]
            
            if len(marks) == num_subjects:
                break  # Exit validation loop if count is correct
            else:
                print(f"Error: You must enter exactly {num_subjects} marks. Please try again.")

        student_obj = Student(name, marks)
        all_students.append(student_obj)
        
        choice = input("\nDo you want to add another student? (y/n): ").lower()
        if choice != 'y':
            break 

    # Final Analysis Table
    print("\n" + "="*55)
    print(f"{'Name':<15} | {'Total':<8} | {'Percentage':<12} | {'Grade':<6}")
    print("-" * 55)
    
    total_class_percentage = 0
    for s in all_students:
        print(f"{s.name:<15} | {s.total:<8} | {s.percentage:>10.2f}% | {s.get_grade():<6}")
        total_class_percentage += s.percentage

    # Issue 2 Fix: Class Average Performance
    class_average = total_class_percentage / len(all_students)
    
    print("-" * 55)
    print(f"TOTAL STUDENTS: {len(all_students)}")
    print(f"CLASS AVERAGE:  {class_average:.2f}%")
    print("="*55)

if __name__ == "__main__":
    main()
