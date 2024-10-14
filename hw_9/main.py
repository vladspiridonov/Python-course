import os
import pickle
from src.utils import prepare_data, train_model, read_model

import pandas as pd
import streamlit as st
import locale
locale.setlocale( locale.LC_ALL, 'ru-Ru' )

model_path = 'gb_fitted.pkl'
if not os.path.exists(model_path):
    train_data = prepare_data()
    train_data.to_csv('data.csv')
    train_model(train_data)

with open('l.pkl', 'rb') as file:
        l = pickle.load(file)

st.set_page_config(
    page_title="Skolko App",
)
area_select = st.sidebar.selectbox(
    "Район",
    l, 166,

)
square = st.sidebar.number_input(
    "Площадь м",
    1, 2000, 33,
)
rooms = st.sidebar.number_input(
    "комнаты",
    1, 10, 1,
)
floor = st.sidebar.number_input(
    "этаж",
    1, 66, 7,
)
inputDF = pd.DataFrame(
    {
        'total_square': square,
        'rooms': rooms,
        'floor': floor,
        'x0_Академический район': area_select == 1, 'x0_Алексеевский район': area_select == 2,
        'x0_Алтуфьевский район': area_select == 3, 'x0_Арбат район': area_select == 4,
        'x0_Аэропорт район': area_select == 5, 'x0_Бабушкинский район': area_select == 6,
        'x0_Балашиха': area_select == 7, 'x0_Басманный район': area_select == 8, 'x0_Беговой район': area_select == 9,
        'x0_Бескудниковский район': area_select == 10, 'x0_Бибирево район': area_select == 11,
        'x0_Бирюлёво Восточное район': area_select == 12, 'x0_Бирюлёво Западное район': area_select == 13,
        'x0_Богородское район': area_select == 14, 'x0_Братеево район': area_select == 15,
        'x0_Бутырский район': area_select == 16, 'x0_Вешняки район': area_select == 17, 'x0_Видное': area_select == 18,
        'x0_Внуково район': area_select == 19, 'x0_Внуковское поселение': area_select == 20,
        'x0_Войковский район': area_select == 21, 'x0_Воскресенское поселение': area_select == 22,
        'x0_Восточное Дегунино район': area_select == 23, 'x0_Восточное Измайлово район': area_select == 24,
        'x0_Восточный район': area_select == 25, 'x0_Выхино-Жулебино район': area_select == 26,
        'x0_Гагаринский район': area_select == 27, 'x0_Головинский район': area_select == 28,
        'x0_Гольяново район': area_select == 29, 'x0_Даниловский район': area_select == 30,
        'x0_Десёновское поселение': area_select == 31, 'x0_Дзержинский': area_select == 32,
        'x0_Дмитровский район': area_select == 33, 'x0_Долгопрудный': area_select == 34,
        'x0_Донской район': area_select == 35, 'x0_Дорогомилово район': area_select == 36,
        'x0_Замоскворечье район': area_select == 37, 'x0_Западное Дегунино район': area_select == 38,
        'x0_Зюзино район': area_select == 39, 'x0_Зябликово район': area_select == 40,
        'x0_Ивановское район': area_select == 41, 'x0_Ивантеевка': area_select == 42,
        'x0_Измайлово район': area_select == 43, 'x0_Капотня район': area_select == 44,
        'x0_Коньково район': area_select == 45, 'x0_Коптево район': area_select == 46, 'x0_Королёв': area_select == 47,
        'x0_Косино-Ухтомский район': area_select == 48, 'x0_Котельники': area_select == 49,
        'x0_Котловка район': area_select == 50, 'x0_Красногорск': area_select == 51,
        'x0_Красносельский район': area_select == 52, 'x0_Крылатское район': area_select == 53,
        'x0_Кузьминки район': area_select == 54, 'x0_Кунцево район': area_select == 55,
        'x0_Куркино район': area_select == 56, 'x0_Левобережный район': area_select == 57,
        'x0_Лефортово район': area_select == 58, 'x0_Лианозово район': area_select == 59, 'x0_Лобня': area_select == 60,
        'x0_Ломоносовский район': area_select == 61, 'x0_Лосиноостровский район': area_select == 62,
        'x0_Лыткарино': area_select == 63, 'x0_Люберцы': area_select == 64, 'x0_Люблино район': area_select == 65,
        'x0_Марушкинское поселение': area_select == 66, 'x0_Марфино район': area_select == 67,
        'x0_Марьина Роща район': area_select == 68, 'x0_Марьино район': area_select == 69,
        'x0_Метрогородок район': area_select == 70, 'x0_Мещанский район': area_select == 71,
        'x0_Митино район': area_select == 72, 'x0_Можайский район': area_select == 73,
        'x0_Молжаниновский район': area_select == 74, 'x0_Москворечье-Сабурово район': area_select == 75,
        'x0_Московский': area_select == 76, 'x0_Московский поселение': area_select == 77,
        'x0_Мосрентген поселение': area_select == 78, 'x0_Мытищи': area_select == 79,
        'x0_Нагатино-Садовники район': area_select == 80, 'x0_Нагатинский Затон район': area_select == 81,
        'x0_Нагорный район': area_select == 82, 'x0_Некрасовка район': area_select == 83,
        'x0_Нижегородский район': area_select == 84, 'x0_Ново-Переделкино район': area_select == 85,
        'x0_Новогиреево район': area_select == 86, 'x0_Новокосино район': area_select == 87,
        'x0_Обручевский район': area_select == 88, 'x0_Одинцово': area_select == 89,
        'x0_Орехово-Борисово Северное район': area_select == 90, 'x0_Орехово-Борисово Южное район': area_select == 91,
        'x0_Останкинский район': area_select == 92, 'x0_Отрадное район': area_select == 93,
        'x0_Очаково-Матвеевское район': area_select == 94, 'x0_Перово район': area_select == 95,
        'x0_Печатники район': area_select == 96, 'x0_Подольск': area_select == 97,
        'x0_Покровское-Стрешнево район': area_select == 98, 'x0_Преображенское район': area_select == 99,
        'x0_Пресненский район': area_select == 100, 'x0_Проспект Вернадского район': area_select == 101,
        'x0_Пушкино': area_select == 102, 'x0_Раменки район': area_select == 103, 'x0_Реутов': area_select == 104,
        'x0_Ростокино район': area_select == 105, 'x0_Рязановское поселение': area_select == 106,
        'x0_Рязанский район': area_select == 107, 'x0_Савёловский район': area_select == 108,
        'x0_Свиблово район': area_select == 109, 'x0_Северное Бутово район': area_select == 110,
        'x0_Северное Измайлово район': area_select == 111, 'x0_Северное Медведково район': area_select == 112,
        'x0_Северное Тушино район': area_select == 113, 'x0_Северный район': area_select == 114,
        'x0_Сокол район': area_select == 115, 'x0_Соколиная Гора район': area_select == 116,
        'x0_Сокольники район': area_select == 117, 'x0_Солнцево район': area_select == 118,
        'x0_Сосенское поселение': area_select == 119, 'x0_Строгино район': area_select == 120,
        'x0_Таганский район': area_select == 121, 'x0_Тверской район': area_select == 122,
        'x0_Текстильщики район': area_select == 123, 'x0_Тимирязевский район': area_select == 124,
        'x0_Тропарёво-Никулино район': area_select == 125, 'x0_Тёплый Стан район': area_select == 126,
        'x0_Фили-Давыдково район': area_select == 127, 'x0_Филимонковское поселение': area_select == 128,
        'x0_Филёвский парк район': area_select == 129, 'x0_Хамовники район': area_select == 130,
        'x0_Химки': area_select == 131, 'x0_Ховрино район': area_select == 132,
        'x0_Хорошёво-Мнёвники район': area_select == 133, 'x0_Хорошёвский район': area_select == 134,
        'x0_Царицыно район': area_select == 135, 'x0_Чертаново Северное район': area_select == 136,
        'x0_Чертаново Центральное район': area_select == 137, 'x0_Чертаново Южное район': area_select == 138,
        'x0_Черёмушки район': area_select == 139, 'x0_Щербинка': area_select == 140,
        'x0_Щукино район': area_select == 141, 'x0_Щёлково': area_select == 142,
        'x0_Южное Бутово район': area_select == 143, 'x0_Южное Медведково район': area_select == 144,
        'x0_Южное Тушино район': area_select == 145, 'x0_Южнопортовый район': area_select == 146,
        'x0_Якиманка район': area_select == 147, 'x0_Ярославский район': area_select == 148,
        'x0_Ясенево район': area_select == 149, 'x0_д.\xa0Аристово': area_select == 150,
        'x0_д.\xa0Болтино': area_select == 151, 'x0_д.\xa0Большие Жеребцы': area_select == 152,
        'x0_д.\xa0Глухово': area_select == 153, 'x0_д.\xa0Жабкино': area_select == 154,
        'x0_д.\xa0Марусино': area_select == 155, 'x0_д.\xa0Мисайлово': area_select == 156,
        'x0_д.\xa0Мотяково': area_select == 157, 'x0_д.\xa0Мякинино': area_select == 158,
        'x0_д.\xa0Островцы': area_select == 159, 'x0_д.\xa0Пирогово': area_select == 160,
        'x0_д.\xa0Подолино': area_select == 161, 'x0_д.\xa0Путилково': area_select == 162,
        'x0_д.\xa0Раздоры': area_select == 163, 'x0_д.\xa0Сабурово': area_select == 164,
        'x0_д.\xa0Сапроново': area_select == 165, 'x0_д.\xa0Солманово': area_select == 166,
        'x0_д.\xa0Сосенки': area_select == 167, 'x0_дп.\xa0Красково': area_select == 168,
        'x0_дп.\xa0Лесной Городок': area_select == 169, 'x0_пос.\xa0Битца': area_select == 170,
        'x0_пос.\xa0ВНИИССОК': area_select == 171, 'x0_пос.\xa0Ильинское-Усово': area_select == 172,
        'x0_пос.\xa0Коммунарка': area_select == 173, 'x0_пос.\xa0Марьино': area_select == 174,
        'x0_пос.\xa0Мебельной фабрики': area_select == 175, 'x0_пос.\xa0Мирный': area_select == 176,
        'x0_пос.\xa0Нагорное': area_select == 177, 'x0_пос.\xa0Отрадное': area_select == 178,
        'x0_пос.\xa0Развилка': area_select == 179,
        'x0_пос.\xa0подсобного хозяйства "Воскресенское"': area_select == 180, 'x0_рп.\xa0Боброво': area_select == 181,
        'x0_рп.\xa0Бутово': area_select == 182, 'x0_рп.\xa0Дрожжино': area_select == 183,
        'x0_рп.\xa0Заречье': area_select == 184, 'x0_рп.\xa0Лопатино': area_select == 185,
        'x0_рп.\xa0Малаховка': area_select == 186, 'x0_рп.\xa0Нахабино': area_select == 187,
        'x0_рп.\xa0Новоивановское': area_select == 188, 'x0_рп.\xa0Октябрьский': area_select == 189,
        'x0_рп.\xa0Томилино': area_select == 190, 'x0_с.\xa0Домодедово': area_select == 191,
        'x0_с.\xa0Молоково': area_select == 192, 'x0_с.\xa0Немчиновка': area_select == 193,
        'x0_с.\xa0Николо-Урюпино': area_select == 194, 'x0_с.\xa0Ромашково': area_select == 195

    },
    index=[0],
)



model = read_model('gb_fitted.pkl')

preds = model.predict(inputDF)

st.write(f'Цена:', locale.currency(preds[0]))
if area_select.find(".") == -1:
    st.image("imgs/img_1.png", use_column_width=True)
else: st.image("imgs/img.png", use_column_width=True)

