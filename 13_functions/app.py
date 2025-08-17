# System Info (Fixed)
SYSTEM_INFO = ("LMS Students Portal", "v1.0", "Edify University")
ADMIN_INFO = ("admin@edify.ai", "+91-9876543210", "201")

# Store Students Info
students = {}


# ---------------- Functions ----------------
def display_system_info():
    print("=" * 50)
    print(f"Welcome To {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
    print(f"Developed By {SYSTEM_INFO[2]} students")
    print("=" * 50)


def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student Already Exists")
        return

    name = input("Enter Student Name: ").strip().title()

    scores = []
    while True:
        score_input = input("Enter a score or type 'done': ").strip().lower()
        if score_input == "done":
            break
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Invalid Score, only 0-100 allowed")
        else:
            print("Invalid input, only numbers accepted")

    skills = set()
    while True:
        skill_input = input("Enter a skill or type 'done': ").strip().lower()
        if skill_input == "done":
            break
        if skill_input:
            skills.add(skill_input.title())

    students[student_id] = {"name": name, "scores": scores, "skills": skills}
    print(" Student Added Successfully")


def modify_student():
    student_id = input("Enter Student ID To Modify: ")
    if student_id in students:
        new_name = input("Enter New Name: ").strip().title()
        students[student_id]["name"] = new_name
        print("Student Updated Successfully")
    else:
        print("Student ID Not Found")


def delete_student():
    student_id = input("Enter Student ID To Delete: ")
    removed = students.pop(student_id, None)
    if removed:
        print(" Student Deleted Successfully")
    else:
        print(" Student ID Not Found")


def list_students():
    if not students:
        print(" No Students Available")
        return

    print("\n--- All Students Information ---")
    for sid, data in students.items():
        scores = data["scores"]
        avg = sum(scores) / len(scores) if scores else 0
        top_score = max(scores) if scores else 0

        print(f"ID: {sid}")
        print(f"Name: {data['name']}")
        print(f"Scores: {scores}")
        print(f"Average Score: {avg:.2f}")
        print(f"Top Score: {top_score}")
        print(f"Skills: {data['skills']}")
        print(f"Skills Count: {len(data['skills'])}")
        print("-" * 40)


def search_by_skill():
    skill_to_search = input("Enter Skill To Search: ").strip().title()
    # Lambda filter
    matched_students = list(
        filter(lambda s: skill_to_search in s[1]["skills"], students.items())
    )

    if matched_students:
        print("\n--- Students with skill:", skill_to_search, "---")
        for sid, data in matched_students:
            print(f"{sid} | {data['name']}")
    else:
        print(f"No students found with skill {skill_to_search}")


def exit_app():
    print("=" * 50)
    print("Contact Admin For Further Help")
    print(f"Mobile Number: {ADMIN_INFO[1]}")
    print(f"Email ID: {ADMIN_INFO[0]}")
    print("=" * 50)
    exit()


# ---------------- Main Program ----------------
def main():
    display_system_info()

    while True:
        print("\nChoose an option:")
        print("1 - Add Student")
        print("2 - Modify Student")
        print("3 - Delete Student")
        print("4 - List All Students")
        print("5 - Search By Skill")
        print("6 - Exit App")

        choice = input("Enter Your Choice (1-6): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            modify_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_students()
        elif choice == "5":
            search_by_skill()
        elif choice == "6":
            exit_app()
        else:
            print("Invalid Choice! Please select only (1-6)")


if __name__ == "__main__":
    main()
