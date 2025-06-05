import json
from collections import defaultdict
from datetime import datetime

def save_expenses_to_json_with_summary(expenses, path):
    try:
        sorted_expenses = sorted(expenses, key=lambda e: e.date)

        total = 0
        count = 0
        category_summary = defaultdict(int)
        month_summary = defaultdict(int)
        max_expense = None
        min_expense = None
        expense_list = []

        for e in sorted_expenses:
            total += e.amount
            count += 1
            category_summary[e.category] += e.amount

            # 월별 요약
            month = e.date[:7]  # "YYYY-MM"
            month_summary[month] += e.amount

            # 최대/최소 지출
            if max_expense is None or e.amount > max_expense.amount:
                max_expense = e
            if min_expense is None or e.amount < min_expense.amount:
                min_expense = e

            expense_list.append({
                "date": e.date,
                "category": e.category,
                "description": e.description,
                "amount": e.amount
            })

        summary = {
            "total": total,
            "count": count,
            "average": round(total / count, 2) if count else 0,
            "max": {
                "amount": max_expense.amount,
                "category": max_expense.category,
                "description": max_expense.description,
                "date": max_expense.date
            } if max_expense else None,
            "min": {
                "amount": min_expense.amount,
                "category": min_expense.category,
                "description": min_expense.description,
                "date": min_expense.date
            } if min_expense else None,
            "by_category": dict(category_summary),
            "by_category_sorted": dict(sorted(category_summary.items(), key=lambda x: -x[1])),
            "by_month": dict(month_summary)
        }

        result = {
            "summary": summary,
            "expenses": expense_list
        }

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"{count}개의 지출 내역이 요약과 함께 '{path}'에 저장되었습니다.\n")

    except Exception as e:
        print(f"[오류] 저장 실패: {e}")
