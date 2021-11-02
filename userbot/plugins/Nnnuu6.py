
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
