import segno

# Contenuto del QR
data = "https://example.com"

# Crea il QR
qr = segno.make(data, error='h')

# Salva in SVG con moduli arrotondati
qr.save(
    "qrcode.svg",
    scale=10,
    # rounded=0.25,   # 0 = squadrato, 1 = cerchi perfetti
    border=4
)