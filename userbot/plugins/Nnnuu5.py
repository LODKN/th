@jmthon.ar_cmd(
    pattern="ابلاغ$",
    command=("ابلاغ", plugin_category),
    info={
        "header": "To tags admins in group.",
        "usage": "{tr}report",
    },
)
async def _(event):
    "To tags admins in group."
    mentions = "⌯︙@admin \n⌯︙انـتباه أيـها الـمشرفين قـام شـخص بـتبليـغكم"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()
