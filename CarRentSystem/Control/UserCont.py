from DAL.UserDAO import SysUser
from passlib.context import CryptContext

class UserService():
    def add_user(self,Name, Address,Email,RoleID,PasswordHash,Phone):

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
        hashed_password = pwd_context.hash(PasswordHash);
        user = SysUser();
        user.add_user(Name, Address,Email,RoleID,hashed_password,Phone);
    
    def user_exists(self, Email):
        user_dao = SysUser()
        return user_dao.check_user_exists(Email)
