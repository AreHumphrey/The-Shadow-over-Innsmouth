﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.


# Игра начинается здесь:
label start:
    jump chapter_2
    scene bg1

    "{i}Зимой 1927/28 года агенты федерального правительства произвели секретное расследование в старинном портовом городке Инсмут, штат Массачусетс.{/i}"

    "{i}Общественность впервые узнала об этом в феврале, когда прокатилась большая волна облав и арестов,{/i}"

    "{i}после которой сожгли и взорвали – с известными,
     конечно, предосторожностями – огромное количество ветхих, изъеденных червями и, как все полагали, давно покинутых зданий близ опустевшего порта.{/i}"

    "{i}Нелюбопытные души сочли все это одним из главных сражений в судорожной войне с бутлегерством.{/i}"

    scene bg2
    "{i}Но люди, жадные до сенсаций, не переставали дивиться невероятному обилию арестов,{/i}"
    "колоссальному числу полицейских и военнослужащих, брошенных на это дело, и засекреченности данных о местонахождении узников."
    "Причем отсутствовали не только сообщения о судебных разбирательствах или хотя бы о конкретных обвинениях,"
    "но и какая‑либо информация о пребывании задержанных в обычных тюрьмах."
    "Строились смутные догадки насчет инфекционных бараков и концентрационных лагерей,"
    "а позже – о рассредоточении арестантов по военно‑морским и армейским тюрьмам, но ничего определенного никто сказать не мог."
    "Инсмут тогда почти обезлюдел и только теперь начинает подавать признаки медленного возвращения к жизни."

    "Недовольство либеральных организаций власти нейтрализовали долгими конфиденциальными собеседованиями,"
    "а их представителей допустили в некоторые лагеря и тюрьмы. В результате эти организации стали на удивление пассивны и сдержанны."
    "Газетчики проявили большую настойчивость, но и они в конце концов поддались на уговоры властей."
    "Только одна газета – но уж таковы бульварные газеты с их неуемным азартом – разродилась сообщением о некоей подводной лодке,"
    "выпустившей торпеды в морскую пучину за Чертовым рифом."
    "Но эта сенсация, основанная на слухах из портовых притонов, выглядела слишком уж притянутой за уши,"
    "тем более что упомянутый риф расположен в добрых полутора милях от собственно Инсмута."

    "Даже в соседних городках люди, обсуждая эти события, старались поменьше сообщать о них внешнему миру."
    "Пересуды о вымирающем и почти заброшенном Инсмуте велись уже чуть ли не столетие, и сейчас, в сущности, не произошло ничего нового,"
    "более дикого и отвратительного, нежели то, о чем говорилось в прошлые годы. У местных жителей было много причин хранить молчание,"
    "так что властям не пришлось особо давить на них, призывая к сдержанности. К тому же они мало что знали на самом деле;"
    "из‑за обширных, пустынных и безлюдных низин, затопляемых во время прилива, добрососедских отношений с жителями Инсмута у них никогда не водилось."

    "Но я в конце концов решил прервать заговор молчания, связанный с этими событиями."
    " Результаты, я уверен, не принесут большого вреда – разве что шок отвращения, когда общественность узнает,"
    " что именно было обнаружено в Инсмуте потрясенными участниками тех полицейских операций. "
    "В то же время вскрытые факты могут иметь очень разные объяснения. Мне и самому известна только часть этой истории,"
    " но у меня достаточно причин не влезать в расследование еще глубже. Моя связь с этим делом и так оказалась более чем тесной,"
    " и полученные тогда впечатления еще отразятся – причем самым радикальным образом – на моем будущем."

define n = Character(None, kind=nvl, window_left_padding=-100, window_yoffset=40)




label chapter_1:
    scene bg3

    "Собственно, это не кто иной, как я, охваченный безумным ужасом, бежал из Инсмута в ранние утренние часы шестнадцатого июля 1927 года,"
    " и это именно мой панический призыв к властям произвести расследование дал толчок последующим событиям."
    " Я не хотел прерывать молчание, пока дело было свежо в памяти его непосредственных участников;"
    " но теперь, когда к этой старой истории уже утрачен интерес любознательной публики,"
    " во мне растет желание поведать об ужасающих часах, что я провел в том издавна пользующемся дурной славой морском порту,"
    " в логове гибельных и богопротивных пороков. Надеюсь, этот рассказ поможет мне самому поверить в то,"
    " что я еще в своем уме и что я не оказался всего‑навсего жертвой кошмарных галлюцинаций. "
    scene bg4

    "Это также поможет мне собраться с духом перед ужасным шагом, который мне вскорости предстоит совершить. "
    "О существовании Инсмута я узнал за день до того, как увидел его в первый и – на данный момент – последний раз."
    " Решив отметить предстоящее совершеннолетие путешествием по Новой Англии – полюбоваться природой, "
    "стариной и заодно выяснить кое‑что по части собственной генеалогии, – я планировал добраться из старинного Ньюберипорта до Аркхема, откуда происходил род моей матери."
    " Не имея машины, я путешествовал поездом либо автобусом, стараясь по возможности экономить на дорожных расходах."
    " Как сейчас помню начало этой истории, которая навсегда перевернула мою жизнь..."

    define i = Character("Кассир", color="#0B888E")

    scene bg5
    image insm_7 = im.Scale("insm_7.png", 1080 / 1.6, 1920 / 1.6)
    image insm_7_1 = im.Scale("insm_7_1.png", 1080 / 1.6, 1920 / 1.6)
    show insm_7 at center
    i "{i}Есть тут один дряхлый автобус. Он, правда, делает крюк, заезжая в Инсмут – вы, может, слышали о нем, – так что людям это не нравится.{/i}"
    i" Водит его инсмутский малый по имени Джо Сарджент, и пассажиров у него всегда негусто – что здесь, что в Аркхеме."
    i" Удивляюсь, как вообще люди решаются ездить на этаком тарантасе. Однако проезд стоит недорого, хоть я никогда не видал, чтобы кто‑то, кроме инсмутских жителей, им пользовался."
    i" Он отходит с площади – остановка напротив аптеки Хаммонда – дважды в день: в десять утра и семь вечера, если только ничего не изменилось в последнее время."
    i" Впрочем, я бы на вашем месте не рискнул садиться в эту жуткую развалюху."

    scene bg6

    n 'Это было первое, что я узнал о помраченном Инсмуте. Подобная справка о городе, не обозначенном на обычных картах'
    n 'и не упоминаемом в современных путеводителях, как и отдельные намеки в рассказе кассира возбудили мое любопытство.'
    n 'Город, способный внушить соседям такую неприязнь, подумал я, на самом деле может оказаться гораздо более примечательным'
    n 'и вполне достойным внимания туриста. Если он расположен по пути в Аркхем, я должен его посетить'

    scene bg5
    show insm_7 at center
    i "{i}Есть тут один дряхлый автобус. Он, правда, делает крюк, заезжая в Инсмут – вы, может, слышали о нем, – так что людям это не нравится.{/i}"
    show insm_7_1 at center
    i"{i}Инсмут? Ну, это захолустный такой городишко в устье Мануксета.{/i}"
    i "{i}Было время, когда он что‑то собой представлял – до войны тысяча восемьсот двенадцатого там был порт, – но за последнюю сотню лет он превратился в труху, разваливается на глазах. {/i}"
    i "{i}Теперь туда и поезда не ходят – «Бостон‑Мэн» и прежде проходил стороной, а несколько лет назад закрыли и ветку из Ровлея.{/i}"
    show insm_7 at center
    i "{i}Там, я думаю, пустых домов больше, чем людей, да и занятий никаких нет, разве что рыбу ловят да омаров.{/i}"
    i "{i} Торгуют в большинстве здесь, еще в Аркхеме да Ипсвиче. Когда‑то у них было несколько мельниц, но ничего не осталось,{/i}"
    i "{i} кроме одного золотоплавильного заводика, да и тот нынче на ладан дышит.{/i}"
    i "{i} А в свое время завод, скажу я вам, без дела не стоял, и старик Марш, его владелец, будет побогаче Креза.{/i}"
    i "{i} Странный тип, однако, хоть и слывет крупной шишкой среди своих. Но у него не то кожная болезнь, не то уродство какое, появившееся недавно, так что на глаза людям не показывается. {/i}"
    i "{i}Он внук капитана Оубеда Марша, основателя дела. Его мать вроде была иностранкой – говорили, откуда‑то с островов южных морей, – так что большой был скандал,{/i}"
    i "{i} когда он пятнадцать лет назад женился на девушке из Ипсвича. Здесь это не приветствуют – и горожане, и люди из окрестностей стараются скрыть инсмутскую кровь, если та течет в их жилах.{/i}"
    i "{i} Но дети и внуки Марша выглядели совсем нормально, насколько я могу судить. Мне их как‑то показывали, однако потом старшие из детей здесь уже не появлялись. {/i}"
    i "{i} А вот старика того и вообще никогда не видел.{/i}"
    show insm_7_1 at center
    i "{i}Спросите, почему все так пренебрегают Инсмутом? Ну, молодой человек, вы не ошибетесь, если поверите тому, о чем говорят здесь повсюду.{/i}"
    i "{i} Дыма без огня не бывает – уж если народ поговаривает, это неспроста. Люди болтают об Инсмуте – шепотом по большей части – уже чуть не сто лет, вот я и думаю, все потому,{/i}"
    i "{i} что инсмутцы отвратительнее кого бы то ни было в этих местах. {/i}"
    i "{i}Некоторые сплетни рассмешили бы вас – насчет, например, старого капитана Марша: вроде он заключил сделку с дьяволом и поставлял из ада чертенят,{/i}"
    i "{i} чтобы жили в Инсмуте, или о чем‑то вроде сатанинского культа и жутких жертвоприношениях в одном местечке близ пристаней – это будто бы происходило году в тысяча восемьсот сорок пятом или около того; {/i}"
    i "{i}но я прибыл сюда из Пэнтона, штат Вермонт, и такого рода россказням веры не даю.{/i}"
    show insm_7 at center
    i "{i}Вы, может, еще услышите, что тут со стародавних времен болтают о черном рифе у побережья – они называют его Чертовым рифом.{/i}"
    i "{i} Большую часть времени он торчит над водой, а в прилив если и скрывается, то самую малость, но все же островом его не назовешь.{/i}"
    i "{i} Говорят, что там, на этом рифе, показывается иногда целый легион чертей, расползающихся повсюду и снующих туда‑сюда через какие‑то дыры вроде пещер возле верхушки. {/i}"
    i "{i}Эта зазубренная штуковина торчит в миле с лишним от берега, и моряки обычно делают большой крюк, чтобы его обогнуть.{/i}"
    i "{i}Я говорю о моряках, которые родом не из Инсмута. Они крепко невзлюбили старого капитана Марша за то, что он будто бы иногда высаживался на рифе по ночам, во время отлива.{/i}"
    i "{i} Может, оно и верно – место это уединенное, так что он мог выискивать там старый пиратский клад, а то и нашел его; но ходили еще слухи, что он якшается там с демонами.{/i}"
    i "{i} Слухи слухами, однако я полагаю, что риф обрел дурную славу именно из‑за старого капитана.{/i}"
    i "{i}Но это было еще до большой эпидемии тысяча восемьсот сорок шестого года, когда в Инсмуте перемерла половина народу.{/i}"
    i "{i}Они так и не выяснили, откуда взялась зараза – скорее всего, ее занесли на кораблях из Китая или иных дальних мест.{/i}"
    i "{i} Можно представить, что там творилось, – бунты, беспорядки и всякие ужасы, но, насколько я знаю, города никто не покидал,{i}"
    i "{i} зато сам город остался в страшном виде, да и живет там теперь не больше трех‑четырех сотен человек.{/i}"
    i "{i}Но главное, люди по всей округе испытывают к ним что‑то типа расовой ненависти – и я их не осуждаю.{/i}"
    show insm_7_1 at center
    i "{i} Я и сам терпеть не могу этот инсмутский народец и не имею ни малейшего желания посетить их городишко.{/i}"
    i "{i} Полагаю, вам известно – хотя, по говору судя, вы с Запада, – что много кораблей из Новой Англии ходило в подозрительные порты Африки, Азии, южных морей и черт знает куда еще, а возвращаясь,{/i}"
    i "{i}они привозили всякого рода сомнительных пассажиров. Может, вы слышали насчет человека из Салема, вернувшегося домой с женой‑китаянкой, а в районе Кейп‑Кода, говорят, до сих пор живут выходцы с островов Фиджи.{/i}"
    i "{i}Вот и с этими инсмутцами дело нечисто, можете мне поверить. Место всегда было плохое, отрезанное болотами, заливами и устьем реки, так какая у нас может быть уверенность насчет всех их ходов‑выходов и разных {/i}"
    i "{i}там делишек? Но все знают, что старый капитан Марш годах в двадцатых или тридцатых – прошлого века, разумеется, – когда все три его судна еще были на плаву, как‑то привез невесть откуда мерзкого вида дикарей.{/i}"
    i "{i} Да уж, есть в этих инсмутцах какая‑то дурная примесь, – не знаю, чем и объяснить, но это сразу чувствуется.{/i}"
    i "{i}Если вы сядете в автобус Джо Сарджента, то по одному виду водителя многое поймете о тамошней публике.{/i}"
    i "{i}У большинства из них необычно сплюснутые головы с плоскими носами и выпученными глазами, которых они никогда вроде и не закрывают, да и про кожу их не скажешь, что она больно чиста.{/i}"
    i "{i}Грубая и будто запаршивевшая, а шеи какие‑то сморщенные и все в складках. Плешивых много, даже среди молодежи. Кто постарше выглядят и того хуже, а настоящих стариков из Инсмута я не видал вовсе.{/i}"
    i "{i} Небось, мрут как мухи, глядя в стакан. Животные тоже их ненавидят: с лошадьми у них вечно были проблемы, покуда не появились автомобили.{/i}"
    i "{i}Никто вокруг – возьмите хоть Аркхем, хоть Ипсвич – не хочет иметь с ними дел, а они сами держатся нелюдимо – и когда сюда, в город, приходят, и когда кто‑нибудь пытается ловить рыбу у их берега.{/i}"
    i "{i}Вообще, странно, рыбы там всегда навалом, хотя ни у нас, ни в других местах поблизости ее не видать, – но только попробуйте порыбачить там и сами увидите, как эти людишки погонят вас оттуда.{/i}"
    i "{i} Прежде они добирались сюда поездом, а как ветку до станции Ровлей закрыли, стали ездить на этом автобусе.{/i}"
    show insm_7 at center
    i "{i}Да, кстати, у них, в Инсмуте, есть отель – называется «Гилмэн‑хаус», – но я бы не посоветовал там останавливаться. Лучше заночевать здесь, а уж завтра утречком десятичасовым автобусом и поехать;{/i}"
    i "{i} тогда вечерним восьмичасовым сможете двинуть оттуда дальше до Аркхема. Не то было дело пару лет назад: отправился туда инспектор по фабричным делам, ну и остановился в «Гилмэн‑хаусе»,{/i}"
    i "{i} а потом как только не клял эту дыру. Будто бы их понабилось туда великое множество, так что в его комнату со всех сторон доносились голоса – хотя большинство номеров пустовало – и он всю ночь трясся от страха. {/i}"
    i "{i}Какие‑то непонятные разговоры, будто на чужих языках, но больше всего его напугал один голос, который раздавался время от времени. Он звучал так ненатурально – будто мокрый какой‑то,{/i}"
    i "{i}  – так что этот несчастный инспектор побоялся даже раздеться, так и улегся в чем был. Но и не спал совсем, только знай дожидался, когда первый утренний свет забрезжит. А разговоры эти велись у них чуть не всю ночь.{/i}"
    i "{i}Инспектор этот – Кэзи его звали – много чего порассказал: мол, эти инсмутцы следили за ним, вроде как стражу приставили. А заводик Марша нашел он в странном месте – на старой мельнице, у нижних плотин Мануксета. {/i}"
    i "{i}Ну что он рассказывал, то я и раньше слыхал. В бухгалтерии там неразбериха, учет сделок толком не ведется. И концов не найти, откуда эти Марши берут золото для очистки и переплавки. {/i}"
    i "{i}Больших закупок они вроде никогда не делали, но в былые годы вывозили чертову уйму готовых слитков. Доходили слухи о странных, нездешнего вида драгоценностях, их иногда тайком продавали моряки и фабричные,{/i}"
    i "{i}да и на женщинах из семьи Маршей их пару‑тройку раз видели. Люди допускают, что старый капитан Оубед обменял это в каком‑нибудь языческом порту, тем более что он в те времена мешками заказывал стеклянные бусы и безделки,{/i}"
    i "{i} какими мореходы запасались для туземной торговли. А некоторые до сих пор считают, что он нашел возле Чертова рифа пиратский клад. Но вот странная штука.{/i}"
    i "{i}Старый капитан уже лет шестьдесят тому как помер, а после Гражданской войны у них там и приличных морских судов не осталось,{/i}"
    show insm_7_1 at center
    i "{i}но Марши по‑прежнему знай себе закупают этот обменный туземный товар – всякие стеклянные и каучуковые безделки. Может, инсмутская шваль берет их для себя?{/i}"
    i "{i} Сами‑то они не шибко далеко ушли от каннибалов южных морей и дикарей Гвинеи.{/i}"
    i "{i}Бедствие сорок шестого забрало, надо думать, из тех мест лучшую кровь. Как ни крути, а выглядят они жутко, что Марши, что другие тамошние богачи.{/i}"
    i "{i} Я говорил, там в городе осталось теперь не больше четырех сотен людей, и домов полно пустых. На Юге таких называют «белым отребьем», – беззаконные и грешные, вечно со своими темными делишками.{/i}"
    i "{i} Они добывают уйму рыбы и омаров и грузовиками вывозят все это на продажу. Подозрительно все же, как это так выходит, что рыба кишмя кишит только у них, а больше нигде.{/i}"
    show insm_7 at center
    i "{i}Никто за ними уследить не может – ни школьные инспекторы, ни те, что уже черт знает сколько времени проводят перепись населения. Можно пари держать, что любопытным туристам тоже не слишком рады в Инсмуте.{/i}"
    i "{i} Я слыхал, там без следа пропали несколько заезжих бизнесменов и чиновников, а один будто бы сошел с ума и теперь, бедняга, лечится в Денверсе. Да уж, эти могут нагнать страху на кого угодно.{/i}"
    i "{i}Вот потому я и не советую ехать в Инсмут с ночевкой. Сам‑то я никогда там не бывал и не горю желанием побывать, но, думаю, дневная поездка вреда не причинит – хотя здешние люди и будут отговаривать вас от этого.{/i}"
    i"{i} Если же вы любитель всякого древнего старья, так для вас Инсмут – как раз то, что надо.{/i}"




label library:

    scene bg6

    n '{i}После того разговора с кассиром я потратил часть вечера на посещение Ньюберипортской публичной библиотеки, чтобы пополнить сведения об Инсмуте.{/i}'
    n '{i}Когда я пытался расспрашивать местных жителей в магазинах и закусочных, в гараже и пожарном депо, они реагировали еще менее дружелюбно,{/i}'
    n '{i}чем предупреждал меня билетный кассир; и я решил не тратить зря времени на попытки их разговорить.{/i}'

    scene bg7

    "{i}Справочник по истории округа Эссекс, найденный мною на полках библиотеки, сообщал о городе немного: основан он был в 1643 году, в колониальную эпоху там процветало судостроение,{/i}"
    "{i}а в начале девятнадцатого века – мореходство; позднее он был известен как незначительный промышленный центр, использующий энергию реки Мануксет.{/i}"
    "{i}Эпидемия и мятежи 1846 года были упомянуты вскользь, ибо они плохо вписывались в славную историю этого округа.{/i}"
    "{i}Зато немногие записи, свидетельствовавшие об упадке города, не подлежали сомнению. После Гражданской войны вся индустриальная жизнь сосредоточилась в руках «Марш рефайнинг компани»,{/i}"
    "{i}а торговля золотыми слитками составляла единственный местный источник дохода помимо исконного занятия рыболовством, которое становилось все менее прибыльным,{/i}"
    "{i}поскольку крупные корпорации навязывали конкуренцию и цена товара падала, при том что рыбные промыслы близ Инсмута никогда не оскудевали.{/i}"
    "{i}Иностранцы редко там приживались, доказательством чему мог служить осторожный намек на историю с изгнанием попытавшихся было осесть в тех местах поляков и португальцев.{/i}"

    scene bg8

    "{i}Более всего заинтересовали меня упоминания о необычных драгоценностях, которые так или иначе ассоциировались с Инсмутом.{/i}"
    "{i}Это, похоже, были далеко не заурядные изделия, ибо некоторые из них хранились в Мискатоникском университете Аркхема и выставочном зале Исторического общества Ньюберипорта.{/i}"
    "{i}Описания этих вещей, весьма прозаичные и фрагментарные, в то же время содержали намек на нечто таинственное.{/i}"
    "{i}Я был заинтригован и, несмотря на поздний час, решил, если удастся, посмотреть на местную достопримечательность – нечто вроде крупной тиары необычной формы.{/i}"
    "{i}Библиотекарь написал записку, рекомендующую меня хранительнице музея Исторического общества мисс Анне Тилтон, живущей поблизости, и почтенная леди любезно открыла ради меня выставочный зал,{/i}"
    "{i}благо время было еще не такое уж позднее.{/i}"

    scene bg9

    "{i}Коллекция, воистину незаурядная, все же не привлекла моего внимания, ибо им полностью завладел сияющий в электрическом свете причудливый предмет в угловой витрине.{/i}"
    "{i}Я не великий знаток и поклонник красоты, но странное, фантастическое великолепие неведомого шедевра, покоящегося на бархатной пурпурной подушке, заставило меня буквально задохнуться от изумления.{/i}"
    "{i}Вскоре я обнаружил, что неясная тревога, вызываемая во мне этой вещью, имела второй и, возможно, не менее сильный источник в изобразительной и математической многозначности странных орнаментов.{/i}"
    "{i}Все эти узоры намекали на некие тайны и невообразимые бездны времени и пространства, а повторяющиеся морские элементы рельефов казались почти зловещими.{/i}"

    scene bg10

    "{i}Мисс Тилтон так же поведала и о возникновении данной тиары в местном хранилище. Эту вещь в 1873 году за смехотворно низкую цену оставил под залог в лавке на Стейт‑стрит какой‑то пьянчужка из Инсмута,{/i}"
    "{i}вскоре убитый в уличной потасовке. Историческое общество приобрело предмет непосредственно у ростовщика и сразу нашло ей почетное место в музейной витрине.{/i}"
    "{i}Сопроводительная надпись допускала вероятность вест‑индского или индокитайского происхождения экспоната, хотя четкого мнения на сей счет у специалистов не было.{/i}"




label chapter_2:
    scene bg11

    "{i}Незадолго до десяти утра я с небольшим саквояжем стоял на старой торговой площади, прямо перед аптекой Хаммонда, в ожидании инсмутского автобуса.{/i}"
    "{i}Когда подошло время его прибытия, я заметил общее стремление праздношатающихся горожан перейти на другую сторону улицы.{/i}"
    "{i}Видно, билетный кассир не сильно преувеличивал, говоря о нелюбви местных жителей к Инсмуту и его обитателям.{/i}"
    "{i}Через несколько минут в конце Стейт‑стрит появился маленький автобус – дряхлый, непрезентабельный и серый от дорожной пыли – и, сделав круг по площади, с большим шумом притормозил у остановки.{/i}"
    "{i}Я сразу же почувствовал, что это именно он и есть, убедившись в этом чуть погодя, когда заметил на переднем стекле табличку с полустершейся надписью: «Аркхем – Инсмут – Ньюб’порт».{/i}"

    image insm_2 = im.Scale("insm_2.png", 1080 / 1.6, 1920 / 1.6)
    show insm_2 at center
    "{i}Это, должно быть, и есть Джо Сарджент, упомянутый билетным кассиром; и еще до того, как я успел рассмотреть детали, меня вдруг окатила волна неприязни, столь же непреодолимой, сколь и необъяснимой.{/i}"
    "{i}Поведение местных людей, отхлынувших от остановки, вполне естественно: они не желали соприкасаться ни с этим автобусом, ни с человеком, владеющим и управляющим им,{/i}"
    "{i}ни с чем бы то ни было связанным с местами его обитания и его сородичами. Очевидно, долгое пребывание возле рыбных промыслов наделило его характерным запахом.{/i}"
    "{i}А уж какая кровь текла в его жилах, определить я так и не смог. Вряд ли в нем можно было найти черты азиата, полинезийца, левантинца или негроида, однако люди принимали его за чужака.{/i}"

    scene bg6

    n "{i}Я уселся подальше от него, но на той же стороне салона, откуда во время поездки было удобнее обозревать берег.{/i}"
    n "{i}Наконец дряхлый транспорт, покряхтев, тронулся с места, выпустил облако отработанного газа и шумно двинулся мимо старых зданий Стейт‑стрит.{/i}"

    scene bg15

    "{i}День стоял солнечный, теплый, но песчаный ландшафт, украшенный лишь зарослями осоки и низкорослым кустарником, по мере нашего продвижения становился все более унылым.{/i}"
    "{i}Время от времени мы переезжали грубой постройки деревянные мосты над бухточками, образованными приливом или рукавами речного устья и отрезавшими эту местность от окружающего региона.{/i}"

    scene bg12

    "{i}Но вот наконец мы миновали островок Плюм‑Айленд, и слева раскинулся широкий вид на Атлантику.{/i}"
    "{i}Дорога пошла в крутой подъем, и я забеспокоился, глядя на длинный гребень впереди, где наш путь с четко врезанными колеями как будто встречался с небом.{/i}"

    scene bg14

    "{i}Казалось, что автобус, преодолев эту крутизну, навсегда покидает землю, чтобы слиться с неведомой тайной вышнего воздуха и сокровенных небес.{/i}"
    "{i}Запах моря теперь казался зловещим, а молчаливо сутулящийся водитель, с его напряженной спиной и узкой головой, становился мне все более и более ненавистен.{/i}"

    scene bg13

    "{i}Но вот мы достигли гребня, и внизу открылась долина, где река Мануксет впадала в море чуть севернее протяженной линии скал и далее несла свои воды в сторону мыса Энн.{/i}"
    "{i}На горизонте маячила одинокая гора Кингсгюрт‑Хэд, увенчанная старинным домом, о котором так много говорят легенды; но все мое внимание в этот момент поглотила расстилающаяся внизу панорама.{/i}"
    "{i}Я догадался, что это и был всеми проклятый и презираемый Инсмут.{/i}"

    scene bg17

    "{i}При его широкой протяженности и плотной застройке город неприятно поражал отсутствием признаков жизни.{/i}"
    "{i}Над беспорядочно разбросанными трубами почти не виднелось клубов дыма.{/i}"
    "{i}Обширное пространство занимали беспорядочно разбросанные кровли, а фронтоны и коньки крыш даже издали выглядели насквозь прогнившими; когда же мы подъехали ближе к городу,{/i}"
    "{i}я увидел, что многие кровли целиком провалились внутрь зданий.{/i}"

    scene bg16

    "{i}Не избежали этой участи и несколько огромных квадратных домов георгианского стиля с куполами и высокими верандами.{/i}"
    "{i}Эти дома отстояли дальше от воды; один или два из них казались еще довольно крепкими.{/i}"
    "{i}Вглядываясь в просветы меж руинами, я заметил ржавые, заросшие травой рельсы бывшей железной дороги с покосившимися телеграфными столбами,{/i}"
    "{i}лишенными проводов, и едва заметные колеи старых дорог на Ипсвич и Ровлей.{/i}"

    scene bg18

    "{i}В наихудшем состоянии были дома вблизи береговой линии, среди которых по контрасту выделялась прекрасно сохранившаяся башня на здании кубической формы, напоминавшем небольшую фабрику.{/i}"
    "{i}Гавань, давно занесенная песком, была огорожена древним каменным молом; на нем я различил несколько крошечных фигурок рыбаков,{/i}"
    "{i}а на самом конце мола вырисовывалось что‑то вроде фундамента стоявшего там некогда маяка. Внутри этого рукотворного барьера сформировался песчаный язык,{/i}"
    "{i}и на нем я увидел несколько дряхлых хижин, деревянных рыбачьих плоскодонок и разбросанные повсюду верши для омаров.{/i}"
    "{i}Глубоководье вроде бы начиналось за тем местом, где река, огибая башенную конструкцию, разливалась и поворачивала на юг, впадая в океан у конца мола.{/i}"

    scene bg19

    "{i}По дороге мы никого не встретили, но вскоре за окнами автобуса потянулись заброшенные фермы в разных стадиях разрушения.{/i}"
    "{i}Затем я приметил несколько обитаемых домов с разбитыми окнами, заткнутыми тряпьем и всяким хламом, и дворами, усеянными ракушками и рыбьими костями.{/i}"

    scene bg20

    "{i}Автобус пересекал некое подобие площади, на противоположных концах которой стояли две церкви, а в центре возлежали замусоренные останки того, что некогда называлось сквером,{/i}"
    "{i}и я взглянул вправо, на огромное здание с колоннами. Когда‑то белое, оно посерело от грязи и потеряло часть штукатурки,{/i}"
    "{i}а черная с золотом надпись на фронтоне настолько выцвела, что я с трудом разобрал слова: «Тайный орден Дагона».{/i}"

    scene bg6

    n "{i}И вдруг все мысли о времени бесследно исчезли под натиском явившегося мне видения, причем я исполнился необъяснимого ужаса еще до того,{/i}"
    n "{i}как понял, что такое в самом деле вижу.{/i}"

    scene bg21

    "{i}Дверь, открытая в церковный полуподвал, вырисовывалась прямоугольником мрака.{/i}"
    "{i}И там я увидел субъекта, который пересек – или казалось, что пересек, – этот темный прямоугольник.{/i}"
    "{i}Видение казалось тем более жутким и сводящим с ума, что здравый рассудок отрицал наличие в нем чего‑либо кошмарного.{/i}"

    scene bg6

    n "{i}Так вот что подействовало на мое воображение и придало зловещий вид в остальном лишь смутно различимой, прошаркавшей внизу фигуре!{/i}"
    n "{i}Нет никаких оснований, тотчас подумал я, испытывать ужас от этого мрачного псевдовоспоминания.{/i}"
    n "{i}Разве не естественно, что таинственный местный культ утвердил в качестве своего атрибута уникальный тип головного убора,{/i}"
    n "{i}пусть исполненный в несколько странном стиле, но зато хорошо знакомый общине – хотя бы как часть драгоценного клада?{/i}"

    scene bg23

    "{i}Проехав мост, мы оказались на огромной полукруглой площади и свернули направо, прямо к высокому зданию с куполом,{/i}"
    "{i}остатками желтой краски на стенах и полустершейся вывеской, из которой следовало, что это и есть «Гилмэн‑хаус».{/i}"
    "{i}Радуясь концу поездки, я покинул автобус и зашел в отель, чтобы оставить там свой багаж.{/i}"

    scene bg22

    "{i}Холл, убранство которого не было столь ужасным, как изначально представлялось, тоже оказался совершенно пустым, без каких либо признаков жизни.{/i}"
    "{i}Вместо того, чтобы искать и ррасспрашивать постояльцев отеля я вышел на площадь, откуда автобус уже уехал, и внимательно осмотрелся.{/i}"

    scene bg24

    "{i}Здания в этой части города находились в приличном состоянии и включали не менее дюжины торговых заведений.{/i}"
    "{i}Я приметил бакалею Первой национальной торговой сети, мрачноватый ресторан, аптеку и офис оптовой рыботорговли,{/i}"
    "{i}а также контору единственного промышленного предприятия города, «Марш рефайнинг компани», на восточной стороне площади, ближе к реке.{/i}"
    "{i}Было ясно, что я нахожусь в городском административном центре. На востоке глаз мой уловил голубые проблески гавани,{/i}"
    "{i}напротив которой поднимались жалкие развалины трех некогда прекрасных колоколен георгианского стиля.{/i}"
    "{i}А на другом берегу реки белела башня, венчающая то, что являлось, по всей вероятности, фабрикой Марша.{/i}"


    return
