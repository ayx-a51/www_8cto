"""Makes everything in img/ from the app's files.

    python tool/site_images.py

Needs Pillow. APP is the 8ctoMath repository, SHOTS the folder holding the
tablet screenshots that the app's tool/store_shots_test.dart renders (Play's
upload copies, 2560 x 1440 PNG). Every picture is written as webp at the size
the page lays it out at, or twice that for the small ones, so nothing is
served larger than it is shown. Files the pages stop referencing are not
removed here; grep the HTML for img/ paths and delete the strays.
"""

import os
from PIL import Image

APP = r'C:\Users\r\CODING\8ctoMath2'
SHOTS = r'C:\Users\r\Downloads\8cto\play\tablet'
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'img')
ART = os.path.join(APP, 'assets', 'art')


def export(src, dst, width=None, height=None, q=85):
    """Scales src down to width or height (never up) and writes it as webp."""
    im = Image.open(src)
    w, h = im.size
    if width and w > width:
        im = im.resize((width, round(h * width / w)), Image.LANCZOS)
    elif height and h > height:
        im = im.resize((round(w * height / h), height), Image.LANCZOS)
    dst = os.path.join(SITE, dst)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if im.mode == 'RGBA' and im.getextrema()[3] == (255, 255):
        im = im.convert('RGB')
    im.save(dst, 'WEBP', quality=q, method=6)
    print(f'{os.path.relpath(dst, SITE)}: {im.size[0]}x{im.size[1]} '
          f'{os.path.getsize(dst) // 1024} KB')


def art(name):
    return os.path.join(ART, name + '.webp')


# Characters and props.
export(art('mascot_happy'), '8cto-happy.webp', width=640)
export(art('mascot_finished'), '8cto-finished.webp', width=560)
export(art('mascot_thinking'), '8cto-thinking.webp', width=520)   # 404.html
export(art('mascot_encouraging'), '8cto-cheer.webp', width=640)
export(art('brainy_moving'), 'brainy-swim.webp', width=420)
export(art('avatar/racer/turtle'), 'racer-turtle.webp', width=420)
export(art('starfish_lit'), 'starfish.webp', width=260)
export(art('pearl'), 'pearl.webp', width=260)
export(art('sticker_pack'), 'pack.webp', width=300)

# The eight pages of the sticker book.
for page in ['reef', 'wreck', 'village', 'kelp', 'deep', 'lagoon', 'open', 'ice']:
    export(art(f'page_{page}'), f'page-{page}.webp', width=1000, q=78)

# Eighteen of the two hundred stickers.
STICKERS = {
    'clownfish': 'fish', 'seahorse': 'fish', 'manta-ray': 'fish',
    'sea-turtle': 'flippers', 'penguin': 'flippers', 'sea-otter': 'flippers',
    'rainbow-whale': 'rare', 'crab': 'shells', 'nautilus': 'shells',
    'starfish': 'shells', 'axolotl': 'squishy', 'jellyfish': 'squishy',
    'golden-turtle': 'rare', 'cuttlefish': 'squishy',
    'treasure-chest': 'things', 'abacus': 'things', 'sailboat': 'things',
    'baby-kraken': 'rare',
}
for name, group in STICKERS.items():
    export(art(f'stickers/{group}/{name}'), f'stickers/{name}.webp', width=220)

# Sixteen of the forty faces, and a few hats, things and backdrops.
CREATURES = [
    'octo', 'clownfish', 'seahorse', 'turtle', 'crab', 'jellyfish', 'otter',
    'axolotl', 'golden-turtle', 'rainbow-whale', 'baby-kraken', 'mermaid',
    'starry-narwhal', 'jellyfish-king', 'magic-conch', 'sea-angel',
]
for name in CREATURES:
    export(art(f'avatar/creature/{name}'), f'creatures/{name}.webp', width=200)
PARTS = {
    'hat': ['pirate', 'crown', 'wizard', 'party'],
    'item': ['lantern', 'pet-fish', 'treasure'],
    'backdrop': ['reef', 'shipwreck', 'sunset'],
}
for slot, names in PARTS.items():
    for name in names:
        export(art(f'avatar/{slot}/{name}'), f'avatar/{slot}-{name}.webp', height=160)

# The app's button icons the page uses beside its tiles.
ICONS = [
    'op_plus', 'op_minus', 'op_times', 'op_divide', 'op_big_times', 'shop',
    'collection', 'group_rare', 'gift', 'dice', 'crown', 'trophy', 'voices',
    'music_on', 'calm', 'pages', 'children', 'lock', 'levels', 'pencil',
    'star', 'settings',
]
for name in ICONS:
    export(art(f'icon_{name}'), f'icons/{name}.webp', height=128)

# The screens: the Play screenshots, at 1600 px.
SCREENS = {
    '01_quiz': 'quiz', '02_results': 'results', '03_sticker_page': 'page',
    '04_menu': 'menu', '06_avatar': 'avatar', '07_shop': 'shop',
    '08_parents': 'parents',
}
for src, dst in SCREENS.items():
    export(os.path.join(SHOTS, f'{src}.png'), f'shots/shot-{dst}.webp', width=1600, q=80)
