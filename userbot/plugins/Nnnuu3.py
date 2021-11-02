@iqthon.iq_cmd(
    pattern="تاريخ الرساله$",
    command=("when", plugin_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(
        event, f"**هذا تاريخ الرساله والوقت  ♰ :** `{yaml_format(result)}`"
    )
