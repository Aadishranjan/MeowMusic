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

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton


# Kurigram 2.2.24 supports Telegram colored inline buttons and custom emoji icons.
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                icon_custom_emoji_id="5258289810082111221",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_11"], callback_data="about_page")  # About button
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                icon_custom_emoji_id="5258289810082111221",
                style=enums.ButtonStyle.PRIMARY,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_GROUP,
                icon_custom_emoji_id="5357080225463149588",
                style=enums.ButtonStyle.SUCCESS,
                ),
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{config.OWNER_USERNAME.lstrip('@')}",
                icon_custom_emoji_id="5348306023889254367",
                style=enums.ButtonStyle.SUCCESS,
                ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_6"], 
                url=config.SUPPORT_CHANNEL,
                icon_custom_emoji_id="5260491539167073671",
                style=enums.ButtonStyle.SUCCESS,
                ),
            InlineKeyboardButton(
                text="ʟᴀɴɢᴜᴀɢᴇ",
                callback_data="LG",
                icon_custom_emoji_id="5447410659077661506",
                style=enums.ButtonStyle.SUCCESS,
                ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="help_page_1", icon_custom_emoji_id="5341715473882955310", style=enums.ButtonStyle.PRIMARY),
        ],
    ]
    return buttons

def about_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons

def owner_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_H_1"], url=config.INSTAGRAM),
            InlineKeyboardButton(text=_["S_H_2"], url=config.YOUTUBE),
        ],
        [
            InlineKeyboardButton(text=_["S_H_3"], url=config.GITHUB),
            InlineKeyboardButton(text=_["S_H_4"], url=config.DONATE),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
