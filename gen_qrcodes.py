import qrcode
from qrcode.image.styledpil import StyledPilImage

from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import ImageColorMask, RadialGradiantColorMask

import psycopg
import pandas as pd
import os
import numpy as np

URL = os.environ.get("DB_EXT_URL")
# connessione tramite context manager
with psycopg.connect(URL) as conn:
    # leggi direttamente in Pandas
    query = "SELECT * FROM scribble_scribblepointinfo;"
    df = pd.read_sql(query, conn)

# print(df.head())


for id, row in df.iterrows():
    name = dict(row)['name']
    qr = qrcode.QRCode(
        version=9,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(f"https://djanloo.xyz/scribble/{row.token}")

    # factory = qrcode.image.svg.SvgPathImage
    img = qr.make_image(fit=True, image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                         color_mask=RadialGradiantColorMask(center_color=(np.random.randint(1, size=3)), edge_color=(0,0,0)),
                        #  embedded_image_path="/path/to/image.png"
                        )



    img.save(f"qrcodes/{row.token}_{name}.png")
