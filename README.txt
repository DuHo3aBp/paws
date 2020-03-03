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

9. можем проверить модуль через try.py

10. создаем PYTHONPATH в переменной activate