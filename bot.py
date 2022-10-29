import interactions
from language_dict import language_dict
from googletrans import Translator

from cred import token, guildId

translator = Translator()
user_language = {'global':'ja'}

bot = interactions.Client(token=token)

@bot.event()
async def on_start():
    print(f'We have logged in as {bot.me.name}')

"""Translating Text"""
@bot.command(description="Translate Text")
@interactions.option(name='text', description="Translate Text")
async def ts(ctx: interactions.CommandContext, option: str):
    user = ctx.author.user.id
    if user in user_language.keys():
        language = language_dict[user_language[user]]
        translation = translator.translate(option, src='en', dest=language)
    else:
        language = language_dict[user_language['global']]
        translation = translator.translate(option, src='en', dest=language)
    await ctx.send(f"{translation.text}\n{translation.pronunciation}")

"""Translator bot settings"""
@bot.command(description="Translator bot settings")
async def ts_settings(ctx: interactions.CommandContext):
    """This description isn't seen in UI (yet?)"""
    pass

"""Change global translation option"""
@ts_settings.subcommand(description='Change global translation option')
@interactions.option(name='option', description="Set global language translation")
async def global_language(ctx: interactions.CommandContext, option: str):
    if option in language_dict.keys():
        user_language['global']=option
        await ctx.send(f"Setting global translation to: {language_dict[option]}")
    else:
        await ctx.send(f"Language Option not available")

"""Change user translation option"""
@ts_settings.subcommand(description="Change user translation option")
@interactions.option(name='option', description="Set user language translation, use 0 to reset user language")
async def set_user_language(ctx: interactions.CommandContext, option: str):
    if option in language_dict.keys():
        user = ctx.author.user.id
        user_language[user]=option
        await ctx.send(f"Setting {ctx.author}'s translation to: {language_dict[option]}")
    elif option=='0':
        user_language.pop(user)
    else:
        await ctx.send(f"Language Option not available")

"""List all language options"""
@ts_settings.subcommand(description="List all language options")
async def list_language_options(ctx: interactions.CommandContext):
    await ctx.send('\n'.join([f'{key} : {val}' for key, val in language_dict.items()]))


bot.start()