# json_loader.py
import json
from expense import Expense

def load_expenses_from_json(path, existing_expenses=None):
    expenses = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        existing_set = set()
        if existing_expenses:
            for e in existing_expenses:
                key = (e.date, e.category, e.description, e.amount)
                existing_set.add(key)

        for i, item in enumerate(data):
            try:
                date = item["date"]
                category = item["category"]
                description = item["description"]
                amount = int(item["amount"])
                key = (date, category, description, amount)

                if key in existing_set:
                    print(f"[중복] {i+1}번째 항목은 이미 존재하여 건너뜀")
                    continue

                expense = Expense(date, category, description, amount)
                expenses.append(expense)
                existing_set.add(key)
            except (KeyError, ValueError, TypeError) as e:
                print(f"[경고] {i+1}번째 항목 무시됨: {e}")
                continue

        # ✅ 날짜순 정렬 (불러오기 후)
        expenses.sort(key=lambda e: e.date)

    except Exception as e:
        print(f"오류 발생: {e}")
    
    return expenses
