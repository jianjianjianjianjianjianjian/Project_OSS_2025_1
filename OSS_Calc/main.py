from langcalc import parse_expression, calculate_expression

def show_guide():
    print("=======================================")
    print("자연어 계산기 사용법 (예시 입력 문장)")
    print("---------------------------------------")
    print("  - 3 더하기 7")
    print("  - 15 빼기 5")
    print("  - 2 곱하기 6")
    print("  - 10 나누기 2")
    print("  - 2의 5제곱")
    print("  - 9의 제곱")
    print("  - 루트 16")
    print("  - 17 나머지 3")
    print("  - 17 몫 3")
    print("종료하려면 'exit' 또는 'quit' 입력")
    print("=======================================\n")

def main():
    show_guide()
    while True:
        text = input("수식을 입력하세요 > ")
        if text.lower() in ("exit", "quit"):
            break

        expr = parse_expression(text)
        result = calculate_expression(expr)

        if result is not None:
            print(f"계산 결과: {result}\n")
        else:
            print("수식을 이해하지 못했습니다. 다시 입력해주세요.\n")


if __name__ == "__main__":
    main()
