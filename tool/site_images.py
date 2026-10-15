"""Makes everything in img/ from the app's files.

    python tool/site_images.py            # all of it
    python tool/site_images.py og         # only the social previews
    python tool/site_images.py art shots  # any of the steps: art, shots, og

Needs Pillow. APP is the 8ctoMath repository, SHOTS the folder its
tool/store_shots_test.dart renders the store screenshots into, one folder
per language (the tablet ones, 2560 x 1440 PNG, are used here); run that
first. Every picture is written as webp at the size
the page lays it out at, or twice that for the small ones, so nothing is
served larger than it is shown. Files the pages stop referencing are not
removed here; grep the HTML for img/ paths and delete the strays.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

APP = r'C:\Users\r\CODING\8ctoMath2'
SHOTS = os.path.join(APP, 'build', 'store_shots')
TOOL = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(TOOL, '..', 'img')
ART = os.path.join(APP, 'assets', 'art')
FONT = os.path.join(APP, 'assets', 'fonts', 'Fredoka.ttf')


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


def export_art():
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
    stickers = {
        'clownfish': 'fish', 'seahorse': 'fish', 'manta-ray': 'fish',
        'sea-turtle': 'flippers', 'penguin': 'flippers', 'sea-otter': 'flippers',
        'rainbow-whale': 'rare', 'crab': 'shells', 'nautilus': 'shells',
        'starfish': 'shells', 'axolotl': 'squishy', 'jellyfish': 'squishy',
        'golden-turtle': 'rare', 'cuttlefish': 'squishy',
        'treasure-chest': 'things', 'abacus': 'things', 'sailboat': 'things',
        'baby-kraken': 'rare',
    }
    for name, group in stickers.items():
        export(art(f'stickers/{group}/{name}'), f'stickers/{name}.webp', width=220)

    # Sixteen of the forty faces, and a few hats, things and backdrops.
    creatures = [
        'octo', 'clownfish', 'seahorse', 'turtle', 'crab', 'jellyfish', 'otter',
        'axolotl', 'golden-turtle', 'rainbow-whale', 'baby-kraken', 'mermaid',
        'starry-narwhal', 'jellyfish-king', 'magic-conch', 'sea-angel',
    ]
    for name in creatures:
        export(art(f'avatar/creature/{name}'), f'creatures/{name}.webp', width=200)
    parts = {
        'hat': ['pirate', 'crown', 'wizard', 'party'],
        'item': ['lantern', 'pet-fish', 'treasure'],
        'backdrop': ['reef', 'shipwreck', 'sunset'],
    }
    for slot, names in parts.items():
        for name in names:
            export(art(f'avatar/{slot}/{name}'), f'avatar/{slot}-{name}.webp', height=160)

    # The app's button icons the page uses beside its tiles.
    icons = [
        'op_plus', 'op_minus', 'op_times', 'op_divide', 'op_big_times', 'shop',
        'collection', 'group_rare', 'gift', 'dice', 'crown', 'trophy', 'voices',
        'music_on', 'calm', 'pages', 'children', 'lock', 'pencil',
        'star', 'settings', 'progress', 'reminder', 'sync',
    ]
    for name in icons:
        export(art(f'icon_{name}'), f'icons/{name}.webp', height=128)


def export_shots():
    # The screens: the Play screenshots, at 1600 px, the English ones in
    # shots/ for the English pages and every other language's in
    # shots/<lang>/ for the pages under <lang>/.
    screens = {
        '2_quiz': 'quiz', '3_results': 'results', '5_page': 'page',
        '1_menu': 'menu', '6_avatar': 'avatar', '7_shop': 'shop',
        '8_parents': 'parents', '9_progress': 'progress',
    }
    for lang, folder in [('en', 'shots'), ('de', 'shots/de'),
                         ('es', 'shots/es'), ('fr', 'shots/fr')]:
        for src, dst in screens.items():
            export(os.path.join(SHOTS, lang, f'tablet_{src}.png'),
                   f'{folder}/shot-{dst}.webp', width=1600, q=80)


# The social previews. tool/og_base.png is the 1200 x 630 picture with the
# name and the sun-yellow bar but no tagline; each language's tagline, the
# home page's headline, goes on it in two lines. Each line has to stay
# clear of 8cto, so no wider than about 510 px.
OG_TAGLINES = {
    'og.png': ('Mental maths that adapts', 'to your child'),
    'og-de.png': ('Kopfrechnen, das sich', 'deinem Kind anpasst'),
    'og-es.png': ('Cálculo mental que se', 'adapta a tu hijo'),
    'og-fr.png': ('Le calcul mental qui', 's\u2019adapte à votre enfant'),
}
OG_LINES = [(81, 342), (81, 399)]
OG_MAX_WIDTH = 510


def export_og():
    font = ImageFont.truetype(FONT, 42)
    font.set_variation_by_axes([500, 100])   # wght 500, wdth 100
    for name, lines in OG_TAGLINES.items():
        im = Image.open(os.path.join(TOOL, 'og_base.png')).convert('RGB')
        draw = ImageDraw.Draw(im)
        for xy, line in zip(OG_LINES, lines):
            width = font.getlength(line)
            assert width <= OG_MAX_WIDTH, f'{name}: "{line}" is {width:.0f} px wide'
            draw.text(xy, line, font=font, fill='#8BE3EE')
        dst = os.path.join(SITE, name)
        im.save(dst, optimize=True)
        print(f'{name}: {im.size[0]}x{im.size[1]} {os.path.getsize(dst) // 1024} KB')


STEPS = {'art': export_art, 'shots': export_shots, 'og': export_og}

if __name__ == '__main__':
    names = sys.argv[1:] or list(STEPS)
    unknown = [n for n in names if n not in STEPS]
    if unknown:
        sys.exit(f'unknown step {", ".join(unknown)}; the steps are {", ".join(STEPS)}')
    for n in names:
        STEPS[n]()
