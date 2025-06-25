from typing import List, Dict

students: List[Dict[str, str | List[int]]] = [
    {"name": "Ali", "scores": [78, 65, 90]},
    {"name": "Vali", "scores": [55, 40, 60]},
    {"name": "Lola", "scores": [95, 92, 98]}
]

def add_student(name: str, scores: List[int]) -> None:
    """
    Yangi studentni ro'yxatga qo'shadi.
    :param name: Talabaning ismi
    :param scores: Baholar ro'yxati
    """
    students.append({"name": name, "scores": scores})
