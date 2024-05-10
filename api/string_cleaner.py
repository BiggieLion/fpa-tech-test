import json
import re


def remove_extra_curly_bracket(string):
    print("In remove extra curly bracket")
    return string[:-1]


def remove_data_field(string):
    print("In remove data field")
    return string.split('data": ')[1]


def remove_nones(string):
    print("In remove Nones")
    return string.replace("None", '""')


def remove_rn(string):
    print("In remove RNs")
    return re.sub(r"\r*\n\r*", "", string)


def remove_before_curly_bracket(string):
    print("In remove before curly bracket")
    return re.split("^[^{]*{", string)[1]


def remove_after_curly_bracket(string):
    print("In remove after curly bracket")
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
