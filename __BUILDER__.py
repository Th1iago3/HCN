from .__ENCRYPTION__ import Encryption
import re

class Builder:
    def __init__(self):
        self.enc = Encryption()

    def build(self, path):
        with open(path, "rb") as f:
            raw = f.read()

        title = self._title(raw)
        payload = self.enc.encrypt(raw)
        key = self.enc.pack()

        return (
            '<!DOCTYPE html><html><head><meta charset="utf-8"><title>' + title + '</title>'
            '<script src="https://cdn.jsdelivr.net/npm/pako@2.1.0/dist/pako.min.js"></script>'
            '<script>'
            '(function(){'
            'let K=Uint8Array.from(atob("' + key + '"),c=>c.charCodeAt(0));'
            'let P="' + payload + '";'
            'let B=Uint8Array.from(atob(P),c=>c.charCodeAt(0));'
            'for(let i=0;i<B.length;i++)B[i]^=K[i%K.length];'
            'let D=new TextDecoder().decode(pako.inflate(B));'
            'if(navigator.webdriver||/Headless|Phantom|Playwright|Puppeteer/i.test(navigator.userAgent)){document.documentElement.innerHTML="";throw 0;}'
            'let t=Date.now();debugger;if(Date.now()-t>50){document.documentElement.innerHTML="";throw 0;}'
            'let s=setInterval(function(){if(window.outerWidth-window.innerWidth>200||window.outerHeight-window.innerHeight>200){document.documentElement.innerHTML="";clearInterval(s);}},300);'
            'document.open();document.write(D);document.close();'
            'setTimeout(function(){D=null;B=null;K=null;},100);'
            '})();'
            '</script></head><body></body></html>'
        )

    def _title(self, html):
        try:
            m = re.search(br"<title>(.*?)</title>", html, re.I | re.S)
            return m.group(1).decode(errors="ignore") if m else ""
        except:
            return ""

