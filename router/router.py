from fastapi import APIRouter, status
from schemas.contact_schema import ContactSchema
from config.db import engine
from model.comment import comment

user= APIRouter()



@user.get(
    path='/',
    tags=['HOME'],
    status_code=status.HTTP_200_OK,
    summary='App home page'
    )
def home():
    return {'Welcome to':'MY API'}

@user.post(
    path='/api/contact',
    tags=['Contact'],
    status_code=status.HTTP_201_CREATED,
    summary='Create a contact in the app and save in the database'
    )
def Contact(data_contact: ContactSchema):
    with engine.connect() as conn:
        new_contact = data_contact.dict()
        conn.execute(comment.insert().values(new_contact))
        #return 'new_contact'

# @user.get('/api/showContact')
# def ShowContact():
#     with engine.connect() as conn:
#         result= conn.execute(comment.select()).fetchall()
#         return result