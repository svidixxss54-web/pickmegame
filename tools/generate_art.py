"""Draw the small, original pixel sprites used by the game.

All shapes are painted on a 1/2 scale canvas and enlarged with nearest-neighbor
sampling. Running this file again regenerates the PNGs in ``assets``.
"""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

INK = "#633754"
DEEP_PINK = "#9c497d"
PINK = "#f47daf"
PALE_PINK = "#ffd5e8"
CREAM = "#fff2e8"


def canvas(size):
    image = Image.new("RGBA", size, (0, 0, 0, 0))
    return image, ImageDraw.Draw(image)


def save(image, name):
    image.resize((image.width * 2, image.height * 2), Image.Resampling.NEAREST).save(ASSETS / name)


def draw_player():
    image, d = canvas((30, 38))

    # Her hair falls behind the face and the dress.
    d.polygon([(7, 10), (10, 5), (18, 4), (24, 8), (25, 15), (26, 27),
               (22, 29), (19, 25), (9, 27), (5, 29), (5, 17)], fill=INK)
    d.polygon([(8, 11), (11, 6), (18, 5), (23, 9), (24, 17), (24, 26),
               (22, 27), (19, 23), (9, 25), (7, 27), (7, 16)], fill="#cb5b91")
    d.rectangle((7, 14, 9, 25), fill=PINK)
    d.rectangle((22, 13, 24, 24), fill=PINK)

    # Boots, stockings, arms, and the flared heart dress.
    d.rectangle((10, 31, 13, 35), fill=INK)
    d.rectangle((17, 31, 20, 35), fill=INK)
    d.rectangle((11, 31, 13, 34), fill=CREAM)
    d.rectangle((17, 31, 19, 34), fill=CREAM)
    d.rectangle((9, 35, 14, 36), fill=INK)
    d.rectangle((16, 35, 21, 36), fill=INK)
    d.rectangle((10, 35, 13, 35), fill="#ee68a1")
    d.rectangle((17, 35, 20, 35), fill="#ee68a1")
    d.polygon([(8, 22), (11, 21), (19, 21), (22, 22), (24, 32),
               (21, 34), (9, 34), (6, 32)], fill=INK)
    d.polygon([(10, 23), (20, 23), (22, 31), (20, 32), (10, 32), (8, 31)], fill="#ea65a2")
    d.polygon([(11, 23), (14, 23), (12, 30), (9, 30)], fill="#ff9bc3")
    d.line([(9, 31), (21, 31)], fill="#ad4f84", width=1)
    d.polygon([(7, 23), (10, 24), (8, 28), (5, 27)], fill=INK)
    d.polygon([(6, 24), (9, 25), (7, 27), (6, 26)], fill="#ffe0d2")
    d.polygon([(20, 24), (23, 23), (25, 27), (22, 28)], fill=INK)
    d.polygon([(21, 25), (23, 24), (24, 26), (22, 27)], fill="#ffe0d2")

    # Face, rosy cheeks, and asymmetric bangs.
    d.ellipse((8, 9, 22, 24), fill=INK)
    d.ellipse((9, 10, 21, 23), fill="#ffe4d7")
    d.rectangle((11, 18, 12, 19), fill="#f4adc1")
    d.rectangle((19, 18, 20, 19), fill="#f4adc1")
    d.rectangle((12, 15, 13, 17), fill="#58435b")
    d.rectangle((18, 15, 19, 17), fill="#58435b")
    d.point((12, 15), fill="white")
    d.point((18, 15), fill="white")
    d.line((15, 20, 17, 20), fill="#c46f89")
    d.polygon([(8, 12), (9, 8), (13, 6), (19, 7), (22, 10),
               (21, 13), (17, 12), (15, 10), (13, 13), (10, 14)], fill=INK)
    d.polygon([(9, 11), (11, 8), (14, 7), (20, 8), (21, 11),
               (17, 10), (15, 8), (12, 12)], fill=PINK)
    d.line((12, 8, 16, 7), fill="#ffc6df")

    # A tiny heart clip is part of the silhouette.
    d.polygon([(19, 5), (20, 3), (22, 4), (23, 3), (25, 5),
               (23, 8), (22, 9), (20, 7)], fill=INK)
    d.polygon([(20, 5), (21, 4), (22, 5), (23, 4), (24, 5), (22, 7)], fill="#fff0f4")
    d.point((20, 5), fill="white")
    save(image, "player.png")


def draw_platform():
    image, d = canvas((40, 40))

    # Every horizontal row reaches both edges with the same color, so adjacent
    # tiles join cleanly. The lower face deliberately resembles layered cake.
    d.rectangle((0, 0, 39, 39), fill="#ab4d83")
    d.rectangle((0, 9, 39, 37), fill="#e878ac")
    d.rectangle((0, 10, 39, 11), fill="#b44e85")
    d.rectangle((0, 14, 39, 16), fill="#f596bd")
    d.rectangle((0, 17, 39, 17), fill="#c25a91")
    d.rectangle((0, 27, 39, 28), fill="#f493ba")
    d.rectangle((0, 29, 39, 29), fill="#c25a91")
    d.rectangle((0, 37, 39, 39), fill="#a94a80")

    # A strawberry frosting cap, repeated with a 40-pixel period.
    d.rectangle((0, 0, 39, 7), fill="#ffd8e9")
    d.rectangle((0, 0, 39, 1), fill="#fff3f8")
    d.rectangle((0, 7, 39, 8), fill="#a94f84")
    for x, length in ((5, 3), (13, 5), (22, 2), (31, 4)):
        d.rectangle((x, 6, x + 2, 7 + length), fill="#ffd8e9")
        d.rectangle((x, 8 + length, x + 2, 8 + length), fill="#a94f84")
    for x in (3, 19, 35):
        d.rectangle((x, 3, x + 2, 3), fill="white")
    for x, color in ((9, "#f467a4"), (26, "#fa76ae"), (34, "#ed8e42")):
        d.rectangle((x, 4, x + 1, 5), fill=color)

    # Alternating cake-brick facets; no dark border at x=0 or x=39.
    d.line((12, 18, 12, 26), fill="#ce6599", width=1)
    d.line((31, 18, 31, 26), fill="#ce6599", width=1)
    d.line((4, 30, 4, 36), fill="#ce6599", width=1)
    d.line((21, 30, 21, 36), fill="#ce6599", width=1)
    d.line((37, 30, 37, 36), fill="#ce6599", width=1)
    d.rectangle((2, 19, 7, 20), fill="#f8a9c9")
    d.rectangle((23, 22, 28, 23), fill="#f8a9c9")
    d.rectangle((9, 32, 14, 33), fill="#f8a9c9")

    # Small heart stamped in the side of each tile.
    d.polygon([(16, 22), (17, 21), (19, 22), (21, 21), (23, 22),
               (23, 24), (20, 27), (19, 28), (15, 24), (15, 22)], fill="#b9588c")
    d.polygon([(17, 22), (19, 23), (21, 22), (22, 23), (19, 26), (16, 23)], fill="#ffc0db")
    save(image, "platform.png")


def draw_heart():
    image, d = canvas((32, 32))

    # Double outline gives the pickup a readable edge on light backgrounds.
    outer = [(16, 29), (12, 26), (4, 18), (2, 13), (3, 8), (6, 5),
             (10, 4), (13, 5), (16, 8), (19, 5), (22, 4), (26, 5),
             (29, 8), (30, 13), (28, 18), (20, 26)]
    d.polygon(outer, fill=INK)
    d.polygon([(16, 27), (12, 24), (5, 17), (4, 12), (5, 9), (7, 7),
               (10, 6), (13, 7), (16, 11), (19, 7), (22, 6), (25, 7),
               (28, 10), (28, 13), (26, 17), (20, 23)], fill="#ef4e91")
    d.polygon([(6, 10), (8, 8), (11, 8), (14, 11), (14, 17), (10, 17),
               (6, 14)], fill="#ffb6d2")
    d.polygon([(17, 13), (21, 8), (24, 8), (27, 11), (25, 16),
               (19, 22), (16, 25), (11, 20)], fill="#ff79ae")
    d.rectangle((8, 9, 11, 10), fill="#fff2f7")
    d.rectangle((6, 11, 7, 13), fill="#fff2f7")
    d.line((16, 25, 20, 22), fill="#d93e82")
    d.point((24, 12), fill="#fff0f6")
    save(image, "heart.png")


def draw_enemy():
    image, d = canvas((30, 38))

    # A purple candy imp with pointed ears, wings, and little fangs.
    d.polygon([(4, 18), (1, 14), (1, 23), (5, 26), (6, 31),
               (11, 34), (19, 34), (24, 31), (25, 26), (29, 23),
               (29, 14), (26, 18), (23, 13), (24, 4), (19, 10),
               (15, 9), (11, 10), (6, 4), (7, 13)], fill="#4f315e")
    d.polygon([(5, 20), (3, 18), (3, 22), (7, 25), (8, 30),
               (12, 32), (18, 32), (22, 30), (23, 25), (27, 22),
               (27, 18), (25, 20), (21, 13), (22, 8), (18, 12),
               (12, 12), (8, 8), (9, 13)], fill="#a968b6")
    d.polygon([(8, 16), (11, 13), (19, 13), (22, 16), (23, 25),
               (20, 30), (10, 30), (7, 25)], fill="#c68ac8")
    d.rectangle((8, 26, 10, 29), fill="#dfaad8")
    d.rectangle((20, 26, 22, 29), fill="#dfaad8")
    d.rectangle((8, 33, 12, 35), fill="#4f315e")
    d.rectangle((18, 33, 22, 35), fill="#4f315e")
    d.rectangle((9, 33, 11, 33), fill="#a968b6")
    d.rectangle((19, 33, 21, 33), fill="#a968b6")

    # Slanted brows, bright eyes, and a tiny mischievous mouth.
    d.line((8, 18, 12, 19), fill="#4f315e", width=2)
    d.line((18, 19, 22, 18), fill="#4f315e", width=2)
    d.rectangle((10, 20, 12, 23), fill="#fff0cc")
    d.rectangle((18, 20, 20, 23), fill="#fff0cc")
    d.rectangle((12, 21, 12, 23), fill="#5a345d")
    d.rectangle((18, 21, 18, 23), fill="#5a345d")
    d.line((12, 26, 18, 26), fill="#6b355e", width=1)
    d.polygon([(13, 26), (15, 26), (14, 29)], fill="#fff5eb")
    d.polygon([(16, 26), (18, 26), (17, 29)], fill="#fff5eb")
    d.point((8, 23), fill="#f294be")
    d.point((21, 23), fill="#f294be")
    save(image, "enemy.png")


if __name__ == "__main__":
    draw_player()
    draw_platform()
    draw_heart()
    draw_enemy()
    print("Generated pink platformer sprites in", ASSETS)
