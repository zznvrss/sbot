import os
import logging
import sqlite3
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from transformers import pipeline
from PIL import Image
import pytesseract
from langdetect import detect
import PyPDF2
from aiogram import F


API_TOKEN = '7586450131:AAF5qHGEUSZcQo540x0lbTlZz8wju0mMsO8'



logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


conn = sqlite3.connect("questions.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question TEXT,
    answer TEXT,
    language TEXT,
    file_path TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def save_question(user_id, question, answer, language, file_path=None):
    cursor.execute('''
        INSERT INTO questions (user_id, question, answer, language, file_path)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, question, answer, language, file_path))
    conn.commit()


qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question: str, language: str) -> str:
    prompt = f"Answer in {language}: {question}"
    result = qa_pipeline(prompt, max_length=100)[0]['generated_text']
    return result


def detect_language(text: str) -> str:
    try:
        lang_code = detect(text)
        return {"uz": "Uzbek", "ru": "Russian", "en": "English"}.get(lang_code, "English")
    except:
        return "English"

def extract_text_from_image(image_path: str) -> str:
    return pytesseract.image_to_string(Image.open(image_path))

def extract_text_from_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return ''.join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


async def start_cmd(message: Message):
    await message.answer("✅ Savolingizni yuboring (matn, rasm yoki fayl ko‘rinishida).")

async def handle_file(message: types.Message):
    document = message.document
    file_ext = document.file_name.split('.')[-1].lower()
    file_path = f"files/{document.file_unique_id}.{file_ext}"
    os.makedirs("files", exist_ok=True)
    await document.download(destination_file=file_path)

    if file_ext == "pdf":
        text = extract_text_from_pdf(file_path)
    elif file_ext == "txt":
        text = extract_text_from_txt(file_path)
    else:
        return await message.answer("❗ Faqat PDF yoki TXT fayllar qabul qilinadi.")

    if not text.strip():
        return await message.answer("❗ Faylda matn topilmadi.")

    lang = detect_language(text)
    answer = generate_answer(text, lang)
    if not answer.strip():
        return await message.answer("❗ Javob topilmadi.")
    save_question(message.from_user.id, text, answer, lang, file_path)
    await message.answer(answer)

async def handle_text(message: types.Message):
    text = message.text
    if not text.strip():
        return await message.answer("❗ Matn yuboring.")
    lang = detect_language(text)
    answer = generate_answer(text, lang)
    if not answer.strip():
        return await message.answer("❗ Javob topilmadi.")
    save_question(message.from_user.id, text, answer, lang)
    await message.answer(answer)


dp.message.register(start_cmd, CommandStart())
dp.message.register(handle_file, F.document)
dp.message.register(handle_text, F.text)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.delete_webhook())
    loop.run_until_complete(dp.start_polling(bot))
    conn.close()