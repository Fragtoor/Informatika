from math import factorial

def fact_ten(num):
    res = 0
    for i in range(len(num)):
        res += int(num[i]) * factorial(len(num) - i)
    return res


def ten_fact(num):
    """
    Более простая реализация преобразования в факториальную систему.
    """
    if num == 0:
        return "0"
    
    digits = []
    divisor = 1
    
    while num > 0:
        divisor += 1
        remainder = num % divisor
        digits.append(str(remainder))
        num //= divisor
    
    # Переворачиваем цифры (младшие разряды сначала)
    return ''.join(reversed(digits))


def fib_ten(num):
    """
    Переводит число в фибоначиевой СС в десятичное число
    """
    fib = [1, 2]
    for i in range(50):
        fib.append(fib[i] + fib[i+1])
    res = sum([int(num[i]) * fib[len(num) - i-1] for i in range(len(num))])
    return res


def ten_fib(num):
    """
    Переводит число из десятичной системы счисления в фибоначиеву
    """
    if num == 0:
        return "0"
    
    # Генерируем числа Фибоначчи, пока не превысим наше число
    fib = [1, 2]
    while fib[-1] <= num:
        n = fib[-1] + fib[-2]
        fib.append(n)
    
    fib = fib[:-1]
    
    remainder = num
    result_digits = []
    
    # Проходим от большего числа Фибоначчи к меньшему
    for fib in reversed(fib):
        if remainder >= fib:
            result_digits.append('1')
            remainder -= fib
        else:
            result_digits.append('0')
    
    # Убираем лидирующие нули
    result_str = ''.join(result_digits).lstrip('0')
    
    return result_str if result_str else "0"


def ten_begrman(num):
    """
    Переводит десятичное число в систему счисления Бергмана (на основе золотого сечения).
    """
    # Золотое сечение
    phi = (1 + 5**0.5) / 2
    
    # Определяем диапазон степеней
    max_power = 0
    while phi**max_power <= num:
        max_power += 1
    
    # Начинаем со старшей степени
    result_digits = []
    remainder = num
    
    # Обрабатываем целую часть (положительные степени)
    for power in range(max_power, -1, -1):
        current_value = phi**power
        
        if remainder >= current_value and (not result_digits or result_digits[-1] != '1'):
            result_digits.append('1')
            remainder -= current_value
        else:
            result_digits.append('0')
    
    # Добавляем точку для дробной части
    result_digits.append('.')
    
    # Обрабатываем дробную часть (отрицательные степени)
    for power in range(-1, -11, -1):
        current_value = phi**power
        
        if remainder >= current_value and result_digits[-1] != '1':
            result_digits.append('1')
            remainder -= current_value
        else:
            result_digits.append('0')
        
        if abs(remainder) < 1e-10:  # Малая величина для остановки
            break
    
    # Форматируем результат
    bergman_str = ''.join(result_digits)
    
    # Убираем лидирующие нули и лишние хвостовые нули
    bergman_str = bergman_str.rstrip('0').rstrip('.')
    if bergman_str.startswith('.'):
        bergman_str = '0' + bergman_str
    
    return float(bergman_str)


def bergman_ten(num):
    """
    Конвертирует число из системы счисления Бергмана в десятичную систему.
    """
    phi = (1 + 5**0.5) / 2
    
    # Разделяем на целую и дробную части
    if '.' in num:
        integer_part, fractional_part = num.split('.')
    else:
        integer_part, fractional_part = num, ''
    
    result = 0.0
    
    # Обрабатываем целую часть (положительные степени)
    for i, digit in enumerate(integer_part):
        power = len(integer_part) - i - 1  # Степень уменьшается слева направо
        if digit == '1':
            result += phi ** power
    
    # Обрабатываем дробную часть (отрицательные степени φ)
    for i, digit in enumerate(fractional_part):
        power = -(i + 1)  # Степени: -1, -2, -3, ...
        if digit == '1':
            result += phi ** power
    
    return round(result)

 
def ten_CC(num, cc1):
    res = ''
    ost = '0123456789ABCDEF'
    num2int = int(str(float(str(num))).split('.')[0])
    num2float = float('0.' + str(float(str(num))).split('.')[1])
    while num2int > 0:
        res += str(ost[num2int % cc2])
        num2int //= cc2
    res2 = ''
    ind = 0 # с точнотью до 10 знаков после запятой
    while ind < 10 and num2float:
        num2float *= cc2
        res2 += ost[int(num2float)]
        num2float = num2float - int(num2float)
        ind += 1
    if res == '':
        res = '0'
    if res2 == '':
        res2 = '0'

    if '-' in str(num):
        return -(res[::-1] + "." + res2)
    return float(res[::-1] + "." + res2)


def CC_ten(num, cc1):
    """Переводит число из одной позиционной в десятичную"""
    num1 = num
    if '.' not in num1:
        num1 += '.0'
    if '-' in num:
        num1 = num[1:]
    int_num1 = num1[:num1.index('.')]
    float_num1 = num1[num1.index('.') + 1:]
    num2int = sum([int(int_num1[i], cc1) * (cc1 ** (len(int_num1) - i - 1)) for i in range(len(int_num1))])
    num2float = sum([int(float_num1[i], cc1) * (cc1 ** (-i - 1)) for i in range(len(float_num1))])
    # num2 - десятичная запись num
    num2 = int(num2int) + num2float
    return float(str(num2))


def is_number(s):
    try:
        float(s)  # Пробуем преобразовать в float
        return True
    except ValueError:
        return False

def is_integer(s):
    try:
        int(s)  # Пробуем преобразовать в int
        return True
    except ValueError:
        return False

def check_number_type(s):
    if is_integer(s):
        return "Целое число"
    elif is_number(s):
        return "Дробное число"
    else:
        return "Не число"
    
def identify_CC(cc):
    """Определяет, какую CC ввёл пользователь"""
    result = None
    if cc == "1":
        try:
            result = int(input("Какое значение системы счисления?(Введите число) "))
            if result <= 1:
                raise ValueError
        except:
            ...
    elif cc == "2":
        result = 'Б'
    elif cc == "3":
        result= 'Ц'
    elif cc == "4":
        result= 'Ф'
    if result is None:
        return None
    return result



number = input("Введите число: ")
# if check_number_type(number) == "Не число":
#     print("Нужно вводить целое и дробное число")
#     exit()
print(
"""
Доступные CC: 
1) 2 <= натуральное число <= 16
2) Б (СС Бергмана)
3) Ц (СС Цекендорфа)
4) Ф (Факториальная СС)
""")
cc1 = identify_CC(input("Введите номер, указывающий на вид СС числа (от 1 до 4): "))
if cc1 is None:
    exit()
cc2 = identify_CC(input("Введите номер, указывающий на вид СС, в которую хотите перевести число (от 1 до 4): "))
if cc2 is None:
    exit()
if cc1 == cc2:
    print("Нужно вводить разные СС")
    exit()


# число в cc1
N1 = None
N2 = None
if str(cc1) in '2345678910111213141516':
    N1 = CC_ten(number, cc1)
elif cc1 == 'Б':
    N1 = bergman_ten(number)
elif cc1 == 'Ц':
    N1 = fib_ten(number)
elif cc1 == 'Ф':
    N1 = fact_ten(number)


if str(cc2) in '2345678910111213141516':
    N2 = ten_CC(N1, cc2)
elif cc2 == 'Б':
    N2 = ten_begrman(N1)
elif cc2 == 'Ц':
    N2 = ten_fib(N1)
elif cc2 == 'Ф':
    N2 = ten_fact(N1)

print(f'{number} ({cc1})-> {N2} ({cc2})')
