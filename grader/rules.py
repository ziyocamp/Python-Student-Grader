def is_passed(average: float) -> bool:
    """
    Talaba imtihondan o'tganligini aniqlaydi.
    :param average: O'rtacha baho
    :return: True agar o‘tgan bo‘lsa
    """
    return average >= 60

def get_letter_grade(average: float) -> str:
    """
    O'rtacha bahoga qarab harfli baho beradi.
    :param average: O'rtacha baho
    :return: A, B, C yoki F
    """
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"
