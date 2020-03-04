1. создать Makefile

2. запускаем make setup (создает вирт.среду в репозитории)

3. pawstop - ввод команды в командной строке активирует виртуальную среду проекта (.pragai)
для этого в файле .bashrc прописать альяс alias pawstop="cd ~/Repository && source ./.pragai/bin/activate"

4. создать учетную запись AWS и добавить именованный профиль
http://docs.aws.amazon.com/IAМ/latest/UserGuide/id_ users_create.html

5. настроить профиль AWS (создать в корне папку .aws)
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

добавляем в ЛК амазона Access keys for CLI, SDK, & API access

эти данные прописываем по команде в терминале
aws configure --profile example, где example - название профиля

6. для автоматической активации профиля aws добавляем в activate 
#Export AWS Profile
AWS_PROFILE="example"
export AWS_PROFILE

7. создаем папки в репозитории
mkdir paws
touсh paws/__init__.ру
touсh paws/sЗ.py
mkdir tests
touсh tests/test_sЗ.py

8. пишем модуль s3.py

9. при необходимости проверяем модуль через try.py

10. создаем PYTHONPATH в переменной activate, чтобы отразить расположение созданной библиотеки
#Export PYTHONPATH
PYTHONPATH="paws"
export PYTHONPATH

11. создаем модульный тест при помощи pytest и moto

11.1. добавляем код в test_sЗ.py
11.2. добавляем в requirements.txt новые библиотеки
awscli
bоtоЗ
moto
pytest
pylint
sensible
jupyter
pytest-cov
pandas

11.3. запускаем make install

11.4. модифицируем Makefile, добавляем в него
test:
	PYTHONPATH=. && pytest -vv --cov=paws tests/*.py

lint:
	pylint --disable=R,C paws

11.5. запускаем тесты: make test
                        make lint
11.6. добавляем в Makefile запуск трех действий последовательно all: install lint test

12. интеграция с блокнотом Jupiter