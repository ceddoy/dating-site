## **Мини-проект "Сайт знакомств"**

* в качестве тестирования прошу использовать приложение postman, либо сайт https://www.postman.com/
### Реализованы следующие задачи:

1) Регистрация пользователя -
**/api/clients/create/**
#### Поля для заполнения (POST-запрос)
* first_name
* last_name
* sex (male или female)
* email
* password
* avatar (необязательно)
2) Авторизация пользователя (по токену) - **/api_auth_token/**
#### Поля для заполнения (POST-запрос)
* email
* password
* latitude (широта)
* longitude (долгота)
* в качестве источника координат для заполнения, можете воспользоваться этим сайтом https://www.mapcoordinates.net/ru , либо другим удобным для вас.
* получаем Token для дальнейшего прохождения по проекту.
#### Особенность заполнения долготы и широты при авторизации, актуализирует информацию о местонахождении пользователя
3) Просмотр списка всех зарегистрированных пользователей, с возможность фильтрации по: имени, фамилии, полу и дистанции (км) - **/api/list/**
#### Для отображения списка (GET-запрос)
#### фильтровать можно по след. полям:
* distance_km
* first_name
* last_name
* sex
4) Просмотр пользователя с дальнейшей возможность поставить отклик "Мне нравится", в случае взаимности, то система предоставит электронную почту понравившегося человека, а также разошлет уведомления на электронную почту обоим пользователем о взаимности (в письме будет указаны: имя, фамилия, почта) - **/api/clients/(id)/match/**
#### Для отображения пользователя (GET-запрос)
* вставляем id зарегистрированного пользователя и смотрим на аватарку
* если, понравился пользователь вы можете в этом же api поставить "Мне нравится"
#### Для нажатия "Мне нравится" используйте PUT-запрос

### Прошу обратить внимание, что для просмотра и использования некоторых api, за исключением регистрации и авторизации, необходимо добавлять Token пользователя.
