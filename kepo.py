from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token bot Anda
BOT_TOKEN = "7542249132:AAHOM9hlpl4wImdC7Oq5mMKXfj7A7vCX6w8"

# Fungsi untuk menangani perintah /send
def send_message(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Format salah! Gunakan: /send <Chat ID> <Pesan>")
        return

    chat_id = context.args[0]
    text_message = " ".join(context.args[1:])

    try:
        context.bot.send_message(chat_id=chat_id, text=text_message)
        update.message.reply_text(f"Pesan berhasil dikirim ke {chat_id}")
    except Exception as e:
        update.message.reply_text(f"Terjadi kesalahan: {e}")

# Fungsi utama untuk menjalankan bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("send", send_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
