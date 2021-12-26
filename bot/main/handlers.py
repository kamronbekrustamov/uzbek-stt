import os

from telegram.ext import CallbackContext
from telegram import Update
import main.service as svc
import pathlib

from config import URL, BASE_PATH

DIR = os.path.join(BASE_PATH, "transcripts")


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome!")


def stop_command(update: Update, context: CallbackContext):
    update.message.reply_text("Good bye!")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Help!")


def error(update: Update, context: CallbackContext):
    update.message.reply_text(f"Error: {context.error}")


def request_handler(update: Update, context: CallbackContext):
    if not (update.message.audio or update.message.voice):
        raise Exception("Iltimos ovozli habar yuboring")
    update.message.reply_text("Iltimos kutib turing...")
    try:
        if update.message.audio:
            transcript = svc.get_text_from(URL, update.message.audio)
            update.message.reply_text(f'Natija:\n"{transcript}"')
        else:
            transcript = svc.get_text_from(URL, update.message.voice)
            update.message.reply_text(f'Natija:\n"{transcript}"')
    except BaseException:
        raise Exception("Tizimda hatolik yuz berdi. Birozdan so'ng harakat qilib ko'ring")

