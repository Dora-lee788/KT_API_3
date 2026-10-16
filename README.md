
# КТ — API Testing

## Цель работы

Протестировать REST API Swagger Petstore с помощью Python и библиотеки `pytest`, используя базовый класс `BaseRequest` из примера `api_testing`.

- **Тестируемый API:** https://petstore.swagger.io/
- **Репозиторий с примером:** https://github.com/sadboy2001/api_testing

## Структура проекта

```text
KT_API/
├── base_request.py
├── tests/
│   ├── test_user.py
│   └── test_store.py
├── Screenshots/
└── README.md
```

## 1. Базовый класс BaseRequest

В файле `base_request.py` реализован класс `BaseRequest` для выполнения HTTP-запросов к API.

Реализованы методы:

- `get()` — получение данных;
- `post()` — создание данных;
- `put()` — изменение данных;
- `delete()` — удаление данных.

**Базовый URL:** `https://petstore.swagger.io/v2`

![Реализация BaseRequest](Screenshots/base_request.png)

## 2. Тестирование сущности User

Для сущности `user` реализованы четыре автоматизированных теста с использованием `pytest`.

| Тест | HTTP-метод | Endpoint | Проверка |
|---|---|---|---|
| `test_create_user` | POST | `/user` | Создание пользователя |
| `test_get_user` | GET | `/user/test_user_1001` | Получение пользователя |
| `test_update_user` | PUT | `/user/test_user_1001` | Изменение данных пользователя |
| `test_delete_user` | DELETE | `/user/test_user_1001` | Удаление пользователя |

После изменения данных выполняется дополнительный GET-запрос для проверки обновлённых значений. После удаления выполняется GET-запрос для проверки отсутствия пользователя.

**Скриншоты:**

- Создание и получение пользователя:

  ![Создание и получение пользователя](Screenshots/user_create_get.png)

- Изменение данных пользователя:

  ![Изменение пользователя](Screenshots/user_update.png)

- Удаление пользователя:

  ![Удаление пользователя](Screenshots/user_delete.png)

Файл с тестами: `tests/test_user.py`.

## 3. Тестирование сущности Store

Для сущности `store` реализованы четыре автоматизированных теста с использованием `pytest`.

| Тест | HTTP-метод | Endpoint | Проверка |
|---|---|---|---|
| `test_get_inventory` | GET | `/store/inventory` | Получение информации о наличии товаров |
| `test_create_order` | POST | `/store/order` | Создание заказа |
| `test_get_order` | GET | `/store/order/5` | Получение заказа по идентификатору |
| `test_delete_order` | DELETE | `/store/order/5` | Удаление заказа |

После удаления заказа выполняется дополнительный GET-запрос для проверки результата удаления.

**Скриншоты:**

- Получение Inventory:

  ![Получение Inventory](Screenshots/store_inventory.png)

- Создание заказа:

  ![Создание заказа](Screenshots/store_create_order.png)

- Получение заказа:

  ![Получение заказа](Screenshots/store_get_order.png)

- Удаление заказа:

  ![Удаление заказа](Screenshots/store_delete_order.png)

Файл с тестами: `tests/test_store.py`.

## 4. Запуск автоматизированных тестов

Для запуска всех тестов используется команда:

```powershell
python -m pytest -v
```

По результатам запуска успешно пройдены все восемь тестов: четыре для `user` и четыре для `store`.

**Результат выполнения pytest:**

![Результат запуска pytest — 8 тестов пройдены](Screenshots/pytest_results.png)

## 5. Соответствие заданию

- Использован Swagger Petstore API.
- Изучен пример реализации API-запросов из репозитория `api_testing`.
- Реализован базовый класс `BaseRequest`.
- Использованы HTTP-методы GET, POST, PUT и DELETE.
- Реализованы четыре теста для сущности `user`.
- Реализованы четыре теста для сущности `store`.
- Тестовые методы оформлены с использованием `pytest`.
- Добавлены проверки результатов выполнения запросов.
- Выполнен запуск автоматизированных тестов: **8 тестов пройдены успешно**.
- Добавлены скриншоты результатов тестирования.


