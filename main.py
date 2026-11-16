import re
import sys

def convert_md_to_tg(text):
    # 1. Жирный текст (**текст** или __текст__)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    
    # 2. Курсив (*текст* или _текст_)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'_(.*?)_', r'<i>\1</i>', text)
    
    # 3. Моноширинный код (`текст`)
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # 4. Ссылки ([текст](url))
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    # 5. Заголовки (## Текст) -> просто жирный текст
    text = re.sub(r'^#+\s+(.*)$', r'<b>\1</b>', text, flags=re.MULTILINE)
    
    return text

def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <файл.md>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    # Читаем файл, игнорируя любые ошибки кодировки (заменяем битые символы)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        sys.exit(1)
            
    tg_text = convert_md_to_tg(md_text)
    
    print("\n--- Результат для Telegram ---")
    print(tg_text)
    print("------------------------------")
    print("Скопируй текст выше и вставь в Телеграм.")

if __name__ == "__main__":
    main()