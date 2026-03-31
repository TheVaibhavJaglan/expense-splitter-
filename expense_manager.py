import json

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"expenses": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(payer, amount, participants):
    data = load_data()

    expense = {
        "payer": payer,
        "amount": amount,
        "participants": participants
    }

    data["expenses"].append(expense)
    save_data(data)

    print("Expense added successfully!")

def show_balances():
    data = load_data()
    balances = {}

    for exp in data["expenses"]:
        split_amount = exp["amount"] / len(exp["participants"])

        for person in exp["participants"]:
            balances[person] = balances.get(person, 0) - split_amount

        balances[exp["payer"]] += exp["amount"]

    print("\nBalances:")
    for person, balance in balances.items():
        print(f"{person}: {round(balance,2)}")
