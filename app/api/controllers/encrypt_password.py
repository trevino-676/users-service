"""
"""
import bcrypt


def encrypt_password(password):
    salt = bcrypt.gensalt()
    hash_passwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_passwd.decode("utf-8")


def check_password(password, hash_passwd):
    return bcrypt.checkpw(password.encode("utf-8"), hash_passwd.encode("utf-8"))

