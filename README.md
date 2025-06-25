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

## ✅ Uyga vazifalar

1. `rules.py` faylini shunday o‘zgartiringki, agar bahosi `F` bo‘lsa, **yana test topshirishi kerak** degan ogohlantirish chop etilsin (`print_result()` funksiyasida).
2. `filter()` orqali faqat `Passed` bo‘lgan studentlar ro‘yxatini chiqaring.
3. `map()` orqali yangi ro‘yxat yarating: faqat `(name, grade)` juftliklari.

---

## 🎁 Bonus topshiriq:

`students.py` fayliga `load_students_from_json(filename)` funksiyasi qo‘shing. U JSON fayldan studentlar ro‘yxatini yuklaydi.
