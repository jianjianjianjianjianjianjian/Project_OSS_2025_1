import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def check_badges(self):
        badges = []

        total = sum(e.amount for e in self.expenses)
        if total == 0:
            return ["❌ 무소비 챌린저"]

        # 1. 투자 귀신
        if sum(1 for e in self.expenses if e.category == "투자") >= 5:
            badges.append("💎 투자 귀신")

        # 2. 먹보
        food_total = sum(e.amount for e in self.expenses if e.category == "식비")
        if food_total / total >= 0.3:
            badges.append("🍔 먹보")

        # 3. ALL IN
        if any(e.amount >= 500000 for e in self.expenses):
            badges.append("🔥 ALL IN")

        # 4. 소확행러
        small_cat = {"문화", "쇼핑", "기타"}
        if sum(1 for e in self.expenses if e.category in small_cat) >= 5:
            badges.append("🍰 소확행러")

        # 5. 절약왕
        if all(e.category != "현금" for e in self.expenses):
            badges.append("🥇 절약왕")

        # 6. 카드값 지옥
        if total >= 2000000:
            badges.append("💳 카드값 지옥")

        # 7. 고정지출 러버
        if sum(1 for e in self.expenses if e.category in {"예금", "적금"}) >= 2:
            badges.append("🧾 고정지출 러버")

        # 8. 한우먹은날
        if any(e.amount >= 50000 and e.category == "식비" for e in self.expenses):
            badges.append("🥩 한우먹은날")

        return badges
    
    def get_level(self):
        badges = self.check_badges()
        return len(badges) // 5 + 1

    def get_category_ratio_text(self):
        from collections import defaultdict

        category_totals = defaultdict(int)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount

        total = sum(category_totals.values())
        if total == 0:
            return "지출 내역이 없습니다."

        result = "[카테고리별 지출 비율]"
        for category, amount in sorted(category_totals.items(), key=lambda x: -x[1]):
            ratio = amount / total
            bar = "█" * int(ratio * 20)
            percent = round(ratio * 100)
            result += f"\n{category.ljust(10)}: {bar.ljust(20)} {percent}%"
        return result



    def get_character_art(self, level):
        if level == 1:
            return r"""
         (•‿•)
        /(   )\
         ^^ ^^
            """
        elif level == 2:
            return r"""
        \(•̀ᴗ•́)/
         (   )
        /|   |\
            """
        elif level == 3:
            return r"""
        ＼(°▽°)／
         <(   )>
          /| |\ 
            """
        elif level == 4:
            return r"""
         (ง •̀_•́)ง 
         /     \
        /|     |\
            """
        elif level >= 5:
            return r"""
        🏆(★‿★)🏆
           /█\ /█\
           / \ / \
            """
        else:
            return r"""
        (•_•)
            """