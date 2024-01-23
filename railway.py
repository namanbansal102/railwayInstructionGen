import os
import pandas as pd
from gtts import gTTS
from pydub import AudioSegment

def TextToSpeech(name,filename):
    txt=str(name)
    language='hi'
    myobj=gTTS(text=txt,lang=language,slow=True)
    myobj.save(f"./voices/{filename}")


def merge_audios(*audiolst):
    pass


def readData(filename):
    file=pd.read_excel(filename)
    print(file)
    for index,item in file.iterrows():
        print(index)
        print(item['train_no'])
        TextToSpeech(item['from'])


   




if __name__=="__main__":
    print("Welcome To Indian railway Management Software")
    print("Generating Skeleton")
    readData('./voices/announce_hindi.xlsx')
    