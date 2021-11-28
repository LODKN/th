import asyncio
 from collections import deque
 from random import choice

 from userbot import jmthon
 from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
 from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
 from telethon.tl.functions.phone import GetGroupCallRequest as getvc
 from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
 from userbot import jmthon
 from ..core.managers import edit_delete, edit_or_reply

 async def get_call(event):
     mm = await event.client(getchat(event.chat_id))
     xx = await event.client(getvc(mm.full_chat.call))
     return xx.call

 def user_list(l, n):
     for i in range(0, len(l), n):
         yield l[i : i + n]

 @jmthon.on(admin_cmd(pattern="دعوه للمكالمه(?: |$)(.*)"))
 async def _(e):
     ok = await edit_or_reply(e, "`Inviting Members to Voice Chat...`")
     users = []
     z = 0
     async for x in e.client.iter_participants(e.chat_id):
         if not x.bot:
             users.append(x.id)
     hmm = list(user_list(users, 6))
     for p in hmm:
         try:
             await e.client(invitetovc(call=await get_call(e), users=p))
             z += 6
         except BaseException:
             pass
     await ok.edit(f"`Invited {z} users`")
 @jmthon.on(admin_cmd(pattern="بدء مكالمه(?: |$)(.*)"))
 async def _(e):
     try:
         await e.client(startvc(e.chat_id))
         await edit_or_reply(e, "`جار بدء المكالمة ✅...`")
     except Exception as ex:
         await edit_or_reply(e, f"`{str(ex)}`")

 # ================العاب جيبثون=========================

 R = [
     "**♰**العـاب الاحترافيه** 🎮𓆪 \n"
     "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
     "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
     "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
     "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
     "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
     "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
     "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
     "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
     "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
     "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
     "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
     "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
     "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n"
     "**-** ﻣطوࢪ اެلسۅࢪس  **⪼ [᥉َ𝖴᥆ᖇᥴᥱ ♰ ](t.me/nnnuu)   \n"
     "**- قناة اެلسۅࢪس⪼ [ᖇ  Ꮛ  Ꮶ ](t.me/k4kk44)   "
 ]

 @jmthon.on(admin_cmd(pattern="بلي$"))
 async def ithker(knopis):
     await knopis.edit(choice(R))
