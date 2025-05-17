# sbot
**IN UZBEK**
aiogram==3.4.1 Telegram botni yaratish uchun asinxron kutubxona (Python Telegram Bot Framework)
transformers HuggingFace moduli — AI modeldan (masalan, distilbert) savollarga javob olish uchun
torch AI modelni ishga tushirish uchun zarur bo‘lgan PyTorch kutubxonasi
langdetect Matn tilini aniqlash (UZ, RU, EN va h.k.) uchun
sqlite3 (standart) Savollar/javoblar va foydalanuvchilarni SQL bazada saqlash uchun

Modul Maqsad
Pytesseract Rasm ichidagi matnni o‘qish (OCR)
Pdfplumber PDF fayl ichidagi matnni chiqarish
Matndagi tilni aniqlash va shunga mos AI javobi qaytarish
Savollar va javoblarni SQLite bazasiga saqlash
Eng yaxshi qilgan tarafi
foydalanuvchilar bergan savolni tekshiradi va ularni saqlaydi 

Cheklovlar
Faqat PDF va TXT formatdagi hujjatlar qabul qilinadi
Faylda yoki rasmda matn topilmasa, javob qaytarilmaydi
Javob uzunligi 100 so‘z atrofida



**IN ENGLISH**
aiogram==3.4.1 Telegram bot framework for creating asynchronous bots (Python Telegram Bot Framework)
transformers HuggingFace module — used to get answers from AI models (e.g., distilbert)
torch Required PyTorch library to run the AI model
langdetect To detect the language of the text (UZ, RU, EN, etc.)
sqlite3 (standard) To store questions/answers and users in an SQL database

Module	Purpose
Pytesseract	Read text from images (OCR)
Pdfplumber	Extract text from PDF files
Detect the language of the text and return AI response accordingly	
Save questions and answers to SQLite database	
Best feature
Checks the questions submitted by users and saves them

Limitations
Only PDF and TXT document formats are accepted
If no text is found in the file or image, no response is returned
Response length is around 100 words
