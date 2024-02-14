import hashlib

def verify_password(input_password, stored_hashed_password, salt):
    salted_input_password = input_password + salt
    salted_input_password_bytes = salted_input_password.encode('utf-8')
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(salted_input_password_bytes)
    hashed_input_password = hash_algorithm.hexdigest()
    if hashed_input_password == stored_hashed_password:
        return True
    else:
        return False
stored_hashed_password = input("Enter the stored hashed password: ")
salt = input("Enter the salt used for encryption: ")

input_password = input("Enter the password to verify: ")

if verify_password(input_password, stored_hashed_password, salt):
    print("Password matches!")
else:
    print("Password does not match.")
