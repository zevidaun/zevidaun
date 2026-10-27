# Convierte el logo de AS (trazo negro sobre naranja) en arte ASCII estilo fastfetch
import sys
from PIL import Image

src, cols = sys.argv[1], int(sys.argv[2])
img = Image.open(src).convert("L")
w, h = img.size
# recorta al trazo para aprovechar todo el ancho
bbox = img.point(lambda p: 255 if p < 90 else 0).getbbox()
img = img.crop((bbox[0] - 6, bbox[1] - 6, bbox[2] + 6, bbox[3] + 6))
w, h = img.size
rows = round(cols * h / w / 2.05)  # las celdas de texto miden ~2:1
img = img.resize((cols * 4, rows * 8), Image.LANCZOS)
ramp = " .:-=+*#%@"
out = []
for r in range(rows):
    line = ""
    for c in range(cols):
        cell = img.crop((c * 4, r * 8, c * 4 + 4, r * 8 + 8))
        dark = sum(1 for p in cell.getdata() if p < 90) / 32
        line += ramp[min(len(ramp) - 1, round(dark * (len(ramp) - 1) * 1.25))]
    out.append(line.rstrip())
print("\n".join(out))
