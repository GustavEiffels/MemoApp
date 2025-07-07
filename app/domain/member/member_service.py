from typing import Optional
from domain.member.member import Member
from domain.member.member_schema import MemberCreate
from domain.member.member_repository import MemberRepositoryInterface
from domain.exceptions import ValidationError, MemberAlreadyExistsError, NotFoundMember

class MemberService:
    def __init__(self,repository:MemberRepositoryInterface):
        self.repo = repository
    
    def create_member(self,command:MemberCreate) -> Member:
        
        existing_member = self.find_by_email(command.email)

        if existing_member:
            raise MemberAlreadyExistsError(email=command.email, message=f"Email '{command.email}' already exists.")  

        
        new_member = Member(
            command.email,
            command.password
        )

        return self.repo.add(new_member)
    
    def find_by_email(self,email:str) -> Optional[Member]:
         return self.repo.find_by_email(email)


    def exist_member(self,id:int):
        
        if self.repo.find_by_id(id) is None:
            raise NotFoundMember('Not Found Member!!')
            
    