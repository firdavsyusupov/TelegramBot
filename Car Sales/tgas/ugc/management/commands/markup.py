from telegram import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup([['Онлайн заявка📝'],
                                   ['Список дилерских центров 📑'],
                                   ['Список продукции компании 🗂'],
                                   ['Автомобили в наличии 🛞', 'Текущие акции компании📈'],
                                   ['Прайс лист🔖', 'Контакты🪪'],
                                   ['Сменить язык⚙️']
                            ])

btns_admin = ReplyKeyboardMarkup([['Добавить диллерский центр 📑'],
                             ['Тестовая кнопка']
                             ])

region = ReplyKeyboardMarkup([['Ташкент'],
                              ['Самарканд']
                              ])

dealer_company = ReplyKeyboardMarkup([["Показать все компании"]])

car_models = ReplyKeyboardMarkup([['Показать все модели']])

online_app = ReplyKeyboardMarkup([['Заявка на тест драйв'],
                                   ['Заявка на продукцию'],
                                   ['Заявка на запасные части'],
                                   ['Заявка на сервис'],
                                   ['Назад']
                                  ])

cars = ReplyKeyboardMarkup([['Автобус'],
                             ['Грузовой Автомобиль'],
                             ['Специализированный автомобиль'],
                             ['Пикап']
                            ])

locate = [[KeyboardButton(text="Отправить локацию", request_location=True)]]

IN_DEVELOPMENT = ReplyKeyboardMarkup([['В разработке']])


buttons = [
        [KeyboardButton(text="Онлайн заявка📝"),
         KeyboardButton(text="Список дилерских центров 📑")]
        ]
