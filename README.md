## ✅ Loyiha: `student_grader` (classsiz, dictli, modulli)

### 🗂 Struktura:

```
Python-Student-Grader/                # 📁 Bosh loyiha papkasi
│
├── main.py                           # ▶️ Loyiha ishga tushadigan markaziy fayl
│                                     # Har bir student uchun average, grade, status chiqaradi
│
├── data/                             # 📁 Student ma'lumotlarini saqlovchi paket
│   ├── __init__.py                   # Bu papkani package sifatida belgilaydi (bo‘sh bo‘lishi mumkin)
│   └── students.py                   # students ro'yxati va add_student() funksiyasi shu yerda
│
├── grader/                           # 📁 Baholovchi funksiya va qoidalar uchun paket
│   ├── __init__.py                   # Bu papkani package sifatida belgilaydi
│   ├── average.py                    # calculate_average(scores) — o‘rtacha hisoblash
│   └── rules.py                      # is_passed(), get_letter_grade() — baholash qoidalari
│
└── utils/                            # 📁 Natijalarni chiroyli chiqarish uchun yordamchi funksiyalar
    ├── __init__.py                   # Bu papkani package sifatida belgilaydi
    └── printer.py                    # print_result(), print_sorted_by_average() — chop qilish
```

---

## 📄 Fayllar mazmuni:

### 1. `data/students.py`

```python
students = [
    {"name": "Ali", "scores": [78, 65, 90]},
    {"name": "Vali", "scores": [55, 40, 60]},
    {"name": "Lola", "scores": [95, 92, 98]}
]

def add_student(name, scores):
    students.append({"name": name, "scores": scores})
```

---

### 2. `grader/average.py`

```python
def calculate_average(scores):
    return sum(scores) / len(scores)
```

---

### 3. `grader/rules.py`

```python
def is_passed(average):
    return average >= 60

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"
```

---

### 4. `utils/printer.py`

```python
def print_result(student):
    status = "✅ Pass" if student["passed"] else "❌ Fail"
    print(f"{student['name']}: Avg = {student['average']:.2f}, Grade = {student['grade']}, {status}")

def print_sorted_by_average(students):
    for s in sorted(students, key=lambda x: x["average"], reverse=True):
        print_result(s)
```

---

### 5. `main.py`

```python
from data.students import students, add_student
from grader.average import calculate_average
from grader.rules import is_passed, get_letter_grade
from utils.printer import print_sorted_by_average

def main():
    add_student("Diyorbek", [90, 88, 92])

    results = []
    for student in students:
        avg = calculate_average(student["scores"])
        results.append({
            "name": student["name"],
            "average": avg,
            "passed": is_passed(avg),
            "grade": get_letter_grade(avg)
        })

    print_sorted_by_average(results)

if __name__ == "__main__":
    main()
```

---

## ✅ Uyga vazifalar

1. `rules.py` faylini shunday o‘zgartiringki, agar bahosi `F` bo‘lsa, **yana test topshirishi kerak** degan ogohlantirish chop etilsin (`print_result()` funksiyasida).
2. `filter()` orqali faqat `Passed` bo‘lgan studentlar ro‘yxatini chiqaring.
3. `map()` orqali yangi ro‘yxat yarating: faqat `(name, grade)` juftliklari.

---

## 🎁 Bonus topshiriq:

`students.py` fayliga `load_students_from_json(filename)` funksiyasi qo‘shing. U JSON fayldan studentlar ro‘yxatini yuklaydi.
