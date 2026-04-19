# Validate passwords against rules: (1) at least 1 lowercase letter [a-z], (2) at least 1 digit [0-9], (3) at least 1 uppercase letter [A-Z], (4) at least 1 special character [$#@], (5) length between 6 and 12, (6) no whitespace. Print valid passwords.

password = "Delta123"

has_lower = False
has_upper = False
has_digit = False
has_special = False

special_chars = "$#@"

if 6 <= len(password) <=12 and " " not in password:
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
        
    if has_lower and has_upper and has_digit and has_special:
        print("Valid Password")
    else:
        print("Invalid Password")

else:
    print("Invalid Password")

        

                
    