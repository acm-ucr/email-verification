import os
from dotenv import load_dotenv


class Guild:

    def __init__(self):
        load_dotenv()
        ROLE = os.getenv('DISCORD_ROLE')
        GUILD = os.getenv('DISCORD_GUILD')

        self.server = None
        self.role_id: int = int(ROLE)
        self.guild_id: int = int(GUILD)

    def get_member(self, ctx):
        return self.server.get_member(ctx.user.id)

    def get_role(self):
        return self.server.get_role(self.role_id)

    def get_guild(self) -> int:
        return self.guild_id
