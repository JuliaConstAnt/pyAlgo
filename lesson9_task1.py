# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

def rabinkarp(string, pattern):
    if string == pattern or pattern == "":
        return 0
    n, m = len(string), len(pattern)
    print()
    cnt = 0
    hpattern = hash(pattern)
    for i in range(n-m+1):
        hs = hash(string[i:i+m])
        if hs == hpattern:
            if string[i:i+m] == pattern:
                cnt += 1
    return cnt


s1 = "Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке"

print(rabinkarp(s1, "строк"))    # 3
print(rabinkarp(s1, "вернуть"))  # 1
print(rabinkarp(s1, "лич"))      # 2
print(rabinkarp(s1, s1))         # 0
print(rabinkarp(s1, ""))         # 0
