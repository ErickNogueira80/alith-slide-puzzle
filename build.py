"""Gera o jogo a partir de src/:
- alith-puzzle.html : arquivo único para abrir direto no navegador
- app/              : versão PWA (instalável quando servida por HTTPS)
"""
import base64, io, json, pathlib
from PIL import Image

root = pathlib.Path(__file__).parent
VERSION = "1.1.0"

img = Image.open(root / "src" / "alith.png").convert("RGB")
buf = io.BytesIO()
img.save(buf, "JPEG", quality=90, optimize=True, progressive=True)
data = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
tpl = (root / "src" / "template.html").read_text(encoding="utf-8").replace("__IMG__", data)

# 1) arquivo único
(root / "alith-puzzle.html").write_text(
    tpl.replace("__PWA_HEAD__", "").replace("__PWA_SW__", ""), encoding="utf-8")

# 2) PWA
app = root / "app"; (app / "icons").mkdir(parents=True, exist_ok=True)
BG = (11, 7, 16)
face = img.crop((195, 95, 575, 475))          # rosto e chifres
for size in (192, 512):
    face.resize((size, size), Image.LANCZOS).save(app / "icons" / f"icon-{size}.png")
face.resize((180, 180), Image.LANCZOS).save(app / "icons" / "apple-touch-icon.png")
m = Image.new("RGB", (512, 512), BG)           # maskable: margem de segurança
m.paste(face.resize((410, 410), Image.LANCZOS), (51, 51))
m.save(app / "icons" / "icon-maskable-512.png")

head = """<meta name="theme-color" content="#0b0710">
<meta name="robots" content="noindex, nofollow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Alith">"""
sw_reg = """if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
  navigator.serviceWorker.register('sw.js').catch(()=>{});
}"""
(app / "index.html").write_text(
    tpl.replace("__PWA_HEAD__", head).replace("__PWA_SW__", sw_reg), encoding="utf-8")

manifest = {
    "name": "Alith Yngvirld",
    "short_name": "Alith",
    "description": "Slide puzzle 18+ da paladina Alith Yngvirld",
    "lang": "pt-BR",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#0b0710",
    "theme_color": "#0b0710",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
(app / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

sw = f"""const CACHE = 'alith-{VERSION}';
const FILES = ['./', 'index.html', 'manifest.webmanifest',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png'];
self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request).then(r => {{
      if (r.ok && new URL(e.request.url).origin === location.origin) {{
        const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy));
      }}
      return r;
    }}).catch(() => caches.match(e.request).then(r => r || caches.match('index.html')))
  );
}});
"""
(app / "sw.js").write_text(sw, encoding="utf-8")
print("ok:", sorted(str(p.relative_to(root)) for p in app.rglob("*") if p.is_file()))
