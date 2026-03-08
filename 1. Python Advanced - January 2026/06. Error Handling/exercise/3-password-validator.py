class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


SPECIAL_CHARS = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    has_digit = any(ch.isdigit() for ch in password)
    has_letter = any(ch.isalpha() for ch in password)
    has_special = any(ch in SPECIAL_CHARS for ch in password)

    if not has_special:
        raise PasswordNoSpecialCharactersError(
            "Password must contain at least 1 special character"
        )

    if (has_digit and not has_letter and not has_special) or \
       (has_letter and not has_digit and not has_special) or \
       (has_special and not has_digit and not has_letter):
        raise PasswordTooCommonError(
            "Password must be a combination of digits, letters, and special characters"
        )

    print("Password is valid")