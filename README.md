# Описание проекта банковского приложения
1. **Цель проекта**
   - Данный проект предназначен для осуществления функционала банковских операций.
2. **Требования к окружению**:
   - Для корректной работы необходимы версии:
     ```
     Python 3.12+
     ```
3. **Установка проекта**:
   - Шаги для установки проекта на локальной машине:
     - Склонировать репозиторий:
       ```bash
       git clone https://github.com/LarisaVikulova/Bank-project
       ```
     - Перейти в директорию проекта:
       ```bash
       cd Bank-project
       ```
     - (Если требуется) Создать и активировать виртуальное окружение:
       ```bash
       python -m venv venv
       source venv\Scripts\activate для Windows #или source venv/bin/activate для MacOS
       ```

4. **Установка зависимостей**:
   - Шаг по установке зависимостей из `requirements.txt` 
     ```bash
     pip install -r requirements.txt
     ```

5. **Примеры работы функций**
   - При подаче на вход функции словаря с данными о банковских операциях
   возвращается новый список словарей, который содержит переданное значение:
   ```commandline
   # Выход функции со статусом по умолчанию 'EXECUTED'
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

   # Выход функции, если вторым аргументов передано 'CANCELED'
   [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
   ```

6. **Дополнительная информация**:
   - При необходимости проверки кода на других данных, рекомендуется запускать их из папки tests.
   
# Тестирование

В папке *tests* содержится тестирование функций проекта

1. В модуле *test_masks* проверяются тестированием маски сокрытия номера карты при различных 
условиях введения номера, учитывая неверно введенные данные.
2. В модуле *test_processing* проверяются тестированием списки словарей для функций на корректность их работы
3. В модуле *test_widget* проверяются тестированием маски карт и счетов, учитывая их назначение (Счет или название 
карты), а также маска перевода даты в формат ДД.ММ.ГГГГ на корректность работы функции
4. В модуле *test_generators* проверяются тестированием:
- Функция *filter_by_currency* на корректный вывод транзакций по заданной валюте;
- Функция *transaction_descriptions* на корректный вывод описания к каждой операции;
- Функция *card_number_generator* на корректность генерации номеров банковских карт.

5. Примеры использования функции *filter_by_currency* модуля **generators**:
```commandline
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
6. Примеры использования функции *transaction_description* модуля **generators**:
```commandline
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
7. Примеры использования функции *card_number_generator* модуля **generators**:
```commandline
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```