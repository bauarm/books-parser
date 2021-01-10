Парсер для пакетного извлечения текста из отсканированных книг
=====================
# books-parser
## Установка в виртуальное окружение 

#### Скачать репозиторий
```bash
git clone https://github.com/bauarm/books-parser.git
```

#### Установить и активировать виртуальное окружение
```bash
cd ./books-parser && virtualenv venv && source venv/bin/activate
```
#### Установить все пакеты из requirement.txt
```bash
pip install -r requirement.txt
```
## Назначение файлов
#### Файл pdfSpliter.py
##### Разделяет книгу в формате PDF на отдельные страницы
```bash
python pdfSpliter.py
```