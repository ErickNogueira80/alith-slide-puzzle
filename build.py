"""Gera alith-puzzle.html embutindo src/alith.png (convertida para JPEG) no template."""
import base64, io, pathlib
from PIL import Image

root = pathlib.Path(__file__).parent
img = Image.open(root / "src" / "alith.png").convert("RGB")
buf = io.BytesIO()
img.save(buf, "JPEG", quality=90, optimize=True, progressive=True)
data = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
html = (root / "src" / "template.html").read_text(encoding="utf-8").replace("__IMG__", data)
(root / "alith-puzzle.html").write_text(html, encoding="utf-8")
print(f"ok: {len(html)/1024:.0f} KB")
