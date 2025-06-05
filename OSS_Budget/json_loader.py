import json
from expense import Expense

def load_expenses_from_json(file_path):
    expenses = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            if all(k in item for k in ("date", "category", "description", "amount")):
                expense = Expense(
                    date=item["date"],
                    category=item["category"],
                    description=item["description"],
                    amount=item["amount"]
                )
                expenses.append(expense)
            else:
                print(f"[무시됨] 잘못된 항목: {item}")

    except Exception as e:
        print(f"[오류] JSON 불러오기 실패: {e}")

    return expenses
