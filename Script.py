class script(object):
    START_TXT = """<b>ʜᴇʏ {}, {}\n\n𝒊 𝑨𝒎 𝑻𝒉𝒆 𝑴𝒐𝒔𝒕 𝑷𝒐𝒘𝒆𝒓𝒇𝒖𝒍 𝑨𝒖𝒕𝒐 𝑭𝒊𝒍𝒕𝒆𝒓 𝑩𝒐𝒕 𝑾𝒊𝒕𝒉 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒆𝒂𝒕𝒖𝒓𝒆.</b>"""

    GSTART_TXT = """<b>ʜᴇʏ {},\n\n𝒊 𝑨𝒎 𝑻𝒉𝒆 𝑴𝒐𝒔𝒕 𝑷𝒐𝒘𝒆𝒓𝒇𝒖𝒍 𝑨𝒖𝒕𝒐 𝑭𝒊𝒍𝒕𝒆𝒓 𝑩𝒐𝒕 𝑾𝒊𝒕𝒉 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒆𝒂𝒕𝒖𝒓𝒆.</b>"""
    
    HELP_TXT = """<b>ʜᴇʏ {},
    
ᴡᴇ ʜᴀᴠᴇ ᴅᴇᴠɪᴅᴇᴅ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ᴀɴᴅ ʙᴏᴛ ᴜꜱᴇʀꜱ.\nᴀɴᴅ ᴡᴇ ʜᴀᴠᴇ ꜱᴏᴍᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ
</b>"""

    ABOUT_TXT = """<b>╭────[ MY ᴅᴇᴛᴀɪʟꜱ ]────⍟
├⍟ Mʏ Nᴀᴍᴇ : <a href='https://t.me/mawhOrzzBackUp2'>~𝙼𝙰𝚆𝙷 𝙾𝚛𝚣𝚣~</a>
├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Usernamesnothing'>जय श्री राम</a> 
├⍟ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
├⍟ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a> 
├⍟ Dᴀᴛᴀʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a> 
├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ4.2 [ꜱᴛᴀʙʟᴇ]
╰───────────────⍟</b>"""
        
    CHANNELS = """
<b>⚡ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ ⚡ 

▫ ᴀʟʟ ɴᴇᴡ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs.
▫ ғᴀsᴛᴇsᴛ ʙᴏᴛs ᴀʀᴇ ᴀᴅᴅᴇᴅ.
▫ ғʀᴇᴇ & ᴇᴀsʏ ᴛᴏ ᴜsᴇ.
▫ 𝟸𝟺x𝟽 sᴇʀᴠɪᴄᴇs ᴀᴠᴀɪʟᴀʙʟᴇ.</b>"""

    
    STATUS_TXT = """<b>╭────[ Deendayal_dhakad ]────⍟
├⍟ Tᴏᴛᴀʟ Fɪʟᴇs : <code>{}</code>
├⍟ Tᴏᴛᴀʟ Usᴇʀs : <code>{}</code>
├⍟ Tᴏᴛᴀʟ Cʜᴀᴛs : <code>{}</code>
├⍟ Usᴇᴅ Sᴛᴏʀᴇɢᴇ : <code>{}</code>
├⍟ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ : <code>{}</code>
╰───────────────⍟</b>"""

    LOG_TEXT_G = """#NewGroup
    
Gʀᴏᴜᴘ = {}
Iᴅ = <code>{}</code>
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}
"""

    LOG_TEXT_P = """#NewUser
    
Iᴅ - <code>{}</code>
Nᴀᴍᴇ - {}
"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,
ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """<b>𝑆𝑝𝑒𝑙𝑙𝑖𝑛𝑔 𝑀𝑖𝑠𝑡𝑎𝑘𝑒 𝐵𝑟𝑜 ‼️\n𝐷𝑜𝑛'𝑡 𝑊𝑜𝑟𝑟𝑦 😊 𝐶ℎ𝑜𝑜𝑠𝑒 𝑇ℎ𝑒 𝐶𝑜𝑟𝑟𝑒𝑐𝑡 𝑂𝑛𝑒 𝐵𝑒𝑙𝑜𝑤 👇\n\n<blockquote>नीचे दिए गए विकल्पों में से movie के नाम की सही Spelling चुनें 👇</blockquote></b>"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

📝 ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

⚜️ ᴇxᴀᴍᴘʟᴇ : Jawan or Jawan 2023 

📝 ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

⚜️ ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""
    
    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs</b>"""

    MVE_NT_FND = """<b>🔻 𝑻𝒉𝒊𝒔 𝑴𝒐𝒗𝒊𝒆 𝑵𝒐𝒕 𝑭𝒐𝒖𝒏𝒅 𝒎𝒚 𝑫𝒂𝒕𝒂𝒃𝒂𝒔𝒆. 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝒕𝒐 𝒂𝒅𝒎𝒊𝒏..

🔻 𝒀𝒆 𝒎𝒐𝒗𝒊𝒆 𝑯𝒂𝒎𝒂𝒓𝒆 𝒅𝒂𝒕𝒂𝒃𝒂𝒔𝒆 𝒎𝒆 𝑨𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒏𝒂𝒉𝒊 𝒉𝒂𝒊 𝑵𝒊𝒄𝒉𝒆 𝒂𝒅𝒎𝒊𝒏 𝒔𝒆 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 𝒌𝒂𝒓𝒆... 

🚸 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝒕𝒐 𝒂𝒅𝒎𝒊𝒏.. 👇</b>"""
    

    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ǫᴜᴇʀʏ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🍁 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n🌟 {} \n\n🔍 ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ 🔎\n\n⚠️ ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ 👇</b>"""
    
    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 
</b>"""

    USERS_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴜꜱᴇʀꜱ ⇊
    
• /batch - ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.
• /stats - ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.
• /request - sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ( ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ )
• /plan - ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ.
• /myplan - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ."""

    GROUP_TXT = """👋 ʜᴇʏ {},

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ⇊
    
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /shortlink - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /remove_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
• /setshortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /setshortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ.
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ɢʀᴏᴜᴘ.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ."""

    DHAKAD_DONATION = """<b>👋 ʜᴇʏ {},
    
<b>𝑷𝒍𝒆𝒂𝒔𝒆 𝑫𝒐𝒏𝒂𝒕𝒆 𝑻𝒉𝒆 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑭𝒐𝒓 𝑲𝒆𝒆𝒑𝒊𝒏𝒈 𝑻𝒉𝒆 𝑺𝒆𝒓𝒗𝒊𝒄𝒆 𝑨𝒍𝒊𝒗𝒆 & 𝑲𝒆𝒆𝒑 𝑩𝒓𝒊𝒏𝒈𝒊𝒏𝒈 𝑴𝒐𝒓𝒆 𝑵𝒆𝒘 𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔 𝑭𝒐𝒓 𝒀𝒐𝒖...... 𝑰𝑻 𝑾𝒊𝒍𝒍 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑼𝒔 𝑻𝒐 𝑲𝒆𝒆𝒑 𝑶𝒖𝒓 𝑩𝒐𝒕 𝑶𝒏 𝑯𝒆𝒓𝒐𝒌𝒖 𝑨𝒏𝒅 𝑺𝒐 𝑻𝒉𝒂𝒕 𝑾𝒆 𝑪𝒂𝒏 𝑲𝒆𝒆𝒑 𝑼𝒑𝒍𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒗𝒊𝒆𝒔 𝑨𝒏𝒅 𝑾𝒆𝒃𝒔𝒆𝒓𝒊𝒆𝒔 𝑵𝒐𝒏 𝑺𝒕𝒐𝒑 𝑰𝒏 𝑩𝒆𝒔𝒕 𝑸𝒖𝒂𝒍𝒊𝒕𝒊𝒆𝒔.<b>

<b>𝒀𝒐𝒖 𝑪𝒂𝒏 𝑫𝒐𝒏𝒂𝒕𝒆 𝑨𝒏𝒚 𝑨𝒎𝒐𝒖𝒏𝒕 𝒀𝒐𝒖 𝑯𝒂𝒗𝒆 🌝<b>

<b>🎉 𝑺𝒆𝒍𝒆𝒄𝒕 𝒀𝒐𝒖𝒓 𝑫𝒐𝒏𝒂𝒕𝒆 𝑴𝒆𝒕𝒉𝒐𝒅 👇</b>

➢ QR Cᴏᴅᴇ : <a href='https://graph.org/file/e419f801841c2ee3db0fc.jpg'>𝑪𝑳𝑰𝑪𝑲 𝑯𝑬𝑹𝑬 𝑻𝑶 𝑺𝑪𝑨𝑵</a>

➢ Uᴘɪ Iᴅ : <code>deendayaldhaked@ybl</code>

‼️ 𝑴𝒖𝒔𝒕 𝑺𝒆𝒏𝒅 𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝑨𝒇𝒕𝒆𝒓 𝑫𝒐𝒏𝒂𝒕𝒆.</b>"""
    
    
    SELECT = """
➢ ᴄʟɪᴄᴋ ᴏɴ "ǫᴜᴀʟɪᴛʏ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ʟᴀɴɢᴜᴀɢᴇ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ꜱᴇᴀꜱᴏɴ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ꜱᴇᴀꜱᴏɴ.

➢ ᴄʟɪᴄᴋ ᴏɴ "♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ᴄʟɪᴄᴋ.

"""

    REQINFO = """➢ ᴄʟɪᴄᴋ "ǫᴜᴀʟɪᴛʏ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ "ʟᴀɴɢᴜᴀɢᴇ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ "ꜱᴇᴀꜱᴏɴ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ꜱᴇᴀꜱᴏɴ.
➢ ᴄʟɪᴄᴋ "♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️" ᴀɴᴅ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ."""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
    
    CAPTION = """<b><a href="https://t.me/moviesandwebserieshubOrzz">{file_caption}</a></b>\n\n<b>⚜️ Powered By : <a href=https://t.me/mawhOrzzBackUp2>[~𝑴𝑨𝑾𝑯 𝑶𝒓𝒛𝒛⁠•]</a></b>"""

    IMDB_TEMPLATE_TXT = """
<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>


⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by : {message.from_user.mention}</b>"""
    

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 Deendayal_dhakad</code>
</b>"""

    LOGO = """

BOT WORKING PROPERLY"""

    #PLANS

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {},

🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

⚜️ ɴᴏ ɴᴇᴇᴅ ᴛᴏ Vᴇʀɪғʏ
⚜️ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
⚜️ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ                           
⚜️ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs

🌹 ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
🤟 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    CPREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

⚜️ ɴᴏ ɴᴇᴇᴅ ᴛᴏ Vᴇʀɪғʏ
⚜️ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
⚜️ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ                           
⚜️ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs


🌹 ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    PLAN_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

🩸 ɴᴏ ɴᴇᴇᴅ ᴛᴏ Vᴇʀɪғʏ
🩸 ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
🩸 ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ                       
🩸 ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs

🌹 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ <a href='https://t.me/Usernamesnothing'>Owner</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>👋 ʜᴇʏ {},
    
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 15 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 15₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>👋 ʜᴇʏ {},
    
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 30₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>👋 ʜᴇʏ {},
    
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 45 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 45₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 ʜᴇʏ {},
    
🏅 <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
⏰ 60 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 60₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>👋 ʜᴇʏ {},

💎 <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
⏰ 90 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 90₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/Sorry_Sorry_Galti_Ho_Gai'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>deendayaldhaked@ybl</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
 ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/e419f801841c2ee3db0fc.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},
    
🌍 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

⚜️ ɴᴏ ɴᴇᴇᴅ ᴛᴏ Vᴇʀɪғʏ
⚜️ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
⚜️ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ                           
⚜️ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs

🪔 ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
🪔 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan
‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""    

    SOURCE_TXT =""" <b>
    ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ᴀ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ ᴍᴀᴋᴇ ᴛʜɪꜱ ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ 💰 </b> """

    EXTRAF_TXT =""" <b> ʜᴇʀᴇ ɪꜱ ᴍʏ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ </b>"""

    STICKER_TXT = """<b>ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ. 
 • ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ 
   
  ʜᴏᴡ ᴛᴏ ᴜꜱᴇ 
 ◉ ʀᴇᴘʟʏ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ [/stickerid]  
 </b>""" 
  
    FONT_TXT= """<b>ᴜꜱᴀɢᴇ 
  
 ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ꜰᴏɴᴛ ꜱᴛyʟᴇ   
  
 ᴄᴏᴍᴍᴀɴᴅ : /font ʏᴏᴜʀ ᴛᴇxᴛ (ᴏᴩᴛɪᴏɴᴀʟ) 
 ᴇɢ:- /font ʜᴇʟʟᴏ 
  
 </b>"""
    TELE_TXT = """<b>ʜᴇʟᴘ: ᴛᴇʟᴇɢʀᴀᴘʜ ᴅᴏ ᴀꜱ ʏᴏᴜ ᴡɪꜱʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ! 
  
 ᴜꜱᴀɢᴇ: /telegraph - ꜱᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ) 
  
 ɴᴏᴛᴇ: 
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ 
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ</b>"""
    SONG_TXT = """<b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ</b> 
      
 <b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ꜰᴏʀ ᴛʜᴏꜱᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜꜱɪᴄ. yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴy ꜱᴏɴɢ ᴡɪᴛʜ ꜱᴜᴩᴇʀ ꜰᴀꜱᴛ ꜱᴩᴇᴇᴅ. ᴡᴏʀᴋꜱ ʙᴏᴛ ᴀɴᴅ ɢʀᴏᴜᴩꜱ ᴏɴʟy...</b> 
  
  /song ꜱᴏɴɢ ɴᴀᴍᴇ</b>"""

    YOUTUBE_TXT = """<b>ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴍᴀɴᴅ, ᴛʜᴏꜱᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴠɪᴅᴇᴏꜱ
 
 <b>/video<b> <b> /ᴠɪᴅᴇᴏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ<b>"""

    INSTAGRAM_TXT = """<b>Wɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴇᴀsɪʟʏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ Iɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟs.

/Instagram  sᴇɴᴅ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ,sᴛᴏʀɪᴇs ᴀɴᴅ ᴘᴏsᴛ ʟɪɴᴋ ᴛᴏ ᴛʜɪs ʙᴏᴛ, ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ, ᴘᴜʙʟɪᴄ ᴏɴʟʏ.

Exᴀᴍᴘʟᴇ 👉 /Instagram ʜᴛᴛᴘs://ᴡᴡᴡ.ɪɴsᴛᴀɢʀᴀᴍ.ᴄᴏᴍ/ʀᴇᴇʟ/CᴠTɴᴋᴄ𝟷ᴏᴜD𝟹/?ɪɢsʜ=YᴢʟᴊYTᴋ𝟷ODɢ𝟹Zɢ==<b>"""
    
    JSON_TXT = """<b> 
 ᴊsᴏɴ:  
 ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json 
  
 ꜰᴇᴀᴛᴜʀᴇs: 
  
 ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ 
 ᴘᴍ sᴜᴘᴘᴏʀᴛ 
 ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ 
  
 ɴᴏᴛᴇ: 
  
 ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.</b>"""
