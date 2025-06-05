from budget import Budget
from json_loader import load_expenses_from_json

def main():
    budget = Budget()

    while True:
        display_main_menu()
        choice = input("선택 > ")

        if choice == "1":
            handle_add_expense(budget)
        elif choice == "2":
            budget.list_expenses()
        elif choice == "3":
            budget.total_spent()
        elif choice == "4":
            display_badges(budget)
        elif choice == "5":
            print("가계부를 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.\n")


def display_main_menu():
    print("==== 간단 가계부 ====")
    print("1. 지출 추가")
    print("2. 지출 목록 보기")
    print("3. 총 지출 보기")
    print("4. 배지 보기")
    print("5. 종료")


def handle_add_expense(budget):
    print("1. 직접 입력")
    print("2. JSON 파일에서 불러오기")
    sub_choice = input("선택 > ")

    if sub_choice == "1":
        add_expense_manually(budget)
    elif sub_choice == "2":
        add_expense_from_json(budget)
        # OSS_Budget\example_budget.json
    else:
        print("잘못된 선택입니다.\n")


def add_expense_manually(budget):
    category = input("카테고리 (예: 식비, 교통 등): ")
    description = input("설명: ")
    try:
        amount = int(input("금액(원): "))
    except ValueError:
        print("잘못된 금액입니다.\n")
        return
    budget.add_expense(category, description, amount)


def add_expense_from_json(budget):
    path = input("불러올 JSON 파일 경로 입력 > ").strip('"')
    from json_loader import load_expenses_from_json
    new_expenses = load_expenses_from_json(path)
    for e in new_expenses:
        budget.expenses.append(e)
    print(f"{len(new_expenses)}개의 지출 내역이 추가되었습니다.\n")


def display_badges(budget):
    print("\n(・ω・)ノ  당신의 소비 모험 결과!")
    print("=====================================")

    budget.check_badges()
    level = budget.get_level()
    print("✨ 당신의 캐릭터")
    art = budget.get_character_art(level)
    print(art)

    badges = budget.check_badges()
    print(f"🎖 현재 레벨: Lv.{level}")
    print(f"🏅 보유한 배지 수: {len(badges)}개")
    print("📌 보유 배지 목록:")
    for b in badges:
        print(f" - {b}")
    print("")
    print(budget.get_category_ratio_text())
    print("=====================================\n")

if __name__ == "__main__":
    main()
