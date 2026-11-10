def validate_email(email):
    if email.lower() == "exit":
        return "exit"

    elif "@" not in email:
        return "Invalid email: Missing @ symbol."

    elif "." not in email:
        return "Invalid email: Missing domain extension."

    elif email.startswith("@") or email.endswith("."):
        return "Invalid email address."

    else:
        return "valid"


def slice_email(email):
    username = email.split("@")[0]

    domain_part = email.split("@")[1]
    domain = domain_part.split(".")[0]

    extension = domain_part.split(".")[-1]

    print("\n--- EMAIL DETAILS ---")
    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)


def main():
    while True:
        email = input("Enter your email address (or 'exit' to quit): ")

        result = validate_email(email)

        if result == "exit":
            print("Goodbye!")
            break

        elif result != "valid":
            print(result)

        else:
            slice_email(email)


main()