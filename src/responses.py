import discord
import datetime

def get_response(user_input : str) -> str:
    p_message = user_input.lower()

    if p_message == 'hello':
        embed = discord.Embed()(description="__                                                                                                                                  __\n\n**Player Info:**\nUsername:\n\nTagline:\n__                                                                                                                                  __\n\n**Player Stats:**\nLevel: {Level}\n\nWins: {Wins}\n\nLosses: {Losses}\n\nWin Rate: {Win Rate}%\n\nGames Played: {Games Played}\n\nPeak Rating: {Peak Rating}\n\nCurrent Rating: {Current Rating}\n\nLast Game Result: {Last Game Result}\n__                                                                                                                                  __\n\n```\nValorant EP9 Act 1\n```",
                      colour=0x00b0f4,
                      #timestamp=datetime.now()
                      )

        embed.set_author(name="Peak rating: Diamond 2",
                        url="https://media.valorant-api.com/competitivetiers/564d8e28-c226-3180-6285-e48a390db8b1/19/smallicon.png",
                        icon_url="Peak rating: Diamond 2")

        embed.set_image(url="https://media.valorant-api.com/playercards/c7e58b09-4b1f-ca2a-5ab6-daa6cab2fa6c/wideart.png")

        embed.set_thumbnail(url="https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/smallicon.png")

        embed.set_footer(text="H00DBYAIR#BMWM5",
                        icon_url="https://media.valorant-api.com/playercards/c7e58b09-4b1f-ca2a-5ab6-daa6cab2fa6c/smallart.png")
        return embed
