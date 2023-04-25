import time
import jwt


SECRET_KEY = '1243bioqo943!#1b<>?_)(R-`\/%!!90345'
ALGO = 'HS256'
ACCESS_TOKEN_EXPIRE = 5 #5 секунд
REFRESH_TOKEN_EXPIRE = 30 

def encodeJWT(data):
    payload_access = {
        'data': data,
        'expiry': time.time()+ACCESS_TOKEN_EXPIRE
    }
    payload_refresh = {
        'data': data,
        'expiry': time.time()+REFRESH_TOKEN_EXPIRE
    }
    access_token = jwt.encode(payload_access,SECRET_KEY,algorithm=ALGO)
    refresh_token = jwt.encode(payload_refresh,SECRET_KEY,algorithm=ALGO)

    return {'access': access_token, 'refresh': refresh_token}


def  decodeJWT(token:str):
    try:
        decoded = jwt.decode(token, SECRET_KEY,algorithms=[ALGO])
        if decoded['expiry']>=time.time():
            # если еще не истек срок
            return decoded
        return {'token': 'token is invalid!'}
    except:
        return {'error': 'не верные данные'}
    
def refreshJWT(refresh:str):
    decoded = decodeJWT(refresh)
    if decoded:
        return encodeJWT(decoded['data'])
    return {'error': 'invalid data!'}
        