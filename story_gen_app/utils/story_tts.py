import asyncio
import edge_tts
import tempfile
import os


VOICE_MAP = {
    "English": "en-US-GuyNeural",
    "Hindi": "hi-IN-MadhurNeural",
    "Hinglish": "en-US-GuyNeural",
    "French": "fr-FR-HenriNeural",
    "Spanish": "es-ES-AlvaroNeural",
    "German": "de-DE-ConradNeural"
}


async def generate_audio_async(text, voice):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    filename = temp_file.name

    temp_file.close()

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(filename)

    return filename


def generate_audio(text, language):

    voice = VOICE_MAP.get(
        language,
        "en-US-GuyNeural"
    )

    filename = asyncio.run(
        generate_audio_async(
            text,
            voice
        )
    )

    return filename