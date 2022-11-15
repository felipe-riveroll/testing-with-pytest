""" format_data.py"""


def format_data_for_display(people):
    """format_data_for_display(people)"""
    formated_list = []
    for person in people:
        formated_list.append(
            f"{person.get('given_name')} {person.get('family_name')}: {person.get('title')}"
        )
    return formated_list


def format_data_for_excel(people):
    """format_data_for_excel(people)"""
    head = "given,family,title"
    body = []
    for person in people:
        body.append(
            f"{person.get('given_name')},{person.get('family_name')},{person.get('title')}"
        )
    return f"{head}\n" + "\n".join(body)
