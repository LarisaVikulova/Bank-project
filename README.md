# Инструкция к проекту банковского приложения
1. **Описание проекта**
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

5. **Дополнительная информация**:
   - При необходимости проверки кода на других данных, рекомендуется запускать их из папки tests.