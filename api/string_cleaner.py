import json
import re


def remove_extra_curly_bracket(string):
    """
    This function removes the extra curly bracket at the end of the string

    Args:
        - string: The raw string to be cleaned from the text vars

    Returns:
        - string: The cleaned string

    Raises:
        - Internal Error: If the string does not have an extra curly bracket
    """
    return string[:-1]


def remove_data_field(string):
    """
    This function removes the data field from the string

    Args:
        - string: The raw string to be cleaned from the text vars

    Returns:
        - string: The cleaned string

    Raises:
        - Internal Error: If the string does not have a data field
    """
    return string.split('data": ')[1]


def remove_nones(string):
    """
    This function removes the None values from the string

    Args:
        - string: The raw string to be cleaned from the text vars

    Returns:
        - string: The cleaned string

    Raises:
        - Internal Error: If the string does not have a None value
    """
    return string.replace("None", '""')


def remove_rn(string):
    """
    This function removes the \r and \n from the string

    Args:
        - string: The raw string to be cleaned from the text vars

    Returns:
        - string: The cleaned string

    Raises:
        - Internal Error: If the string does not have a \r or \n
    """
    return re.sub(r"\r*\n\r*", "", string)


def remove_before_curly_bracket(string):
    """
    This function removes the text before the first curly bracket that is not the JSON Object

    Args:
        - string: The raw string to be cleaned from the text vars that is not the JSON Object

    Returns:
        - string: The cleaned string

    Raises:
        - None
    """
    return re.split("^[^{]*{", string)[1]


def remove_after_curly_bracket(string):
    """
    This function removes the text after the last curly bracket that is not the JSON Object

    Args:
        - string: The raw string to be cleaned from the text vars that is not the JSON Object

    Returns:
        - string: The cleaned string

    Raises:
        - None
    """
    pre_cleaned = string.rsplit("}", 1)[0]
    return pre_cleaned.replace(" ", "")


def clean_string(string):
    """
    This is the main function that cleans all the raw text to be parsed as a JSON Object

    Args:
        - string: The raw string to be cleaned from the text vars

    Returns:
        - string: The cleaned string

    Raises:
    """
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
