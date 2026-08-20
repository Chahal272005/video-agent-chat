from dotenv import load_dotenv
load_dotenv()
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import os

print("Key Loaded:", os.getenv("SARVAM_API_KEY"))
print("CWD", os.getcwd())

source = "https://www.youtube.com/watch?v=vFP1mgZ_LEY"
language = "hinglish"

chunks = process_input(source)
transcript = transcribe_all(chunks, language=language)


print(transcript)