import os
try:
  import emoji
  from googletrans import Translator
  from telethon import events, TelegramClient as tg
except:
  os.system("pip install emoji && pip install googletrans==3.1.0a0 && pip install telethon")
  import emoji
  from googletrans import Translator
  from telethon import events, TelegramClient as tg
token = "1738596677:AAGPRFJEErGKuq8EEGalVA53mk5511xkGM8"
#1738596677:AAGPRFJEErGKuq8EEGalVA53mk5511xkGM8
borg = tg("translatte", 1621727, "31350903c528876f79527398c09660ce").start(bot_token=token)

async def eor(event, msg):
  """FOR ERROR HANDLING"""
  try:
    await event.reply(msg)
  except:
    await event.edit(msg)
 
@borg.on(events.NewMessage(pattern="/tr"))
async def _(event):
    try:
      input_str = event.text.split(" ", 1)[1]
    except:
    	input_str = "zh-CN"
    previous_message = await event.get_reply_message()
    text = previous_message.message
    lan = input_str
   # text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated By bot** 
         Source **( {} )**
         Translation **( {} )**
         {}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await eor(event, output_str)
    except Exception as exc:
        await eor(event, str(exc))
borg.run_until_disconnected()
