# Check Fucking Money Web-app

Web приложение для контроля доходов и рассходов

### Инструкция по запуску
1. Склонируйте репозиторий

``` 
git clone https://gitlab.com/Bushmester/check-fucking-money-web-app.git

or

git clone git@gitlab.com:Bushmester/check-fucking-money-web-app.git
```

2. Создайте вертуальное окуржение и установите все зависимости (все делается при помощи poetry)

```
poerty install
```

3. Создайте в файле ```.env``` переменные окружения ```SECRET_KEY``` и ```DATABASE_URI```

4. ~~э~~Мигрируйте ~~из России~~ базу данных ```flask db upgrade```

5. Запускайте проект

    1. При помощи ```flask run```

    2. При помощи wsgi ```gunicorn -w 4 wsgi:app```

6. ##### ez game

>Glad to see you on the radio wave CheckFM
