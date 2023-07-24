from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db

from servis import user as UserServise
from dto import user as UserDTO

router = APIRouter()

@router.post('/',tags=['user'])
async def create(data:UserDTO.User= None,db:Session = Depends(get_db)):
    return UserServise.creat_user(data,db)

@router.get('/{id}',tags=['user'])
async def get(id:int = None,db:Session= Depends(get_db)):
    return UserServise.get_user(id,db)

@router.put('/{id}',tags=['user'])
async def put(id:int = None,data:UserDTO.User = None,db:Session = Depends(get_db)):
    return UserServise.updata(data,db,id)

@router.delete('/{id}',tags=['user'])
async def delete(id:int = None,db:Session = Depends(get_db)):
    return UserServise.remove(db,id)
