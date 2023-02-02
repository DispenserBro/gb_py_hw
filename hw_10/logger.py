from datetime import datetime
from os.path import exists, join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
COL_NAMES = ('Время', 'ID Пользователя', 'Пользователь', 'Ввод', 'Результат')


def log(user_id: str, username: str,
        data: str, result: str, 
        file_path: str = 'log') -> None:
    time = datetime.now()
    user_id = str(user_id)
    result = str(result)

    log_path = join(BASE_DIR, file_path + '.csv')

    if not exists(log_path):
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(', '.join(COL_NAMES) + '\n')

    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f'{time}, {user_id}, {username}, {data}, {result}\n')


def get_logs(file_path: str = 'log') -> list:
    log_path = join(BASE_DIR, file_path + '.csv')

    if not exists(log_path):
        return []

    with open(log_path, 'r', encoding='utf-8') as f:
        logs = f.readlines()

        for i in range(len(logs)):
            logs[i] = logs[i].strip('\n').split(', ')

    # print(logs)
    return logs


if __name__ == "__main__":
    log(1337, 'Dis_Bro', '12+1', 13)
    logs = get_logs()

    for el in logs[1:]:
        for i in range(len(el)):
            print(f'{logs[0][i]}: {el[i]}')
        print()