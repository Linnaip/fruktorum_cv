# fruktorum_cv
Тестовое задание в компанию Фрукторум

Описание задания в pdf файле.

# Как запустить проект:
1. Клонировать репозиторий
```
git@github.com:Linnaip/fruktorum_cv.git
```
2. в домашней директории проекта создать файл .env по примеру .env_sample

3. перейти в директорию infra
```
cd infra
```
4. запустить сборку контейнеров:
```
docker-compose up -d --build
```
5. выполнить команды:
```
docker-compose exec backend python manage.py migrate
```
docker-compose exec backend python manage.py collectstatic --no-input
```

6. После сборки контейнеров проект будет доступен по адресу:
```
http://localhost/
```
Документация доступна по адресу:
```
http://localhost/api/schema/swagger-ui/
```
