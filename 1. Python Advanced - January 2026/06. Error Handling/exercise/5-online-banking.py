class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, balance, age = input().split(", ")
pin_code = int(pin_code)
balance = float(balance)
age = int(age)

while True:
    command = input()
    if command == "End":
        break

    action, *parts = command.split("#")

    if action == "Send Money":
        money = float(parts[0])
        entered_pin = int(parts[1])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if entered_pin != pin_code:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError(
                "You must be 18 years or older to perform online transactions"
            )

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        money = float(parts[0])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += money / 2
        print(f"{money / 2:.2f} money went straight into the bank account")