"""Draw the heart-shaped finish portal for Heart Hop.

Like the other sprites, it is drawn at half size and scaled without smoothing.
Running this script only regenerates ``assets/finish.png``.
"""

from pathlib import Path

from PIL import Image, ImageDraw


ASSET = Path(__file__).resolve().parent.parent / "assets" / "finish.png"
INK = "#633754"
FRAME = "#d85d9c"
LIGHT = "#ffd5e8"
CREAM = "#fff2e8"


def draw_finish():
    image = Image.new("RGBA", (56, 72), (0, 0, 0, 0))
    d = ImageDraw.Draw(image)

    # The little shadow and feet anchor the doorway to the platform.
    d.polygon([(5, 65), (12, 62), (44, 62), (51, 65), (53, 69), (3, 69)], fill=INK)
    d.rectangle((5, 66, 51, 68), fill="#ad4f84")
    d.rectangle((8, 64, 48, 65), fill=LIGHT)
    d.rectangle((10, 68, 16, 69), fill="#f49ac2")
    d.rectangle((40, 68, 46, 69), fill="#f49ac2")

    # A wide, rounded frame reads clearly even when the camera is moving.
    d.polygon(
        [(7, 64), (7, 28), (8, 22), (11, 16), (16, 11), (22, 8),
         (34, 8), (40, 11), (45, 16), (48, 22), (49, 28), (49, 64)],
        fill=INK,
    )
    d.polygon(
        [(9, 63), (9, 28), (10, 22), (13, 17), (18, 13), (23, 11),
         (33, 11), (38, 13), (43, 17), (46, 22), (47, 28), (47, 63)],
        fill=FRAME,
    )
    d.polygon(
        [(11, 60), (11, 28), (12, 23), (15, 19), (19, 15), (24, 13),
         (32, 13), (37, 15), (41, 19), (44, 23), (45, 28), (45, 60)],
        fill="#ffacd0",
    )

    # Dark inner edge, with a soft magical glow in the open doorway.
    opening = [(14, 61), (14, 28), (16, 23), (20, 19), (25, 17),
               (31, 17), (36, 19), (40, 23), (42, 28), (42, 61)]
    d.polygon(opening, fill=INK)
    d.polygon(
        [(17, 60), (17, 29), (19, 25), (22, 22), (26, 20),
         (30, 20), (34, 22), (37, 25), (39, 29), (39, 60)],
        fill="#a46aa9",
    )
    d.polygon(
        [(19, 59), (19, 30), (21, 26), (24, 24), (27, 23),
         (30, 23), (33, 25), (36, 29), (37, 59)],
        fill="#e8acda",
    )
    d.polygon(
        [(23, 58), (23, 29), (26, 26), (29, 25), (32, 27),
         (34, 30), (34, 58)],
        fill="#ffe2ef",
    )
    d.rectangle((25, 34, 29, 54), fill="#fff0f6")
    d.rectangle((25, 55, 34, 59), fill="#ffd9eb")

    # Frosting-like trim connects the portal to the candy platforms.
    d.rectangle((6, 60, 16, 64), fill=INK)
    d.rectangle((40, 60, 50, 64), fill=INK)
    d.rectangle((8, 61, 16, 62), fill=CREAM)
    d.rectangle((40, 61, 48, 62), fill=CREAM)
    d.rectangle((9, 24, 11, 49), fill=CREAM)
    d.rectangle((45, 24, 47, 49), fill=CREAM)
    for y in (29, 40, 51):
        d.rectangle((9, y, 11, y + 1), fill="#f186b6")
        d.rectangle((45, y, 47, y + 1), fill="#f186b6")

    # The crown heart is the landmark visible from a distance.
    d.polygon(
        [(28, 19), (22, 15), (17, 9), (17, 5), (20, 2), (24, 2),
         (28, 5), (32, 2), (36, 2), (39, 5), (39, 9), (34, 15)],
        fill=INK,
    )
    d.polygon(
        [(28, 16), (22, 12), (19, 8), (19, 5), (22, 4),
         (25, 4), (28, 7), (31, 4), (34, 4), (37, 6),
         (37, 9), (33, 13)],
        fill="#f3579b",
    )
    d.polygon([(20, 6), (22, 4), (25, 5), (27, 8), (26, 10),
               (22, 9), (20, 8)], fill="#ffb8d4")
    d.rectangle((21, 5, 24, 5), fill=CREAM)

    # A few simple star pixels suggest that the destination is active.
    for x, y in ((24, 38), (34, 43), (28, 50)):
        d.line((x - 2, y, x + 2, y), fill=CREAM)
        d.line((x, y - 2, x, y + 2), fill=CREAM)
    for x, y in ((3, 23), (53, 34), (3, 48)):
        d.line((x - 1, y, x + 1, y), fill="#fff5f9")
        d.line((x, y - 1, x, y + 1), fill="#fff5f9")

    ASSET.parent.mkdir(exist_ok=True)
    image.resize((112, 144), Image.Resampling.NEAREST).save(ASSET)
    print("Created", ASSET)


if __name__ == "__main__":
    draw_finish()
