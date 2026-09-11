import pyrogram
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ..logging import LOGGER


class Nand(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting bot...")
        super().__init__(
            name="ShrutiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Add Me To Your Group",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_photo(
                    config.LOG_GROUP_ID,
                    photo=config.START_IMG_URL,
                    caption=f"<b>🎵 Bot Started Successfully</b>\n\n"
                            f"<b>Name:</b> {self.name}\n"
                            f"<b>Username:</b> @{self.username}\n"
                            f"<b>ID:</b> <code>{self.id}</code>\n\n"
                            f"<i>Bot is now online and ready to serve!</i>",
                    reply_markup=button,
                )
            except pyrogram.errors.ChatWriteForbidden:
                LOGGER(__name__).error("Bot cannot write to the log group")
                try:
                    await self.send_message(
                        config.LOG_GROUP_ID,
                        f"<b>🎵 Bot Started Successfully</b>\n\n"
                        f"<b>Name:</b> {self.name}\n"
                        f"<b>Username:</b> @{self.username}\n"
                        f"<b>ID:</b> <code>{self.id}</code>\n\n"
                        f"<i>Bot is now online and ready to serve!</i>",
                        reply_markup=button,
                    )
                except Exception as e:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
            except Exception as e:
                LOGGER(__name__).error(f"Error while sending to log group: {e}")
        else:
            LOGGER(__name__).warning("LOG_GROUP_ID is not set")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            except Exception as e:
                LOGGER(__name__).error(f"Error checking bot status: {e}")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
    # Telegram Premium custom emoji used throughout bot responses. The text
    # inside each tag is a fallback for clients that cannot display it.
    PREMIUM_EMOJI = {
        "👋": "5298590020796429445",
        "😱": "5298501840822875885",
        "⚙️": "5341715473882955310",
        "👇": "5463390772097199381",
        "✅": "5980930633298350051",
        "🥂": "6172657075743625817",
        "❌": "5796615668023435743",
        "⚡️": "6046338355241687218",
        "✨": "6046240412807469383",
        "🎵": "5463107823946717464",
        "🌸": "5449714299146629735",
        "📸": "5447152480003567767",
        "📹": "5192794260352541359",
        "❄️": "5449449325434266744",
        "⏱️": "5382194935057372936",
        "🥀": "5208923808169222461",
        "➕": "4956507094124594921",
        "📂": "5931718859366075705",
        "❔": "5316988329252627954",
        "📩": "5472239203590888751",
    }

    @classmethod
    def _premium_emoji(cls, value, parse_mode=None):
        """Convert configured Unicode emoji to Telegram custom-emoji HTML."""
        if not isinstance(value, str) or "<emoji id=" in value:
            return value

        if parse_mode and str(parse_mode).lower() not in {"html", "parsemode.html"}:
            return value

        for emoji, emoji_id in cls.PREMIUM_EMOJI.items():
            value = value.replace(
                emoji, f'<emoji id="{emoji_id}">{emoji}</emoji>'
            )
        return value

    async def send_message(self, chat_id, text, parse_mode=None, *args, **kwargs):
        return await super().send_message(
            chat_id,
            self._premium_emoji(text, parse_mode),
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )

    async def send_photo(self, chat_id, photo, caption="", parse_mode=None, *args, **kwargs):
        return await super().send_photo(
            chat_id,
            photo,
            caption=self._premium_emoji(caption, parse_mode),
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )

    async def edit_message_text(
        self, chat_id, message_id, text, parse_mode=None, *args, **kwargs
    ):
        return await super().edit_message_text(
            chat_id,
            message_id,
            self._premium_emoji(text, parse_mode),
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )

    async def edit_message_caption(
        self, chat_id, message_id, caption="", parse_mode=None, *args, **kwargs
    ):
        return await super().edit_message_caption(
            chat_id,
            message_id,
            caption=self._premium_emoji(caption, parse_mode),
            parse_mode=parse_mode,
            *args,
            **kwargs,
        )
