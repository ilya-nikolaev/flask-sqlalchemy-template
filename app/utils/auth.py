import bcrypt


def get_password_hash(password: str):
    password_bytes = password.encode("UTF-8")

    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)

    return password_hash.decode("UTF-8")


def check_password(password: str, hashed: str):
    password_bytes = password.encode("UTF-8")
    hash_bytes = hashed.encode("UTF-8")

    return bcrypt.checkpw(password_bytes, hash_bytes)


def main():
    password = input("Password: ")
    print(get_password_hash(password))


if __name__ == '__main__':
    main()
