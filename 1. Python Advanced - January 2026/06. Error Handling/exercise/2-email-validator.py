class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = (".com", ".bg", ".org", ".net")

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_part = email.split("@", 1)

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not email.endswith(VALID_DOMAINS):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")