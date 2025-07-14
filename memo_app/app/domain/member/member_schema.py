from pydantic import BaseModel, Field

from app.domain.member.member import Member


class MemberCreate(BaseModel):
    email: str = Field(min_length=100)
    nick: str = Field(min_length=30)
    password: str = Field(min_length=8)

    def to_domain(self) -> Member:
        return Member(email=self.email, nick=self.nick, password_hash=self.password)
