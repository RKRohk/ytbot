import asyncio
from pyrogram import Client
from pyrogram.types import BotCommand, Message
import pyrogram.filters as filters

from download import downloadVideo


def CreateApp() -> Client:
    return Client(
        "veryrustybot",
        bot_token="1772958748:AAEkt533w__yNuQj_FyQvm4KTo7tb7116sE"
    )


def main():
    app = CreateApp()

    @app.on_message(filters.command("download"))
    def download(client: Client, message: Message):
        sent_message = message.reply("Downloading")
        url = message.text.replace("/download", "", 1).strip()
        # validate url
        try:
            downloadVideo(url=url, client=client, message=sent_message)
        except:
            print("Something went wrong")
            message.reply("something went wrong! Please try again later")

    app.run()


main()
