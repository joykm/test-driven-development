import re

def check_pwd(str):

    pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)" + "(?=.*[-~`!@#$%^&*()_+=]).+$")

    if (len(str) < 8 or len(str) > 20) or not re.search(pattern, str):
        return False

    return True