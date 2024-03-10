import random

def binary_search_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_num = 1
    max_num = 100

    while min_num <= max_num:
        count += 1
        predict_number = (min_num + max_num) // 2  # предполагаемое число
        
        if predict_number == number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            min_num = predict_number + 1
        else:
            max_num = predict_number - 1
            
    return count


def score_game(binary_search_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = [random.randint(1, 100) for _ in range(1000)]  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search_predict(number))

    score = int(sum(count_ls) / len(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search_predict)






