<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/swiper-bundle.min.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Home</title>
    <script src="https://api-maps.yandex.ru/2.1/?apikey=9d41c8c3-eca5-4b49-9eaa-c08e88bbd00a&lang=ru_RU"></script>
    <script src="js/map.js"></script>
    <script src="js/swiper-bundle.min.js"></script>
</head>
<body>
    <header>
        <nav class="navigation">
            <a href="#" class="logotype-anchor">
                <img src="img/logo.svg" alt="logotype">
                <h1 class="logotype-header">MAP OF INTEREST</h1>
            </a>
            <form class="search-form">
                <input class="search-field" type="search" placeholder="Искать маршруты...">
            </form>
            <a href="#">
                <img src="" alt="" title="">
            </a>
            <a href="#">
                <img src="" alt="" title="">
            </a>
            <button class="route-window-toggler">
                <img src="img/settings.svg" class="button-panel" alt="settings">
            </button>
            <div class="header-buttons">
                <a href="#" class="header-text">Пользователь</a>
                <a href="#" class="header-text">Выход</a>
                <!-- <a href="#" class="header-text">Регистрация</a>
                <a href="#" class="header-text">Вход</a> -->
            </div>
        </nav>
    </header>
    <main>
        <div>
            <div id="map" style="height: 100vh"></div>
        </div>
        <body>
            <div id="map"></div>
            <div class="inputs">
                <input type="button" value="Показать пример GPX" class="load-gpx" />
            </div>
        </body>
        <div class="propeties-container">
            <button class="route-arrow-container">
                <img src="img/arrow.svg" class="route-arrow-button" alt="arrow">
            </button>
            <h1 class="propeties-text-header">Вокруг реки Исеть</h1>
            <div class="propeties-block-slider">

                <img src="img/arrow-left.svg" class="swiper-button-prev" alt="arrow-left">

                <div class="swiper">

                    <!-- Additional required wrapper -->
                    <div class="swiper-wrapper">
                        <!-- Slides -->
                        <img src="img/1.JPG" class="swiper-slide" alt="1">
                        <img src="img/2.JPG" class="swiper-slide" alt="2">
                        <img src="img/3.JPG" class="swiper-slide" alt="3">
                        <img src="img/4.JPG" class="swiper-slide" alt="4">
                    </div>
                  
                    <!-- If we need scrollbar -->
                    <div class="swiper-scrollbar"></div>
                </div>

                <img src="img/arrow-right.svg" class="swiper-button-next" alt="arrow-right">

            </div>
            <img src="img/difficult.svg" class="propeties-block-difficult" alt="difficult">

            <img src="img/information.svg" class="propeties-block-information" alt="informaton">

            <div class="propeties-block-description">
                <span class="propeties-text">Описание:</span>
                <p class="properties-text-description">История города Екатеринбурга ведет отсчет с 1723 года, когда на реке Исети был основан завод-крепость, именно вокруг этой красивой реки проходит данный маршрут. 
                    На нем вы увидите прекрасные сады  возле главного здания Свердловской ЖД, прокатитесь по паркам УрГУПС’а и 22 партсъезда с шикарными видами, 
                    посмотрите здания правительства области и администрации города Екатеринбург, полюбуетесь видами на набережной, заедете к памятнику человека, 
                    в честь которого был назван Екатеринбург в Советское время, а также почувствуете дух «меховой» улицы нашего города.
                </p>    
            </div>
            <div class="propeties-block-description">
                <span class="propeties-text">Тип маршрута: Городской</span>
                <a href="https://getfile.dokpub.com/yandex/get/https://disk.yandex.ru/d/flTT2Nh97Oz7ug" class="propeties-text">Ссылка на скачивание .gpx</a>
            </div>
        </div>
        <div class="route-container">
            <div class="route">
                <img src="img/fake-1.svg" alt="Маршрут 1" class="route-image">
                <div class="route-header">
                    <div class="route-header-text">Вокруг реки Исеть</div>
                    <div class="route-header-text-2">Точка старта: памятник Уральскому добровольческому танковому корпусу</div>
               </div>
                <div class="route-description">
                    <div class="route-header-text-3"><b>Маршрут:</b> памятник Удтк - Макаровский мост - парк УрГУПС - парк партсъезда - набережная рабочей молодежи – 
                        администрация города - цирк - плотинка - театр оперы и балета - Храм на крови - Харитоновский сад - памятник Удтк.</div>
                    <input class="submit-field" type="submit" value="Поехали!" data-routeid='21'>
                </div>
            </div>
            <div class="route">
                <img src="img/fake-2.svg" alt="Маршрут 1" class="route-image">
                <div class="route-header">
                    <div class="route-header-text">Исторический район</div>
                    <div class="route-header-text-2">ул.Вайнера, 11 - ул. Радищева - парк Зеленная роща 1,8км</div>
               </div>
                <div class="route-description">
                    <div class="route-header-text-3">Достопримечательности...</div>
                    <input class="submit-field" type="submit" value="Поехали!">
                </div>
            </div>
            <div class="route">
                <img src="img/fake-3.svg" alt="Маршрут 1" class="route-image">
                <div class="route-header">
                    <div class="route-header-text">Улица Отдыха</div>
                    <div class="route-header-text-2">ул. Отдыха 107Б - ул. Отдыха 11 2.8 км</div>
               </div>
                <div class="route-description">
                    <div class="route-header-text-3">Достопримечательности...</div>
                    <input class="submit-field" type="submit" value="Поехали!">
                </div>
            </div>
        </div>
    </main>
    <footer>
        <div>
            <span></span>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
