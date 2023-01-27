from db_scripts import get_disciplines_dict, get_students_dict


def search_discipline(name: str) -> tuple[bool, str]:
    disc_dict = get_disciplines_dict()

    if name.capitalize() in disc_dict.keys():

        return True, disc_dict[name.capitalize()]

    return False, ''


def search_student(discipline: str, stud_name: str) -> bool:
    stud_dict = get_students_dict(discipline)
    name_to_search = stud_name.capitalize()

    if name_to_search in stud_dict.keys():
        return True

    return False
