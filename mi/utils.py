import hashlib
import hmac
import base64
import config

def generate_sign(message, secret):
    secret = base64.b64decode(secret)
    message = message.encode('utf8')
    val = hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()
    return val

def get_post_authorization(headers):
    message='%s\n%s\n\n%s\n%s\n%s\n%s\n'%(
        headers.environ.get('REQUEST_METHOD',''),
        headers.environ.get('PATH_INFO',''),
        headers.get('X-Xiaomi-Date',''),
        headers.get('HOST',''),
        headers.get('CONTENT_TYPE', ''),
        headers.get('CONTENT_MD5','')
    )
    sign = generate_sign(message, config.MI_SECRET)
    return 'MIAI-HmacSHA256-V1 %s::%s' % (config.MI_KEY_ID, sign)

def validate(headers):
    auth=headers.get('Authorization','')
    if get_post_authorization(headers) == auth:
        return True
    else:
        return False
