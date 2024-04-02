# Тестовое задание LESTA
 

<br>

- [Установка и запуск](#установка-и-запуск)


<br>


## Установка и запуск:



1. git clone https://github.com/TasteBeam/lesta_test && cd lesta_test



2. python -m venv venv && source venv/bin/activate (linux) <br>
   python -m venv venv && venv\Scripts\activate (windows)

3. pip install requirements.txt
4. python app/manage.py makemigrations <br>
   python app/manage.py migrate <br>
   python app/manage.py runserver <br>

Запустится локальный сервер. `http://127.0.0.1:8000/`

Далее выбираем текстовый файл, если в нем не будет 50 слов, он заполнится случайными словами из этого же файла <br>
Получаем таблицу

5. Остановить приложение можно комбинацией клавиш Ctrl-C.

6. Удаление проекта :
   - CTRL + C (Если еще не вышли из программы)
   - deactivate
   - cd ..
   - rm -fr lesta_test (для Linux)
   - del /s /q lesta_test && rmdir /s /q lesta_test (для Windows)
