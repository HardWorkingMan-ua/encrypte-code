import os
import random
from colored import attr

# Функция для очистки экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для плавного градиента
def gradient_text(text, start_color, mid_color, end_color):
    gradient_colors = [start_color, mid_color, end_color]
    lines = text.split('\n')
    result = ""

    for line in lines:
        length = len(line)
        for i, char in enumerate(line):
            if i < length / 2:
                ratio = (i / (length / 2))  # Переход от start_color к mid_color
                color = [(gradient_colors[0][j] * (1 - ratio) + gradient_colors[1][j] * ratio) for j in range(3)]
            else:
                ratio = ((i - length / 2) / (length / 2))  # Переход от mid_color к end_color
                color = [(gradient_colors[1][j] * (1 - ratio) + gradient_colors[2][j] * ratio) for j in range(3)]
            
            red, green, blue = [int(c) for c in color]
            result += f'\033[38;2;{red};{green};{blue}m{char}{attr("reset")}'
        result += '\n'
    
    return result

# Мусорные символы
garbage_chars = '*":;!?@#₽_&-+()/%[]{}\\=°^¢$€£×÷•|`~' * 10  # Увеличенное количество мусорных символов

# Функция для добавления мусорных символов в текст
def add_garbage(text, garbage_prob=0.2):
    result = ""
    for char in text:
        result += char
        if random.random() < garbage_prob:
            result += random.choice(garbage_chars)
    return result

# Функция для удаления мусорных символов из текста
def remove_garbage(text):
    return ''.join(char for char in text if char not in garbage_chars)

# Простое шифрование и расшифровка методом сдвига символов (работает с любыми символами)
def encrypt(text, shift=5):
    text_with_garbage = add_garbage(text)
    encrypted_text = ''.join(chr((ord(char) + shift) % 65536) for char in text_with_garbage)
    return encrypted_text

def decrypt(text, shift=5):
    text = ''.join(chr((ord(char) - shift) % 65536) for char in text)
    cleaned_text = remove_garbage(text)
    return cleaned_text

# Вступительный экран с градиентом
def intro_screen():
    intro = """███████╗██╗  ██╗██╗███████╗██████╗  ██████╗ ██╗   ██╗██╗  ██╗ █████╗ 
██╔════╝██║  ██║██║██╔════╝██╔══██╗██╔═══██╗██║   ██║██║ ██╔╝██╔══██╗
███████╗███████║██║█████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ ███████║
╚════██║██╔══██║██║██╔══╝  ██╔══██╗██║   ██║╚██╗ ██╔╝██╔═██╗ ██╔══██║
███████║██║  ██║██║██║     ██║  ██║╚██████╔╝ ╚████╔╝ ██║  ██╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                     
"""
    start_color = (0, 0, 255)  # Синий
    mid_color = (255, 255, 255)  # Белый
    end_color = (0, 0, 255)    # Синий
    print(gradient_text(intro, start_color, mid_color, end_color))
    input("Нажмите Enter для продолжения...")

# Центрирование строки
def center_text(text, width=80):
    lines = text.split('\n')
    centered_text = ""
    for line in lines:
        centered_text += line.center(width) + '\n'
    return centered_text

# Меню программы с градиентом и центрированием
def show_menu():
    menu = """
╔============================╗
║        Главное меню        ║
║ [1] Шифровка               ║
║ [2] Расшифровка            ║
║ [3] Выход                  ║
╚============================╝
"""
    start_color = (0, 0, 0)  # Очень темный черный
    mid_color = (255, 255, 255)  # Белый
    end_color = (0, 0, 0)    # Очень темный черный
    print(gradient_text(center_text(menu), start_color, mid_color, end_color))

# Главная функция
def main():
    clear_screen()
    intro_screen()

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            text_to_encrypt = input("Введите текст для шифрования: ")
            encrypted = encrypt(text_to_encrypt)
            print(f"Зашифрованный текст: {encrypted}")
        elif choice == "2":
            encrypted_text = input("Введите зашифрованный текст: ")
            decrypted = decrypt(encrypted_text)
            print(f"Расшифрованный текст: {decrypted}")
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()