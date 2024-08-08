first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


##########################################################################################

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for i in data_set:
                file.write(f'{i}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


###########################################################################################

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        import random as ch
        return ch.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Примерно')

print(first_ball())
print(first_ball())
print(first_ball())
