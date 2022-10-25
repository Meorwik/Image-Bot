from requests import get

# TODO: превратить список в словарь {nameOfCategory: pageNumber}\done
# nameOfCategory (str)"Абстрактные"
# pageNumber (int)

CategoryDict = {
"Абстрактные": 1,
"Авиация": 1,
"Аниме": 1,
"Архитектура": 1,
"Векторные": 1,
"Весна": 1,
"Винтаж": 1,
"Вода": 1,
"Водопады": 1,
"Города": 2,
"Горы": 2,
"Девушки": 2,
"Деньги": 2,
"Дети": 2,
"Дождь": 2,
"Еда": 2,
"Животные": 2,
"Закаты": 2,
"Земноводные": 3,
"Зима": 3,
"Игры": 3,
"Интерьер": 3,
"Корабли": 3,
"Космос": 3,
"Кошки": 3,
"Лето": 3,
"Любовь": 3,
"Люди": 4,
"Макро": 4,
"Машины": 4,
"Мосты": 4,
"Мотоциклы": 4,
"Мужчины": 4,
"Музыка": 4,
"Мультфильмы": 4,
"Напитки": 4,
"Насекомые": 5,
"Неоновые":5,
"Ночь": 5,
"Облака": 5,
"Озёра": 5,
"Океан": 5,
"Осень": 5,
"Пейзажи": 5,
"Подводный мир": 5,
"Природа": 6,
"Птицы": 6,
"Рассвет": 6,
"Рендеринг": 6,
"Ретро автомобили": 6,
"Рисованные": 6,
"Сладости": 6,
"Собаки": 6,
"Спорт": 6,
"Узоры": 7,
"Фантастика": 7,
"Фильмы": 7,
"Фоны": 7,
"Фрукты": 7,
"Цветы": 7
}


class PictureGeter:
    url = "https://7fon.org/Обои/"
    r = get(url)
    start_indx = r.text.find('<div id="cbox">')
    end = r.text.find('<ins class="adsbygoogle"')
    delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
    html_list = r.text[start_indx:end].split(delimetr)
    on_page = 0
    list_of_links: list = []

    @classmethod
    def __reset_url(cls):
        cls.url = "https://7fon.org/Обои/"

    @classmethod
    def __clear_cls_memory(cls):
        cls.list_of_links = []
        cls.on_page = 0

    @classmethod
    def __set_category(cls, category: str):
        cls.__reset_url()
        cls.url += category

    @classmethod
    def __open_next_page(cls):
        cls.on_page += 1
        cls.url = cls.url + f"/{cls.on_page}.html"

    @classmethod
    def __reset_page_info(cls):
        r = get(cls.url)
        start_indx = r.text.find('<div id="cbox">')
        end = r.text.find('<ins class="adsbygoogle"')
        delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
        cls.html_list = r.text[start_indx:end].split(delimetr)

    @classmethod
    def __update_all(cls, cat):
        cls.__set_category(cat)
        cls.__open_next_page()
        cls.__reset_page_info()

    @classmethod
    def __get_links(cls):
        temp_list = []
        for line in cls.html_list:
            index_img = line.find("<img src=") + 12
            tmp = line[index_img:]
            finish_index = tmp.find('alt=') - 2
            temp_list.append(tmp[:finish_index])
        return temp_list

    @classmethod
    def __check_count(cls, count_of_pictures, category):
        cls.__clear_cls_memory()
        cls.__update_all(category)
        cls.list_of_links += cls.__get_links()
        now_count = len(cls.list_of_links)
        if now_count > count_of_pictures:
            return cls.list_of_links[:count_of_pictures]
        else:
            cls.__update_all(category)
            while now_count < count_of_pictures:
                cls.list_of_links += cls.__get_links()[1:]
                now_count = len(cls.list_of_links)
                cls.__update_all(category)
            else:
                return cls.list_of_links[:count_of_pictures]

    @classmethod
    def get_list_with_urls_on_pictures(cls, count_of_pictures: int, category: str):
        return cls.__check_count(count_of_pictures+1, category=category.capitalize())[1:]
