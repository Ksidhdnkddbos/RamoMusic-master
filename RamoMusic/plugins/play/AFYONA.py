import asyncio
from pyrogram import Client, filters
from strings.filters import command
from RamoMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from RamoMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس♡"),
      
    ],
    
    [
        ("العكس🎸"),
        ("احرف🎸")
    ],
    [
        ("مطور السورس♕")
     
    ],
   
    [
         ("كت🎸"),
        ("صراحه🎸")
    ],
    [
        ("استوري❤")
    ],
    [
        ("نكته😂"),
        ("كتابات💔")
    ],
    [
        ("اذكارﷺ"),
        ("قرانﷺ") 
    ],
    [
         ("شعر🎸"),
        ("انصحني🎸")
    ],
    [
         ("صوره🌚")
        
    ],
    [
        ("لو خيروك🎸"),
         ("احكام🎸")
    ],    
    [
        ("قفل الازرار🎸")
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("قفل الازرار🎸"))
async def down(client, message):
          m = await message.reply("**تم قفل الكيبورد بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://graph.org/file/170b5e339b1d0a4f57ce5.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ S𝙾𝚞𝚁𝙲𝙴 𝚁𝚊𝚖𝚘 𖠛", url=f"https://t.me/R_surce"),
            ]
         ]
     )
  )

