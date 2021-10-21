from userbot import jmthon

plugin_category = "extra"


@jmthon.ar_cmd(
    pattern="الاوامر$",
    command=("الاوامر", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمـه ﭑوامـر سـۅࢪس ديـو : ♰\n✛━━━━━━━━━━━━━✛\n(`.م1`) - ﭑوامࢪ اެلادمن ♰\n(`.م2`) -  ﭑوامࢪ اެلمجموعهہَ ♰\n(`.م3`) - ﭑوامࢪ اެلترحيب واެلࢪدود ♰\n\n(`.م4`) - حمايهہَ خاصہَ ولتلڪࢪاف ♰\n(`.م5`) - ﭑوامࢪ اެلمنشنہَ ۅ اެلاެنتحال ♰\n(`.م6`) - ﭑوامࢪ اެلتحميلہَ ۅ اެلترجمهہَ ♰\n(`.م7`) - ﭑوامࢪ المنعہَ ۅ اެلقفل ♰\n(`.م8`) - ﭑوامࢪ اެلتنظيفہَ ۅ اެلتڪرار ♰\n(`.م9`) - ﭑوامࢪ اެلوقتيہَ ۅ اެلتشغيلہَ ♰\n(`.م10`) - ﭑوامࢪ اެلڪشف ۅ اެلࢪوابط ♰\n(`.م11`) - ﭑوامࢪ اެلمساعدة ۅ اެلاެذاعه ♰\n(`.م12`) - ﭑوامࢪ اެلاެرسال ♰\n(`.م13`) - ﭑوامࢪ اެلملصقات ۅ ڪوڪل ♰\n(`.م14`) - ﭑوامࢪ اެلتسليه ۅ اެلتحشيش ♰\n(`.م15`) - ﭑوامࢪ اެلصيغہَ ۅ اެلجهات ♰\n(`.م16`) - شࢪحہَ اެلتنصيبہَ ۅ اެلمتحࢪڪات ♰\n\n✛━━━━━━━━━━━━━✛\n ♰ ﻣطوࢪ اެلسۅࢪس : @reKhso"
        )


@jmthon.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الادمن لسورس ديـو :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر المجـموعه لسورس ديـو :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الـترحيب والـردود :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر حـماية الخاص والتلكراف :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الخاص` )\n- ( `.اوامر التلكراف` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الـمنشن والانتحال :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر التحميل والترجمه :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر القفل والمنع :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر التكرار والتنظيف :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الوقتي والتشغيل :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الكـشف و الروابط :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر المساعدة  :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الارسال :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر الملصقات وكوكل :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر التسلية والتحشيش :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )


@jmthon.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر تحويل الصيغ و الجهات:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )
        
@jmthon.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "قائمة اوامر المتـحركات :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.متحركات كيوت` ) \n- ( `.متحركات ساد` )\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n- شࢪح تنصيبہَ :  https://t.me/DEOOUS/10\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DEOOUS"
        )
