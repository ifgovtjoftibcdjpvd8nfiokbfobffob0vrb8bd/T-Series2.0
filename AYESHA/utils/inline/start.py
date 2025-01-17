from pyrogram.types import InlineKeyboardButton

import config
from AYESHA import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_14"],
                url=f"https://youtube.com/@tseries?si=y7I_dU7yjiBbjG3V",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_12"], callback_data=f"abot_cb"),
            InlineKeyboardButton(text=_["S_B_13"], callback_data=f"ubot_cb"),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_10"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons
