import datetime
import io
import os

from telegram import Audio, Voice
from typing import Union
from config import BASE_PATH, URL
import requests
from docx import Document

AUDIO_DIR = os.path.join(BASE_PATH, "audios")
TRANSCRIPT_DIR = os.path.join(BASE_PATH, "transcripts")


def get_text_from(url: str, message: Union[Audio, Voice]):
    filename = download_message_as_file(message)
    with open(filename, 'rb') as file:
        text = download_transcript(url, file)

    return text


def download_message_as_file(message: Union[Audio, Voice]):
    filename = message.bot.get_file(file_id=message.file_id) \
        .download(custom_path=os.path.join(AUDIO_DIR, f"{message.file_id}.wav)"))
    return filename


def download_transcript(url: str, file):
    response = requests.get(url, files={"audio": file})
    assert response.status_code == 200

    # transcript = convert_to_doc_file(response.content.decode())
    transcript = response.content.decode()
    return transcript

    # transcript = convert_to_doc_file("Test transcript of something")
    # return transcript


def convert_to_doc_file(transcript: str):
    document = Document()
    document.add_paragraph(transcript)
    file_name = f"{generate_name()}.docx"
    file_path = os.path.join(TRANSCRIPT_DIR, file_name)
    document.save(file_path)
    return file_path


def generate_name():
    name = datetime.datetime.now().isoformat()
    name = name.split(".")[0]
    name = name.replace(":", "-")
    return name


if __name__ == "__main__":
    doc = convert_to_doc_file("Blah blah  blah ")
    print(type(TRANSCRIPT_DIR))
