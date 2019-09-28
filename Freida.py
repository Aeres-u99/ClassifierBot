import DBman.dbManager as DBm
import botogram
import random
import time

bot = botogram.create("YOUR-API-KEY")

bot.about = "This bot is Sets you up in groups. That is, It will assign you a class."
bot.owner = "@imbloodymorningstar"

bot.after_help = [
    "For now, only three default classes are implemented. More will come in later :-) ",
]

squads = [
    "dummy squad",
    "Maou",
    "Chosen Undead",
    "Senpai's Squad",
    "Prime Eractus",
    "soaperS",
    "BlackSquad",
    "Elemental",
    "Punishers",
    "Yorozuya"
]

admins = {
    "814418325":"KuroAkuma",
    "140860604":"Mika Senpai",
    "932138471":"Lucifer",
    "609134614":"Uzumaki Konzoku",
    "945257374":"Asuna",
    "691607802":"Escanor",
    "740866586":"Prinz",
    "316541168":"Rick Sanchez",
    "791289016":"Sakata Gintoki"
}


@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("I am a classifier and I drop people into their required classes. For now I have defMultiple classes.")

@bot.command("assign")
def assign_command(chat, message, args):
    """Testing the assignment"""
    chat.send("I am a train choo choo")
    chat.send(str(chat.id))
    chat.send(str(chat.type))
    chat.send(str(message.sender.id))
    chat.send(str(chat.admins))
    #chat.send(str(chat.members))
    chat.send(str(User.id))
    print(str(chat.id))
    print(str(chat.type))
    print(str(message.sender.id))
    print(str(chat.admins))
    #print(chat.sendstr(chat.members))
    print(str(User.id))

@bot.command("recruitme")
def recruitme_command(chat,message,args):
    userID = message.sender.id
    squad = squads[random.randint(1,9)]
    rank = "cadet"
    name = message.sender.first_name
    if userID in admins.keys():
        chat.send("Already registered!")
    elif DBm.retrieve_assg(userID):
        chat.send("You are already **recruited**,\n check status by /status.")
        time.sleep(3)
    else:
        DBm.insert_assg(squad,rank,userID,name)
        time.sleep(3)
        print("Recruited ",name)
        chat.send("Recruited! check status by /status ^_^ ")


@bot.command("status")
def status_command(chat,message,args):
    userID=message.sender.id
    output = DBm.retrieve_assg(userID)
    if len(output)<2:
        output = "Not found! Try getting recruited first :D"
    chat.send(str(output))

@bot.command("mydetails")
def get_details(chat,message,args):
    userID=message.sender.id
    print(userID)
    chat.send("TBI")


if __name__ == "__main__":
    bot.run()

