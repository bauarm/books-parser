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
### Файл pdfSpliter.py
##### Разделяет книгу в формате PDF на отдельные страницы
```bash
python pdfSpliter.py
```
### Файл pdfToImg.py
##### Перегоняет PDF в PNG картинки
```bash
python pdfToImg.py
```
Для работы библиотеки [Wand](https://pypi.org/project/Wand/) необходима программа [ImageMagick](https://imagemagick.org/script/download.php) . На Ubuntu ImageMagick обычно установленна изначально. Возможны проблемы с [настройками безопасности](https://imagemagick.org/script/security-policy.php). Необходима правка файла /etc/ImageMagick-6/policy.xml 
```bash
vi /etc/ImageMagick-6/policy.xml
```
Данная строка
```xml
<policy domain="coder" rights="none" pattern="PDF" />
```
Заменяется этой
```xml
<policy domain="coder" rights="read|write" pattern="PDF" />
```
### Файл pngToTxt.py
##### Извлекает текст из картинок
```bash
python pngToTxt.py
```
Для работы скрипта на машине должен быть установлен [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
##### Проверка на наличие установленной программы Tesseract OCR
```bash
tesseract --version
```
Если не установленна
```bash
sudo apt install tesseract-ocr
```
Установка русского языкового пакета
```bash
sudo apt-get install tesseract-ocr-rus
```
Так же для работы скрипта необходима программа [ImageMagick](https://imagemagick.org/script/download.php) . На Ubuntu ImageMagick обычно установленна изначально.

##### Проверка на наличие установленной программы ImageMagick
```bash
convert -version
```
Если не установленна. Команда для установки imagemagick
```bash
sudo apt install imagemagick
```