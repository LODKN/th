iqthon.iq_cmd(
    pattern="اطفاء تليثون$",
    command=("اطفاء تليثون", plugin_category),
    info={
        "header": "♰︙ إيقاف التشغيـل ✕",
        "description": "♰︙لإيقـاف الدايـنو لموقـع هيروڪو، عندها لايمڪنك التشغيـل من البوت وبذلك عليك الذهـاب لموقـع هيروڪو لتشغيـله 💡",
        "usage": "{tr}اطفاء تليثون",
    },
)


async def _(event):
    "♰︙ إيقاف التشغيـل ✕"
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**⌔︙ إيقاف التشغيـل ✕ **\n" "**⌔︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**",
        )
    await edit_or_reply(
        event,
        "**♰︙جـاري إيقـاف تشغيـل البـوت الآن ..**\n **أعـد تشغيـلي يدويـاً لاحقـاً عـبر هيـروڪو ..**\n**سيبقى البـوت متوقفـاً عن العمـل لغايـة** \n**الوقـت المذڪـور 💡**",
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@iqthon.iq_cmd(
    pattern="اطفاء مؤقت( [0-9]+)?$",
    command=("اطفاء مؤقت", plugin_category),
    info={
        "header": "Userbot will stop working for the mentioned time.",
        "usage": "{tr}sleep <seconds>",
        "examples": "{tr}sleep 60",
    },
)
async def _(event):
    "To sleep the userbot"
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "♰︙بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**♰︙ تـم وضـع البـوت في وضـع السڪون لـ : ** "
            + str(counter)
            + " **⌔︙عـدد الثوانـي ⏱**",
        )
    event = await edit_or_reply(
        event, f"`⌔︙ حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** "
    )
    sleep(counter)
    await event.edit("**♰︙حسنـاً، أنـا نشـط الآن ᯤ **")
