import json
import re


def remove_extra_curly_bracket(string):
    return string[:-1]


def remove_data_field(string):
    return string.split('data": ')[1]


def remove_nones(string):
    return string.replace("None", '""')


def remove_rn(string):
    return re.sub(r"\r*\n\r*", "", string)


def remove_before_curly_bracket(string):
    return re.split("^[^{]*{", string)[1]


def remove_after_curly_bracket(string):
    pre_cleaned = string.rsplit("}", 1)[0]
    return pre_cleaned.replace(" ", "")


def clean_string(string):
    cleaned = remove_data_field(string)
    cleaned = remove_rn(cleaned)
    cleaned = remove_extra_curly_bracket(cleaned)

    if "None" in cleaned:
        cleaned = remove_nones(cleaned)

    if cleaned[0] != "{":
        cleaned = "{" + remove_before_curly_bracket(cleaned)

    if cleaned[-1] != "}":
        cleaned = remove_after_curly_bracket(cleaned) + "}"

    return cleaned
