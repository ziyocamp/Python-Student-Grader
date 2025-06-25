def print_result(student: dict[str, str | float | bool]) -> None:
    """
    Student haqida natijani chiroyli chiqaradi.
    :param student: Natijalar saqlangan dict
    """
    status = "✅ Pass" if student["passed"] else "❌ Fail"
    print(f"{student['name']}: Avg = {student['average']:.2f}, Grade = {student['grade']}, {status}")

def print_sorted_by_average(students: list[dict[str, str | float | bool]]) -> None:
    """
    Studentlarni o'rtacha baho bo'yicha kamayish tartibida chiqaradi.
    :param students: Natijalar ro'yxati
    """
    for s in sorted(students, key=lambda x: x["average"], reverse=True):
        print_result(s)
