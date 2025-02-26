import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Token bot Anda
BOT_TOKEN = "7542249132:AAHOM9hlpl4wImdC7Oq5mMKXfj7A7vCX6w8"

# Fungsi untuk menangani perintah /send
async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Format salah! Gunakan: /send <Chat ID> <Pesan>")
        return

    chat_id = context.args[0]
    text_message = " ".join(context.args[1:])

    try:
        await context.bot.send_message(chat_id=chat_id, text=text_message)
        await update.message.reply_text(f"Pesan berhasil dikirim ke {chat_id}")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {e}")

# Fungsi utama untuk menjalankan bot
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Menambahkan handler untuk perintah /send
    app.add_handler(CommandHandler("send", send_message))

    print("Bot sedang berjalan...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
