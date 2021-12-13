from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

plugin_category = "utils"


# كـتابة المـلف وتعديل.    :   محـمد الـزهيري.   اخمط وسمي روحك مطور فرخي 😂
# اذا انت ابن حرام اخمط 😂
# اي بعدك تريد تخمط ترا من تخمط مراح تنجح


@jmthon.ar_cmd(
    pattern="رفع مرتي(?:\s|$)([\s\S]*)",
    command=("رفع مرتي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1450865400:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1397042354:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 668571162:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
    )


@jmthon.ar_cmd(
    pattern="رفع جلب(?:\s|$)([\s\S]*)",
    command=("رفع جلب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1450865400:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1397042354:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 668571162:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفعـه جلب خليه خله ينبح فرخ 😂",
    )


@jmthon.ar_cmd(
    pattern="رفع تاج(?:\s|$)([\s\S]*)",
    command=("رفع تاج", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفعـه تاج 👑🔥"
    )


@jmthon.ar_cmd(
    pattern="رفع قرد(?:\s|$)([\s\S]*)",
    command=("رفع قرد", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1450865400:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1397042354:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 668571162:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفعـه قرد واعطائه موزة في طيزه 🍌",
    )


@jmthon.ar_cmd(
    pattern="رفع نسيم(?:\s|$)([\s\S]*)",
    command=("رفع نسيم", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفعـه ليصبح نسيم 🖤 ",
    )


@jmthon.ar_cmd(
    pattern="رفع صاحب(?:\s|$)([\s\S]*)",
    command=("رفع صاحب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙تـم رفعـه ليصبح صاحـب الحديقه 😂😂 ",
    )


@jmthon.ar_cmd(
    pattern="رفع ريكو(?:\s|$)([\s\S]*)",
    command=("رفع ريكو", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙تـم رفعـه ليصبح ريكو المطور .",
    )


@jmthon.ar_cmd(
    pattern="رفع مطي(?:\s|$)([\s\S]*)",
    command=("رفع مطي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1450865400:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1397042354:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 668571162:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙ تـم رفـعه مطي هـنا "
    )


@jmthon.ar_cmd(
    pattern="رفع زوجي(?:\s|$)([\s\S]*)",
    command=("رفع زوجي", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙تـم رفعه زوجج روحوا خلفوا 🤤😂",
    )


@jmthon.ar_cmd(
    pattern="رفع مطور(?:\s|$)([\s\S]*)",
    command=("رفع مطور", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"♰︙المستخدم [{tag}](tg://user?id={user.id}) \n♰︙تـم رفعه مطور من باب الشرجي .",
    )


@jmthon.ar_cmd(
    pattern="جسمه(?:\s|$)([\s\S]*)",
    command=("جسمه", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention,
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"**ببالي كلمه بس**\nفشلة من 🗿[{tag}](tg://user?id={user.id})🗿 .",
    )
