def check_pwd(str):
    if len(str) < 8 or len(str) > 20:
        return False
    return True