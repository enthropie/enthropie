"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np



def double_split_predict(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    
    Алгоритм угадывает число методом половинного деления интервала
    
    """
    count = 0
    minValue = 0
    maxValue = 101
    current_try = 0

    
    while True:
       
        count += 1
        
        if number == current_try:
            break  # выход из цикла если угадали
        elif number > current_try:
            minValue = current_try
            current_try = current_try + round((maxValue - minValue) * 0.5, 0)
        else:
            maxValue = current_try
            current_try = current_try - round((maxValue - minValue) * 0.5, 0)
    return count

def score_game(double_split_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        double_split_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

        
        
    for number in random_array:
        count_ls.append(double_split_predict(number))
        

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(double_split_predict)

