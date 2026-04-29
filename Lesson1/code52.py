def input_students():
    students = []
    n = int(input("Nhập số sinh viên: "))
    
    for i in range(n):
        name = input(f"Tên sinh viên {i+1}: ")
        score = float(input("Điểm: "))
        students.append({"name": name, "score": score})
    
    return students


def average_score(students):
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)


def top_student(students):
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top


def passed_students(students):
    result = []
    for s in students:
        if s["score"] >= 5:
            result.append(s)
    return result


# ===== MAIN =====
students = input_students()

print("\nĐiểm trung bình:", average_score(students))

top = top_student(students)
print("Sinh viên cao điểm nhất:", top["name"], "-", top["score"])

passed = passed_students(students)
print("\nDanh sách đậu:")
for s in passed:
    print(s["name"], "-", s["score"])