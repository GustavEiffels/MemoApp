from pydantic import BaseModel

from app.domain.member.member import Member


class MemberCreate(BaseModel):
    email: str
    nick: str
    password: str

    def to_domain(self,password:str) -> Member:
        return Member(email=self.email, nick=self.nick, password_hash=password)
