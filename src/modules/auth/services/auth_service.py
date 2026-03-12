import bcrypt
from fastapi import HTTPException
from src.modules.users.services.users_service import user_repository
from src.shared.utils.jwt_utils import generate_token

async def login_user_service(email: str, password: str):
    user = await user_repository.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=401, detail="INVALID CREDENTIALS")
    result = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
    print("THE RESULT: ", result)
    if not result:
        print("INVALID CREDENTIALS")
        raise HTTPException(status_code=401, detail="INVALID CREDENTIALS")
    token = await generate_token(user)
    data = {
        "user_id": user.user_id,
        "user_role": user.role_id,
        "user_email": user.email,
        "user_phone": user.phone,
        "access_token": token
    }
    return data