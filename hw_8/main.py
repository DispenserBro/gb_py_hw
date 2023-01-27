from controllers import user_interface

def run():
    decision = ''

    while not decision:
        user_interface()

        decision = input('Для продолжения нажмите ENTER. Для завершения напишите что-нибудь: ')

if __name__ == '__main__':
    run()