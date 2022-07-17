import datetime
import os
import shutil
from pathlib import Path
from app_parser_youla import aiohttp64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from app_parser_youla import links_items
from app_parser_youla import pars_item
from app_parser_youla import variables

import json
from django.core import serializers
# <editor-fold desc="отрисовка главной страницы">
def index(request):
    return render(request, 'app_parser_youla/index.html')
# </editor-fold>

# <editor-fold desc="Стартовая функция">
def start(request):
    variables.phons_list = []
    variables.stop = 1
    variables.work_status = 1  # Статус работы. 0 - не работает, 1 - работает
    variables.phone_availability = 0  # Число объявлений с телефонами
    variables.aiohttp_64 = aiohttp64.async64()
    variables.links_item = []  # Список куда собираются все ссылки
    variables.parsed_link_count = 0  # Обработано объявлений
    variables.find_links = 0  # Сколько объявлений найдено
    variables.directory = ''  # Папка для сохранения результата

    links_items.main()  # сбор ссылок на товары

    today = datetime.datetime.today()
    variables.directory = str(today.strftime("%Y-%m-%d_%H.%M.%S"))
    path = Path(os.getcwd(), "app_parser_youla", "result", f"result {variables.directory}")
    try:
        os.mkdir(path)
    except Exception as ex:
        print(f"ошибка при создании папки {ex}")

    # path_test_file = Path(path, "text.txt")
    # with open(path_test_file, "w", encoding="utf-8") as f:
    #     f.write('тест')

    pars_item.main()  # парс собранных ссылок


    path_write_arhive = Path(os.getcwd(), "media", "result", "result")  # путь для записи архива
    shutil.make_archive(str(path_write_arhive), "zip", path)  # делаю архив
    # print(f"статус  {variables.work_status}")
    variables.urls_category = ''  # ссылки на категории
    variables.work_status = 0
    return HttpResponse("ok", content_type='text/html')
    # return HttpResponse(f"{path_write_arhive}.zip", content_type='text/html')
    # return HttpResponse(open(f"{path_write_arhive}.zip", "rb"), content_type='text/html')
# </editor-fold>

# <editor-fold desc="Отображение работы парсера в реальном времени">
def real_time_display(request):

    # data_json = JsonResponse({
    #     'find_links': variables.find_links,  # Сколько объявлений найдено
    #     'parsed_link_count': variables.parsed_link_count,  # Обработано объявлений
    #     'phone_availability': variables.phone_availability,  # Число объявлений с телефонами
    #     'work_status': variables.work_status
    # })
    data = {
        'find_links': variables.find_links,  # Сколько объявлений найдено
        'parsed_link_count': variables.parsed_link_count,  # Обработано объявлений
        'phone_availability': variables.phone_availability,  # Число объявлений с телефонами
        'work_status': variables.work_status
    }
    # data_json = serializers.serialize('json', data)
    data_json = json.dumps(data)
    # return HttpResponse(data_json, content_type='text/html')
    return HttpResponse(data_json, content_type='application/json')
# </editor-fold>

# <editor-fold desc="Получить категории и прокси для парсинга из textarea" >
def get_proxies_and_links_category(request):
    links_category = request.GET["links_category"]
    proxies = request.GET["proxies"]

    if links_category != '' and proxies != '':
        variables.urls_category = links_category
        variables.proxies = proxies

        path_links_category = Path(os.getcwd(), "app_parser_youla", "links_category.txt")
        with open(path_links_category, 'w') as f:
            f.write(variables.urls_category)

        path_proxies = Path(os.getcwd(), "app_parser_youla", "proxies.txt")
        with open(path_proxies, 'w') as f:
            f.write(variables.proxies)

        return HttpResponse("ok", content_type='text/html')
    else:
        return HttpResponse("no", content_type='text/html')
# </editor-fold>

# <editor-fold desc="Чтение категорий для парсинга из links_category.txt и прокси из proxies.txt и передача в textarea">
def read_links_category_and_proxies_txt(request):
    # print("запустилось read_links_category_txt")

    path_links_category = Path(os.getcwd(), "app_parser_youla", "links_category.txt")
    with open(path_links_category, 'r') as f:
        links_category = f.read()
        # if links_category != '':
        #     variables.urls_category = links_category

    path_proxies = Path(os.getcwd(), "app_parser_youla", "proxies.txt")
    with open(path_proxies, 'r') as f:
        proxies = f.read()

    if links_category != '' and proxies != '':
        variables.urls_category = links_category
        variables.proxies = proxies

        data = JsonResponse({
            'links_category': links_category,
            'proxies': proxies
        })

        return HttpResponse(data, content_type='text/html')
    else:
        return HttpResponse("no", content_type='text/html')
        # print(variables.urls_category)
# </editor-fold>

# <editor-fold desc="Остановить парсер">
def stop_parser(request):
    variables.stop = 0
    variables.urls_category = ''  # ссылки на категории
    variables.work_status = 0
    variables.parsed_link_count = 0  # Обработано объявлений
    variables.find_links = 0  # Сколько объявлений найдено
    variables.phone_availability = 0  # Число объявлений с телефонами
    # print(f'кнопка стоп {variables.stop}')
    return HttpResponse("ok", content_type='text/html')

# </editor-fold>


