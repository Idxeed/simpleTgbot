from pyrogram import Client, filters
from time import time
from pyrogram.types import ChatPermissions
import tgcrypto
app = Client(
    "my_bot",
    api_id=,
    api_hash="",
    bot_token=""
)


async def start_message():
    await app.start()
    await app.send_message(chat_id = -1001494065075, text='Здарова, Евафаги' )
#app.run(start_message())

@app.on_message(filters.command(["start", "help"]))
async def my_handler(сlient, message):
    await app.send_message(chat_id=-1001494065075,text='Бот работает стабильно. Ядро стабильно.',reply_to_message_id=message.message_id)

@app.on_message(filters.command(['kick', 'kick@Evafag_shitpostbot']))
async def ban_system(сlient, message):
    if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376:
        await app.send_message(chat_id = -1001494065075, text='Кикаю..' )
        await app.kick_chat_member(chat_id =-1001494065075, user_id = message.reply_to_message.from_user['id'] )
        print(message)

@app.on_message(filters.command(['unban','unban@Evafag_shitpostbot']))
async def unban_system(client, message):
    if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376:
        await app.unban_chat_member(chat_id = -1001494065075, user_id = message.reply_to_message.from_user['id'])

@app.on_message(filters.command(['mute', 'mute@Evafag_shitpostbot']))
async def mute_system(client, message):
    if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376:
        await app.send_message(chat_id = -1001494065075, text='Пользователь в муте' )
        app.restrict_chat_member(chat_id = -1001494065075, user_id = message.from_user['id'], permisson=ChatPermission( ))
@app.on_message(filters.command(['unmute', 'unmute@Evafag_shitpostbot']))

async def unmute_system(client, message):
    if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376:
        await app.send_message(chat_id = -1001494065075, text='Пользователь не в муте' )
        app.restrict_chat_member(chat_id = -1001494065075, user_id = message.from_user['id'], permisson=ChatPermission(can_send_message = True, can_send_media_messages = True, can_send_stickers = True, can_send_animations = True, can_add_web_page_previews = True ))
app.run()
#@app.on_message(filters.command(['readonly']))
#async def readonly(client, message):
   # if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376:
    #    await app.send_message(chat_id = -1001494065075, text='Канал переведен в режим readonly')
     #   app.set_slow_mode("evachah", 3660)

#@app.on_message(filters.command(['readonly_stop']))
#async def readonly_stop(client, message):
 #   if message.from_user.id ==541850733 or message.from_user.id ==1254591448 or  message.from_user.id == 709099376: