# class STTBot(Bot):
#     def __init__(self, token: str, base_url: str):
#         super(STTBot, self).__init__(token, base_url)
#
#
#
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters

import config
from main import handlers as handlers


def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher: Dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", handlers.start_command))
    dispatcher.add_handler(CommandHandler("stop", handlers.stop_command))
    dispatcher.add_handler(CommandHandler("help", handlers.help_command))
    dispatcher.add_handler(MessageHandler(Filters.all, handlers.request_handler))
    dispatcher.add_error_handler(handlers.error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
