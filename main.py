import argparse
import json
import os
import sys
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def next_id(expenses):
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1


def add_expense(args):
    expenses = load_expenses()
    expense = {
        "id": next_id(expenses),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": args.description,
        "amount": args.amount,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense['id']})")


def update_expense(args):
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == args.id:
            if args.description is not None:
                expense["description"] = args.description
            if args.amount is not None:
                expense["amount"] = args.amount
            save_expenses(expenses)
            print(f"Expense (ID: {args.id}) updated successfully")
            return
    print(f"Error: No expense found with ID {args.id}")
    sys.exit(1)


def delete_expense(args):
    expenses = load_expenses()
    filtered = [e for e in expenses if e["id"] != args.id]
    if len(filtered) == len(expenses):
        print(f"Error: No expense found with ID {args.id}")
        sys.exit(1)
    save_expenses(filtered)
    print(f"Expense (ID: {args.id}) deleted successfully")


def list_expenses(args):
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'ID':<5}{'Date':<12}{'Description':<20}{'Amount':>10}")
    for expense in expenses:
        print(
            f"{expense['id']:<5}{expense['date']:<12}"
            f"{expense['description']:<20}${expense['amount']:>9.2f}"
        )


def summary(args):
    expenses = load_expenses()
    if args.month is not None:
        expenses = [
            e for e in expenses
            if datetime.strptime(e["date"], "%Y-%m-%d").month == args.month
        ]
        label = f"for month {args.month}"
    else:
        label = "overall"

    total = sum(e["amount"] for e in expenses)
    print(f"Total expenses {label}: ${total:.2f}")


def build_parser():
    parser = argparse.ArgumentParser(prog="main.py", description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)
    add_parser.set_defaults(func=add_expense)

    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", required=True, type=int)
    update_parser.add_argument("--description", default=None)
    update_parser.add_argument("--amount", default=None, type=float)
    update_parser.set_defaults(func=update_expense)

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int)
    delete_parser.set_defaults(func=delete_expense)

    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.set_defaults(func=list_expenses)

    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", default=None, type=int, choices=range(1, 13))
    summary_parser.set_defaults(func=summary)

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)