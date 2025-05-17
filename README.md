# sbot


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
**Best feature
Checks the questions submitted by users and saves them
**
Limitations
Only PDF and TXT document formats are accepted
If no text is found in the file or image, no response is returned
Response length is around 100 words
