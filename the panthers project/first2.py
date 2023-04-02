import speech_recognition as sr

from translate import Translator
import pyttsx3

r=sr.Recognizer()
text1=sr.AudioFile('music4.wav')
with text1 as source:
    audio=r.record(source)

value=r.recognize_google(audio)    

   
value1=r.recognize_google(audio,language="ma-IN")


value2=r.recognize_google(audio,language="hi-IN")
 

value3=r.recognize_google(audio,language="en-IN") 

value4=r.recognize_google(audio,language="mr-IN") 

value5=r.recognize_google(audio,language="tn-IN") 

value6=r.recognize_google(audio,language="bn-IN") 

value7=r.recognize_google(audio,language="ja-JP")

print("hindi")
print("bengali")
print("english")
print("marathi")
print("tamil")
print("original text")
required=str(input("entert the final output language : "))
if required=="original text":
    print(value," "+"was your original text and this is required answer : \n",value1)
elif(required=="hindi"):
    print(value," "+"was your original text and this is required answer : \n",value2)    
elif(required=="english") :
    print(value," "+"was your original text and this is required answer : \n",value3)   
elif(required=="marathi"):
    print(value," "+"was your original text and this is required answer : \n",value4) 
elif(required=="tamil"):
    print(value," "+"was your original text and this is required answer : \n",value5)       
elif(required=="bengali") :
    print(value," "+"was your original text and this is required answer : \n",value6)
elif(required=="japanese"):
    print(value," "+"was your original text and this is required answer : \n",value7)  
print("\n test is complete")  





        








