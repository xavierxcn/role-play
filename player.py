from typing import Generator

import api


class Player:
    def __init__(self, name: str, personality: str):
        self.messages = []
        self.character_meta = {
            "user_info": "",
            "bot_info": personality,
            "user_name": "",
            "bot_name": name
        }
        self.personality = personality

    def talk_to(self, player) -> None:
        self.character_meta["user_info"] = player.character_meta["bot_info"]
        self.character_meta["user_name"] = player.character_meta["bot_name"]

    def say(self) -> Generator[str, None, None]:
        for chunk in api.get_characterglm_response(self.messages, meta=self.character_meta):
            yield chunk

    def listen(self, message: str) -> str:
        self.messages.append({"role": "user", "content": message})
