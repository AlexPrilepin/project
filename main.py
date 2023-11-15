from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>RITCH? RITCH!!!</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    <link rel="icon" href="image1.png" type="image/x-icon">
    <script type="text/javascript" src='script.js'></script>
  </head>
  <body>
    <!--Ну привет. Садись, не стесняйся... Я тебя давно ждал) -->

        <header class="Header"> 
            <div class="container">
            <div class="Header_body">
                <div class="Header_logo"> 
                    <a href="123.png"><img class='turner' src="lol.png" alt="logo" width="120" height="40"></a>
                </div>
                <div class="Header_items" width=163 height=72> 
                    <div class="Header_signin">
                    </div>
                    <div class="Header_basket">
                    <a></a></div>
                </div>
                </div>
            </div>
        </header>
        <section class="firstsection">
            <div class="container">
                <div class="row">
                    <div class="turner col-xs12 col-md-7 col-lg-5 col-xl-5 card" style='border: 0px'>
                        <div class="card__pushkin" style='display: flex; justify-content: center;border: 4px solid black;'>
                            <div class="one"><div class="name">Методичка для начинающих горе-прогеров</div></div>
                                <div class="second">
                                <div class="pushkindelivery"><i>Welcome to the club, buddy!)</i></div>
                                <div class="time__delivery" style='display: flex; justify-content: center; padding-left: 10px; margin-left: 10px;'><a style='font-size: 22px'>  Удачи...</a></div>
                            </div>
                        </div>   
                    </div>
                </div>
            </div>
        </section>
        <div class='turner' style='margin: auto; width: 80%; padding-top: 25px; display: flex; justify-content: space-around; font-size: 30px'>
            <b>Основные темы:</b>
        </div>
        <div class="accordion container" style='display: flex-inline; justify-content: space-around; align-content: stretch; width: 100%; margin-bottom: 30px;' id="accordionExample">
    <div width=90%;>
    <p style='margin-bottom: 30px; display: flex; justify-content: space-between; text-decoration: none; align-self: stretch;  width: 100%; margin-bottom: 30px; border-bottom: 2px solid gray; border-top: 2px solid gray; margin-top: 50px'>
    <a>   
            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse1" aria-expanded="false" aria-controls="collapse1">
              <strong>Циклы</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse2" aria-expanded="true" aria-controls="collapse2">
              <strong>Массивы</strong>
            </button>



            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse3" aria-expanded="false" aria-controls="collapse3">
              <strong>Функции</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse4" aria-expanded="true" aria-controls="collapse4">
              <strong>TXT-io</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse5" aria-expanded="false" aria-controls="collapse5">
              <strong>Рекурсия</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse6" aria-expanded="false" aria-controls="collapse6">
              <strong>Алг. Евклида</strong>
            </button>


            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse7" aria-expanded="false" aria-controls="collapse7">
              <strong>Простые числа</strong>
            </button>




            </a>
            <a>



      
            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse8" aria-expanded="false" aria-controls="collapse8">
              <strong>Сортировки</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse9" aria-expanded="false" aria-controls="collapse9">
              <strong>Бин.поиск</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse10" aria-expanded="true" aria-controls="collapse10">
              <strong>Посл. Контейнеры</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse11" aria-expanded="false" aria-controls="collapse11">
              <strong>Графы</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse12" aria-expanded="false" aria-controls="collapse12">
              <strong>Математика</strong>
            </button>


                <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse13" aria-expanded="false" aria-controls="collapse13">
              <strong>Множества</strong>
            </button>

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse14" aria-expanded="false" aria-controls="collapse14">
              <strong>Сложность</strong>
            </button>

            </a>
            <a>

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse15" aria-expanded="true" aria-controls="collapse15">
              <strong>Динамика</strong>
            </button>



      
            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse16" aria-expanded="false" aria-controls="collapse16">
              <strong>Комбинаторика</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left  turner" type="button" data-toggle="collapse" data-target="#collapse17" aria-expanded="false" aria-controls="collapse17">
              <strong>Геометрия</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse18" aria-expanded="true" aria-controls="collapse18">
              <strong>С.И.</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse19" aria-expanded="false" aria-controls="collapse19">
              <strong>Теория Чисел</strong>
            </button>

        

            <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse20" aria-expanded="false" aria-controls="collapse20">
              <strong>Структуры данных</strong>
            </button>

        <button style='text-decoration: none; color: black' class="btn btn-link btn-block text-left turner" type="button" data-toggle="collapse" data-target="#collapse21" aria-expanded="false" aria-controls="collapse21">
              <strong>Жадный алг.</strong>
            </button>




        </a>
       </p> 
       <div id="collapse1" class="collapse" aria-labelledby="heading1" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Собственно, база по циклам:</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Циклы</h5><a>Халява</a><a>Надо 100%</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse1_1" aria-expanded="false" aria-controls="collapse1_1"><i>Кратко по вопросу ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://acmp.ru/article.asp?id_text=517'><i>Источник ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://sun9-26.userapi.com/impg/GSTFpMIZHio0D8HAyGT17wwEw3uJHVXef6rRXw/GRNVnvqw6qY.jpg?size=600x528&quality=95&sign=aae25c5fa2fd426d15ac5b1af0d3f9c6&type=album" class="jpg">
                        </div>

                    </div>
                    <div id="collapse1_1" class="collapse" aria-labelledby="heading1_1">
                            <p style="border: 1px solid gray; padding: 3px;">В принципе циклы - это базированная база для любого прогера. Думать и читать много не надо, переходим по ссылке, при непонятках гуглим. Кратко - просто проход по некому контейнеру или множеству чего-то.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
        <div id="collapse2" class="collapse" aria-labelledby="heading2" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Массивы - тоже база</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Одн. массивы</h5><a>Халява</a><a>100% надо</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse2_1" aria-expanded="false" aria-controls="collapse2_1"><i>Кратко по вопросу ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://acmp.ru/article.asp?id_text=518'><i>Источник ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://static.wikia.nocookie.net/1fcf7e77-9b74-4d5f-a463-04b4d7df2abc/scale-to-width/755" class="jpg">
                        </div>

                    </div>
                    <div id="collapse2_1" class="collapse" aria-labelledby="heading2_1">
                            <p style="border: 1px solid gray; padding: 3px;">Массив обыковенный понадобится прогеру всегда - хотя бы для ввода данных, то есть даже до того, как придется придумывать алгоритм. Не знать массивы или их аналоги в других языках - это не беда, а диагноз) Вообще, массив - это просто набор элементов, в некоторых языках  - только какого-то одного типа, в других нет. С массивом и его элементами можно выполнять набор операций - перебор, удаление, сортировка и т.п.</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Двум.массивы</h5><a>Терпимо</a><a>90% надо</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse2_2" aria-expanded="false" aria-controls="collapse2_2"><i>Кратко по вопросу ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://acmp.ru/article.asp?id_text=520'><i>Источник ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://smart-lab.ru/uploads/2022/images/09/57/76/2022/09/06/bb510f.png" class="jpg">
                        </div>

                    </div>
                    <div id="collapse2_2" class="collapse" aria-labelledby="heading2_4">
                            <p style="border: 1px solid gray; padding: 3px;">Двумерный массив, он же матрица, нужен прогеру ну прям очень часто. Немало задач требуют знакомства с реализацией данного типа данных, а также правильного применения. На школьном этапе прожить без этого можно... И все) Ведь это по сути просто массив массивов.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
       <div id="collapse3" class="collapse" aria-labelledby="heading3" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Функции(но не рекурсивные)</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 280px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Функции)</h5><a>Халява+-</a><a>99% надо</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse3_1" aria-expanded="false" aria-controls="collapse3_1"><i>Кратко по теме ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://acmp.ru/asp/do/index.asp?main=section&id_course=1&id_section=6'><i>Источник ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://sun9-75.userapi.com/IwZn6cSXaX9vAMXSHEfU75LdUdZHkc0JVfaKzQ/05RsJebF_zE.jpg" class="jpg" style='height: 280px'>
                        </div>

                    </div>
                    <div id="collapse3_1" class="collapse" aria-labelledby="heading3_1">
                            <p style="border: 1px solid gray; padding: 3px;">Как и в случае с циклами, функции - одна из неотъемлимых составляющих любого ЯП, и если вы про них впервые слышите, и не обратили на себя внимаение санитаров, то к вам большие вопросики) Ну а если серьезно, то функция - это некий набор действий, читай алгоритм, который будет выполнен при его вызове через спец. имя.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
        <div id="collapse4" class="collapse" aria-labelledby="heading4" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Ввод-вывод в txt</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 280px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Ввод+вывод</h5><a>Халява</a><a>75% надо</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse4_1" aria-expanded="false" aria-controls="collapse4_1"><i>Кратко по теме ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://olympiads.ru/zaoch/2012-13/lang.shtml'><i>Источник ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://remarketing.bz/content/uploads/2022/09/razbor.jpg" class="jpg" style='height: 280px'>
                        </div>

                    </div>
                    <div id="collapse4_1" class="collapse" aria-labelledby="heading4_1">
                            <p style="border: 1px solid gray; padding: 3px;">Вообще, конкретно в олимпиадной проге файловый ввод-вывод почти отсутствует, разве что для оч. больших массивов данных, хотя... Едва ли. Но знать точно надо, ведь поможет не только на будущей работе, но и в отдельных олимпиадах, где по тем, или иным причинам нет возможности вводить и выводить данные. В принципе ваши действия - открыть, прочитать и перезаписать файл. Все)))</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
        <div id="collapse5" class="collapse" aria-labelledby="heading5" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Рекурсиивные ф-ии</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Сама рекурсия</h5><a>Пойдет</a><a>95%</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse5_1" aria-expanded="false" aria-controls="collapse5_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/1335/p.1/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=ecafd87a295c3a3f050c541b4aaa51cb-4833780-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse5_1" class="collapse" aria-labelledby="heading5_1">
                            <p style="border: 1px solid gray; padding: 3px;">
                                Что ж... Рекурсия - это в принципе, как и динамика, одна из важнейших тем именно олимпиадной проги, которая выстреливает почти в каждом контесте. Смысл рекурсии состоит вызове некой функции в ее же теле, для вычисления некого конечного результата. Например как в сложном банковском проценте. Тема несложная, но сложной может быть реализация в конкретных задачах.
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Меморизация</h5><a>Халява</a><a>90%</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse5_2" aria-expanded="false" aria-controls="collapse5_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/4302/p.1/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=a7343e6edfbb7b86c2ed51f888804a1d-5870018-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse5_2" class="collapse" aria-labelledby="heading5_4">
                            <p style="border: 1px solid gray; padding: 3px;">Стареющий русский помещик находит в своих вещах крохотный гранатовый крестик, его захлёстывают воспоминания 30-летней давности.

                            Дмитрий Павлович путешествовал по европейским городам и задержался во Франкфурте, где случай свёл его с итальянской семьёй. Он заглянул в их кондитерскую и увидел юную Джемму, которой требовалась помощь — брату Эмилю стало плохо. Санин помог и быстро стал другом семьи.

                            Вскоре герой осознал, что влюблён в Джемму. Она была просватана, но ответила Санину взаимностью и отказала жениху — немцу Клюберу. Дмитрий Павлович отправился продавать поместье, чтобы было чем оплатить свадьбу, но увлёкся Марьей Полозовой и изменил невесте. Любовница вскоре им наигралась, и Санин остался один.

                            Найденный крестик побудил в герое желание узнать, что стало с его возлюбленной. Выяснилось, что Эмиль погиб, а Джемма всё-таки стала фрау Клюбер и родила пятерых детей. Старшая дочь одно лицо с той итальянской девушкой, что когда-то растопила сердце Санина. Дмитрий Павлович отправляет девушке крестик, когда-то подаренный ему её юной матерью.

                            Вывод:

                            Чтобы жизнь не умчалась без следа словно вешние воды, своё счастье нужно беречь и дорожить истинными чувствами, а не мимолётными вспышками страсти.
                            </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
        <div id="collapse6" class="collapse" aria-labelledby="heading6" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Александр Грибоедов</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Горе от ума</h5><a>Повесть</a><a>1824 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse6_1" aria-expanded="false" aria-controls="collapse6_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/5/p.1/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=f81467fb3f8ed4d3a2883889194a23c6-3572439-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse6_1" class="collapse" aria-labelledby="heading6_1">
                            <p style="border: 1px solid gray; padding: 3px;">Действие I<br> Дочь Фамусова, молодая девушка Софья Фамусова, влюблена в молодого человека Молчалина. Он служит секретарем Фамусова и живет в его доме. По ночам влюбленные тайно встречаются в комнате Софии. Служанка Лиза сторожит под дверью, чтобы Фамусов не застал их.   Однажды утром Фамусов видит, как Молчалин выходит от Софии. Старику кажется все это подозрительным, но все успокаивают его. В этот же день к Фамусовым приезжает Чацкий, молодой дворянин, их давний знакомый. Он 3 года путешествовал и только сегодня вернулся домой в Москву. Чацкий давно влюблен в Софию и надеется, что она осталась верна ему. Но Софья не рада Чацкому, потому что влюблена в Молчалина. Она боится сказать правду Чацкому.  Старик Фамусов видит, что у дочери есть два "ухажера" - Чацкий и Молчалин. Но отец хочет выдать ее за третьего "кандидата", полковника Скалозуба, богатого, уважаемого, но глуповатого "солдафона". <br>Действие II<br> Фамусов со слугой Петрушкой записывает свои дела в календарь. Входит Чацкий и беседует с Фамусовым. Чацкий придерживается новых, "прогрессивных" взглядов на жизнь. Он высмеивает людей, которые гонятся за чинами, деньгами и связями. Старику Фамусову не нравятся нападки Чацкого на "нормы" дворянской жизни, по которым живут все вокруг. В это время в гости к Фамусову приходит полковник Скалозуб. Хозяин принимает его с особым почтением, потому что надеется выдать за него Софию. Фамусов уводит Скалозуба в свой кабинет, чтобы Чацкий своими "странными" разговорами не испортил все дело. В это время Софья видит в окно, как ее любимый Молчалин падает с лошади. От волнения с ней случается обморок. По ее реакции Чацкий замечает, что Софии нравится Молчалин. Тут же выясняется, что Молчалин просто ушиб руку и нет причин волноваться. Все уходят. Оставшись наедине, Молчалин признается служанке Лизе в любви. Девушка осуждает его за то, что он обманывает Софию. Сама же Лиза, вероятно, любит слугу Петрушу и не отвечает взаимностью Молчалину.  <br>Действие III <br>Софья и Чацкий беседуют наедине. Из разговора Чацкий понимает, что Софья влюблена в Молчалина. Софья оставляет Чацкого, чтобы готовиться к очередному тайному свиданию с Молчалиным. Тем временем к Фамусову съезжаются гости на званый вечер: Наталья Дмитриевна Горич и ее муж Платон Михайлович Горич, князь Тугоуховский и его жена княгиня Марья Алексеевна, Загорецкий, Хлестова, графини Хрюмины и другие. Беседуя с одним из гостей, Софья в шутку говорит, что Чацкий - сумасшедший. Гость передает это замечание другим посетителям. В итоге все собравшиеся обсуждают "сумасшедшего" Чацкого. Когда в зал входит сам Чацкий, все гости уже смотрят на него как на сумасшедшего. <br> Действие IV <br>Вечер заканчивается, гости разъезжаются. В это время к Фамусовым вбегает Репетилов, старый знакомый Чацкого. Он зовет его в Английский клуб, но Чацкий отказывается. Оставшись один, Чацкий прячется в зале за колонной. Он слышит, как Молчалин снова признается Лизе в любви. Это признание слышит сама Софья. Она разоблачает обманщика Молчалина и прогоняет его. Тем временем Чацкий выходит из-за колонны и стыдит Софию за обман. В зал входит Фамусов. Он ругает дочь за "непристойное поведение" с мужчинами и обещает выслать ее в деревню. Фамусов запрещает Чацкому ухаживать за ней, но тот больше не намерен ухаживать за обманщицей Софией. Глупое Светское общество и измена Софии разочаровывают Чацкого. Он решает снова уехать из Москвы и просит карету. Конец.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
<div id="collapse7" class="collapse" aria-labelledby="heading7" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Михаил Лермонтов</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Герой нашего времени</h5><a>роман</a><a>1840 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse7_1" aria-expanded="false" aria-controls="collapse7_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/12/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=8d01a5f9ed8cd45265a1a4407af1954c-5233195-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse7_1" class="collapse" aria-labelledby="heading7_1">
                            <p style="border: 1px solid gray; padding: 3px;">Однажды, путешествуя по Кавказу, автор знакомится с офицером Максимом Максимычем. Тот рассказывает о своем знакомом, молодом офицере Григории Печорине.

Когда-то Максим Максимыч служил вместе с Печориным в крепости N на Кавказе. Здесь Печорин влюбился в местную красавицу Бэлу и украл ее из дома. Добившись любви Бэлы, Печорин вскоре начал скучать с ней. Вскоре Бэла погибла: ее убил разбойник Казбич.  На этом рассказ Максима Максимыча заканчивается. Автор и Максим Максимыч прощаются.

Вскоре они снова встречаются, уже во Владикавказе. Здесь они случайно видят Печорина, который едет в путешествие в Персию. Уезжая, Печорин оставляет Максиму Максимычу свои дневники. Тот решает избавиться от записок Печорина и отдает их автору романа. Некоторое время спустя автор узнает, что Григорий Печорин умер по дороге из Персии. Тогда автор решает опубликовать дневники Печорина.

Оставшаяся часть романа представляет собой дневники Печорина (“Журнал Печорина”). В них Печорин описывает события, произошедшие с ним до встречи с Бэлой: поездка в Тамань (где Печорин раскрывает банду контрабандистов), поездка в Пятигорск и Кисловодск (где Печорин знакомится с княжной Мери и убивает на дуэли Грушницкого), командировка в казачью станицу (где Печорин предсказывает смерть офицеру Вуличу).

В дневнике Печорин делится самыми сокровенными мыслями и переживаниями. Читателям становится ясно, что, несмотря на свое богатство, ум и красоту, Печорин — глубоко несчастный человек.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse8" class="collapse" aria-labelledby="heading8" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Максим Горький</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Мои университеты</h5><a>Повесть</a><a>1923 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse8_1" aria-expanded="false" aria-controls="collapse8_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/3221/p.1/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=217a15486df7f48e57388247d65f8b43-4538830-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse8_1" class="collapse" aria-labelledby="heading8_1">
                            <p style="border: 1px solid gray; padding: 3px;">Повествование краткого содержания «Мои университеты» Горького начинается с того, что Алексей Пешков, повзрослевший и определившийся с планами на жизнь, отправляется в Казань, чтобы поступить в университет. Эту идею в голову герою вложил Николай Евреинов, который видел у парня стремление к знаниям. Он посоветовал Пешкову пройти курс гимназии и пожить пока в их семье. Однако жизнь в доме друга не задалась.
                            Евреиновы жили втроем — мать и два сына. Денег не хватало. Алексей, чтобы не объедать вдову обитал в подвале, понимая, что университет — несбыточная мечта. В этот момент Пешков и понял, что человека формирует его сопротивление окружающей среде.
                            В гимназии юноша познакомился с Гурием Плетневым. Парень подрабатывал по ночам в типографии, а Пешков днями на пристани. Они вместе готовились к обучению, под этим предлогом Гурий и предложил своему новому другу поселиться у него. Дом оказался полуразрушенным, но очень населенным. Там обитало много бедных студентов, проституток. Спустя некоторое время Алексей знакомится с Андреем Деренковым. Он владел бакалейной лавкой. Андрей привлекал много людей, которые увлекались запрещенной литературой и имели революционные настроения. Деренков все свои деньги, которые получал от магазинчика, отдавал людям в качестве помощи за «народное счастье». Алексей устроился на работу в булочную Андрея. Там он месил тесто, пек хлеб, разносил его по квартирам. Заразившись настроением радикалов, Пешков вместе с булочками доставлял людям пропагандистские листовки о революции и свободе. Через некоторое время действия юноши начали вызывать подозрения городового, который хотел узнать, что задумал Деревенков. Алексей стал частым объектом допросов Никифорыча. В итоге городовой арестовал Плетнева, выследив его, и продолжал наблюдать за Алексеем. Парню пришлось быть осторожнее. Пешков пытался понять, как жить, в чем смысл его существования. Он изучал запрещенные книги, все больше заражаясь революционными идеями. Однако парень понимал, все бессмысленно. Пешков принял решение покончить жизнь самоубийством.
                            Пешков продолжал наблюдать за людьми, приходившими в булочную. Среди них особенно выделялся Михаил Ромась, которого все называли Хохол. Он вернулся из Якутии, где находился в ссылке. Ромась также был сторонником революции. Чтобы повлиять на умы людей, он открыл рыболовецкую артель, а главного героя пригласил в качестве помощника. Пешков узнал много о жизни Хохла, и сам воспрянул духом, ведь именно Ромась помог ему оправиться после неудачной попытки самоубийства.
                            Спустя время Ромась вместе с Пешковым арендовал у местного богача Панкова избу. Пешков смог увидеть, как живут люди в селе, и осознание не принесло удовлетворение. Мужики работали «как лошади», женщины из-за усталости жаловались на здоровье, парни грубо относились к девушкам, но те были рады даже такому общению. Хохла люди не жаловали, особенно староста и местные богачи. Его пытались убить, поджечь его и лавку с товаром. Это был последней каплей. Пешков старался спасти книги, но из-за взрыва бочки с керосином путь к отступлению оказался перекрыт. Ему ничего не оставалось, как обмотаться тулупом и выпрыгнуть в окно. Юноша остался цел, лишь слегка подвернул ногу. Ромась же решил уехать, поскольку спокойной жизни ему бы никто не дал. Алексею Хохол посоветовал никого не осуждать, сделав ударение на том, что все изменится к лучшему, рано или поздно. Встретились старые друзья только через пятнадцать лет. Завершается история Пешкова его отъездом на Каспийское море. Из села парень сбежал, лишившись друга и почувствовав себя потерянным. Крестьяне не принимали его, относились враждебно. Алексей пережил много приключений в дороге, но все-таки добрался до Каспия, где начал работать в рыболовецкой артели.
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse9" class="collapse" aria-labelledby="heading9" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Михаил Булгаков</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Собачье сердце</h5><a>Повесть</a><a>1925 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse9_1" aria-expanded="false" aria-controls="collapse9_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://azbyka.ru/fiction/sobache-serdce-bulgakov/'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=73fe128620990d80127a6eaed156761e-6311157-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse9_1" class="collapse" aria-labelledby="heading9_1">
                            <p style="border: 1px solid gray; padding: 3px;">Уличного пса Шарика, замерзавшего в подворотне, привёл в свою семикомнатную квартиру профессор Преображенский, открывший способ омоложения организма. К нему приходят члены домкома с требованием освободить две комнаты для вселения в них людей, нуждающихся в жилплощади. Профессор получает броню на квартиру, позвонив своему высокопоставленному пациенту. Профессор и его ассистент доктор Борменталь, обедая, слышат революционные песни, которые поют «жилтоварищи», пришедшие на общее собрание. Профессор возмущён беспорядками в доме и прогнозирует ещё большие катаклизмы. Причём утверждает, что всё это происходит из-за разрухи в головах пролетариев. Профессор с доктором в порядке эксперимента заменили мозговой придаток (гипофиз) Шарика на человеческий (от алкоголика Клима Чугункина, убитого в пьяной драке). Умный и доброжелательный пёс постепенно стал превращаться в человека, а именно в Чугункина, со всеми его недостатками. Председатель домкома Швондер посоветовал этому существу взять имя и отчество, а фамилию тот решил принять «наследственную». Таким образом, он стал называться Полиграфом Полиграфовичем Шариковым. Получив с помощью Швондера паспорт, Шариков устроился на должность заведующего подотделом по очистке города от бродячих животных и с удовольствием стал собственноручно душить ненавистных ему котов. Пользуясь служебным положением, Шариков добивается у своей подчинённой согласия быть его женой, приводит её в квартиру Преображенского. Тот раскрывает барышне кто на самом деле Шариков, и она, рыдая, уходит. Старый профессор, видя ужасный результат медицинского эксперимента, признал свою ошибку. Шариков своим бескультурьем и безнравственностью сделал жизнь Преображенского ужасной. Донос Шарикова на профессора, переполнил у того чашу терпения, и он посредством операции снова превратил Полиграфа Полиграфовича в пса Шарика, который стал жить в профессорской квартире.

                        </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse10" class="collapse" aria-labelledby="heading10" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Вильям Козлов</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 265px'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Президент каменного острова</h5><a>Повесть</a><a>1964 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse10_1" aria-expanded="false" aria-controls="collapse10_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://mir-knig.com/read_175191-1'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://knigirossii.ru/pictures/5/73/4852708_sbig.jpg" class="jpg" style='height: 265px'>
                        </div>

                    </div>
                    <div id="collapse10_1" class="collapse" aria-labelledby="heading10_1">
                            <p style="border: 1px solid gray; padding: 3px;">Повесть «Президент Каменного острова» — о юности послевоенного поколения, которая хоть и протекает под мирным небом Родины, но для многих омрачена смертельным дыханием минувшей войны. Так, двое главных действующих лиц повести — Гарик и Сорока — сироты. Военная тема и здесь нашла свое место, современность переплетается с событиями прошлого: неприступный остров посреди большого озера притягивает любопытство приехавших на отдых ребят своей героической историей, а главное, таинственной, окутанной ореолом романтики деятельностью расположившихся там ребят из интерната, живо интересующихся подвигами своих отцов и дедов и свято чтящих память о них. Ближе узнавая Сороку и его товарищей, приезжие мальчишки, а вместе с ними и читатели проникаются глубоким сочувствием к их следопытской работе, к дружеской связи с героями войны, с летчиками, к тому, как эти ребята готовят себя к активной взрослой жизни.</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 265px'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Президент не выходит в отставку</h5><a>Повесть</a><a>1979 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse10_2" aria-expanded="false" aria-controls="collapse10_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://libking.ru/books/child-/children/29359-vilyam-kozlov-prezident-ne-uhodit-v-otstavku.html#book'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=cdf1d85dc79e4cde358d31b02ae51e08-5888278-images-thumbs&n=13" class="jpg" style='height: 265px'>
                        </div>

                    </div>
                    <div id="collapse10_2" class="collapse" aria-labelledby="heading10_2">
                            <p style="border: 1px solid gray; padding: 3px;">Продолжение популярной повести «Президент Каменного острова», в которой автор, известный ленинградский писатель, прослеживает дальнейшие судьбы основных героев — Сорокина и его друзей, окончивших школу, вступивших в большую жизнь.<br>
                            Является продолжением книги "Президент Каменного острова".
                            </p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Волосы Вероники</h5><a>Роман</a><a>1988 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse10_3" aria-expanded="false" aria-controls="collapse10_3"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://libking.ru/books/prose-/prose-contemporary/531282-vilyam-kozlov-volosy-veroniki.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=4127208aae7c13365f02a43c3fbbce32-5292620-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse10_3" class="collapse" aria-labelledby="heading10_3">
                            <p style="border: 1px solid gray; padding: 3px;">Произведение было выпущено в 1988 году, как раз в эпоху открытой любви в советском союзе. Автор пишет вполне "советским языком", т. е. показывает жизнь советских людей. Быт, увлечения, дружба, отдых и конечно, как любили люди.

                            Действие ведется от лица Георгия Шувалова. Это мужчина возраста чуть больше 40 лет, является начальником переводчиков в НИИ. Его можно охарактеризовать как вполне спокойную личность. Вокруг него вьются судьбы людей, бурлит окружающая его жизнь, но он все равно остается спокойным и адекватным человеком.

                            Автор хочет донести до нас смысл жизни советских людей, а это - любовь. Может, в то время любили люди по-другому, однако эта история зайдет в душу многим читателям.

                             </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

        <div id="collapse11" class="collapse" aria-labelledby="heading11" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Василь Быков</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Сотников</h5><a>Повесть</a><a>1969 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse11_1" aria-expanded="false" aria-controls="collapse11_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/PROZA/BYKOW/sotnikov.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=b5baea70be03526de74c30dbfb4be7be-5490194-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse11_1" class="collapse" aria-labelledby="heading11_1">
                            <p style="border: 1px solid gray; padding: 3px;">
                            Военное время. Двух разведчиков -

                            Сотникова и Рыбака - командир отправляет в хутор, чтобы добыть провизию для отряда, затаившегося в лесу. Староста хутора дал им овечку. В дороге они попадаются немцам, Сотникова, и так больного, ранят в ногу, но им удается скрыться. Они находят ближайший дом и входят, их кормит девчушка.

                            В доме с ней еще два ребенка. Вскоре приходит их мать — Демчиха, она не рада партизанам, но обрабатывает Сотникову раны. Приходят немцы и забирают не только мужчин, но и женщину. Сотников всячески пытается выгородить Демчиху, Рыбак обвиняет во всем товарища.

                            Их допрашивают и пытают, Рыбак рассказывает всё, Сотников и Демчиха держатся. Рыбаку предлагают стать полицаем, он соглашается, чтобы спастись.

                            Утром назначают казнь. Рыбаку приказано вести товарищей на эшафот, Сотникова, Демчиху и Старосту вешают. Рыбак понимает, что пути назад нет, он хочет повеситься и сам, но у него нет ремня, теперь ему не вернуться к своим.


                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Знак беды</h5><a>повесть</a><a>1982 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse11_2" aria-expanded="false" aria-controls="collapse11_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/PROZA/BYKOW/disaster.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=8bbddaf74cb8c9ae720efee124fac87f-4730430-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse11_2" class="collapse" aria-labelledby="heading11_4">
                            <p style="border: 1px solid gray; padding: 3px;">На хуторе Яхимовщина жили Петрок и Степанида Богатька. Сын их служил в армии, а дочь училась в Минске. Когда началась война, и фронт откатился на восток, на хуторе расположился немецкий офицер со своей командой. Хозяева стали жить в истопке. Немцы устроили разгром хозяйства. Степанида выкрала у них винтовку и бросила в колодец. Немцы застрелили немого мальчика, подошедшего к хутору. На следующий день они с хутора уехали. Степанида вспоминает, как в Выселках организовали колхоз, как она с мужем ухаживала за землёй, которую им выделили на пригорке. Петрок поставил там крест, чтобы отвести от земли беды, и люди прозвали то место Голгофой. Полицай Гуж приказал Петроку идти достраивать мост. Работа была невыносима, и Петрок сделал самогон, чтобы откупиться от полицаев. Но те требовали всё больше и больше самогона и избили хозяев до полусмерти. Петра утащили в Выселки в полицию. Степанида, чтобы отомстить полицаям и немцам, решила взорвать мост. Она выменяла бомбу на поросёнка у Корнилы, который увёз к себе неразорвавшуюся бомбу. Степанида закопала её. Она надеялась, что найдёт со временем кого-нибудь, кто бы наладил эту бракованную бомбу. Увидев, что Корнилу арестовали полицаи, Степанида перепрятала бомбу. Полицаи стали ломиться к ней в истопку, требуя, чтобы она сказала, где бомба. Степанида облила помещение бензином и подожгла. Полицаи разбежались, опасаясь взрыва, а Степанида погибла, «но бомба дожидалась своего часа» — так заканчивается повесть.

                            </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse12" class="collapse" aria-labelledby="heading12" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Фёдор Достоевский</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Белые ночи</h5><a>Повесть</a><a>1848 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse12_1" aria-expanded="false" aria-controls="collapse12_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://ilibrary.ru/text/29/p.1/index.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=0b06157448a41d87f63f2968562b70cb-5348391-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse12_1" class="collapse" aria-labelledby="heading12_1">
                            <p style="border: 1px solid gray; padding: 3px;">Молодой человек, главный герой повести, робок, одинок, живет мечтами. Однажды петербургской ночью он встречает плачущую девушку. Она живет со слепой бабушкой, их дни не веселы и однообразны. Жилец, который снимал мезонин у Настиной бабушки, проявил к девушке сострадание и сочувствие.

                            Настя влюблена и готова уехать с молодым человеком. Постоялец объяснил, что сначала должен устроить свои дела. Через год он вернется, и молодые люди смогут пожениться. Настя ждет возлюбленного, но на обещанную встречу молодой человек не приходит.

                            Настя решается ответить на чувства главного героя, но внезапно встречает возлюбленного. Она убегает от мечтателя, написав письмо с извинениями. Мечты о счастье не сбылись, мечтатель вновь одинок.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse13" class="collapse" aria-labelledby="heading13" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Виталий Закруткин</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Матерь человеческая</h5><a>Повесть</a><a>1969 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse13_1" aria-expanded="false" aria-controls="collapse13_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://libking.ru/books/prose-/prose-military/308808-vitaliy-zakrutkin-mater-chelovecheskaya.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=2ef4be89e7f7fd40ec97733e002c0b45-5228667-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse13_1" class="collapse" aria-labelledby="heading13_1">
                            <p style="border: 1px solid gray; padding: 3px;">В сентябре 1941 года гитлеровские войска далеко продвинулись в глубь советской территории. Многие области Украины и Белоруссии оказались оккупированными. Остался на занятой немцами территории и затерянный в степях хуторок, где счастливо жили молодая женщина Мария, её муж Иван и их сын Васятка.

                            Захватив ранее мирную и обильную землю, фашисты все разорили, спалили хутор, угнали людей в Германию, а Ивана и Васятку повесили. Одной Марии удалось спастись. Одинокой, ей пришлось бороться за свою жизнь и за жизнь своего будущего ребёнка.

                            Дальнейшие события повести раскрывают величие души Марии, ставшей воистину Матерью человеческой. Голодная, измученная, она совершенно не думает о себе, спасая девочку Саню, смертельно раненную фашистами.

                            Саня заменила погибшего Васятку, стала частичкой той жизни Марии, которую растоптали фашистские захватчики. Когда девочка умирает, Мария едва не сходит с ума, не видя смысла своего дальнейшего существования. И все же она находит в себе силы для того, чтобы жить.

                            Испытывая жгучую ненависть к фашистам, Мария, повстречав раненого молодого немца, исступлённо кидается на него с вилами, желая отомстить за сына и за мужа. Но немец, беззащитный мальчик, крикнул: «Мама! Мама!» И сердце русской женщины дрогнуло. Великий гуманизм простой русской души предельно просто и ясно показан автором в этой сцене.

                            Мария ощущала свой долг перед людьми, угнанными в Германию, поэтому стала собирать урожай с колхозных полей не только для себя, но и для тех, кто, может быть, ещё вернётся домой. Чувство исполняемого долга поддерживало её в тяжёлые и одинокие дни.

                            Скоро у неё появилось большое хозяйство, потому что на разграбленное и сожжённое подворье Марии стекалось все живое. Мария стала как бы матерью всей окружающей её земли, матерью, похоронившей мужа, Васятку, Саню, Вернера Брахта и совсем незнакомого ей, убитого на передового политрука Славы. Мария смогла принять под свой кров семерых ленинградских сирот, волею судеб, занесённых на её хутор.

                            Так и встретила эта мужественная женщина советские войска с детьми. И когда в сожжённый хутор вошли первые советские солдаты, Марии показалось, что она родила на свет не только своего сына, но и всех обездоленных войной детей мира…</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse14" class="collapse" aria-labelledby="heading14" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Оноре де Бальзак</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Евгения Гранде</h5><a>Роман</a><a>1833 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse14_1" aria-expanded="false" aria-controls="collapse14_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/INOOLD/BALZAK/egrande.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=84d00753a153497299fc2ff787266086-5309995-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse14_1" class="collapse" aria-labelledby="heading14_1">
                            <p style="border: 1px solid gray; padding: 3px;">В жизни провинциального землевладельца Гранде, бывшего крестьянина, разбогатевшего после Французской революции, нет иных привязанностей, кроме золота. Он ведёт практически нищенский образ жизни, этому же вынуждена следовать его семья, которую он тиранит и которой сочувствуют все местные жители, но никто не знает истинных размеров его состояния. За перспективу получить руку Евгении, единственной наследницы сельского магната, идёт вялотекущая война между местными почтенными семействами. Все меняется, когда в доме старика Гранде появляется парижанин Шарль, сын его брата, парижского банкира; он поражает местное общество и кузину Евгению светским блеском и модными нарядами, галантностью покоряет сердце наивной провинциалки. Но ему приходится уезжать в Индию — его отец банкрот. Евгения тайно передаёт ему свои скромные ценности, вызывая двойной гнев отца — тем, что она отдала нищему парижскому прощелыге и своё сердце и его золото. Через некоторое время Гранде умирает, перед этим загнав в могилу супругу. Евгения остаётся одна и продолжает вести дела отца, Шарль же, нажившись на работорговле в колониях, решается на двойное предательство — он обманывает кредиторов отца и не желает платить по его долгам, и пишет Евгении Гранде о том, что его юношеская влюблённость в неё прошла (вместо этого он мечтает выгодно породниться со знатным семейством). Унаследовавшая железный характер отца Евгения мстит кузену и несостоявшемуся жениху: посылает в Париж одного из своих сомюрских воздыхателей с миссией — заплатить долги своего дяди и выкупить у Шарля золотые вещицы, когда-то отданные ею и послужившие началом его обогащения. Посланец все исполняет быстро и в точности, воодушевлённый обещанием Евгении после завершения выйти за него замуж, о чем и сообщает Шарлю, окончательно добив того сообщением, что бедная сомюрская девушка унаследовала от скряги-отца почти двадцать миллионов.

</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Отец Горио</h5><a>Роман</a><a>1832 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse14_2" aria-expanded="false" aria-controls="collapse14_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/INOOLD/BALZAK/gorio.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=34e83351cf6ef135f0f9fe7c64d6b4cb-5905127-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse14_2" class="collapse" aria-labelledby="heading14_2">
                            <p style="border: 1px solid gray; padding: 3px;">Студент-юрист Растиньяк, бедный провинциал, живёт в Париже в пансионе Воке. Среди его соседей — бывший торговец мукой папаша Горио, которого все высмеивают за нищету и жалкий вид. Оказывается, что он блестяще выдал двух своих дочерей замуж — Анастази за графа де Ресто, Дельфину за банкира де Нусингена, дав каждой приданое в 800 тыс. франков.

                            Среди других обитателей пансиона Воке — 40-летний Вотрен, харизматичный и загадочный, а также студент-медик Бьяншон. Растиньяк желает войти в высший свет, и в этом ему помогают родственные связи со светской львицей виконтессой де Боссеан. Он знакомится с сёстрами и узнаёт, что они стыдятся своего отца и обращаются к нему, только когда им нужны деньги. Горио, однако, беззаветно любит дочерей и готов ради них на любые жертвы.

                            Вотрен пытается склонить Растиньяка к браку по расчёту с богатой наследницей, юной девицей, но Растиньяк отказывается от его искушений, думая пробиться собственными силами. В итоге Вотрен оказывается беглым каторжником по прозвищу «Обмани смерть» и его арестовывает полиция.

                            Растиньяк же становится любовником баронессы де Нусинген. Тем временем Анастази в поисках денег, чтобы заплатить долги своего любовника Максима де Трай, доводит отца до инсульта. Дельфина не настолько жестока, но также очень небрежна и эгоистична. Горио в течение нескольких дней умирает, брошенный детьми, за ним ухаживают Растиньяк и Бьяншон на свои последние студенческие гроши.

                            Роман заканчивается сценой, где Растиньяк смотрит с горы на светящийся ночными огнями Париж и бросает ему вызов: « А теперь — кто победит: я или ты!».

                            Действие книги начинается в июне 1819 года и происходит параллельно со второй частью романа «Гобсек», многие из событий которого отражаются в «Отце Горио». В обеих книгах второстепенным персонажем является графиня Анастази де Ресто и её муж, и их поступки в «Отце Горио» не всегда понятны без знания романа «Гобсек».</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse15" class="collapse" aria-labelledby="heading15" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Алексей Каплер</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Двое из 20 миллионов</h5><a>Повесть</a><a>1984 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse15_1" aria-expanded="false" aria-controls="collapse15_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/PROZA/KAPLER/dwoe.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://filed8-26.my.mail.ru/pic?url=https%3A%2F%2Fcontent-27.foto.my.mail.ru%2Fmail%2Fms.bayorene%2F_musicplaylistcover%2Fi-3822.jpg&mw=&mh=&sig=8bd7cb33df8be227b10ce882c0bb25f9" class="jpg">
                        </div>

                    </div>
                    <div id="collapse15_1" class="collapse" aria-labelledby="heading15_1">
                            <p style="border: 1px solid gray; padding: 3px;">Выпускник летного училища Сергей и совсем еще юная медсестра Маша. Их любовь зародилась в том подземном аду, в самое неподходящее для того время. Они, как тысячи других узников, были обречены.

                            Но однажды Маша, уставшая от стонов умирающих и собственной беспомощности, не выдержала, выбралась из каменоломни. И пошла колодцу, на который был круглые сутки нацелен немецкий автомат. Она шла открыто, не таясь…

                            Случилось чудо. Несколько секунд в голове немецкого автоматчика происходила борьба между «чувством долга» и жалостью к изможденной человеческой фигурке. Последнее победило. Немец не выстрелил. Через несколько минут Маша вернулись в каменоломню с полным ведром. Спасла себя, Сергея и еще кого-то из тех сорока восьми…

                            Акция Рассрочка на 90 дней без процентов - для постов -1
                            А после Каплер рисует черно-белую картину жизни, которая с каждым годом обретает цвета. Да, Маша, засыпая, нередко оказывается в керченских каменоломнях, но, просыпаясь, видит мирное небо над головой…и продолжает жить. Позади Великая Победа, голодный карточный сорок шестой. И рядом всегда Сергей, который в самые трудные минуты напоминает: «Подумай! Мы живы!». 

                             

                            И вот уже тридцать лет прошло. В квартире Марии и Сергея дети, внуки, фронтовые друзья. Празднуют День Победы. Салют. Застольные речи. Смех…

                            Дойдя до этого места, немного забываешь о том, с чего начиналась эта история любви. А потому концовка повести пробирает до мурашек.

                            Автор возвращает нас в 1942-й, в Аджимушкайские каменоломни.

                            Чуда не случилось. Немец не сжалился. </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse16" class="collapse" aria-labelledby="heading16" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Борис Васильев</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Завтра была война</h5><a>Повесть</a><a>1987 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse16_1" aria-expanded="false" aria-controls="collapse16_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://revdabiblios.ru/f/bvasilyev_zavtra_byla_voyna.pdf'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://alifba.ru/storage/img/products/139540/cover.jpg" class="jpg">
                        </div>

                    </div>
                    <div id="collapse16_1" class="collapse" aria-labelledby="heading16_1">
                            <p style="border: 1px solid gray; padding: 3px;">1940 год. В центре сюжета — Искра Полякова, староста 9 «Б» класса, живущая вдвоём с матерью, принципиальным партработником, фанатично преданной партии. Искра — убежденная комсомолка, её идеалы нерушимы, а идеи прозрачны и, как ей кажется, правильны. Собравшись на дне рождения одного из одноклассников, Искра слушает стихи Есенина, которые читает её подруга Вика, дочь известного в городе человека, директора авиазавода Леонида Люберецкого. Искре нравится поэзия Есенина, но она считает его чуждым советской культуре «кабацким певцом». Вика даёт однокласснице книгу и объясняет Искре, что Есенин — не «упаднический» поэт, а чувства — неотъемлемая часть жизни. Проходит несколько дней. Искра знакомится с отцом Вики, начинает глубже понимать некоторые вещи, задаёт вопросы матери и самой себе, пытаясь разобраться в понятиях справедливости, долга и счастья.

                            Искра принимает ухаживания бывшего одноклассника Сашки Стамескина, которого Люберецкий устраивает к себе на завод.
                            Внезапно всё меняется: в один из вечеров ребята узнают, что директор завода Люберецкий арестован по подозрению во вредительской деятельности против СССР.

                            Искра решает поддержать подругу, несмотря на предупреждение матери о возможных репрессиях. Завуч школы Валентина Андроновна вызывает Люберецкую в кабинет и сообщает, что завтра на школьной линейке та должна будет публично отречься от своего отца — врага народа, но Вика отказывается. После этого завуч приглашает в кабинет Полякову и просит её созвать собрание и с позором изгнать Люберецкую из комсомола. Искра сообщает завучу, что никогда не сделает этого, и от волнения падает в обморок. Директор школы уносит девочку в медкабинет и хвалит за проявление человечности.

                            Узнав о стойкости подруги и преданности своих школьных друзей, Вика приглашает ребят на пикник. За городом она признаётся в любви своему однокласснику Жоре Ландысу, и они впервые целуются. Утром Вика не приходит на объявленное комсомольское собрание. Когда завуч посылает за ней одноклассницу Зину, та возвращается в полуобморочном состоянии и сообщает классу, что «Вика в морге». Искру вызывают к следователю и сообщают, что Люберецкая покончила с собой, оставив две предсмертные записки, в том числе одну, адресованную персонально Поляковой. Викины одноклассники узнают, что хоронить девочку некому, и решают заняться погребением самостоятельно.

                            Мать Искры просит не читать речей и не устраивать панихиду, называя самоубийство Люберецкой поступком «хлюпика», однако девушка идёт наперекор воле матери и, впечатлившись речью директора школы на кладбище, читает над могилой подруги её предсмертную записку и стихи Есенина. За похоронами дочери Люберецкого следит на расстоянии Сашка Стамескин. Он беспокоится о будущей карьере и не решается открыто посетить похороны дочери врага народа. О прочитанных Искрой стихах узнаёт её мать и устраивает скандал, пытаясь применить силу, однако Искра сообщает, что если та ещё раз поднимет на неё руку, то она уйдёт навсегда, несмотря на всю любовь к ней. Похороны Вики не проходят бесследно и для директора школы — его увольняют.

                            Проходит ещё один месяц. Шок от смерти Вики Люберецкой понемногу утихает. После праздничной демонстрации в честь 7 Ноября 9 «Б» навещает бывшего директора. У него дома ребята узнают, что его, героя Гражданской войны, исключают из партии.

                            Школьники пишут сочинение, и в это время становится известно, что Леонид Люберецкий оправдан и вернулся домой. Класс срывается с места и спешит к нему домой. Ребята находят Люберецкого в квартире, всё ещё помнящей обыск НКВД. «Какой тяжёлый год», — говорит отец Вики. В порыве чувств одноклассница Искры Зина бросается ему на шею и говорит, что год печальный потому, что он високосный, а следующий, 1941 год, будет очень счастливым.

                            В следующем кадре появляются марширующие по улицам солдаты Красной армии в сопровождении песни «Священная война». Звучит эпилог, раскрывающий судьбы главных героев, учеников 9-го «Б»: лётчик Жора Ландыс посмертно получил звание Героя Советского Союза, Артём Шефер и Паша Остапчук погибли во время войны, а Искра Полякова, будучи во время оккупации связной в антифашистском подполье, которое возглавлял бывший директор школы, была схвачена немцами и повешена вместе с матерью.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

        <div id="collapse17" class="collapse" aria-labelledby="heading17" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Александр Вампилов</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Старший сын</h5><a>Пьеса</a><a>1975 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse17_1" aria-expanded="false" aria-controls="collapse17_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/PXESY/WAMPILOW/vampilov1_1.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=7b919dace48f4803219ded5f744414df-3593759-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse17_1" class="collapse" aria-labelledby="heading17_1">
                            <p style="border: 1px solid gray; padding: 3px;">Двое незадачливых молодых людей — студент Владимир Бусыгин и его случайный приятель Семён Севостьянов по прозвищу Сильва — провожают двух девушек, с которыми только что познакомились в кафе, домой в пригород, в надежде на продолжение отношений. Получив отказ, бегом возвращаются на станцию, но последнюю электричку упускают, опоздав на считанные секунды. Оказавшись холодной осенней ночью в чужом городке, они пытаются напроситься к кому-нибудь переночевать, но безуспешно.

                            На той же электричке, на которой приехали Владимир и Семён с девушками, домой возвращается молодая женщина Наталья. Её встречает живущий по соседству старшеклассник Васенька, который влюблён в Наталью, но та непреклонна: она заметно старше Васеньки и, будучи секретарём районного суда, насмотрелась на разводы. Из-за неразделённой любви Васенька собирается уйти из дома, сначала конфликтует с сестрой, потом с отцом. Бурное выяснение отношений отца и сына увидели с улицы Бусыгин и Сильва. Отец идёт поговорить с Натальей, постучавшись в дверь, представляется. Находящиеся рядом Владимир и Семён услышали его имя и по-своему поняли, зачем мужчина пошёл ночью к молодой женщине. Владимиру приходит в голову авантюрная идея — назваться внебрачным сыном хозяина квартиры и таким образом решить проблему с ужином и ночлегом.

                            Андрей Григорьевич Сарафанов, музыкант-кларнетист, воспитавший без жены двоих детей, сознаётся сыну, что до знакомства с мамой Васеньки и его сестры Нины у музыканта были мимолётные романы, и он признаёт в неожиданном госте своего внебрачного сына. Реакция Сарафанова так искренна и трогательна, что во Владимире пробуждается совесть. Кроме того, сам он рос без отца. Он не может обманом отвечать на такое доверие и понимает, что проблемы этой семьи ему небезразличны.

                            Чтобы скоротать время, Сильва тайком от Васеньки начинает успешно ухаживать за Натальей. Бусыгин влюбляется в Нину, но поскольку он — «брат», то открыто признаться ей не может и мучается, ревнуя её к жениху, авиационному радиоинженеру.

                            Не выдержав, Владимир признаётся во всём Нине, которая тоже прониклась к нему симпатией. Они размышляют, как сообщить Андрею Григорьевичу. В этот момент появляется Сильва: Васенька, обнаружив его в гостях у Натальи, из ревности пытался поджечь её дом. Между Сильвой и Бусыгиным вспыхивает ссора, и Сильва в отместку сообщает отцу Сарафанову правду. Владимир вынужден во всём сознаться. Андрей Григорьевич отказывается в это верить, искренне полюбив своего «старшего сына», и прощает ему этот обман.</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Прощание в июне</h5><a>Пьеса</a><a>1964 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse17_2" aria-expanded="false" aria-controls="collapse17_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/PXESY/WAMPILOW/vampilov_proshanie.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=7a1f347c42f5a6e44dc64742e59d0e38-5576139-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse17_2" class="collapse" aria-labelledby="heading17_4">
                            <p style="border: 1px solid gray; padding: 3px;">Действие первое<br>Первая встреча Тани и Колесова происходит на автобусной остановке, возле афишной тумбы с портретом эстрадной певицы Голощёкиной. Колесов почти с ходу приглашает приятную незнакомку на свадьбу к друзьям, называет адрес, но Таня отказывается.

Затем действие переносится в студенческое общежитие, где за накрытыми столами сидят жених и невеста — Маша и Букин, а также их многочисленные друзья. Все ждут Колесова, который обещал «прийти с самой симпатичной девушкой в городе».

Вскоре в комнате появляется ректор Репников, совершающий обход общежития. Внезапно распахивается окно, в комнату впрыгивает Колесов и, не заметив ректора, бросается к выключателю. Потушив свет, он объясняет, что за ним гонится милиция. Оказывается, он пришёл в гостиницу, где остановилась певица Голощёкина, чтобы пригласить эстрадную диву на свадьбу, но повздорил с одним из музыкантов и, как позже пояснил милиционер, «нанёс ему телесные повреждения».

Колесова уводят. Репников даёт понять, что дебоширу грозит отчисление.

В этот момент в комнате появляется Таня.

Получив 15 суток, Колесов «отбывает срок» вдвоём с Золотуевым — 58-летним мужчиной, которого наказали за то, что он на городской площади выкопал орхидею для своей дачи. Милиционер приводит их на кладбище и указывает на старую ограду, которую нужно разобрать. Едва «арестанты» нехотя приступают к работе, как появляются Маша и Таня. Они приносят плохие вести: приказа об отчислении пока нет, но ректор говорит, что всё уже решено. При этом Таня признаётся, что из-за Колесова она поссорилась с отцом.

Спустя несколько дней Колесов сам приходит домой к Репникову, чтобы объяснить, что давно занимается серьёзной научной работой, а отчисление в канун государственных экзаменов — это для начинающего учёного серьёзная потеря времени. Разговор складывается нервно, ректор фактически выставляет визитёра из квартиры.

Таня в знак протеста уходит из дома.

<br>Действие второе<br>
Понимая, что возвращение в вуз не состоится, Колесов соглашается работать сторожем-садовником на даче у Золотуева. Здесь его и находит Таня, которая всю ночь бродила одна по городу. Молодые люди переходят на «ты» и договариваются встретиться вечером.

Их свиданию предшествует появление Репникова. Ректор просит, чтобы Колесов оставил его дочь в покое, обещая взамен получение диплома. Весь день Колесов пребывает в рассеянной задумчивости. Когда Таня приходит, он объявляет, что встреч у них больше не будет.

На выпускном вечере Колесов чувствует себя неуютно и прибытие на торжество Тани воспринимает поначалу холодно. Его волнует вопрос, сможет ли девушка простить, если узнает, что стала предметом торга.

Между тем торг продолжается: Репников, видя, что молодых людей тянет друг к другу, предлагает Колесову поступление в аспирантуру — в обмен на окончательный разрыв с Таней. Колесов решает всё рассказать девушке. Она ошеломлена: «Ты выиграл время, теперь ты своего добьёшься… Всё будет по-твоему… Без меня».

После Таниного ухода Колесов на глазах у однокурсников рвёт свой диплом и бросает его на стол: «Я за него заплатил».

В конце пьесы Колесов ждёт Таню на той же самой улице, где они познакомились. Он вновь приглашает девушку на свидание, она отвечает: «Счастливо оставаться».</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>


<div id="collapse18" class="collapse" aria-labelledby="heading18" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Галина Щербакова</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h4>Вам и не снилось</h4><a>Повесть</a><a>1975 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse18_1" aria-expanded="false" aria-controls="collapse18_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='https://mir-knigi.info/books/proza/sovremennaya-proza/50206-vam-i-ne-snilos-shcherbakova-galina-nikolaevna-259876.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=92d62efbef1783ce6c285c2be6285a34-5526617-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse18_1" class="collapse" aria-labelledby="heading18_1">
                            <p style="border: 1px solid gray; padding: 3px;">В преддверии нового учебного года в одну из столичных новостроек поселяется Юлька (ученица 9 класса), ее мать Людмила Сергеевна (привлекательная женщина в возрасте сорока лет) и отчим Владимир (он был младше своей супруги).

                            Учась в школе, у Людмилы Сергеевны случился роман с парнем Костей Лавочкиным. Она рассталась с ним ради летчика, за которого потом вышла замуж и родила от него Юльку. Костя тяжело все это переживал, и хоть у него самого уже была семья, он все так же приходил к своей любимой. В один из скандалов связанных с изменами мужа, Людмила Сергеевна прогнала его, и у Константина появился лучик надежды на то, что они будут вместе с любимой. Людмила Сергеевна отвергает Костю и не хочет никаких с ним отношений.

                            В первый день учебного года, Юлька пришла в новый для себя класс. В этом классе был ученик – Роман, сын Константина. Ребята начинают дружить и их дружеские отношения перерастают в светлое и искреннее чувство – любовь. Вера (жена Кости) заботится о заболевшем и ослабшем муже, Людмила Сергеевна в ожидании пополнения семьи, а ребята в итоге остались на какое-то время без должного присмотра.

                            После появления сына на свет, Людмила Сергеевна придя в школу на родительское собрание, была ошарашена новостью, что в классе с ее дочерью учится и дружит с ней сын Кости Лавочкина. Мать Ромы рада новости, что у Юльки родился брат, это значило, что Костя не нужен совсем Людмиле Сергеевне, но в тоже время она приходит в шоковое состояние, узнав, что Рома и Юлька дружат.

                            По окончании девятого класса, мальчишек отправляют на практику, а девочки остаются в городе. Вера пришла провожать сына и видит Рому и Юльку вместе, ее это не радует, она принимает решение перевести мальчика в другую школу. Людмила Сергеевна тоже не в восторге от дружбы и общения ребят, но пытается спокойно относиться к этому.

                            По возвращению домой, Рома узнает, что его перевели в другую школу и относится к этому резко негативно, но все же уступает матери.

                            Юля, узнав о переводе парня в другую школу, делает вывод, что их хотят разлучить. Рома делает все, что бы успокоить девушку. Учитель ребят объясняет директору школы, что их нельзя разлучать, но тот в свою очередь становится на сторону Веры.

                            Вера узнает, что дети все равно встречаются и решает отправить сына в Ленинград обманным путям, для ухода за якобы больной бабушкой. Вера считает, что Юлька недостойна ее сына и она его, таким образом, спасает.

                            Ребята пишут друг - другу письма, но они не доходят до адресата. Юля принимает решение лететь в Ленинград, а Рома вернувшись раньше со школы, понимает, что его обманывали и бабушка здорова. Закрывшись в комнате, он грозится убить себя. В этой же комнате он находит письма отправленные Юльке и выпрыгивает в окно, но не удачно. В этот момент во дворе появляется Юля.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

        <div id="collapse19" class="collapse" aria-labelledby="heading19" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Виктор Гюго</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height:  280px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Человек, который смеётся</h5><a>Исторический роман</a><a>1860 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse19_1" aria-expanded="false" aria-controls="collapse19_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/INOOLD/GUGO/laughman.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=c2b633448f468aededf252d70b58247c-3948343-images-thumbs&n=13" class="jpg" style='height:  280px'>
                        </div>

                    </div>
                    <div id="collapse19_1" class="collapse" aria-labelledby="heading19_1">
                            <p style="border: 1px solid gray; padding: 3px;">
                            Точкой отсчёта в сюжете романа является 29 января 1690 года, когда с острова Портленд скрывается на корабле шайка компрачикосов. Они — торговцы детьми, превращающие тех в уродов для потехи публики. Ещё недавно их деятельность поощрялась обществом и правительствами, но теперь они объявлены преступниками и преследуются. На берегу остается брошенный компрачикосами ребёнок.

                            Преодолевая холод, смертельную опасность и страх, ребёнок спасает слепую девочку-младенца. Столкнувшись с человеческим равнодушием, он находит приют в возке Урсуса, бродячего актёра, лекаря и философа.

                            В то же время корабль компрачикосов, застигнутый бурей, начинает тонуть. В качестве жеста покаяния они бросают в море бутылку с признанием в своих преступлениях.

                            Действие продолжается спустя 15 лет, в 1705 году. Урсус стал отцом и учителем для превратившейся в прекрасную девушку Деи и выросшего Гуинплена. Изуродованное компрачикосами лицо, с «ртом, открывающимся до ушей, ушами, загнутыми до самых глаз, бесформенным носом, …, и лицом, на которое нельзя было взглянуть без смеха», позволяет Гуинплену и его названной семье выручать у веселящейся публики достаточно для жизни. Несмотря на своё уродство и вызываемые им насмешки, Гуинплен был счастлив и был способен на сострадание к другим людям. Молодой человек и Дея влюблены друг в друга, Гюго подчеркивает чистоту и одухотворенность их любви, в которой нет ничего плотского.

                            Гуинплена замечает герцогиня Джозиана, пресыщенная и надменная красавица, чувственная женщина, не заводящая любовника лишь потому, что никого не могла признать достойным. Её притягивает его уродство, и она решает, что «король уродов», низший человек в мире, должен стать её любовником. Хотя Гуинплена впечатляет телесная красота герцогини, он не отвечает на её призыв.

                            Выясняется, что главный герой — сын лорда, по приказу короля Иакова II лишённый титула и отданный в руки компрачикосов. У него есть имя — Фермен Кленчарли, и ему по праву принадлежит титул, носимый до этого момента его единокровным братом, пэром Дэвидом Дерри-Мойр Кленчарли. Вместе с титулом и поместьем к нему переходит и помолвка с невестой Дэвида, которой оказалась герцогиня Джозиана. Гуинплен стремится поделиться новостью и деньгами с Урсусом, но ему мешает интриган Баркильфедро. Баркильфедро сообщает Урсусу, что Гуинплен мёртв, и приказывает покинуть Англию.


                            Фронтиспис первого американского издания (1869)
                            В первую ночь и первый день своей новой жизни Гуинплен сталкивается с множеством искушений, он упивается обретённым богатством и властью, на краткое время забывает о своих близких и почти уступает животной любви к Джозиане.

                            На церемонии посвящения в пэры Англии герой, считающий себя посланцем от низов английского общества, выступает с речью, рассказывая о нищете и бесправии простого народа в надежде достучаться до сердец власть имущих. Речь вызывает лишь насмешки, и только повеса Дэвид, который нередко раньше ходил среди простого народа под видом матроса Том-Джим-Джека и под этим именем покровительствовал Гуинплену, согласен с его идеями. Однако в своей сумбурной речи тот ненароком задел честь матери Дэвида и теперь должен биться на дуэли с недавно обретённым братом.

                            Гуинплен бежит из Лондона, надеясь увидеть Дею, но узнаёт, что Урсус продал свой возок и уехал. Чувствующий, что пока он был увлечён свалившимися на него богатством и властью, он потерял всё самое дорогое, юноша хочет покончить жизнь самоубийством, но в последний момент встречает Гомо, ручного волка Урсуса. Они находят Урсуса и Дею, но больное сердце девушки не выносит тоски по потерянному любимому, а вслед за тем — потрясения от внезапного его возвращения. Дея умирает, и юноша в горе бросается в воду.

</p>


                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height:  280px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Собор Парижской Богоматери</h5><a>исторический роман</a><a>1831 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse19_2" aria-expanded="false" aria-controls="collapse19_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/INOOLD/GUGO/sobor.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://www.podpisnie.ru/upload/iblock/5e0/h1vg42cjnhuqom15xc2y1p1mzc8m60et.jpg" class="jpg" style='height:  280px'>
                        </div>

                    </div>
                    <div id="collapse19_2" class="collapse" aria-labelledby="heading19_4">
                            <p style="border: 1px solid gray; padding: 3px;">6 января 1482 года в Париже идут «гуляния, объединяющие праздник Крещения Господня с древним языческим праздником шутов». В этот день, по традиции, на Гревской площади зажигают потешные огни, украшают деревья (своего рода прообраз рождественской ёлки).

По приказу кардинала Бурбонского в центральном зале Дворца правосудия («Большая зала») должны были представить пьесу с участием персонажей из Библии, а также древнеримских богов — «Мистерию». Пьеса была посвящена планировавшемуся в то время бракосочетанию «сына льва Франции», наследника французского престола дофина Карла и Маргариты Австрийской. После мистерии должно было состояться избрание главного комедианта Парижа — шутовского папы.

Состоялось избрание шутовского папы — им стал горбатый звонарь собора Парижской Богоматери Квазимодо. Пьер Гренгуар, автор «Мистерии», в отчаянии бежал из дворца, так как публика постоянно отвлекалась от представления то на запоздалое прибытие кардинала, затем фландрских послов, то на избрание шутовского папы, то на появление танцовщицы Эсмеральды. Ему негде было скоротать ночь, ведь на вырученные за «Мистерию» деньги он рассчитывал расплатиться за жильё. Он решил разделить с народом радость и отправился к огню на площади. Там Пьер увидел танцующую девушку «такой красоты, что сам Бог предпочел бы её Деве Марии». После танца Эсмеральда стала демонстрировать необычные способности своей козочки Джали, за что Эсмеральду критиковал стоящий в толпе священнослужитель, архидиакон Клод Фролло (в католической церкви титул архидиакон ближе к викарному епископу православной церкви), наставник горбуна Квазимодо. Воры, нищие и бродяги чествовали своего нового горбатого короля. Увидев это, Клод срывает с Квазимодо «папскую» одежду, отбирает скипетр и уводит горбуна.

Цыганка собирает деньги за свой танец и отправляется домой. Пьер следует за ней, в надежде на то, что у неё, помимо прекрасной внешности, доброе сердце и она поможет ему с жильём. На глазах Пьера цыганку похищают Квазимодо и ещё некто с закрытым лицом. Эсмеральду спасает капитан королевских стрелков Феб де Шатопер. Эсмеральда влюбляется в него.

Следуя за девушкой, Гренгуар оказывается во Дворе чудес, где проживают парижские нищие. Клопен обвиняет Пьера в незаконном вторжении на территорию Двора чудес и собирается его повесить. Поэт просит принять его в их сообщество, но не выдерживает сложного испытания; нужно было вытащить кошелёк у чучела с бубенчиками, да так, чтобы они не зазвенели. В последние минуты перед казнью нищие вспомнили, что по закону Пьер должен спросить, нет ли женщины, которая выйдет за него замуж. Если таковая найдётся — приговор отменяется. Стать женой поэта согласилась Эсмеральда. Он узнал её. Их «обвенчали» на 4 года. Однако девушка не даёт Гренгуару притронуться к себе. Как оказалось, Эсмеральда носила амулет, который должен был помочь ей найти родителей, но было одно весомое «но» — талисман действует только до тех пор, пока цыганка остаётся девственницей.

После «свадьбы» Гренгуар сопровождает Эсмеральду во время её выступлений на площади, где сам подрабатывает клоунскими номерами. Во время очередного танца цыганки архидиакон Фролло узнаёт в её новом спутнике своего ученика Гренгуара и начинает подробно расспрашивать поэта о том, как он связался с уличной плясуньей. Факт женитьбы Эсмеральды и Гренгуара возмущает священника, он берёт с философа слово, чтобы тот не прикасался к цыганке. Гренгуар сообщает Фролло, что Эсмеральда влюблена в некого Феба и грезит им дни и ночи напролёт. Эта новость вызывает у архидиакона небывалый приступ ревности, он решает во что бы то ни стало узнать, кто этот Феб, и разыскать его.

Поиски Фролло увенчиваются успехом. Движимый ревностью, он не только находит капитана Феба, но и наносит ему серьёзную рану во время его свидания с Эсмеральдой, чем ещё больше настраивает против себя цыганку.


Эсмеральду обвиняют в убийстве Феба (Клоду удается покинуть место преступления, выпрыгнув через окно в реку), заключают под стражу и подвергают пыткам, не вынеся которых, девушка признаёт свою «вину». Эсмеральда приговорена к казни через повешение на Гревской площади. В ночь перед казнью в темницу к девушке приходит архидиакон. Он предлагает пленнице бежать с ним, но она в гневе отталкивает несостоявшегося убийцу своего любимого Феба. Даже перед казнью все её мысли заняты капитаном. Судьба даровала ей шанс увидеть его в последний раз. Он стоял совершенно хладнокровный на балконе дома своей невесты Флёр-де-Лис Гонделорье. В последний момент её спасает Квазимодо и прячет в соборе, который может служить убежищем для осуждённых и откуда никто не имеет права забрать получившего убежище.

Эсмеральда и тогда не перестаёт грезить капитаном королевских стрелков (рана его оказалась несмертельной), не веря в то, что он давно её забыл. Свою невиновную сестру идут вызволять все обитатели Двора чудес. Они штурмуют Собор Парижской Богоматери, который ревностно защищает Квазимодо, полагая, что бродяги пришли для того, чтобы казнить цыганку. В этой схватке погибают предводитель нищих Клопен Труйльфу и бывший школяр Жеан Фролло, младший брат Клода, примкнувший к бродягам.

Когда началась осада собора, Эсмеральда спала. Внезапно в её келью приходят двое: её «муж» Пьер Гренгуар и некий человек в чёрной одежде. Объятая страхом, она всё же идёт следом за мужчинами. Они тайно выводят её из собора. Слишком поздно Эсмеральда понимает, что таинственный молчаливый спутник — не кто иной, как архидиакон Клод Фролло. На другом берегу реки Клод последний раз спрашивает, что она выбирает: быть с ним или быть повешенной. Девушка непреклонна. Тогда разгневанный священник отдаёт её под охрану затворнице Гудуле.

Затворница жестока и бесцеремонна с девушкой: ведь та цыганка. Но всё решается самым необычным образом — оказывается, что малышка Агнесса, которую похитили цыгане у Гудулы (Пакетты Шантфлери) и Эсмеральда — один и тот же человек. Гудула обещает спасти дочь и прячет её в своей келье. За девушкой приходят стражники, среди них и Феб де Шатопер. В порыве любви Эсмеральда забывает об осторожности и зовёт его. Все старания матери напрасны. Дочь забирают. Она до последнего пытается спасти её, но в итоге погибает сама.

Эсмеральду вновь приводят на площадь. Только тогда девушка осознаёт ужас неминуемой смерти. С вершины собора за этой трагической сценой наблюдали Квазимодо и, конечно, Клод Фролло.

Понимая, что Фролло виновен в смерти цыганки, обезумевший от гнева Квазимодо скидывает своего приёмного отца с вершины собора. После этого горбун исчезает.

В финальной сцене романа повествуется о том, как в гробнице Монфоконской виселицы были найдены два скелета, один из которых обнимал другой. Это были останки Эсмеральды и Квазимодо. Когда их попытались разъединить, скелет Квазимодо рассыпался в прах.
                            </p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div id="collapse20" class="collapse" aria-labelledby="heading20" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Уильям Шекспир</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Ромео и Джулиетта</h5><a>Трагедия</a><a>1595 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse20_1" aria-expanded="false" aria-controls="collapse20_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/SHAKESPEARE/shks_romeo8.txt_with-big-pictures.html'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=7606fc0a1b876b75bf217fffa5f663e5-5298175-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse20_1" class="collapse" aria-labelledby="heading20_1">
                            <p style="border: 1px solid gray; padding: 3px;">В старинном городе Вероне жили две богатые и влиятельные семьи: Капулетти и Монтекки. В течении многих лет они враждовали между собой, и немало сыновей, сильных и мужественных, было убито в жестоких схватках. Чтобы остановить эти кровопролитные побоища, правитель Вероны издал указ, согласно которому смертная казнь настигнет того, кто нарушит перемирие двух семейств. Однако, так или иначе, стыки продолжались.

Единственный сын Монтекки, прекрасный юноша Ромео, был влюблен в Розалинду. Чтоб отвлечь друга от романтических мечтаний, Меркуцио предложил ему пробраться на костюмированный бал-маскарад, устроенный Капулетти для местной знати.

Надев маски, юноши свободно проникли на торжество, где Ромео тут же влюбился в красавицу Джульетту. Даже известие о том, что они принадлежат враждующим семьям, не остановило пылкого юношу. Тем временем Тибальт узнал под маской Ромео, и, взбешенный его наглостью, решил проучить его. Однако Капулетти запретил племяннику портить праздник.

Той же ночью Ромео прокрался в сад Капулетти и признался Джульетте в своих чувствах. Влюбленные решили уже на следующий день связать себя узами брака. Священник Лоренцо с радостью согласился обвенчать влюбленных – он верил, что этот союз положит конец многолетней вражде.

Влюбленные тайно обвенчались. Отправившись на поиски друзей, Ромео наткнулся на Тибальта, который давно хотел поквитаться с ним. Меркуцио встал на защиту друга, но был убит. Разъяренный Ромео смертельно ранил Тибальта, за что был изгнан Веронским герцогом из города.

Тем временем Капулетти намеревался отдать дочь замуж за графа Париса. В отчаянии девушка обратилась к священнику Лоренцо. Тот дал ей настой из трав, способный ввести в летаргический сон на двое суток. Он также написал письмо Ромео, чтобы он тайно проник в родовой склеп и увез свою жену.

Однако посыльный опоздал – Ромео узнал печальную весть о смерти возлюбленной. Он помчался в склеп, где сказал последнее «прости» и выпил яд. Спустя время Джульетта пробудилась и, увидев мертвого Ромео, вонзила себе в сердце кинжал. Смерть двух влюбленных настолько всех поразила, что Монтекки и Капулетти добровольно прекратили давнюю вражду.</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 265px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Гамлет, принц датский</h5><a>Трагедия</a><a>1601 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse20_2" aria-expanded="false" aria-controls="collapse20_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/SHAKESPEARE/hamlet5.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=03e6a76537827b957530c73b136d83d7-4120677-images-thumbs&n=13" class="jpg" style='height: 265px'>
                        </div>

                    </div>
                    <div id="collapse20_2" class="collapse" aria-labelledby="heading20_2">
                            <p style="border: 1px solid gray; padding: 3px;">Солдатам ночных караулов у дворца датского короля две ночи подряд являлся призрак, похожий на недавно умершего короля. Узнав об этом, сын покойного монарха принц Гамлет решил удостовериться в этом. Встреча с призраком привела его в смятение — призрак поведал, что отца Гамлета отравил, влив яд спящему в ухо, его брат Клавдий, нынешний король. Призрак призвал Гамлета к мщению. Гамлет решил притвориться безумцем, чтобы получить правдивое доказательство вины Клавдия. Тот, подозревая, что принц на самом деле не безумен, а с какой-то целью притворяется, послал к нему его друзей Гильденстерна и Розенкранца, чтобы они выведали, что на уме у Гамлета. Но тот понял истинную причину их приезда и стал на вопросы отвечать бессмысленными монологами. В это время в город прибыла труппа бродячих артистов. Гамлет попросил их поставить пьесу «Убийство Гонзаго», немного изменив её сюжет, чтобы герой пьесы был убит таким же способом, как отец Гамлета. Король Клавдий поднялся и ушёл, когда увидел сцену убийства героя пьесы. Гамлет понял, что его отца убил именно Клавдий. Вскоре принц увидел короля, преклонившего колени в молитве. Гамлет решил, что не будет сейчас его убивать, так как убитый во время молитвы попадёт в рай. Принц пришёл к королеве Гертруде, своей матери, ставшей женой Клавдия. Во время разговора с ней, Гамлет убил Полония, ближнего вельможу короля, который спрятался за ковром, чтобы подслушать разговор. Принц думал, что там прячется король. Король, понимая, что Гамлет опасен для него, отослал его в Англию вместе с Гильденстерном и Розенкранцем за данью. Этим придворным он вручил письмо для английского правителя, в котором содержалось требование, чтобы он казнил Гамлета. Принц спас свою жизнь, подменив письмо. РЕКЛАМА Дочь Полония и возлюбленная Гамлета Офелия после смерти отца сошла с ума. Тем временем Гамлет возвратился в Данию. Сын Полония Лаэрт намерен отомстить за убийство отца. Король посоветовал ему вызвать принца на поединок на затупленных рапирах, но выбрать наточенный клинок и убить, как бы случайно. Лаэрт решил смазать свой клинок ядом, а король предложил дать принцу отравленное вино, если не удастся первый замысел. Безумная Офелия утонула, намеренно либо случайно совершив самоубийство. Гамлет и его друг Горацио, не знавшие об этом, зашли на кладбище и неожиданно увидели похороны Офелии. Вскоре Лаэрт вызвал принца на поединок. Во время поединка они оба получили ранения отравленным клинком, а королева, ощутив жажду, выпила отравленное питьё. Лаэрт, умирая, раскрыл Гамлету замысел короля. Принц убил Клавдия и умер сам. Королевский престол Дании перешёл норвежскому принцу Фортинбрасу.
                            </p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main" style='height: 265px;'>
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Сонеты</h5><a>сборник стихотворений(154 шт.)</a><a>1592—1599 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse20_3" aria-expanded="false" aria-controls="collapse20_3"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/SHAKESPEARE/sonets.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=aa08d31771eb5d441d791dc1897492dd-4291891-images-thumbs&n=13" class="jpg" style='height: 265px'>
                        </div>

                    </div>
                    <div id="collapse20_3" class="collapse" aria-labelledby="heading20_3">
                            <p style="border: 1px solid gray; padding: 3px;"> 
                            Сборник из 154 более или менее продолжительных стихотворений Шекспира. Из них: 
                            сонеты, посвящённые другу: 1—126. Воспевание друга: 1—26. Испытания дружбы: 27—99.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>


        <div id="collapse21" class="collapse" aria-labelledby="heading21" data-parent="#accordionExample">
          <div style='border: 0px solid gray; width: 100%; align-items: center; margin: auto;'>
                <div class="container">
        <div class="main-list-title" style='padding-bottom: 15px'>
            <h3>Жан-Батист Мольер</h3>
        </div>
        <div class="main-list-card">
            <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Мещанин во дворянстве</h5><a>Комедия</a><a>1670 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse21_1" aria-expanded="false" aria-controls="collapse21_1"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/MOLIER/meshanin.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://avatars.mds.yandex.net/i?id=76851ca85921c0f7d494fdb18927f3bb-3699759-images-thumbs&n=13" class="jpg">
                        </div>

                    </div>
                    <div id="collapse21_1" class="collapse" aria-labelledby="heading21_1">
                            <p style="border: 1px solid gray; padding: 3px;">Главный герой произведения – господин Журден. Его самая заветная мечта – стать дворянином. Для того, чтобы стать хоть немного похожим на представителя дворянского сословия, Журден нанимает для себя преподавателей. У главного героя есть образец для подражания – это некий граф Дорант, который слывет в обществе подлецом и мошенником.

У Журдена также есть жена, которая невероятно умна, а также хорошо образована, но она не питает ни малейшей симпатии к дворянскому сословию. Эта прекрасная женщина считает своей главной задачей выдать собственную дочь за замечательного достойного молодого человека. Дочь Журдена и его жены зовут Люсиль.

Девушка влюблена в некого Клеонта. Этот молодой человек очень умен, благороден и красив, а что самое главное – он невероятно любит Люсиль. Но, конечно же, Журден отказывает Клеонту, так как юношу не имеет ничего общего с дворянским сословием. Казалось бы, что молодой паре не суждено быть вместе. Но обстоятельства складываются абсолютно иным образом. Слуга, которого зовут Ковелье, решается на очень отчаянный, но в то же время хитрый шаг.

Для того, чтобы молодые люди наконец-то обрели свое счастье, он переодевает Клеонта, который в свою очередь предстает перед Журденом в качестве «сына султана». После чего, так давно мечтавший о дворянском титуле Журден, дает свое согласие на свадьбу Клеонта и своей прекрасной дочери. Таким невероятным образом хитрый слуга помогает молодым людям обрести истинное счастье, ведь отец юной Люсиль дал свое родительское благословение.

А что же происходит с самим Журденом? Он очень долго жаждал драгоценный дворянский титул, но при этом остался ни с чем. Зато его жена выполнил свою главную задачу, а дочь выходит замуж за стоящего человека. На этом произведение и подходит к своему логическому завершению.</p>    
                        </div>
                </div>
                <div class="col-xs-12 col-sm-12 col-md-12 col-lg-6">
                    <div class="card_main">
                        <div class="left__card">
                                <p class="card__uptext" style='text-decoration: underline;'><h5>Тартюф</h5><a>комедийная пьеса</a><a>1644 г.</a></p>
                                <p style='padding-left: 0px; font-size: 15px; color: black; text-decoration: underline;' id="eggs" class="pushkindelivery btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse21_2" aria-expanded="false" aria-controls="collapse21_2"><i>Краткое содержание ->></i></p>
                                <p class="card__lowtext"><a  style='color: black; text-decoration: underline; cursor: pointer;' href='http://lib.ru/MOLIER/tartuf1.txt'><i>Читать книгу ->></i></a></p>
                        </div>
                        <div class="right__card ibg">
                            <img src="https://alifba.ru/storage/img/products/51679/978-5-389-09055-2.jpg" class="jpg">
                        </div>

                    </div>
                    <div id="collapse21_2" class="collapse" aria-labelledby="heading21_2">
                            <p style="border: 1px solid gray; padding: 3px;">В доме господина Оргона все идет не так как надо, по крайней мере, для домочадцев, которые просто были недовольны тем, что их отец и муж госпожи Оргон – ведет себя таким образом. Ведь он разрешил поселить в своем доме одному человеку, который являлся праведником, и кем-то вроде служителя церкви.

                            Его звали господин Тартюф. Этот человек на самом деле был обманщиком, которому требовалось жилье, крыша над головой, но кроме этого он решил посягнуть на нечто большее, что вообще сильно разгневало все семейство. Господин Оргон сам не видел, что он сделал, так как он не особо хорошо разбирался в людях, и ему казалось, что господин Тартюф заслуживает всяческого преклонения перед ним.

                            Но его родные не разделяли его мнения. Ведь они видели – насколько ужасен этот человек, прикрываясь Библией, умными словами и улыбками. Когда он стал жить у них в доме, он сразу же стал всем заправлять, и ему подчинялся хозяин дома, чтобы всего ужасней. Всей семье пришлось много вытерпеть от него, так как он использовал против них собственного их отца. Именно потому все так возненавидели его.

                            Но сам отец этого не понимал, — ведь как его родные могли гневаться и клеветать на такого человека, просто святого. Именно это и рассердило отца. Дочь господина Оргона была еще незамужней, но она хотела выйти замуж за одного юношу, и до того времени, как появился этот незваный гость, отец семейства почти дал разрешение им пожениться. Но теперь он вроде как медлил с этим решением.

                            И когда сам бедный жених напрямую спросил у отца его любимой – тот ответил, что хочет породниться с господином Тартюфом, так как он считает его достойным и просто – напросто почти святым, если не таким уж. Это просто ошеломило его дочь, но скромная по натуре, она не решилась перечить вспыльчивому в этом случае, отцу. Но другие ее родные были еще больше шокированы глупостью и неведением отца их.

                            Все, кроме господина Оргона и его матери, видели – насколько ужасен и лицемерен господин Тартюф, который испортил им тихую и радостную жизнь. Ведь своими нравоучениями он разогнал всех друзей из их дома, настраивал их отца против всех домашних, занял, чуть ли не командование всей семьей.

                            А теперь он еще хотел жениться на дочери хозяина дома, что еще больше воспротивило всех против господина Тартюфа. Теперь все домашние собрались – и планирую, как бы уберечь себя и свою домашнюю девочку, сестру и дочь от негодяя хитрого и подлого – господина тартюфа. Они стараются что-либо придумать, чтобы как-то вывести на чистую воду этого негодяя.

                            Дорина, их служанка, очень умная девушка, решила все устроить. Она подозревала, что сам святоша не равнодушен к жене самого хозяина дома, а именно потому она предложила поговорить госпоже Эльмире с Тартюфом, и тогда он стал уверять ее, что любит ее. Это очень удивило госпожу, и в какой-то мере, она решила этим воспользоваться. Жена уговорила Оргона залезть под стол и подслушать их беседу.

                            Он так и сделал, и подслушал разговор, в котором господин Тартюф приставал к его жене, признаваясь в любви, и касаясь даже ее, чему та старалась воспрепятствовать. Тогда господин Оргон очень разгневался, и выгнал из дома подлого мошенника, который грозил расплатой, потому что хозяин дома уже успел в какой-то мере изменить завещание. Но все обошлось, так как милостивый король смог воспрепятствовать этому.

                            Читайте также: Комедия Мольера «Мещанин во дворянстве» была написана в 1670 году. Произведение создано в рамках литературного направления реализм. Если вам нужно быстро понять, о чем идет речь, рекомендуем прочитать краткое содержание «Мещанина во дворянстве» по действиям на нашем сайте. Пьеса «Мещанин во дворянстве» включена в школьную программу 8 класса.</p>    
                        </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>







    </div>
</div>
</div>
</div>
</div>

        <footer class="Footer">
            <div class="FooterLogo">
                <div style='margin: auto; width: 70%'>
                <a class="btn btn-dark turner" href="#" role="button" style='float: center;'>Кнопка тут по приколу, первоисточника нет)</a>


        </div></div></div></footer>












    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjsOMm/tB9LTS58ONXgqbR9W8oWht/amnpF" crossorigin="anonymous"></script>
  </body>
</html>
    '''
app.run(debug=True)