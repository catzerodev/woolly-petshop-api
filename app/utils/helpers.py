import bcrypt

def hash_password(pwd: str) -> str:
    bytes_pwd = pwd.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(bytes_pwd, salt)
    return hashed_pwd.decode("utf-8")


def verify_password(hashed_pwd: str, pwd: str) -> bool:
    bytes_hashed_pwd = hashed_pwd.encode("utf-8")
    bytes_pwd = pwd.encode("utf-8")
    return bcrypt.checkpw(bytes_pwd, bytes_hashed_pwd)