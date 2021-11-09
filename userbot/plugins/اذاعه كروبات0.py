@iqthon.on(admin_cmd(pattern="اذاغه مجموعات ?(.*)$"))    
 async def gcast(event):
     if not event.out and not is_fullsudo(event.sender_id):
         return await edit_or_reply(event, "هـذا الامـر مقـيد ")
     xx = event.pattern_match.group(1)
     if not xx:
         return edit_or_reply(event, "**♰ ⦙   يجـب وضـع نـص مع الامـر للتوجيـه**")
     tt = event.text
     msg = tt[6:]
     event = await edit_or_reply(event, "** ♰ ⦙   يتـم الـتوجيـة للـمجموعـات انتـظر قليلا**")
     er = 0
     done = 0
     async for x in bot.iter_dialogs():
         if x.is_group:
             chat = x.id
             try:
                 done += 1
                 await bot.send_message(chat, msg)
             except BaseException:
                 er += 1
     await event.edit(f"♰ ⦙   تـم بنـجـاح فـي {done} من الـدردشـات , خطـأ فـي {er} من الـدردشـات")
 async def getTranslate(text, **kwargs):
     translator = Translator()
     result = None
     for _ in range(10):
         try:
             result = translator.translate(text, **kwargs)
         except Exception:
             translator = Translator()
             await sleep(0.1)
     return result
