from telegram.ext import Updater
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    logger.info("Bot started!")
    
    updater.start_polling()
    updater.idle()  # 🛑 এই লাইন যোগ করুন (এটি বটকে চালু রাখবে)

if __name__ == "__main__":
    main()
