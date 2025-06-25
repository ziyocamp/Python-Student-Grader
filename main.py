from data.students import students, add_student
from grader.average import calculate_average
from grader.rules import is_passed, get_letter_grade
from utils.printer import print_sorted_by_average


def main() -> None:
    """
    Bosh funksiyani ishga tushiradi:
    - Talabalarni ro'yxatga qo'shadi (ixtiyoriy)
    - O'rtacha baho hisoblaydi
    - Pass/fail va grade belgilaydi
    - Natijalarni saralab chiqaradi
    """
    add_student("Diyorbek", [90, 88, 92])

    results: list[dict[str, str | float | bool]] = []
    for student in students:
        avg: float = calculate_average(student["scores"])
        results.append({
            "name": student["name"],
            "average": avg,
            "passed": is_passed(avg),
            "grade": get_letter_grade(avg)
        })

    print_sorted_by_average(results)

if __name__ == "__main__":
    main()
