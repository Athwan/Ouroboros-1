import os
import discord
import json
from functions import FindBest
import ToEmbed

def main():
    (command, name)=input('Input: ').split(' ',1)
    if command == 'quest':
        quest = FindBest(ToEmbed.DIRS['Quests'], name,True)
        (embed,image)=ToEmbed.Quest(quest,'')
        print(json.dumps(embed.to_dict(), indent=4))#,file=discord.File(image,filename='{}.png'.format(quest)).to_dict(),

    if command == 'job':
        job = FindBest(ToEmbed.DIRS['Job'], name,True)
        embed = ToEmbed.Job(job,'main')
        print(json.dumps(embed.to_dict(), indent=4))

    if command == 'unit':
        unit = FindBest(ToEmbed.DIRS['Unit'], name, True)
        print(json.dumps(ToEmbed.Unit(unit,'main').to_dict(), indent=4))

    if command == 'kaigan':
        unit = FindBest(ToEmbed.DIRS['Unit'], name, True)
        print(json.dumps(ToEmbed.Unit(unit,'kaigan').to_dict(), indent=4))

    if command == 'lore':
        unit = FindBest(ToEmbed.DIRS['Unit'], name, True)
        print(json.dumps(ToEmbed.Unit(unit,'lore').to_dict(), indent=4))

    if command == 'art':
        unit = FindBest(ToEmbed.DIRS['Unit'], name, True)
        for embed in ToEmbed.Unit(unit,'art'):
            print(json.dumps(embed.to_dict(), indent=4))
    main()
main()