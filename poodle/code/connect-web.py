import ssl
import urllib.request

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv3)

# SSLv3 is no longer supported
# ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)

# alternatively, for this particular website:
ctx.set_ciphers('DES-CBC3-SHA')
# ctx.set_ciphers('SSLv3')

with urllib.request.urlopen('https://web-server/', context=ctx) as u:
    print(u.read())

# with urllib.request.urlopen('https://127.0.0.1/', context=ctx) as u:
#     print(u.read())