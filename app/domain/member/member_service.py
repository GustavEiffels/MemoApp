from domain.member.member import Member
from domain.member.member_schema import MemberCreate
from domain.member.member_repository import MemberRepositoryInterface

class MemberService:
    def __init__(self,repository:MemberRepositoryInterface):
        self.repo = repository
    
    def create_member(self,command:MemberCreate) -> Member:
        
        existing_member = self.repo.find_by_email(command.email)

        if existing_member:
            raise ValueError(f"Email '{command.email}' already exists ")  

        
        new_member = Member(
            command.email,
            command.password
        )

        return self.repo.add(new_member)