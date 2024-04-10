from classes.exceptions import BadAuthException

def validate_session(token):
    """validates token"""
    if token is None:
        raise ValueError("Missing Header: Authorization")
    elif token == "token":
        return True
    else:
        raise BadAuthException