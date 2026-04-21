# def total(galleons,sickles,knuts):
# 	return (galleons*17+sickles)*29+knuts
# coins = [100,50,25]
# print(total(*coins),"knuts")

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()