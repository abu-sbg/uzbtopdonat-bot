import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# =========================
# ВСТАВЬ СЮДА СВОЙ ТОКЕН
# =========================
TOKEN = "8476106603:AAEOZAtZE1N3W7Upt5aUzwgbfouwAc8XkgM"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# =========================
# НАСТРОЙКА
# =========================
ADMIN_USERNAME = "@GGDONAT1"

# =========================
# ТОВАРЫ
# =========================
PRODUCTS = {
    "⭐ Telegram Stars": {
        "100 ⭐": "30 000 сум",
        "150 ⭐": "45 000 сум",
        "250 ⭐": "70 000 сум",
        "350 ⭐": "95 000 сум",
        "500 ⭐": "140 000 сум",
        "750 ⭐": "199 000 сум",
        "1000 ⭐": "285 000 сум",
    },
    "💎 FC Points": {
        "40 + 40": "13 000 сум",
        "100 + 100": "25 000 сум",
        "500 + 500": "96 000 сум",
        "1000 + 1000": "195 000 сум",
        "2000 + 2000": "380 000 сум",
    },
    "🌟 Звёздный абонемент": {
        "Абонемент": "195 000 сум",
        "+20 уровней": "370 000 сум",
    },
    "🔥 Brawl Pass": {
        "Brawl Pass": "70 000 сум",
        "Brawl Pass Plus": "110 000 сум",
    },
    "💎 Гемы": {
        "30 гемов": "16 000 сум",
        "80 гемов": "40 000 сум",
        "170 гемов": "74 000 сум",
        "360 гемов": "145 000 сум",
        "950 гемов": "355 000 сум",
        "2000 гемов": "685 000 сум",
    },
    "⭐ Telegram Premium": {
        "На 1 месяц": "60 000 сум",
        "На 1 год (40 000 сум каждый месяц)": "480 000 сум",
    }
}

# =========================
# ОПИСАНИЯ
# =========================
CATEGORY_INFO = {
    "⭐ Telegram Stars": """⭐ <b>TELEGRAM STARS — ВЫГОДНО И БЫСТРО</b> ⭐

🚀 Пополняй звёзды без лишних переплат
🔒 Надёжно | Проверено

💰 <b>Цены:</b>
• 100 ⭐ — 30 000 сум
• 150 ⭐ — 45 000 сум
• 250 ⭐ — 70 000 сум
• 350 ⭐ — 95 000 сум
• 500 ⭐ — 140 000 сум
• 750 ⭐ — 199 000 сум
• 1000 ⭐ — 285 000 сум

🔥 Успей купить по текущим ценам

📩 Заказ: {admin}""",

    "💎 FC Points": """💎 <b>FC POINTS — ЗАЛЕТАЙ ПО ВЫГОДЕ</b> 💎

🚀 Хочешь топ состав и быстрый апгрейд?
Не трать время — бери FC Points с бонусом x2!

🔥 Только сейчас:
✔️ Двойной бонус к каждому паку
✔️ Моментальная выдача
✔️ Проверенный продавец

💰 <b>Цены:</b>
• 40 + 40 — 13 000 сум
• 100 + 100 — 25 000 сум
• 500 + 500 — 96 000 сум
• 1000 + 1000 — 195 000 сум
• 2000 + 2000 — 380 000 сум

⚡ Успей купить по этим ценам — потом будет дороже

📩 Пиши прямо сейчас: {admin}""",

    "🌟 Звёздный абонемент": """🌟 <b>ЗВЁЗДНЫЙ АБОНЕМЕНТ</b> 🌟

🔥 Легендарный 120 KLOSE уже доступен!
Прокачай состав и забери топ игрока прямо сейчас ⚽💥

💰 <b>Цены:</b>
⭐ Абонемент — 195 000 сум
🚀 +20 уровней — 370 000 сум

✨ <b>Что получаешь:</b>
✔️ Топовый игрок 120 OVR
✔️ Кучу наград и ресурсов
✔️ Быстрый прогресс
✔️ Максимум буста для аккаунта

📩 Заказ: {admin}
⚡ Быстро | Надежно | Безопасно

Не упусти шанс забрать имбу в свой состав 🔥""",

    "🔥 Brawl Pass": """🔥 <b>BRAWL PASS АКЦИЯ</b> 🔥

Прокачай свой аккаунт в Brawl Stars на максимум 🚀

💰 <b>Цены:</b>
🎟️ Brawl Pass — 70 000 сум
🎟️ Brawl Pass Plus — 110 000 сум 💎

✨ <b>Что получаешь:</b>
✔️ Эксклюзивные награды
✔️ Быстрый прогресс
✔️ Больше ресурсов и ключей
✔️ Дополнительные бонусы в Plus

📩 Заказ: {admin}
⚡ Быстро | Надежно | Безопасно

Не упусти шанс забрать топ-награды 🔥""",

    "💎 Гемы": """💎 <b>ГЕМЫ В НАЛИЧИИ</b> 💎

🚀 Быстрое пополнение | Надежно | Без лишних заморочек

💰 <b>Цены:</b>
🔹 30 гемов — 16 000 сум
🔹 80 гемов — 40 000 сум
🔹 170 гемов — 74 000 сум
🔹 360 гемов — 145 000 сум
🔹 950 гемов — 355 000 сум 🔥
🔹 2000 гемов — 685 000 сум 💎

✨ <b>Почему мы?</b>
✔️ Моментальная выдача
✔️ Выгодные цены
✔️ Проверенный сервис

📩 Заказ: {admin}
⚡ Успей прокачать свой аккаунт уже сейчас!""",

    "⭐ Telegram Premium": """⭐ <b>Telegram Premium</b> ⭐

🚀 Открой больше возможностей в Telegram!
Эксклюзивные функции, высокая скорость и максимум комфорта 💎

💰 <b>Тарифы:</b>
📅 На 1 месяц — 60 000 сум
📆 На 1 год — 480 000 сум
(40 000 сум каждый месяц)

✨ <b>Что получаешь:</b>
✔️ Быстрая загрузка файлов
✔️ Увеличенные лимиты
✔️ Уникальные стикеры и реакции
✔️ Отключение рекламы
✔️ И многое другое!

📩 Заказать: {admin}
⚡ Быстро | Надежно | Доступно

Не упусти шанс прокачать свой Telegram 💜"""
}

# =========================
# КЛАВИАТУРЫ
# =========================
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(
    KeyboardButton("⭐ Telegram Stars"),
    KeyboardButton("💎 FC Points")
)
main_kb.add(
    KeyboardButton("🌟 Звёздный абонемент"),
    KeyboardButton("🔥 Brawl Pass")
)
main_kb.add(
    KeyboardButton("💎 Гемы"),
    KeyboardButton("⭐ Telegram Premium")
)
main_kb.add(KeyboardButton("📞 Связь с продавцом"))


def get_product_keyboard(category):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in PRODUCTS[category]:
        kb.add(KeyboardButton(item))
    kb.add(KeyboardButton("⬅️ Назад"))
    return kb


# =========================
# КОМАНДА START
# =========================
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    text = (
        "🔥 <b>Добро пожаловать в UzbTopDonat!</b>\n\n"
        "Здесь ты можешь быстро и удобно заказать:\n"
        "⭐ Telegram Stars\n"
        "💎 FC Points\n"
        "🌟 Звёздный абонемент\n"
        "🔥 Brawl Pass\n"
        "💎 Гемы\n"
        "⭐ Telegram Premium\n\n"
        "👇 Выбери нужный товар ниже:"
    )
    await message.answer(text, reply_markup=main_kb)


# =========================
# СВЯЗЬ
# =========================
@dp.message_handler(lambda message: message.text == "📞 Связь с продавцом")
async def seller_contact(message: types.Message):
    await message.answer(f"📩 Для заказа пиши сюда: {ADMIN_USERNAME}")


# =========================
# НАЗАД
# =========================
@dp.message_handler(lambda message: message.text == "⬅️ Назад")
async def back_to_menu(message: types.Message):
    await message.answer("🏠 Ты вернулся в главное меню", reply_markup=main_kb)


# =========================
# КАТЕГОРИИ
# =========================
@dp.message_handler(lambda message: message.text in CATEGORY_INFO.keys())
async def category_handler(message: types.Message):
    category = message.text
    text = CATEGORY_INFO[category].format(admin=ADMIN_USERNAME)
    await message.answer(text, reply_markup=get_product_keyboard(category))


# =========================
# ТОВАРЫ
# =========================
@dp.message_handler(lambda message: any(message.text in items for items in PRODUCTS.values()))
async def product_handler(message: types.Message):
    selected = message.text

    for category, items in PRODUCTS.items():
        if selected in items:
            price = items[selected]
            text = (
                f"🛒 <b>Вы выбрали:</b> {selected}\n"
                f"💰 <b>Цена:</b> {price}\n\n"
                f"📩 Для оформления заказа пиши: {ADMIN_USERNAME}"
            )
            await message.answer(text)
            return


# =========================
# ВСЁ ОСТАЛЬНОЕ
# =========================
@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("❗ Выбери товар через кнопки ниже.", reply_markup=main_kb)


# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
