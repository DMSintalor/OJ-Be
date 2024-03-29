from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from sqlalchemy import or_

from OJ.models.UserModels import UserInfo, UserSession
from OJ.util.schedule import *
from OJ.db.database import get_session
from OJ.util import get_random_string

router = APIRouter(
    prefix='/api/user',
    tags=['user']
)


@router.post("/login")
async def login(form: LoginForm, db: Session = Depends(get_session)):
    user = db.query(UserInfo).filter_by(username=form.username).first()
    if not user or not user.check_password(form.password):
        return JSONResponse({
            'status': 404,
            'msg': 'Invalid Username or Password!'
        }, status_code=404)
    token = get_random_string()
    sess = db.query(UserSession).filter_by(user_id=user.id)
    if sess.first():
        sess.update({'token': token})
        db.commit()
    else:
        sess = UserSession(user_id=user.id, token=token)
        db.add(sess)
        db.commit()
    return JSONResponse({
        'msg': 'Login Successfully!',
        'token': token,
    })


@router.post("/register")
async def register(form: RegisterForm, db: Session = Depends(get_session)):
    if form.password != form.confirmPassword:
        return JSONResponse({
            'status': 404,
            'msg': '两次密码不一致'
        }, status_code=404)
    user = UserInfo(username=form.username, email=form.email)
    user.make_password(form.password)
    u = db.query(UserInfo).filter(or_(UserInfo.username == form.username, UserInfo.email == form.email)).first()
    if u:
        return JSONResponse({
            'status': 404,
            'msg': '用户已存在'
        }, status_code=404)
    try:
        db.add(user)
        db.commit()
    except Exception as e:
        return JSONResponse({
            'msg': e
        }, 404)
    return JSONResponse({
        'msg': '注册成功'
    })
