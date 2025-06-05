from budget import Budget
from json_loader import load_expenses_from_json

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. JSON으로 지출 불러오기")
        print("5. 지출 내역을 날짜 순으로 JSON 파일로 저장")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
            
        elif choice == "4":
            path = input("불러올 JSON 파일 경로 입력 > ").strip('"')
            new_expenses = load_expenses_from_json(path, budget.expenses)
            budget.expenses += new_expenses
            budget.expenses.sort(key=lambda e: e.date)
            print(f"{len(new_expenses)}개의 지출 내역이 추가되었습니다.\n")
            # sample data 경로: OSS_Budget\unsorted_data.json
            
        elif choice == "5":
            from json_saver import save_expenses_to_json_with_summary
            path = input("요약 포함 JSON 경로 입력 > ").strip('"')
            save_expenses_to_json_with_summary(budget.expenses, path)
            # 예시 경로: OSS_Budget\result.json

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
