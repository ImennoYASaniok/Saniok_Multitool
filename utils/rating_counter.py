# РУССКИЙ
# 4 2 2 3 3 4 3 3 3 4 4 4 4 4 4 4 3 3

# ВИС
# 5 5 5 5 5
# Если 3 за работу - 5 5 5 5 5 3
# Если 3*2 за работу - 5 5 5 5 5 3 3

def count_oz(data, result_oz, delta_oz):
    data = data.copy()
    threshold = int(result_oz) - 1 + 0.5
    k = 0
    stop_k = 50
    while True:
        mid_val = sum(data) / len(data)
        if mid_val >= threshold: return k, mid_val
        if k > stop_k: return f"слишком много оценок (более {stop_k})", "-"
        data.append(delta_oz)
        k += 1

print("Оценки")
data = list(map(int, input().split()))
print("Средний балл сейчас:", sum(data) / len(data))
print("Сейчас пятёрок:", data.count(5))
print("Сейчас четвёрок:", data.count(4))
print("Сейчас троек:", data.count(3))
print("Сейчас двоек:", data.count(2))
k_4_4, mid_4_4 = count_oz(data, 4, 4)
k_4_5, mid_4_5 = count_oz(data, 4, 5)
print("На четыре (3.5) нужно четвёрок:", k_4_4, "| Средний балл будет:", mid_4_4)
print("На четыре (3.5) нужно пятёрок:", k_4_5, "| Средний балл будет:", mid_4_5)
k_5_5, mid_5_5 = count_oz(data, 5, 5)
print("На пять (4.5) нужно пятёрок:", k_5_5, "| Средний балл будет:", mid_5_5)