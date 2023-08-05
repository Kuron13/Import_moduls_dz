from application.salary import *
from application.db.people import *
from datetime import *

from pymystem3 import *
m = Mystem()

def show_time():
    dt = datetime.today()
    d = datetime.date(dt)
    return d

def diction_form(text):
    '''Лемматизация. Разбивает предложение на слова по пробелу и приводит их к словарной форме'''
    text = text.lower()
    res = ''.join(m.lemmatize(text))
    return res

if __name__ == '__main__':
    print(f'Заработная плата составила {calculate_salary()} рублей.')
    print(f'Нужные сотрудники: {get_emloyees()}.')
    print(f'Сегодняшняя дата: {show_time()}')
    mess = 'Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном обучении (ML).'
    print(diction_form(mess))