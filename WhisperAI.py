import logging
from unittest import result
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
import whisper
import os
file_path  = 'voice_note.mp3'
updater = Updater("", use_context=True)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def WhisperAI():
    model = whisper.load_model("base")
    result1 = model.transcribe("voice_note.mp3")
    print(result1["text"])
    return result1["text"]

def get_voice(update: Update, context: CallbackContext) -> None:
    new_file = context.bot.get_file(update.message.voice.file_id)
    new_file.download("voice_note.mp3")
    result1  =  WhisperAI()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"result: {result1}"
    )
    os.unlink(file_path)
    
updater.dispatcher.add_handler(MessageHandler(Filters.voice , get_voice))   
updater.start_polling()
updater.idle()