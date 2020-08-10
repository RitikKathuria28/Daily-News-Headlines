import requests
import json

def speak(str):
    import win32com.client
    speak = win32com.client.Dispatch("SAPI.spVoice")
    speak.Speak(str)



if __name__ == '__main__':
    speak("Today's Headlines")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=4d8d6bc8e4b74fa2a40fcd32a07771b0"
    news = requests.get(url).text   # now this will give us javascript object we need to convert it into python object
    news_py = json.loads(news)
    arts = news_py['articles']

    for articles in arts:
        speak(articles['title'])
        speak("Moving on to the next news")