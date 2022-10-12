# Для запуска dev версии


1. Установите [Docker](https://www.docker.com/).
2. Скачайте код и перейдите в каталог проекта:
```sh
git clone https://github.com/MeshkovD/payment_system_api_test_task.git
cd payment_system_api_test_task
```
3. Проект настроен на работу с переменными окружения. Для их использования, в корневом каталоге проекта создайте файл .env

Примерное содержимое файла .env:
```sh
SECRET_KEY=ikzst-5&i6x(9gg(example)0bfghtf4ggDFG455thyhwfjqgdg45
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_ALLOWED_HOSTS=127.0.0.1
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_spider_test_task_dev
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
 

5. В терминале введите команду:  
```sh
docker-compose up -d --build
```

6. Сайт доступен в браузере по адресу http://localhost:8000/



#### Для связи продукта и организации используется сущность "товар"(commodity), содержит цену.

## RESTful Structure

| Endpoint              | HTTP Method | CRUD Method | Result                              |
|-----------------------|-------------|-------------|-------------------------------------|
| `organizations/:id`   | GET         | READ        | Информация об организациях в районе |
| `organization/:id`    | GET         | READ        | Детальная информация об организации |
| `products`            | GET         | READ        | Перечень всех продуктов             |
| `products`            | POST        | CREATE      | Добавить продукт                    |
| `product/:id`         | GET         | READ        | Детальная информация о продукте     |
| `commodities/:id`     | GET         | READ        | Информация о товарах организации    |
| `commodities/:id`     | POST        | CREATE      | Добавить товар в организацию        |
| `commodity/:id`       | GET         | READ        | Детальная информация о товаре       |
