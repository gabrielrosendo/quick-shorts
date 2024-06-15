
import os
import io
from pytube import YouTube
from pydub import AudioSegment
import speech_recognition as sr
from youtube_transcript_api import YouTubeTranscriptApi


# Function to download audio from YouTube video
def download_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        audio_file = f"{yt.title}.mp3"
        audio_stream.download(filename=audio_file)
        return audio_file
    else:
        return None
def get_captions(video_url):
    video_id = video_url.split("v=")[1]
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for transcript_line in transcript_list:
            start_time = transcript_line['start']
            end_time = start_time + transcript_line['duration']
            transcript += f"\n{start_time} - {end_time}: {transcript_line['text']}"
        return transcript
    except:
        print("An error occurred while fetching the transcript.")
        return None
    
# Function to get transcript using speech recognition
def get_transcript(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio)
        return transcript
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Example usage
if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=ry8n58JJ4Y4&t=667s'
    
    # Download audio
    #audio_file = download_audio(video_url)
    audio_file = False
    captions = get_captions(video_url)
    if captions:
        print("Captions:")
        print(captions)
    if audio_file:
        # Get transcript
        transcript = get_transcript(audio_file)
        print("Transcript:")
        print(transcript)
        
        # Clean up: remove audio file
        os.remove(audio_file)
    else:
        print("Audio download failed. Captions may not be available for this video.")


