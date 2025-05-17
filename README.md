# 🤖 AI Savol-Javob Telegram Bot

Bu Telegram bot foydalanuvchidan yuborilgan savollarga (matn, PDF yoki TXT fayl ko‘rinishida) sun'iy intellekt yordamida avtomatik javob beradi. Javoblar yuborilgan matn tilini aniqlash orqali (O‘zbek, Rus, Ingliz) mos tarzda yaratiladi. Bot barcha savollarni SQLite bazasida saqlaydi.

---

## 📌 Asosiy imkoniyatlar

- Matnli savollarga AI orqali javob berish
- PDF va TXT fayllardan matn ajratib, savolga AI javobi yaratish
- Tilni avtomatik aniqlash va shunga mos tilda javob berish
- Savollar/javoblarni SQLite bazasida saqlash
- Logging va asosiy xatoliklar uchun foydalanuvchiga xabar berish

---

## 📦 Ishlatilgan kutubxonalar

| Modul        | Maqsad                                                                 |
|--------------|------------------------------------------------------------------------|
| `aiogram==3.4.1`   | Telegram bot yaratish uchun asinxron kutubxona (Python Telegram Bot Framework) |
| `transformers`     | HuggingFace moduli — AI modeldan (masalan, Flan-T5) savollarga javob olish |
| `torch`            | AI modelni ishga tushirish uchun zarur bo‘lgan PyTorch kutubxonasi |
| `langdetect`       | Matn tilini aniqlash (UZ, RU, EN va h.k.) uchun |
| `sqlite3`          | Standart Python kutubxonasi — savollar/javoblarni SQL bazaga yozish |
| `pytesseract`      | Rasm ichidagi matnni o‘qish (OCR) |
| `pillow`           | OCR uchun rasmni ochish va qayta ishlash (PIL) |
| `PyPDF2`           | PDF fayldan matn ajratish uchun |

> ⚠️ `pytesseract` ishlashi uchun Tesseract OCR tizimda o‘rnatilgan bo‘lishi **majburiy**.

---

## ⚙️ O‘rnatish

```bash
git clone https://github.com/username/telegram-ai-bot.git
cd telegram-ai-bot

# Virtual muhit (tavsiya etiladi)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Kutubxonalarni o‘rnating
pip install -r requirements.txt
