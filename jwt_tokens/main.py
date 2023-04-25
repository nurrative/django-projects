from jwt_handlers import encodeJWT, decodeJWT, refreshJWT
import time

user = {
    'id':1,
    'username': 'Logan'
}
jwt_token = encodeJWT(user)
print(encodeJWT(jwt_token))

time.sleep(6)
decoded = decodeJWT(jwt_token['access'])
print(decoded)

new_jwt = refreshJWT(jwt_token['refresh'])
print(new_jwt)