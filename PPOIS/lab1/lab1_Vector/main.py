from Vector import Vector
import math

def get_vector_input(name):
    print(f"Введите координаты для {name}:")
    begin = []
    end = []
    for coord in ['x', 'y', 'z']:
        begin.append(float(input(f"Начало, {coord}-координата: ")))
    for coord in ['x', 'y', 'z']:
        end.append(float(input(f"Конец, {coord}-координата: ")))
    return Vector(end, begin)

def get_scalar_input():
    return float(input("Введите скалярное значение: "))

def get_vector_order():
    order = input("Выберите порядок (1: Вектор 1 - Вектор 2, 2: Вектор 2 - Вектор 1): ")
    return order

def main():
    print("Введите первый вектор:")
    v1 = get_vector_input("вектора 1")
    print("Введите второй вектор:")
    v2 = get_vector_input("вектора 2")
    
    while True:
        print("\nДоступные операции:")
        print("1. Вывести вектора")
        print("2. Сложить два вектора")
        print("3. Вычесть два вектора")
        print("4. Скалярное произведение двух векторов")
        print("5. Умножить первый вектор на скаляр")
        print("6. Разделить первый вектор на скаляр")
        print("7. Вычислить угол между векторами (косинус)")
        print("8. Сравнить длины векторов")
        print("9. Вычислить длину первого вектора")
        print("10. Присваивающее вычитание первому вектору")
        print("11. Присваивающее деление первому вектору")
        print("0. Выход")
        
        choice = input("\nВведите ваш выбор (0-11): ")
        
        if choice == '0':
            break
            
        elif choice == '1':
            print(f"Вектор 1: {v1}")
            print(f"Вектор 2: {v2}")
                
        elif choice == '2':
            result = v1 + v2
            print(f"Результат сложения: {result}")
                    
        elif choice == '3':
            order = get_vector_order()
            if order == '1':
                result = v1 - v2
            else:
                result = v2 - v1
            print(f"Результат вычитания: {result}")
                    
        elif choice == '4':
            result = v1 * v2
            print(f"Скалярное произведение: {result}")
                    
        elif choice == '5':
            scalar = get_scalar_input()
            result = v1 * scalar
            print(f"Результат умножения на скаляр: {result}")
                    
        elif choice == '6':
            scalar = get_scalar_input()
            result = v1 / scalar
            print(f"Результат деления на скаляр: {result}")
                        
        elif choice == '7':
            cos_angle = v1 ^ v2
            angle = math.degrees(math.acos(cos_angle))
            print(f"Косинус угла между векторами: {cos_angle:.4f}")
            print(f"Угол между векторами: {angle:.2f} градусов")
                        
        elif choice == '8':
            print(f"Вектор 1 > Вектор 2: {v1 > v2}")
            print(f"Вектор 1 >= Вектор 2: {v1 >= v2}")
            print(f"Вектор 1 < Вектор 2: {v1 < v2}")
            print(f"Вектор 1 <= Вектор 2: {v1 <= v2}")
                    
        elif choice == '9':
            length = v1.calcLen()
            print(f"Длина первого вектора: {length:.4f}")
                    
        elif choice == '10':
            order = get_vector_order()
            if order == '1':
                v1 -= v2
            else:
                v1 -= v2
                v1 = -v1
            print(f"Новый вектор 1 после присваивающего вычитания: {v1}")
                    
        elif choice == '11':
            scalar = get_scalar_input()
            v1 /= scalar
            print(f"Новый вектор 1 после присваивающего деления: {v1}")

if __name__ == "__main__":
    main()