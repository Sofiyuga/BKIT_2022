from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pandas as pd


def main():
    r = Rectangle("синего", 20, 10)
    c = Circle("зеленого", 20)
    s = Square("красного", 20)
    print(r)
    print(c)
    print(s)


    d = { 'Фигура': ['Ромб', 'Трапеция', 'Овал', 'Параллелограмм'], 'Цвет': ['Коричневый', 'Желтый', 'Розовый', 'Черный'] } 
    df1 = pd.DataFrame(d, columns=['Фигура', 'Цвет']) 
    print(df1)


if __name__ == "__main__":
    main()