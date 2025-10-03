from Matrix import Matrix

def print_menu():
    print("\nМеню операций с матрицей:")
    print("1. Создать новую матрицу")
    print("2. Вывести матрицу")
    print("3. Загрузить матрицу из файла")
    print("4. Получить подматрицу")
    print("5. Транспонировать матрицу")
    print("6. Проверить свойства матрицы")
    print("7. Изменить размер матрицы")
    print("8. Префиксный инкремент")
    print("9. Постфиксный инкремент")
    print("10. Префиксный декремент")
    print("11. Постфиксный декремент")
    print("0. Выход")

def main():
    matrix = None
    while True:
        print_menu()
        choice = input("Введите ваш выбор (1-12): ")
        
        if choice == "1":
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            print("Введите элементы матрицы построчно:")
            data = []
            for i in range(rows):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                data.append(row)
            matrix = Matrix(rows, cols, data)
            print("Матрица создана.")

        elif choice == "2":
            if matrix:
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "3":
            filename = input("Введите имя файла: ")
            matrix = Matrix()
            matrix.load_from_file(filename)
            print("Матрица загружена из файла.")

        elif choice == "4":
            if matrix:
                start_row = int(input("Введите начальную строку: "))
                start_col = int(input("Введите начальный столбец: "))
                end_row = int(input("Введите конечную строку: "))
                end_col = int(input("Введите конечный столбец: "))
                submatrix = matrix.submatrix(start_row, start_col, end_row, end_col)
                print("Подматрица:")
                print(submatrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "5":
            if matrix:
                matrix.transpon()
                print("Матрица после транспонирования:")
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "6":
            if matrix:
                print("Свойства матрицы:")
                print(f"Квадратная: {matrix.is_square()}")
                print(f"Диагональная: {matrix.is_diagonal()}")
                print(f"Нулевая: {matrix.is_zero()}")
                print(f"Единичная: {matrix.is_identity()}")
                print(f"Симметричная: {matrix.is_symmetric()}")
                print(f"Верхняя треугольная: {matrix.is_upper_triangular()}")
                print(f"Нижняя треугольная: {matrix.is_lower_triangular()}")
            else:
                print("Матрица еще не создана.")

        elif choice == "7":
            if matrix:
                new_rows = int(input("Введите новое количество строк: "))
                new_cols = int(input("Введите новое количество столбцов: "))
                matrix.resize(new_rows, new_cols)
                print("Размер матрицы изменен.")
            else:
                print("Матрица еще не создана.")

        elif choice == "8":
            if matrix:
                matrix.__pre_inc()
                print("Матрица после префиксного инкремента:")
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "9":
            if matrix:
                result = matrix.__post_inc()
                print("Матрица до постфиксного инкремента (возвращена):")
                print(result)
                print("Матрица после постфиксного инкремента:")
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "10":
            if matrix:
                matrix.__pre_dec()
                print("Матрица после префиксного декремента:")
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "11":
            if matrix:
                result = matrix.__post_dec()
                print("Матрица до постфиксного декремента (возвращена):")
                print(result)
                print("Матрица после постфиксного декремента:")
                print(matrix)
            else:
                print("Матрица еще не создана.")

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()