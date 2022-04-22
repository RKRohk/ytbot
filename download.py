from __future__ import unicode_literals
from email import message
from fileinput import filename
from venv import create
from pyrogram.client import Client
from pyrogram.types import Message

import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def progress(current, total, client: Client, message: Message):
    try:
        message.edit_text(f"Uploaded {current * 100 / total:.1f}%")
    except Exception as e:
        message.edit_text("Exception occured while uploading....trying again")
        print(f"Error updating upload status: {e}")


def createOpts(client: Client, message: Message):
    print("returning hook")


def downloadVideo(url: str, client: Client, message: Message) -> str:
    def my_hook(d):
        if d['status'] == 'downloading':
            percentage = d["_percent_str"]
            eta = d["_eta_str"]
            try:
                message.edit_text(
                    f'Downloaded: {percentage}\nTime remaining: {eta}')
            except Exception as e:
                print(f"Exception : {e}")

        elif d['status'] == 'finished':
            message.edit_text("Uploading file....")
            client.send_chat_action(message.chat.id, action="upload_video")
            filename = d['filename']
            client.send_video(message.chat.id, filename,
                              progress=progress, progress_args=(client, message))
            message.delete()

    ydl_opts = {
        'hls_prefer_native': True,
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
