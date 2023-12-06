


label whiskey:

    scene bg25

    "Интересно, что посетить в первую очередь..."
    menu:
        "{i}Пожарное депо{/i}":
            jump fire_station_1

        "{i}Исторический дом основателя города{/i}":
            jump march_1

        "{i}Храм на гравной площади{/i}":
            jump temple_1

        "{i}Пройтись по улицам{/i}":
            jump streets_1



label fire_station_1:

    scene bg28

    "{i}Итак, я начал свое заранее обдуманное, но от этого не ставшее менее загадочным путешествие по узким, мрачно‑болезненным улицам Инсмута.{/i}"
    "{i}Перейдя мост и свернув к шумному водосбросу, я прошел мимо фабрики Марша, откуда, к моему удивлению, не доносилось никаких звуков действующего производства.{/i}"
    "{i}Здание стояло на крутом откосе реки близ моста и площади с расходящимися улицами. Вероятно, именно здесь в прошлом находился городской центр, позднее переместившийся на Таун‑сквер.{/i}"

    scene bg27

    "{i}Ненадежный мост, к которому я приблизился, был снабжен запретительной надписью, но я все же рискнул и перешел по нему на южную сторону, где снова показались признаки жизни.{/i}"
    "{i}Скрытные, неуклюже передвигающиеся создания без всякого выражения поглядывали в мою сторону, а на более‑менее нормальных лицах отражалось нечто вроде холодного любопытства.{/i}"
    "{i}Инсмут раздражал меня все сильнее, и я направился по Пейн‑стрит в сторону Таун‑сквер, надеясь отыскать какое‑нибудь транспортное средство,{/i}"
    "{i}могущее отвезти меня в Аркхем еще до того, как придет время отправления зловещего восьмичасового автобуса.{/i}"

    jump fire_station_1_1


define z = Character("Зейдок Аллен", color="#0B888E")
define g = Character("Роберт Олмстед", color="#0B888E")
define v = Character("Валакеа", color="#0B888E")
define m = Character("Оубед Марш", color="#0B888E")

image insm_10 = im.Scale("insm_10.png", 1080 / 1.7, 1920 / 1.7)
image insm_10_2 = im.Scale("insm_10_2.png", 1080 / 1.7, 1920 / 1.7)

image zadok_1 = im.Scale("insm_9.png", 1080 / 1.6, 1920 / 1.6)
image zadok_2 = im.Scale("insm_9_1.png", 1080 / 1.6, 1920 / 1.6)
image zadok_3 = im.Scale("insm_9_2.png", 1080 / 1.6, 1920 / 1.6)
image zadok_4 = im.Scale("insm_9_3.png", 1080 / 1.6, 1920 / 1.6)

image marsh_1 = im.Scale("insm_6.png", 1080 / 1.6, 1920 / 1.6)
image marsh_2 = im.Scale("insm_6_1.png", 1080 / 1.6, 1920 / 1.6)

image val = im.Scale("insm_5.png", 1080 / 1.6, 1920 / 1.6)

label fire_station_1_1:

    scene bg29

    "{i}Тогда‑то я и увидел слева полуразрушенное пожарное депо и краснолицего старика с густой бородой и водянистыми глазами. На нем болтались невыразимые лохмотья,{/i}"

    image zadok = im.Scale("insm_9.png", 1080 / 1.6, 1920 / 1.6)
    show zadok at center

    "{i}а сам он сидел на скамье и разговаривал с двумя рыбаками, неопрятными, но выглядящими почти нормально. Похоже, это был тот самый Зейдок Аллен,{/i}"
    "{i}полубезумный, почти столетний пьянчужка, рассказывавший байки о старом Инсмуте.{/i}"
    "{i}Вряд ли старик мог сообщить нечто ценное, кроме смутных намеков да бессвязных и неправдоподобных историй;{/i}"
    "{i}к тому же меня предупредили, что общение с ним небезопасно, поскольку это наверняка не понравится местным жителям.{/i}"

    scene bg29

    "{i}И все же мысль об этом древнем свидетеле гибели города, помнившем былые времена кораблей и фабрик, была слишком соблазнительна.{/i}"
    "{i}В конце концов, даже самые странные и безумные мифы нередко суть символы и аллегории, основанные на правде, – а старый Зейдок видел все, что происходило с Инсмутом за последние девяносто лет.{/i}"
    "{i}Любопытство охватило меня, совершенно подавив осторожность.{/i}"
    "{i}В молодой своей самонадеянности я вообразил, что способен отделить крупицы реальной истории от сумбурных излияний, и все это можно будет проделать с помощью доброй порции виски.{/i}"

    scene bg30

    "{i}Я  привлек его внимание, махнув благоприобретенной бутылкой, и, вскоре убедившись, что он, шаркая ногами, задумчиво поплелся за мной,{/i}"
    "{i}свернул на Уотер‑стрит, в сторону местности, казавшейся мне наиболее пустынной.{/i}"

    scene bg28

    show zadok_1 at center

    z "{i}Эй, мистер!{/i}"

    scene bg28

    show zadok_1 at right
    show insm_10 at left

    g "{i}Да..{/i}"

    z "{i}Не хотите ли угостить старика порцией виски? Приезжий?{/i}"

    g "{i}Да, некоторые обстоятельства заставили оказаться в этом городе. Не могли бы вы..{/i}"

    z "{i}Ух, что вы, мистер, пожалуй, я не прочь побеседовать, но выбрать бы местечко менее людное чтоли... Знаете, они же... это... наблюдают за мной, а быть может и за вами уже..{/i}"

    scene bg31

    "{i}После этих слов Зейдок молча поплелся в сторону, как я уже понял причала, и мне ничего не оставалось как слепо следовать за ним.{/i}"
    "{i} Пока мы продолжали путь среди вездесущего запустения и опасно накренившихся руин, я попытался завязать разговор, но обнаружилось, что старый язык так быстро не развяжешь.{/i}"
    "{i} Наконец меж осыпающихся кирпичных стен я увидел открытый в сторону моря и заросший бурьяном пустырь перед жалкими остатками пристани.{/i}"
    "{i} Груды замшелых камней близ воды обещали стать сносными сиденьями, а с севера место надежно укрывали от посторонних глаз руины пакгауза.{/i}"

    scene bg31

    "{i}Место идеально подходило для долгой приватной беседы; я направился туда в сопровождении жаждущего компаньона, и мы уселись на замшелые камни.{/i}"
    "{i}Омерзительный запах тлена дополнялся тошнотворной рыбной вонью, но я решил потерпеть, ведь лучшего места все равно было не найти.{/i}"
    "{i}Для разговора, если я хотел успеть на восьмичасовой автобус до Аркхема, оставалось часа четыре, и я, не откладывая дела в долгий ящик,{/i}"
    "{i}предложил древнему выпивохе продолжить возлияние, а сам тем временем отдал должное своим скромным припасам.{/i}"

    scene bg32

    "{i}При этом я старался не переусердствовать с угощением – не хотелось, чтобы хмельная болтливость Зейдока раньше времени перешла в ступор.{/i}"
    "{i}Потребовался час на то, чтобы его разговорить, но и теперь он уклонялся от моих вопросов об Инсмуте и его мрачной истории,{/i}"
    "{i}болтая на злободневные темы и явив широкую газетную осведомленность вкупе с тягой к философствованию на этакий деревенский манер.{/i}"
    "{i}К концу второго часа я испугался, что с этой квартовой бутылью виски не добьюсь нужных результатов,{/i}"
    "{i}и уже подумывал, не лучше ли будет оставить старика Зейдока и скорее идти назад.{/i}"

    scene bg32

    "{i}Но случай сделал то, чего я не мог добиться своими вопросами; с присвистом дыша, Зейдок заговорил сам, и бессвязное стариковское бормотание заставило меня податься вперед и внимательно вслушаться.{/i}"
    "{i}Я сидел спиной к воняющему рыбой морю, а он – лицом к нему, временами обращая блуждающий взор к отсветам на низкой отдаленной линии Чертова рифа, и вдруг как‑то зачарованно показал рукой на волны.{/i}"
    "{i}Вид их, казалось, его беспокоил, ибо он начал с серии слабых проклятий, которые завершились потаенным шепотом и ищущим понимания взглядом искоса.{/i}"
    "{i}Он наклонился, тронул меня за отворот пиджака и с хрипловатым присвистом, но довольно внятно заговорил{/i}"

    show zadok_1 at center

    z "{i}Здесь вот это все и зачалося – это клятое место всех злодейств, вон там, где самая водяная глубь.{/i}"
    z "{i} Врата ада – прямо отсюда они толпой кидались на дно. Все это натворил капитан Оубед – подцепил енту заразу не на добро себе на островах южных морей. {/i}"

    show zadok_2 at center

    z "{i}Все в те дни пошло по худой дорожке. Ремесло упало, мельницы встали – даже новые, – и лучших наших парней поубивало на войне тыща восемьсот двенадцатого года,{/i}"
    z "{i}а какие сгинули с бригом «Элиза» и шаландой «Рейнджер» – обе посудины шли с товарами Гилмэна.{/i}"
    z " {i}У Оубеда Марша на плаву было три судна – бригантина «Коламби», бриг «Хетти» и барк «Королева Суматры».{/i}"
    z "{i}Он только один тогда торговал с Ост‑Индией и островами, хотя баркентина Эсдраса Мартина «Малайская невеста» бегала с товаром чуть не до двадцать восьмого года.{/i}"

    show zadok_1 at center

    z "{i}Никогда не видывал никого хуже капитана Оубеда – старое отродье сатаны!{/i}"

    show zadok_3 at center

    " {i}Кхе‑кхе!{/i}"

    show zadok_1 at center

    z "{i} Помнится, он говорил как‑то насчет веры, называл всех жителей дураками, мол, ходят на христианские собрания и носят свои бремена кротко и смиренно.{/i}"
    z "{i} Говорил, что лучше бы им выбрать себе других богов, вроде нижних, как у индейских народов,{/i}"

    show zadok_2 at center

    z " {i}которые дают туземцам за их жертвоприношения доброе рыболовство, и еще говорил, что только нижние боги по‑настоящему отвечают на молитвы людей..{/i}"

    scene bg33

    "{i}Мэтт Элиот, что плавал у него первым помощником, много чего тогда порассказал, он один не хотел, чтобы люди делали всякие языческие вещи.{/i}"
    "{i}Говорил об острове, что восточнее Отагейта, куда они ходили, что будто на нем прорва каменных развалин старее всего, что кто‑нибудь когда‑нибудь видел,{/i}"
    "{i}что‑то вроде Понапы на Каролинах, но с резными лицами, совсем как у больших статуй на острове Пасхи.{/i}"
    "{i}Там неподалеку был еще невеликий остров с вулканом, где они видели другие развалины со всякой резьбой – камни все поистерлись,{/i}"
    "{i}пока лежали под морем, но ужасные вырезные чудища покрывали их сплошь."

    scene bg34

    "{i}И захотел Оубед вызнать правду насчет их язычества.{/i}"
    "{i}Ведать не ведаю, как он это сделал, а только начал он промышлять торговлей из‑за тех золоченых цацек, что носили туземцы.{/i}"
    " {i}Все выпытывал у них, откудова они их взяли и нельзя ли раздобыть еще, и выведал все ж историю у старого вождя – у Валакеа, как они его называли.{/i}"
    "{i} Никто, кроме Оубеда, не поверил старому желтому дьяволу, но капитан‑то, он умел читать людей как книги.{/i}"
    "{i} Кхе‑кхе!{/i}"
    "{i} Никто никогда и мне не верил, даже когда я им и теперь говорю; вижу, и ты не веришь, молодой человек, хотя, посмотреть на тебя,{/i}"
    "{i}глаза‑то у тебя вроде такие же смышленые, как были у Оубеда.{/i}"

    scene bg35

    "{i}Ну так вот, сэр, Оубед, он узнал, что на ентой земле водятся такие твари, о каких люди никогда и слыхом не слыхивали – и не поверят, даже если им скажут.{/i}"
    "{i} Кажется, енти канаки множество своих юношей и девушек приносили в жертву каким‑то тварям вроде богов, что жили под морем и платили им за это всякого рода пользой.{/i}"
    " {i}Канаки повстречали тех тварей на малом островке со странными развалинами, и они казались им точь‑в‑точь теми ужасными рыбье‑лягушачьими чудищами, что вырезаны там на камнях.{/i}"
    " {i}Может, они все вроде существ, о каких говорят русалочьи истории и все такое.{/i}"
    " {i}У них на дне морском разные города, и ентот остров выпучился оттуда.{/i}"
    " {i}Кажется, там, наверху, оказалось несколько тех самых тварей, что жили в каменных зданиях, когда остров вдруг вылез наружу.{/i}"
    "{i} Так вот канаки и прознали про них, что они оттуда, снизу.{/i}"
    " {i}Сразу, как только высадились, поговорили с ними знаками, а вскоре учинили сделку. Этим тварям нравились человеческие жертвы.{/i}"
    "{i} Им когда‑то давным‑давно их приносили много, потом они надолго потеряли связь с верхним миром. Что они делали с жертвами, этого я не скажу,{/i}"
    "{i} и я так думаю, Оубед не хотел, чтобы кто‑нибудь слишком много об этом расспрашивал.{/i}"
    "{i} Но факт, что ента сделка показалась язычникам выгодной, потому что они переживали тяжкие времена и от нужды готовы были на всякое безумие.{/i}"

    scene bg36

    "{i} Дважды в год – в Вальпургиеву ночь и в канун Дня всех святых – они отдавали морским тварям точно такое число молодых людей, о каком условились.{/i} "
    "{i}Также давали им кой‑какие резные безделки, которые сами делали. А енти твари,{/i}"
    "{i}как обещали, давали им взамен прорву рыбы – они сгребали ее со всех морских глубин – и еще всякий раз давали сколько‑то золоченых вещей.{/i}"

    scene bg37

    "{i}Ну вот, встречались туземцы с тварями на малом острове с вулканом – приходили туда на каноэ с жертвами и всяким прочим, а назад плыли с золочеными драгоценностями.{/i}"
    "{i} Поначалу твари на главный остров к канакам сами никогда не приходили, но потом стали приходить своей охотой.{/i}"
    "{i} Видать, они безумно захотели смешиваться с канаками на церемониях в Вальпургиеву ночь и в канун Дня всех святых.{/i}"
    "{i} Они, видишь ты, могли жить и под водой, и снаружи – потому и зовутся анфибами, так я думаю. Канаки говорили им, мол, если люди с других островов прознают,{/i}"
    "{i} что они вообще здесь существуют, то захотят вымести их отсюда, но твари им отвечали, что тут нечего беспокоиться, потому что они сами могут отовсюду вымести детей человечьих как шелуху,{/i}"
    "{i} если те вздумают надоедать им, – мол, они могут такое, чему даже названия не придумано, потому что подобное делалось только один раз сгинувшими Прежними Существами, кто бы они ни были.{/i}"
    "{i} Но, не желая лишнего беспокойства, твари затаивались, когда на остров приплывали чужие.{/i}"
    "{i} А как дело подошло к спариванию с ентими жабьими рыбами, канаки будто поначалу не хотели, но потом узнали кое‑что, как на деле с этим спознались.{/i}"
    "{i} Оказалось, человечьи люди все вроде родни таким водяным бестиям: мол, все живое однажды вышло из вод и дожидалось только малой перемены, чтоб вернуться назад.{/i}"
    "{i} Твари сказали канакам, что если они смешают крови, то дети будут как нижние, сначала в человечьем виде, а потом превратятся и все больше будут похожи на бестий,{/i}"
    "{i} пока наконец не уйдут в воду и не соединятся там, внизу, с огромным множеством бестий.{/i}"
    "{i} И это в большинстве молодые парни – их превратили в рыбьих тварей, и они пошли в воду, чтобы никогда не умереть.{/i}"
    "{i} Енти твари никогда не умирают, разве что их насильно убьют. {/i}"
    "{i}Ну вот, сэр, со временем Оубед вроде узнал, что тех островитян их водяные твари наполнили рыбьей кровью.{/i}"
    "{i} Когда они старели и это делалось заметно, то держались скрытно, пока не почувствуют, что им уже хочется оставить селение и идти в воду.{/i}"
    " {i}Некоторым больше это нравилось, чем другим, а некоторые медленно изменялись и долго не хотели идти в воду; но в большинстве они сурьезно относились к пути, указанному им бестиями.{/i}"
    "{i} Тот, кто от рождения больше походил на тварей, превращался легко и исчезал безвозвратно, а тот, кто рождался почти человечьего облика,{/i}"
    "{i} иногда оставался на острове лет, почитай, до семидесяти, хотя обычно и до этого ходил вниз, чтобы попробовать плавать. {/i}"
    "{i}Туземцы, уходившие в воду на время, сколько‑то побыв там, возвращались, и будто кое‑кто разговаривал там, внизу, со своим прапрапрапрапрадедом,{/i}"
    " {i}оставившим сушу два века назад или того раньше.{/i}"

    scene bg38

    "{i}После этого все они позабыли про то, что такое смерть – за исключением гибели в войнах с племенами соседних островов, да жертвоприношений подводным богам;{/i}"
    " {i}ну, разве еще если змея ядовитая укусит, или чума какая поразит, прежде чем -они успеют спуститься под воду.{/i}"
    "{i} В общем, стали они ждать-поджидать, когда же с ними произойдет превращение, которое на поверку оказалось не таким уж страшным.{/i}"
    "{i} Просто прикинули и решили, что то, что приобретали, намного больше того, что при этом теряли, да и сам Оубед,{/i}"
    "{i} как я понимаю, тоже пришел к такому же выводу, когда хорошенько помозговал над историей, которую рассказал им этот самый Валакеа.{/i}"
    "{i} Что же до этого Валакеа, то он был одним из немногих, в ком совершенно не было рыбьей крови – он принадлежал к королевскому роду,{/i}"
    "{i} который вступал в брак только с такими же царственными особами с соседних островов.{/i}"

    scene bg39

    show marsh_1 at left
    show val at right

    v "{i}Господин, вам необходимо будет знать некоторые заклинания и обряды, чтобы держать под контролем морских существ,{/i}"
    v "{i} сделать так чтобы заключенный договор поддерживался. Но и вам, в свою очередь, необходимо его соблюдать, несмотря ни на что...{/i}"
    v "{i} щадить они не будут, я вас уверяю...{/i}"

    scene bg39

    show val at right
    show marsh_2 at left

    m "{i}Это звучит довольно...{/i}"

    v "{i}Ничего страшного, я обучу вас всему тому, что сам знаю и умею. Уверен у вас получится.{/i}"


    scene bg39

    show val at right
    show marsh_1 at left

    m "{i}Однако, ужасно видеть изменяющихся жителей деревни. Вас не смущает это?{/i}"

    v "{i}Вовсе нет, это всего лишь необходимая мера, тем более ведущая к вечной жизни, процветаю деревни.{/i}"
    v "{i} Разве это не оправдывает все жертвы? Племя процветает... и это главное{/i}"

    m "{i}И зачем вы мне дали эту странную штуку, похожую на простое украшение? Какая-то подвеска?{/i}"

    v "{i}Это амулет. С него помощью ты сможешь заманить рыбу откуда угодно. Произнеси нужное заклинание и брось в воду.{/i}"
    v " {i}Можешь использовать его где угодно, чтобы поймать рыбу, сколько тебе нужно.{/i}"

    scene bg39

    show val at right
    show marsh_2 at left

    m "{i}Спасибо, Валакеа.{/i}"

    scene bg40

    "{i}Мэру вся эта история очень не понравилась, и он хотел, чтобы Оубед держался подальше от этого острова.{/i}"
    "{i} Но капитан тогда уже помешался на этой затее, потому как обнаружил, что может по дешевке скупать золото,{/i}"
    "{i} причем в таком количестве, что должен всерьез заняться этим бизнесом. Так продолжалось много лет кряду,{/i}"
    "{i} и Оубед получил столько золота, что даже смог построить свою фабрику – как раз на том самом месте, где была старая мельница Уэйта.{/i}"

    scene bg41

    "{i} Он решил не продавать золото в том виде, в каком оно к нему попадало, то есть в этих цацках, поскольку могли возникнуть всякие вопросы.{/i}"
    "{i} И все же члены его экипажа иногда толкали налево какую-нибудь побрякушку, хотя он и взял с них слово молчать;{/i}"
    "{i} да и сам иногда позволял своим женщинам что-нибудь поносить, но только выбирал, чтобы было похоже на человеческие украшения.{/i}"

    scene bg42

    "{i}Ну вот, так продолжалось до тридцать восьмого – мне тогда было семь лет, – когда Оубед обнаружил,{/i}"
    "{i} что от тех островитян почти никого не осталось.{/i}"
    "{i} Похоже на то, что люди с других островов почуяли, откуда ветер дует, и решили взять все это под свой контроль.{/i}"
    "{i} Как знать, может они сами порастаскивали все те волшебные знаки, которые, как говорили сами морские существа, были для них важнее всего.{/i}"
    "{i} Люди они были набожные, а потому не оставили там камня на камне – ни на главном острове,{/i}"
    "{i} ни на маленьком вулканическом островке, – кроме разве лишь самых крупных развалин, к которым и подступиться-то было трудно.{/i}"
    "{i} В некоторых местах там потом находили такие маленькие камушки, вроде талисманов, что ли, а на них нарисовано было то,{/i}"
    "{i} что сейчас называют, кажется, свастикой. Может, это были знаки самих Старожилов.{/i}"
    "{i} Все парни того племени поразбрелись кто куда, от золотых вещей тоже никаких. следов не осталось,{/i}"
    "{i} а про самих этих канаков даже словом боялись обмолвиться. Вообще стали говорить, что на том острове никогда и в помине не было людей.{/i}"

    scene bg43

    "{i} Вот тогда-то Оубед и стал поносить всех и проклинать на чем свет стоит за то, что, дескать, верили в своего христианского бога,{/i}"
    "{i}  да что-то не очень он им помог за это. А потом стал рассказывать им про других людей, которые молились другим богам,{/i}"
    "{i}  зато получали за это все, что душе было угодно. И еще сказал, что если найдется кучка крепких парней,{/i}"
    "{i}  которые согласятся пойти за ним, то он попробует сделать так, чтобы снова появились и золото, и рыба.{/i}"

    scene bg44

    "{i}  Разумеется, они плавали с ним на «Суматранской королеве», видели те острова и потому понимали, о чем идет речь.{/i}"
    "{i}  Поначалу им не очень-то хотелось столкнуться с теми существами, о которых они были много наслышаны,{/i}"
    "{i}  но поскольку сами они толком ничего не знали, то постепенно стали верить Оубеду и спрашивать его, что им надо сделать,{/i}"
    "{i}  чтобы все стало как прежде, чтобы вера их принесла им то, чего они хотели.{/i}"

    scene bg32

    show zadok_3 at right
    show insm_10_3 at left

    z " ..."

    g "{i} Сэр?{/i}"

    z "{i}Бедный Мэтт…{/i}"
    z "{i}он всегда был против этого…{/i}"
    z "{i}пытался привлечь парней на свою сторону,{/i}"
    z "{i}а потом подолгу беседовал с пастором…{/i}"
    z "{i}все было бестолку…сначала они прогнали из города протестантского священника,{/i}"
    z "{i}потом методистского; с тех пор я ни разу не видел нашего Неистового Бэбкока – он заправлял прихожанами-баптистами.{/i}"
    z "{i}О, Иегова, дождутся они гнева твоего!{/i}"
    z "{i}Сам я тогда еще совсем щенком был, но все равно видел и слышал все, что там творилось.{/i}"
    z "{i}Дэгон и Ашторет – Сатана и Вельзевул… Идолы Канаана и филистимлян… страхи вавилонские – Мене, мене текел упарсин…{/i}"

    g "{i} ... {/i}"

    scene bg32

    show zadok_3 at center

    "{i}Ну как, не поверили мне, да?{/i}"
    "{i} Хе-хе-хе,{/i}"
    "{i} но тогда скажите, молодой человек, зачем капитан Оубед и двадцать его парней взяли{/i}"
    "{i} за правило плавать глухими ночами к рифу Дьявола и хором распевать там свои песни, да так громко,{/i}"
    "{i} что при соответствующем ветре их можно было даже в городе. услышать?{/i}"
    "{i} Ну, что вы мне на это ответите?{/i}"

    scene bg32

    show zadok_2 at center

    "{i} И еще скажите, зачем он всегда бросал в воду какие-то тяжелые предметы, причем по другую сторону рифов, на глубине,{/i}"
    "{i} где подводная их часть обрывается в бездну, да такую, что еще никому не удавалось до дна достать?{/i}"
    "{i} Скажите, что он сделал с той свинцовой штуковиной, которую ему дал Валакеа? Ну как, юноша?{/i}"
    "{i} И что они там выкрикивали, когда собирались в канун мая и еще перед днем всех святых, а?{/i}"
    scene bg32

    show zadok_3 at center
    "{i} И почему новые церковные пасторы – в прошлом матросы – носят свои диковинные наряды{/i}"
    "{i} и надевают на голову всякие золотые украшения вроде тех, что привозил капитан Оубед?{/i}"
    "{i} Ну как, можете вы на все это мне ответить?{/i}"

    scene bg32

    show zadok_4 at center

    "{i}Э-хе-хе-хе! Ну как, начинаете соображать?{/i}"
    "{i}Может, хотели бы оказаться на моем месте в те дни, когда я по ночам глазел на море, стоя на крыше своего дома?{/i}"
    "{i}И потом, скажу я вам, маленькие дети всегда любят подслушивать, так что я был в курсе всего, о чем судачили в те времена,{/i}"
    "{i}что говорили про капитана Оубеда и тех парней, которые плавали на риф!{/i}"
    "{i}Хе-хе-хе!{/i}"
    scene bg32

    show zadok_3 at center

    "{i}А что вы скажете насчет той ночи, когда я тайком взял старую отцовскую подзорную трубу, принес ее на крышу и увидел через нее,{/i}"
    "{i}что весь риф усеян какими-то блестящими существами, которые, как только взошла луна, сразу же попрыгали в воду?{/i}"
    "{i}Оубед с парнями только еще плыли на лодке, а те твари уже соскочили в воду, причем с другой,{/i}"
    "{i}глубоководной стороны рифа, и назад больше не вернулись…{/i}"
    "{i}Что бы вы сказали, если бы сами оказались на месте щенка, видевшего все эти фигуры, которые вовсе и не были человеческими фигурами?..{/i}"
    "{i}Ну, как вам это?..{/i}"

    scene bg32

    show zadok_2 at center

    "{i}Хе-хе-хе…{/i}"

    scene bg32

    show zadok_4 at center

    "{i}А представьте себе, что однажды ночью вы видите, как Оубед отправился к рифу на своей лодке,{/i}"
    "{i}груженой чем-то большим и тяжелым, а на следующий день все узнают, что из одного дома пропал молодой парень.{/i}"

    scene bg32

    show zadok_3 at center

    "{i}Хей!{/i}"

    scene bg32

    show zadok_1 at center

    "{i}Видел ли кто хотя бы раз после этого Хирама Джилмена, или Ника Пирса, или Луэлли Уэйта, или Адонирама Саусвика, или Генри Гаррисона?{/i}"

    scene bg32

    show zadok_3 at center

    "{i}Хе~хе, хе, хе…{/i}"
    "{i}Существа эти изъяснялись при помощи знаков, которые подавали своими руками… а руки у них, похоже, ловкие были…{/i}"

    scene bg32

    show zadok_4 at center

    "{i}Ну так вот, сэр, именно тогда-то Оубед и стал снова подниматься на ноги.{/i}"
    "{i}Люди видели на трех его дочерях такие украшения, которых у них в жизни не было, да и дымок стал куриться над его фабрикой.{/i}"
    "{i}И другие парни тоже зажили припеваючи – рыбы в гавани стало хоть пруд пруди, и видели бы вы,{/i}"
    "{i}какие пароходы с грузом мы снаряжали перед их отправкой в Аркхэм, Ньюбэрипорт и Бостон.{/i}"
    "{i}Именно тогда Оубед снова восстановил старую железную дорогу.{/i}"

    scene bg32

    show zadok_2 at center

    "{i}Несколько рыбаков из Кингспорта прослышали про невиданные уловы здешних парней и наведались сюда на своем шлюпе,{/i}"
    "{i}да только все они куда-то пропали, так что никто их с тех пор не видел.{/i}"
    "{i}Вот тогда-то наши парни и организовали этот самый «Тайный орден Дэгона»,{/i}"
    "{i}прикупив для него здание старой масонской ложи…{/i}"

    scene bg32

    show zadok_1 at center

    "{i}Хе,хе,хе,хе!{/i}"
    "{i}Мэтт Элиот был масоном и возражал против того, чтобы дом продавали им, но вскоре и он куда-то исчез.{/i}"

    "{i}Помните, я говорил, что поначалу Оубед ничего не хотел менять в жизни островитян– канаков?{/i}"
    "{i}Думаю, что сначала у него и в мыслях не было заниматься каким-то скрещиванием с этим племенем,{/i}"

    scene bg32

    show zadok_4 at center

    "{i}не надо ему было выращивать людей, которые будут уходить под воду ради бессмертной жизни.{/i}"
    "{i}Все, что ему требовалось, это золото, за которое он готов был платить большую цену,{/i}"

    scene bg32

    show zadok_3 at center

    "{i}и те, другие, тоже вроде бы некоторое время этим ограничивались…{/i}"

    "{i}В сорок шестом в городе, однако, начали кое над чем задумываться.{/i}"
    "{i}Слишком часто стали пропадать люди, очень уж дикие стали читаться проповеди{/i}"
    "{i}на воскресных сборищах и чересчур много разговоров пошло об этом самом рифе.{/i}"
    "{i}Кажется, и я тоже приложил к этому свою руку – рассказал члену городского управления{/i}"
    "{i}о том, что видел с крыши своего дома.{/i}"

    scene bg32

    show zadok_2 at center

    "{i}Как-то однажды они – то есть Оубед и его парни – организовали на рифе что-то вроде сходки,{/i}"
    "{i}и до меня донеслась какая-то пальба, которая велась между несколькими лодками.{/i}"
    "{i}На следующий день Оубед и еще тридцать два его человека оказались в тюрьме, а все вокруг гадали и толковали,{/i}"
    "{i}в чем там дело и какое обвинение им могут предъявить.{/i}"

    scene bg32

    show zadok_4 at center

    "{i}О, Боже, если бы хоть кто-нибудь смог заглянуть вперед… хотя бы на несколько недель,{/i}"
    "{i}в течение которых никто не исчезал и никого не сбрасывали в море.{/i}"

    scene bg45

    show zadok_4 at center

    "{i}В ту ужасную ночь… я увидел их.{/i}"
    "{i}Я снова был у себя на крыше… скопления их… {/i}"
    "{i}чуть ли не настоящие толпы покрывали своими телами поверхность всего рифа, а потом поплыли через гавань в сторону устья Мэнаксета… {/i}"
    "{i}Боже, что творилось в ту ночь на улицах Иннсмаута… {/i}"

    scene bg45

    show zadok_3 at center

    " {i}они колотили в наши двери, но отец не открывал… {/i}"
    "{i}Толпы мертвецов и умирающих… выстрелы и вопли… {/i}"
    "{i} крики на старой площади и центральной площади в Нью-Черч Грин – ворота тюрьмы нараспашку… {/i}"
    "{i}какое-то воззвание… измена… {/i}"

    scene bg45

    show zadok_2 at center

    "{i}все это назвали чумой, когда люди вошли внутрь и обнаружили, что половина наших парней отсутствует…{/i}"
    "{i} никто не спасся, только те, что были с Оубедом, и еще эти существа, или кто там они были…{/i}"
    "{i} а потом все успокоилось, хотя больше своего отца я никогда не видел…{/i}"

    scene bg32

    show zadok_4 at center

    "{i} Наутро все прояснилось – но после них остались следы… {/i}"
    "{i} Оубед взял все под свой контроль и сказал, что намерен многое изменить…{/i}"
    "{i}  сказал, что остальные тоже будут молиться с ними в назначенный час, а в некоторых домах появятся, как он сказал, гости… {/i}"
    "{i} им хотелось смешаться с нашими людьми, как они поступили с канаками, и никто не мог остановить их.{/i}"
    "{i}  Далеко зашел этот Оубед… словно совсем взбесился.{/i}"
    "{i} Говорил, что они принесут нам все – рыбу, сокровища, но и мы дадим им все, чего они пожелают…{/i}"

    scene bg32

    show zadok_3 at center

    "{i}Внешне как будто ничего не изменилось, только нам приходилось вести себя с этими чужаками совсем смирно,{/i}"
    "{i} если, конечно, жизнь была дорога.{/i}"

    "{i}Всем нам пришлось принести присягу на верность Ордену Дэгона,{/i}"
    "{i} а потом пришел черед второй и третьей клятв, которые кое-кто из нас тоже произнесли.{/i}"
    "{i} За все это они могли оказать какую-нибудь услугу, или наградить чем-нибудь особым – золотом или вроде того,{/i}"
    "{i} а сопротивляться им было бесполезно – их ведь там, под водой, целые полчища.{/i}"

    scene bg32

    show zadok_2 at center

    "{i} Обычно они не поднимались на поверхность и не трогали людей, но если что-то понуждало их к этому,{/i}"
    "{i} то тогда сладу с ними не было никакого,{/i}"

    scene bg32

    show zadok_4 at center

    "{i} Мы не дарили им резных амулетов, как это делали туземцы из южною моря, но и не знали, что им надо,{/i}"
    "{i} потому как канаки не раскрывали ни перед кем своих секретов.{/i}"

    "{i} От нас требовалось только регулярно приносить им кого– нибудь в жертву,{/i}"
    "{i}  снабжать всякими дикими безделушками да еще давать приют в юроде – вот тогда они готовы были оставить нас в покое.{/i}"
    "{i}  И еще они терпеть не могли посторонних, чужаков,{/i}"

    scene bg32

    show zadok_3 at center

    "{i}  чтобы слухи о них не просочились за пределы города – новому человеку прежде надо было помолиться за них.{/i}"
    "{i}  Так все мы и оказались в этом «Ордене Дэгона» – зато дети никогда не умирали, {/i}"
    "{i} а просто возвращались назад к матери Гидре и отцу Дэгону, от которых мы все когда-то произошли… {/i}"

    scene bg32

    show zadok_4 at center

    "{i} Йа! Йа!{/i}"
    "{i}  Ктулху фхтагн!{/i}"
    "{i}  Ф'нглуи мглв`тафх Ктулху Р'лия вгах-нагл фхтагн…{/i}"


    scene bg32

    show zadok_2 at center

    "{i} Боже, что же довелось мне повидать с той поры, когда я был пятнадцатилетним мальчишкой.{/i}"
    "{i}  Мене, мене, текел, упарсин! {/i}"
    "{i} Как исчезали люди, как они накладывали на себя руки – когда слухи об этом достигали Аркхэма,{/i}"
    "{i}  Ипсвича, или других городов, там считали, что мы здесь все с ума посходили, вот как вы сейчас считаете, что я тоже помешался…{/i}"
    "{i}  Но Боже мой, что мне довелось повидать за свою жизнь!{/i}"
    "{i}  Меня бы уже давно прикончили за все то, что я знаю, только я успел произнести вторую клятву Дэгона,{/i}"

    scene bg32

    show zadok_1 at center

    "{i}  а потому меня нельзя трогать, если только их суд не признает, что я сознательно рассказал о том, что знаю…{/i}"
    "{i}  но третью клятву я не произнесу – я скорее умру, чем сделаю это…{/i}"

    scene bg32

    show zadok_3 at center

    "{i} А потом, примерно когда Гражданская война началась, стали подрастать дети, которые родились после того сорок шестого года, да,{/i}"
    "{i}  некоторые из них…{/i}"
    "{i}  Я тогда сильно перепугался и никогда больше после той ужасной ночи не подсматривал за ними,{/i}"
    "{i}  и больше никогда их не видел – на всю жизнь тогда насмотрелся.{/i}"
    "{i}  Нет, ни разу больше не видел, ни одного.{/i}"

    scene bg32

    show zadok_2 at center

    "{i}  А потом я пошел на войну, и если бы у меня хватило тогда ума, то ни за что бы не вернулся в эти места,{/i}"
    "{i}  уехал бы потом куда глаза глядят, только подальше отсюда. {/i}"
    "{i} Но парни написал и мне, что дела идут в общем-то неплохо,{/i}"
    "{i}  Это, наверное, потому, что после шестьдесят третьего в городе постоянно находились правительственные войска.{/i}"
    " {i} А как война закончилась, снова настали черные времена. {/i}"

    scene bg32

    show zadok_4 at center

    "{i} Люди стали разбегаться – мельницы не работали, магазины закрывались, судоходство прекратилось, {/i}"
    "{i} гавань словно задыхалась – железная дорога тоже остановилась.{/i}"

    scene bg32

    show zadok_3 at center

    "{i}  Но они…они никогда не переставали плавать вверх и вниз по реке, туда-сюда, постоянно прибывая со своего проклятого,{/i}"
    "{i}  сатанинского рифа – и с каждым днем все больше окон заколачивалось, а из домов,{/i}"
    "{i}  в которых вроде бы никто не должен жить, раздавались какие-то звуки…{/i}"

    scene bg32

    show zadok_1 at center

    


label march_1:
    "МОХМОХ"

label temple_1:
    "МОХМОХ"

label streets_1:
    "МОХМОХ"

    return
