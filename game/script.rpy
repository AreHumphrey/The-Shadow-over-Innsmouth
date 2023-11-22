﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")


# Игра начинается здесь:
label start:

    scene bg1

    "Зимой 1927/28 года агенты федерального правительства произвели секретное расследование в старинном портовом городке Инсмут, штат Массачусетс."

    "Общественность впервые узнала об этом в феврале, когда прокатилась большая волна облав и арестов,"

    "после которой сожгли и взорвали – с известными,
     конечно, предосторожностями – огромное количество ветхих, изъеденных червями и, как все полагали, давно покинутых зданий близ опустевшего порта."

    "Нелюбопытные души сочли все это одним из главных сражений в судорожной войне с бутлегерством."

    scene bg2
    "Но люди, жадные до сенсаций, не переставали дивиться невероятному обилию арестов,"
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

    define i = Character("Кассир", color="#c8c8ff")

    scene bg5
    image insm_7 = im.Scale("insm_7.png", 1080 / 1.6, 1920 / 1.6)
    show insm_7 at center
    i "Привет, я персонаж!"

    return
