# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from pyrogram.types import InlineKeyboardButton as Ikb, InlineKeyboardMarkup

from .functions import get_urls_from_text as is_url


def keyboard(buttons_list, row_width: int = 2):
    data = [
        (
            Ikb(text=str(item[0]), callback_data=str(item[1]))
            if not is_url(item[1])
            else Ikb(text=str(item[0]), url=str(item[1]))
        )
        for item in buttons_list
    ]
    rows = [data[index : index + row_width] for index in range(0, len(data), row_width)]
    return InlineKeyboardMarkup(rows)


def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
