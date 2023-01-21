from controllers import user_interface

def run():
    """Основная функция для запуска программы.
    """
    decision = ''

    while not decision:
        user_interface()

        decision = input('Для продолжения нажмите ENTER. Для завершения напишите что-нибудь: ')

if __name__ == '__main__':
    run()