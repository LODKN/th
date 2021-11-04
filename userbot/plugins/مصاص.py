import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event

plugin_category = "admin"

# =================== مصــــــــاص  ===================  #


@jmthon.ar_cmd(
    pattern="بلع مصاص(?:\s|$)([\s\S]*)",
    command=("بلع مصاص", plugin_category),
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("**♰... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ..♰**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(event, "**♰... . لمـاذا تࢪيـد كتم نفسـك؟  ..♰**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "*♰... غيـر قـادر عـلى جـلب مـعلومات الـشخص ..♰**"
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**♰... هـذا الشـخص بالع بـنجاح ..♰**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** بلع مصـاص من ريك ♰ **",
            )
        else:
            await edit_or_reply(
                event,
                f"** بلع مصـاص من ريك ♰ **",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                " المصاص\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " المصاص\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


# =================== فتــــــّـــحه  ===================  #


@jmthon.ar_cmd(
    pattern="فتحه(?:\s|$)([\s\S]*)",
    command=("فتحه", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("**♰... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ..♰**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(event, "**♰... لمـاذا تࢪيـد كتم نفسك؟ ..♰**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**♰... غيـࢪ قـادࢪ عـلى جـلب مـعلومات الـشخص ..♰**"
        )
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, f"**♰... هـذا الشـخص مفتوح اصلا  ..♰**")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطـأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** تـم فتحـه عن الـمستخـدم بـنجاح ♰ **",
            )
        else:
            await edit_or_reply(
                event,
                f"** تـم فتحـه عن الـمستخـدم بـنجاح ♰ **",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "، بلع مصـاص عزيزي\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " بلع مصـاص عزيزي\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


# ===================================== #


@jmthon.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


# =====================================  #
