from classes.exceptions import BadAuthException
import dao.auth_dao as ad

def validate_session(token):
    """validates token"""
    if token is None:
        raise ValueError("Missing Header: Authorization")
    elif isinstance(token, str):
        return ad.validate_token(token)
    else:
        raise BadAuthException