"""Module for filtering users from a JSON file."""

import json


def load_users():
    """Load and return users from the JSON file."""
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def print_users(users):
    """Print a list of users or a message if none found."""
    if not users:
        print("No users found.")
        return
    for user in users:
        print(user)


def filter_users_by_name(name):
    """Filter users by name (case-insensitive)."""
    users = load_users()
    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]
    print_users(filtered_users)


def filter_users_by_age(age):
    """Filter users by exact age."""
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    """Filter users by email (case-insensitive)."""
    users = load_users()
    filtered_users = [
        user for user in users
        if user["email"].lower() == email.lower()
    ]
    print_users(filtered_users)


def main():
    """Main function to handle user input and filtering."""
    filter_option = input(
        "What would you like to filter by? (name / age / email): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()