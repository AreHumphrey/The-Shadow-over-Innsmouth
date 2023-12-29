

label no_whiskey:
    scene bg25
    "Интересно, что посетить в первую очередь..."
    menu:
        "{i}Пожарное депо{/i}":
            jump fire_station_2

        "{i}Исторический дом основателя города{/i}":
            jump march_2_1

        "{i}Храм на гравной площади{/i}":
            jump temple_2

        "{i}Пройтись по улицам{/i}":
            jump streets_2



label fire_station_2:

    scene bg28

    "{i}Итак, я начал свое заранее обдуманное, но от этого не ставшее менее загадочным путешествие по узким, мрачно‑болезненным улицам Инсмута.{/i}"
    "{i}Перейдя мост и свернув к шумному водосбросу, я прошел мимо фабрики Марша, откуда, к моему удивлению, не доносилось никаких звуков действующего производства.{/i}"
    "{i}Здание стояло на крутом откосе реки близ моста и площади с расходящимися улицами. Вероятно, именно здесь в прошлом находился городской центр, позднее переместившийся на Таун‑сквер.{/i}"

    scene bg27

    "{i}Ненадежный мост, к которому я приблизился, был снабжен запретительной надписью, но я все же рискнул и перешел по нему на южную сторону, где снова показались признаки жизни.{/i}"
    "{i}Скрытные, неуклюже передвигающиеся создания без всякого выражения поглядывали в мою сторону, а на более‑менее нормальных лицах отражалось нечто вроде холодного любопытства.{/i}"
    "{i}Инсмут раздражал меня все сильнее, и я направился по Пейн‑стрит в сторону Таун‑сквер, надеясь отыскать какое‑нибудь транспортное средство,{/i}"
    "{i}могущее отвезти меня в Аркхем еще до того, как придет время отправления зловещего восьмичасового автобуса.{/i}"

    jump fire_station_2_2


define z = Character("Зейдок Аллен", color="#0B888E")
define g = Character("Роберт Олмстед", color="#0B888E")
define v = Character("Валакеа", color="#0B888E")
define m = Character("Оубед Марш", color="#0B888E")
define t = Character("...", color="#0B888E")

image insm_10 = im.Scale("insm_10.png", 1080 / 1.7, 1920 / 1.7)
image insm_10_2 = im.Scale("insm_10_2.png", 1080 / 1.7, 1920 / 1.7)
image insm_10_1 = im.Scale("insm_10_1.png", 1080 / 1.7, 1920 / 1.7)
image insm_10_4 = im.Scale("insm_10_4.png", 1080 / 1.7, 1920 / 1.7)

image zadok_1 = im.Scale("insm_9.png", 1080 / 1.6, 1920 / 1.6)
image zadok_2 = im.Scale("insm_9_1.png", 1080 / 1.6, 1920 / 1.6)
image zadok_3 = im.Scale("insm_9_2.png", 1080 / 1.6, 1920 / 1.6)
image zadok_4 = im.Scale("insm_9_3.png", 1080 / 1.6, 1920 / 1.6)

image marsh_1 = im.Scale("insm_6.png", 1080 / 1.6, 1920 / 1.6)
image marsh_2 = im.Scale("insm_6_1.png", 1080 / 1.6, 1920 / 1.6)

image terr = im.Scale("insm_1.png", 1080 / 1.6, 1920 / 1.6)

image val = im.Scale("insm_5.png", 1080 / 1.6, 1920 / 1.6)

label fire_station_2_2:

    scene bg29

    "{i}Тогда‑то я и увидел слева полуразрушенное пожарное депо и краснолицего старика с густой бородой и водянистыми глазами.{/i}"

    image zadok = im.Scale("insm_9.png", 1080 / 1.6, 1920 / 1.6)
    show zadok at center

    "{i} На нем болтались невыразимые лохмотья,"
    "{i} а сам он сидел на скамье и разговаривал с двумя рыбаками, неопрятными, но выглядящими почти нормально.{/i}"
    "{i} Похоже, это был тот самый Зейдок Аллен, полубезумный, почти столетний пьянчужка, рассказывавший байки о старом Инсмуте.{/i}"
    "{i}Вряд ли старик мог сообщить нечто ценное, кроме смутных намеков да бессвязных и неправдоподобных историй;{/i}"

    scene bg29

    "{i} к тому же меня предупредили, что общение с ним небезопасно, поскольку это наверняка не понравится местным жителям.{/i}"
    "{i} И все же мысль об этом древнем свидетеле гибели города, помнившем былые времена кораблей и фабрик,{/i}"
    "{i} была слишком соблазнительна. В конце концов, даже самые странные и безумные мифы нередко суть символы и аллегории,{/i}"
    "{i} основанные на правде, – а старый Зейдок видел все, что происходило с Инсмутом за последние девяносто лет.{/i}"
    "{i} Любопытство охватило меня, совершенно подавив осторожность. {/i}"
    "{i}В молодой своей самонадеянности я вообразил, что способен отделить крупицы реальной истории от сумбурных излияний.{/i}"
    "{i} Я без лишних раздумий подошел к старику.{/i}"

    scene bg28

    show zadok_1 at right
    show insm_10 at left

    g "{i}День добрый, сэр{/i}"

    z "{i}Милок, я занят. Мне некогда заводить пустые диалоги, да и опасно все это...{/i}"

    scene bg24

    "{i}После отказа я понял, что расспрашивать данного субъекта нет смысла и неторопливо пошел в сторону главной площади. {/i}"
    "{i}Поскольку было еще светло, я  вышел на площадь и огляделся в поисках места, где можно было бы поужинать,{/i}"
    "{i} по-прежнему ловя на себе крайне недружелюбные взгляды праздных зевак. С учетом того, что лавка знакомого бакалейщика была уже закрыта,{/i}"
    "{i} мне пришлось воспользоваться услугами того самого ресторана, который был отвергнут мною поначалу.{/i}"
    "{i} Согбенный, узкоголовый мужчина со ставшими уже почти для меня привычными выпученными, немигающими{/i}"
    "{i} глазами да плосконосая девица с неимоверно толстыми и неуклюжими руками взялись за мое обслуживание.{/i}"
    "{i} К своему немалому облегчению я обнаружил, что основная часть продуктов, которыми пользовались в этом заведении,{/i}"
    "{i}представляла из себя консервы и расфасованные пакеты.{/i}"

    scene bg102

    "{i}С меня хватило миски овощного супа с крэкерами, сразу после чего я вернулся в свою унылую комнату,{/i}"
    "{i} предварительно купив у по-прежнему угрюмою портье лежавшие на рахитичной стойке вечернюю газету и какой-то засиженный мухами журнал.{/i}"
    "{i}После трапизны я глянут на часы и понял, что автобус отправляется с минуты на минуту и поэтому отправился на остановку автобуса. {/i}"

    scene bg72

    "{i}Где-то незадолго до восьми показался грохочущий автобус, в салоне которого сидело три пассажира. {/i}"
    "{i}Когда он остановился, один из парней с подчеркнуто грозным видом подошел к спустившемуся на тротуар водителю и пробормотал ему несколько неразборчивых слов.{/i}"
    "{i} Затем Сарджент выволок из салона пакеты с почтой и газетами и прошел в фойе гостиницы, тогда как пассажиры – та же троица,{/i}"
    "{i} которую я имел возможность наблюдать утром в Ньюбэрипорте, – прошаркала к тротуару и обменялась несколькими гортанными словами со стоявшими там бездельниками,{/i}"
    "{i} причем то, что мне удалось услышать из их реплик, никак не походило на английский язык. {/i}"
    "{i}Я поднялся в салон и занял то же самое место, на котором ехал сюда, однако еще до того как мне удалось как следует устроиться,{/i}"
    "{i} вновь появился Сарджент, принявшийся что-то бормотать своим хрипловатым, надтреснутым и в целом довольно мерзким голосом.{/i}"

    image insm_2 = im.Scale("insm_2.png", 1080 / 1.6, 1920 / 1.6)
    show insm_2 at center

    "{i}Отправимся через 5 минут.{/i}"

    scene bg72

    "{i}После этой короткой фразы он удалился в магазин. {/i}"
    "{i}Спустя назначенное время водитель уселся и объявил об отправлении.{/i}"
    "{i} Пока сменялись пейзажи, мои мысли сосредатачивались на тайнах Инсмута, в которые я к сожалению не успел проникнуть и этот портовый городок с необщительными жителями,{/i}"
    "{i} множеством легенд, так и остался для меня неизведанным. {/i}"

    return

label march_2_1:
    scene bg28

    "{i}Окончив диалог с бакалейщиком, который из всех субъектов, встретившихся в этом городе, оказался самым общительным, я решил бесцельно прогуляться по улицам,{/i}"
    "{i} в поисках местных архитектурных достопримечательностей. "
    "{i}Свернув в сторону так называемого цетра города, который, до сих пор таил в себе прелести архитектурного зодчества прошлого столетия,{/i}"
    "{i} я с головой окунулся в эту амосферу. "
    "{i}Размеренно идя по улице и разглядывая дома, разной степени разложения: какие-то пребывали почти в первозданном состоянии, а какие-то, явно заброшенные,{/i}"
    "{i} причем очень давно."

    scene bg83

    "{i} Этот контраст создавал странное ощущение: таинственного страха, ожидания опасности, подстерегающей буквально на каждом углу. {/i}"
    "{i}Это необъяснимое чуство внушали какие-то мелкие, с виду непримечательные детали, которые в купе, складывались в общую картину,{/i}"
    "{i} дарующую легкий озноб и едва заметную дрожь в ногах."
    "{i} Где-то, в давно обветшалых домах где-то поблескивали  признаки освещения, где-то взляд невольно ловил движение в сгивших, {/i}"
    "{i}деревянных, зашторенных, но все же открывающих взору комнату,окнах. {/i} "

    scene bg103

    "{i}Вдруг мой взгляд упал на заброшенный дом.Дом, на который я наткнулся, отличался уникальной архитектурой, которая казалась смешением различных стилей и эпох.  {/i}"
    "{i}Его фасад был увенчан крупными лепными деталями, которые несли в себе следы времени и погоды. Входные двери, хотя и несут признаки длительного запустения, {/i} "
    "{i}все еще сохраняли изысканность и изящество прошлого. {/i}"
    "{i} Окна, обрамленные старыми деревянными рамами, казалось запечатлили в себе память о загадках и тайнах, коими наполнен город. {/i}"
    "{i} Поддвавшесь неистовому желаю лицезреть и внутреннее убранство данного памятника архитектуры я посмотрел на дверь. {/i}"
    "{i} Дернув слегка за ручку, я понял что дом не заперт. Интерес, смешавшийся с каким то чувстсвам, таящимся в глубине моей души,  {/i}"
    "{i}жаждевшим проникнуть за образовавшуюся вуаль тайны, окутывающей весь город я отворил и зашел. {/i}"

    scene bg80

    "{i}По мере того, как я проходил сквозь коридоры и залы этого дома, я обнаруживал детали, напоминающие о его роскоши и блеске в далеком прошлом.{/i}"
    "{i} Изящные карнизы, арки и стены, покрытые резьбой и узорами, свидетельствовали о величии, которое присуще было этому месту.{/i}"
    "{i} Темные углы и длинные проходы создавали ощущение загадочности и завораживали воображение.{/i}"
    "{i}Со столь богатой историей и разнообразием стилей, заброшенный дом представлял собой уникальное архитектурное произведение, скрытое от глаз многих.{/i}"
    "{i}Увидев лестицу, по-видиму, ведущую на второй этаж я взявшись за перила ступил на ступени, покрытые толстым слоем пыли{/i}"

    jump march_2


label march_2:


    scene bg98

    "{i}Поднимаясь по леснице я уловил запах сырости, смешиваемый с другим, непонятным, но мерзким и зловонным.{/i}"

    scene bg97

    "{i}Поднявшись, я очутился в старинном доме, своей архитектурой напоминающей убранства домов прошлого столетия.{/i}"
    "{i} Слой пыли на столах, некоторых фрагментах пола говорил о том, что этот дом - заброшен. Но вместе с этим кое-где виднелись следы,{/i}"
    "{i} мало чем походившие на человеческие. Разглядывая первый этаж, я заприметил лесницу, которая, по всей видимости, вела на второй.{/i}"

    scene bg96

    "{i}Поддавшись мимолетному желанию, я поднянялся по леснице и оказался в зале, который был менее величественным,{/i}"
    "{i} чем те, что встретились на первом этаже, но вместе с этим, казался более обжитым. На противоположной стороне комнаты располагался камин,{/i}"
    "{i} причем, разожжённый, и кресло повернутое к камину. Хоть картина выглядила довольно жутко: пустой, с виду не обжитый дом с горящим камином.{/i}"
    "{i} Но тут кресло немного ододвинулась, представив моему взору человека, который видимо и был хозяином данного дома.{/i}"
    "{i} Он был низкого роста, конечности его, по видимому, были деформированы, толстая кожа, оттдающая нездоровым синим оттенком.{/i}"
    "{i} Но большое беспокойство у меня вызвали глаза хозяина дома: они сильно контрастировали с бледной кожей, были выпучены и смотрели прямо на меня. {/i}"

    image marsh = im.Scale("insm_8.png", 1080 / 1.7, 1920 / 2.5)

    image insm_10 = im.Scale("insm_10.png", 1080 / 1.7, 1920 / 1.7)
    image insm_10_2 = im.Scale("insm_10_2.png", 1080 / 1.7, 1920 / 1.7)
    image insm_10_1 = im.Scale("insm_10_1.png", 1080 / 1.7, 1920 / 1.7)
    image insm_10_4 = im.Scale("insm_10_4.png", 1080 / 1.7, 1920 / 1.7)

    define g = Character("Роберт Олмстед", color="#0B888E")
    define m = Character("Марш", color="#0B888E")

    show marsh at right
    show insm_10 at left

    m "{i}Я узнаю эти глаза, господин, представьтесь.{/i}"

    g "{i}Роберт Олмстед. А...{/i}"

    m "{i}О, вот как, я думал эта линия давно преравалась, поколения, пожалуй два назад.{/i}"
    m "{i} Не думал, не думал. Хотя нынче множества сходства можно увидеть в вещах вовсе не схожих. {/i}"
    m "{i}Не знаете ли вы, Роберт, какую фамилию, к примеру носила ваша прабабка? {/i}"

    g "{i}Марш, если мне не изменяет память, но я не понимаю к чему вы ведете, Сэр?{/i}"

    m "{i}А, я к вашему сведению, Абед Марш, глава семьи, к которой вы, мой дорогой гость, имеете прямое отношение. {/i}"

    m "{i}Я рад, что за долгое время встретил, того, кого могу назвать родственником. Мои сыновья, дочери, внуки уже уплыли, либо...{/i}"
    m "{i}Несмотря на то, что этот субъект для любого человека, находящегося в зравом уме, не внушал доверия,{/i}"
    m "{i} на меня его речи подействовали странно, можно даже сказать гипнотически.{/i}"
    m "{i} Меня тянуло к Абеду, который судя по его словам был моим прапрадедом...{/i}"
    m "{i}Пока он продолжал свои немного бесвязные речи, затрагивающие то Орден Дагона, то реликвии культа, то генеалогического древа,{/i}"
    m " {i}я заворожённо смотрел на Абеда, мыслями пребывая где-то далеко.{/i}"
    m " {i}Так было до тех пор, пока монолог хозяина дома не прервался.{/i}"
    m "{i} За молчанием последовал вопрос, который заставил меня избавится от мыслей, обуревавших меня доли секунды назад:{/i}"
    m "{i}Не хочешь ли ты помочь мне возродить былое величие  города: запустить торговлю, {/i}"
    m "{i}наладить отношения с близлежащими населенными пунктами, наладить судоходство? Как тебе идея, праправнук?{/i}"

    menu:
        "{i}Согласиться{/i}":
            jump yes_2
        "{i}Отказаться{/i}":
            jump no_2


label yes_2:

    scene bg94

    "{i}Я, потряденный и заворожённый рассказами Абеда Марша, не мог отказать ему в помощи. {/i}"
    "{i}Он понял, что если он не примкнет к Маршу, то он будет потерян для всего мира."
    "{i}Абед Марш рассказал мне о тайнах и заговорах, которые были скрыты в течение нескольких поколений. {/i}"
    "{i}Роберт был ужасён, но в то же время он чувствовал, что ему нужно принять предложение Марша.{/i}"
    "{i}Я был ужасён, но в то же время  чувствовал, что  обрел что-то, что ему нужно.{/i}"
    "{i} Я был косвенно причастен к тайнам и заговорам, которые были скрыты в течение нескольких поколений, и я должен был помочь Маршу вернуть их силу и престиж.{/i}"
    "{i}Я понял, что если не помогу Маршу, то я будет потерян для всего мира, и что мне необходимо принять свою судьбу, несмотря на все риски.{/i}"



label no_2:

        "{i}Я не мог принять столь сумосбродного предложения, от человека, который не внушал доверия ни своим видом,{/i}"
        "{i} ни речами, ни предложением, которое как гром среди ясного неба обрушилось на меня. {/i}"

        m "{i}Ясно, на этом своете не осталось человека, чьи мысли сходны с моими... {/i}"
        m "{i}После этого Марш нажал на кнопку, спрятанную на подлакотнике кресла.{/i}"

        scene bg74_1

        "{i}Ничего не произошло, а хозяин дома, продолжил монолог, рассказывая о тварях обитающих, где-то под водой.{/i}"
        "{i} С каждой минутой мне все сложнее было вникать в суть сказанных слов, да и веки, стали тяжелыми как свинец.{/i}"
        "{i} Вскоре я, почувствовав невыносимую слабость в ногах, обрушился на пол и закрыл глаза.{/i}"

        return


label streets_2:

    scene bg28

    "{i}Окончив диалог с бакалейщиком, который из всех субъектов, встретившихся в этом городе, оказался самым общительным, я решил бесцельно прогуляться по улицам,{/i}"
    "{i} в поисках местных архитектурных достопримечательностей. "
    "{i}Свернув в сторону так называемого цетра города, который, до сих пор таил в себе прелести архитектурного зодчества прошлого столетия,{/i}"
    "{i} я с головой окунулся в эту амосферу. "
    "{i}Размеренно идя по улице и разглядывая дома, разной степени разложения: какие-то пребывали почти в первозданном состоянии, а какие-то, явно заброшенные,{/i}"
    "{i} причем очень давно."

    scene bg83

    "{i} Этот контраст создавал странное ощущение: таинственного страха, ожидания опасности, подстерегающей буквально на каждом углу. {/i}"
    "{i}Это необъяснимое чуство внушали какие-то мелкие, с виду непримечательные детали, которые в купе, складывались в общую картину,{/i}"
    "{i} дарующую легкий озноб и едва заметную дрожь в ногах."
    "{i} Где-то, в давно обветшалых домах где-то поблескивали  признаки освещения, где-то взляд невольно ловил движение в сгивших, {/i}"
    "{i}деревянных, зашторенных, но все же открывающих взору комнату,окнах. {/i} "

    scene bg99

    "{i}Вдруг мой взгляд упал на заброшенный дом.Дом, на который я наткнулся, отличался уникальной архитектурой, которая казалась смешением различных стилей и эпох.  {/i}"
    "{i}Его фасад был увенчан крупными лепными деталями, которые несли в себе следы времени и погоды. Входные двери, хотя и несут признаки длительного запустения, {/i} "
    "{i}все еще сохраняли изысканность и изящество прошлого. {/i}"
    "{i} Окна, обрамленные старыми деревянными рамами, казалось запечатлили в себе память о загадках и тайнах, коими наполнен город. {/i}"
    "{i} Поддвавшесь неистовому желаю лицезреть и внутреннее убранство данного памятника архитектуры я посмотрел на дверь. {/i}"
    "{i} Дернув слегка за ручку, я понял что дом не заперт. Интерес, смешавшийся с каким то чувстсвам, таящимся в глубине моей души,  {/i}"
    "{i}жаждевшим проникнуть за образовавшуюся вуаль тайны, окутывающей весь город я отворил и зашел. {/i}"

    scene bg80

    "{i}По мере того, как я проходил сквозь коридоры и залы этого дома, я обнаруживал детали, напоминающие о его роскоши и блеске в далеком прошлом.{/i}"
    "{i} Изящные карнизы, арки и стены, покрытые резьбой и узорами, свидетельствовали о величии, которое присуще было этому месту.{/i}"
    "{i} Темные углы и длинные проходы создавали ощущение загадочности и завораживали воображение.{/i}"
    "{i}Со столь богатой историей и разнообразием стилей, заброшенный дом представлял собой уникальное архитектурное произведение, скрытое от глаз многих.{/i}"
    "{i} Настолько проникнувшись окружавшим меня убранством я забылся, и пожалуй, ни разу не взглянул на пол.{/i}"
    "{i} Это сыграло со мной злую шутку: наступив в очередной раз я не почувствовал пола и потеряв равновесие скатился в образовавшуюся подо мной яму.{/i}"

    scene bg74_1

    jump tunnel_2

label tunnel_2:

    "{i}Несколько раз ударившись о что-то, походившее на хаотично воткнутые битонные блоки я призимлился на каменный пол.{/i}"
    "{i} Придя в себя, после столь стремительного падения я огляделся.{/i}"

    scene bg99

    "{i}Место, в которое я попал, смело можно было назвать подземным туннелем."
    "{i} Подняв в голову вверх и убедившись в том, выбраться отсюда тем же путем не выйдет я неспешно пошагал вперед.{/i}"

    scene bg100

    "{i}Моему продвижению вглубь туннеля сопутствовали множественные, пугающие звуки: капающая вода, падающие с каменного пола маленькие камушки, бульканье доносившееся из глубины.{/i}"
    "{i}Пройдя довольно долго, я остановился заметив разветвление: направо, налево или прямо. Ориентируясь на инстинкт, я решаю пойти...{/i}"

    menu:
        "{i}Налево{/i}":
            jump left_2
        "{i}Прямо{/i}":
            jump center_2
        "{i}Направо{/i}":
            jump right_2


label left_2:

    scene bg99

    "{i}Когда я решил пойти налево, туннель внезапно расширился, чуть ли не словно бы встрепенулся в подготовке к своему зловещему представлению.{/i}"
    "{i} Огромная расщелина разверзлась передо мной, словно голодная пасть нечеловеческого чудовища, поглощающего свою добычу с безжалостной жестокостью.{/i}"
    " {i}В тот миг, когда земля под моими ногами выдержала свое на время, я упал в эту бездонную пропасть.{/i}"

    scene bg74_1

    "{i}Падение было быстрым и бесконечным, словно я погружался в самые глубины моего страха.{/i}"
    "{i} Темнота окружила меня со всех сторон, лишив всякой возможности различить что-либо вокруг.{/i}"
    "{i} Сердце забилось так сильно, будто оно пыталось выбиться из груди, бесполезно борясь с неизбежным.{/i}"
    "{i}Тоннели подземелья стали слепкими воспоминаниями, а шум падения угас, как последний вздох умирающей свечи.{/i}"
    "{i} В темноте и безысходности, я почувствовал, что смерть неизбежно приближается, ее темные пальцы тянуться ко мне, словно холодный порыв ветра.{/i}"
    "{i}Это был момент абсолютной отчаянности и страха. {/i}"
    "{i}От ужаса прикрыв глаза и почувствовав гулкий, удар головой о железный предмет я почувствовал вкус свинца во рту.{/i}"

    return

label right_2:

    scene bg99

    "{i}Без какой либо мысли, движимый одним лишь подсознанием я выбрал правое ответвление.{/i}"
    "{i} Пройдя еще, по ощущениям минут 20 я натыкаюсь на старый изогнутый коридор, ведущий к извилистой лестнице, ведущей куда-то наверх. {/i}"
    "{i}Не имея альтернатив и не желая возвращаться к разветвлению я поднимаюсь по ветеиватой леснице.{/i}"

    jump march_2

label center_2:

    scene bg99

    "{i}Без какой либо мысли, движимый одним лишь подсознанием я выбрал идти прямо, не откланяясь от выбранного вектора. {/i}"
    "{i}Пройдя еще, по ощущениям минут 20 я ловлю себя на мысли, что в туннеле становится светлее, и вскоре я уже отчетливо увидел очертания прохода.{/i}"

    scene bg101

    "{i} Пребывая долгое время в полупраке я прищурился, но не переставал следовать поставленному марсшруту.{/i}"
    "{i} Наконец выйдя  из туннеля медленно открыл глаза...{/i}"

    jump fire_station_2_2

label temple_2:

    scene bg28

    "{i}Окончив диалог с бакалейщиком, который из всех субъектов, встретившихся в этом городе, оказался самым общительным,{/i}"
    "{i} я решил, несмотря на слова своего недавнего собеседника, получше расмотреть Собор, расположенный на главной прощади.{/i}"
    "{i} Благо, бакалейную лавку с собором разделяло несколько кварталов.{/i}"

    scene bg20

    "{i} Придя на место и взлядевшись, мое сердце забилось сильнее от волнения и любопытства по поводу того,{/i}"
    "{i}  что может скрываться внутри этого древнего сооружения.{/i}"
    "{i}  Поколебавшись несколько секунд, я решил что байки, окутывающие это место наверняка долеки от истины,{/i}"
    "{i}  и реальной угрозы в этом памятнике архитектуры вовсе нет.{/i}"

    scene bg47

    "{i}  Когда я вошел в храм, стены его украшал народный узор, а потолок опоясывала узорчатая лента.{/i}"
    "{i}  Все было наполнено загадочной атмосферой, и мое сердце забилось сильнее от волнения при виде античных символов и изображений,{/i} "
    "{i} напоминающих морских чудовищ.{/i}"
    "{i} Тут я узнал, что храм служит святилищем для культа Ордена Дагона, этому свидетельствовали многочисленные витражи на окнах:{/i}"
    "{i}  изображения рыб, тайных символов, значение которых мне неведомо, надписи на неивестном мне языке, опоясывающие купол .{/i}"
    "{i} Разгадывая острые углы архитектуры и таинствен знаки, я ощутил ввиду нарастающего чувства тревоги.{/i}"
    "{i}  Мои мысли барахтались в мраке страха и отчаяния. {/i}"
    "{i} Но тут я услышал шорох и звуки неясного происхождения изглубины храма, и моя спина пронзила дрожь. {/i}"
    "{i} Что-то темное и мощное шевельнулось внутри, и я понял, что момент истины пришел.{/i}"
    "{i}  Передо мной предстали лишь два пути: бежать, пытаясь найти скрытные тропы сквозь город, окутанный тенью сектантов,{/i}"
    "{i}  или принять свою участь и встретить ее с достоинством, зная, что теперь моя судьба тесно связана с культистами ордена Дагона и тайнами.{/i} "

    menu:
        "{i}Остаться{/i}":
            jump stay_2
        "{i}Бежать{/i}":
            jump run_2

label run_2:

    "{i} Я ощутил, что моя жажда истины была сильнее, чем страх, и я решил осмотреть помещение, пытаясь найти скрытные тропы сквозь город, окутанный тенью сектантов.{/i}"
    "{i} Моему взору открылся маленький люк, в нескольких шагах от меня.{/i}"
    "{i} Я ноги несли меня, но мрачные фигуры начали преследовать меня по улицам, и я понимал, что путь к свободе будет нелегким. {/i}"
    "{i}Время от времени слышались шорохи и шепот, и я знал, что мое решение вызовет непредсказуемые последствия,{/i}"
    "{i} но несмотря на это предолев разделяющее меня с люком расстояние. {/i}"
    "{i}Я открыл люк и не думая спрыгнул, оставляя своих приследоватей.{/i}"

    jump tunnel_2

image insm_3 = im.Scale("insm_3.png", 1080 / 1.6, 1920 / 1.6)
define i = Character("...", color="#0B888E")

label stay_2:
    "{i} Я понял, что мое решение продолжить путь ведомый жаждой истины было слишком наивным, и тени выступили из углов,{/i}"
    "{i} и вскоре я оказался в оковах культистов ордена Дагона.{/i}"
    "{i} Мои надежды на свободу были разбиты, как корабль о скалы во время бури.{/i}"
    "{i} Окруженный мрачными фигурами, я понял, что теперь моя судьба тесно связана с культистами ордена Дагона.{/i}"
    "{i} В этом мрачном мире, полном загадок и ужасов, я сделал свой выбор и смирился с непредвиденными обстоятельствами,{/i}"
    "{i} зная, что моя жизнь навсегда изменена этой встречей с темным и загадочным городом Инсмут. Послышался голос:{/i}"

    show insm_3 at center

    i "{i}O dei Immortali! Aquae eius renovent animas nostras, et sapientia eius magna mentes nostras illuminet."
    i " {i}Nos, servi eius devoti, munera domino maris affer et pro misericordia eius deprecamur."
    i " {i}Profunda eius nos defendat et eorum secreta nobis patefaciat."
    i "{i} Dagon, suscipe cultum nostrum et nobiscum in aeternum!"

    scene bg74_1

    return
