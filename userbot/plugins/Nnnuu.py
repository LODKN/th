@bot.on(admin_cmd(pattern="اكس$"))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@nnLuBoT"
    noob = "@nnLuBoT start61496504"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
