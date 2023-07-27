

Это репозиторий с кодом финального проекта по курсу
[Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/syllabus)
 
#### Дисклеймер для проверяющего
У моего репозитория есть несколько отличие от того, что требовалось в курсе. 
1) Тесты сложены в отдельную папку ui_tests (так мы делали на работе)

2) Для теста test_user_can_add_item_to_basket в setup я заменила регистрацию нового пользователя каждый раз
логин'ом под уже созданным пользователем и чисткой корзины после  каждого прогона теста
Причина: у нас нет API и нет возможности поудалять созданных пользователей, а плодить 100500 пользователей на каждый отладочный прогон теста я считаю некрасивым.

Эти изменения сознательные. Поскольку они не противоречат [требованиям к выпускному заданию](https://stepik.org/lesson/201964/step/15?unit=176022), я 


#### Как запускать проект

3). Клонируем туда автотесты !! c ключом --recurse-submodules
`git clone ssh://git@gitlab.int.ntl:22022/qa1/test_automation.git --recurse-submodules`

4). Создаем виртуальное окружение python (например, с названием  my_venv) 
`sudo apt-get install python3-venv`
`python3 -m venv my_test_venv`

5). Активируаем виртуальное окружение `my_test_venv`
`source my_test_venv/bin/activate`
`python3 -m pip install --upgrade pip`

 и устанавливаем в него нужные автотестам пакеты
`pip install -r test_automation/requirements.txt`


6). Запускаем
`pytest -s -v --host_ip=172.20.77.84 test_suites/test_api/test_watch_lists.py`
