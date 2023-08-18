from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import session
from fastapi.responses import RedirectResponse,JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import models

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static/css", StaticFiles(directory="/Users/AVITA/Desktop/FastAPI_practice/templates/static/css"), name="static")

def get_db():
    db=None
    try:
        db = session()
        yield db
    finally:
        db.close()

@app.get('/')
def base(request: Request):
    return templates.TemplateResponse('base.html', context={'request': request})

@app.get('/home')
def home(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request})

@app.post('/post_form')
def postdata(request:Request, db:Session=Depends(get_db), name:str=Form(...), email:str=Form(...), age:str=Form(...), gender:str=Form(...), dob:str=Form(...)):
    users_data = db.query(models.User).filter(models.User.name!="NULL").all()
    # print(users_data)
    id = len(users_data)+1
    find = db.query(models.User).filter(models.User.email == email).first()
    if find is None:
        body = models.User(id=id,name=name,email=email,age=age,gender=gender,dob=dob)
        db.add(body)
        db.commit()
        return RedirectResponse("/", status_code=303)   
    else:
        return {"message":"user already exist"}
    
# @app.get("/users_api")
# def userapi(request:Request,db:Session=Depends(get_db)):
#     users_data = db.query(models.User).filter(models.User.name!="NULL").all()
#     userList = []
#     for i in users_data:
#         userList.append({"name":i.name,"email":i.email,"age":i.age,"gender":i.gender,"dob":i.dob})
#     print(userList)
#     json_response = jsonable_encoder(userList)
#     return JSONResponse(json_response)


@app.get('/get_users')
def users(request:Request,db:Session=Depends(get_db)):
    users_data = db.query(models.User).filter(models.User.name!="NULL").all()
    print(users_data)
    return templates.TemplateResponse('user.html',context={'request':request,'users':users_data})

@app.put("/put_data/{user}")
def get_form(user:str,request:Request,db:Session = Depends(get_db)):
    body=db.query(models.User).filter(models.User.name==user).first()
    json_compatible_item_data = jsonable_encoder(body)
    return JSONResponse(content=json_compatible_item_data)




