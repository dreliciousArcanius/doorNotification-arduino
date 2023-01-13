from pygame import mixer
import discord
import serial
import time
import multiprocessing
a = True;
arduino = serial.Serial('COM3', 9600)
mixer.init()
def Measure():
    distance = arduino.readline()
    return float(distance)

class MyClient(discord.Client):
    async def on_ready(self):
        while True:
            output = Measure()
            if output < 29.00:
                if a:
                    mixer.music.load('bell.mp3')
                    mixer.music.play()
                    user = await client.fetch_user("userIDGoesHere")
                    await user.send("Door is open!!")
                    a = False
            else:
                a = True
                mixer.music.stop()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('tokenGoesHere')