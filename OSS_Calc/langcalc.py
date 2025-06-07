import re
from sympy import sympify, SympifyError, sqrt


def parse_expression(text):
    """문장에서 수식을 추출해 sympy가 이해할 수 있는 형태로 변환"""
    text = text.lower()

    # 문장형 연산 치환
    text = re.sub(r"(\d+)\s*의\s*제곱", r"(\1**2)", text)
    text = re.sub(r"(\d+)\s*의\s*세제곱", r"(\1**3)", text)
    text = re.sub(r"(\d+)\s*의\s*(\d+)\s*제곱", r"(\1**\2)", text)
    text = re.sub(r"루트\s*(\d+)", r"sqrt(\1)", text)

    # 일반 연산자 치환
    text = text.replace("더하기", "+")
    text = text.replace("빼기", "-")
    text = text.replace("곱하기", "*")
    text = text.replace("곱해", "*")
    text = text.replace("나누기", "/")
    text = text.replace("나눈", "/")
    text = text.replace("나눈값", "/")
    text = text.replace("제곱", "**2")
    text = text.replace("세제곱", "**3")
    text = text.replace("몫", "//")
    text = text.replace("나머지", "%")

    # 특수문자 제거
    text = re.sub(r"[^\d+\-*/().%sqrt]", "", text)

    return text


def calculate_expression(expr):
    """수식 계산 함수"""
    try:
        result = sympify(expr)
        return result.evalf()
    except (SympifyError, ZeroDivisionError):
        return None
