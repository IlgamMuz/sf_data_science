import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Zagadannoe chislo. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

def score_game(random_predict) -> int:
    """За какое количе

    Args:
        random_predict (_type_): _description_

    Returns:
        int: _description_
    """
    
    count_ls = []
    np.random.seed(2)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = (np.mean(count_ls))
    
    print(f'mean count of attempts: {score}')
    
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
