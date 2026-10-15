# www_8cto

The site at **[8cto.net](https://8cto.net)** — the home page for *8ctoMath*,
plus the two legal pages the Google Play listing links to, in English and,
under `de/`, in German.

Static files served by GitHub Pages from `main`. No build step: what is in the
repository is what is served.

## Layout

| path                 | what it is                                            |
|----------------------|-------------------------------------------------------|
| `index.html`         | the landing page; its CSS is inline, in one `<style>` |
| `privacy.html`       | privacy policy — the app's `kPrivacyUrl` target       |
| `data_deletion.html` | data deletion policy                                  |
| `de/`                | the same three pages in German: `index.html`, `datenschutz.html`, `datenloeschung.html` |
| `legal.css`          | shared by all the legal pages, so they cannot drift   |
| `sitemap.xml`, `robots.txt` | every page in both languages, for search engines |
| `404.html`           | GitHub Pages serves this for unknown paths            |
| `fonts/`             | Fredoka, self-hosted                                  |
| `img/`               | art and screens from the app, resized for the web     |
| `tool/site_images.py`| makes everything in `img/` from the app's files       |
| `CNAME`              | `8cto.net`, the Pages custom domain                   |
| `.nojekyll`          | serve the files as they are, no Jekyll pass           |

## Where things come from

Colour and type are the app's own design system: the `Sea` palette from
`lib/ui/theme.dart` in the 8ctoMath repository, copied verbatim, and the
Fredoka variable font the app bundles (`assets/fonts/Fredoka.ttf`), converted
to woff2. Fredoka is self-hosted rather than loaded from Google's CDN so that
rendering a privacy page does not hand a third party the reader's IP address.

Every picture is from the game, and `tool/site_images.py` remakes all of them:

- `img/*.webp`, `img/stickers/`, `img/creatures/`, `img/avatar/`, `img/icons/`
  are the app's own art (`assets/art/` in the app repository: characters,
  reward props, stickers, sticker-book pages, avatar parts and the button
  icons), resized and re-encoded as webp;
- `img/shots/` (English) and `img/shots/de/` (German) are the Play listing's
  tablet screenshots, rendered by the app's `tool/store_shots_test.dart` into
  its `build/store_shots/<lang>/` (run that first), scaled to 1600 px. They
  are real screens of the app with 8ctoMath+ on.

The script wants Pillow (`python -m pip install pillow`) and the two paths at
its top. Run it, then delete anything in `img/` the pages no longer
reference; the pages reference every file by name, so a grep finds the
strays.

`img/og.png` is the social preview, made once by hand from the same art,
and `img/og-de.png` its German twin. Their tagline is the page's headline,
"Mental maths that adapts to your child" / "Kopfrechnen, das sich deinem
Kind anpasst", in Fredoka 500 at 42 px, `#8BE3EE`, on two lines from x 81.
Not "underwater" or "unter Wasser": both also mean swamped.

## Keeping the page true

The home page describes the game as it is, not as planned. When the app
changes what it does — rewards, limits, what 8ctoMath+ holds, what the free
version holds back — change the page too, and re-render the screenshots if a
screen it shows has changed. The app's `store/play_listing.md` carries the
same claims for Google Play, so the two should agree.

Every page has a German twin under `de/`, and a change to one goes into
both. The German follows the app's own (`lib/l10n/app_de.arb`): Swiss
spelling with "ss", never "ß"; "du" throughout; the app's names for things
(Plus, Minus, Einmaleins, Geteilt, Grosses Mal, Abgleich, Gefahrenzone,
Elternbereich). Each page links its twin with `hreflang` in `<head>`, the
two-letter pill in the header and a link in the footer.

The word "sum" means addition only. The app practises adding, taking away,
times tables, sharing and big times, so the copy says "calculation" or
"question" for the general case.

## Google Play

Every store link goes to
`https://play.google.com/store/apps/details?id=io.a51.octomath`: in
`index.html` the header pill, the hero button, the closing call and the
JSON-LD block in `<head>` (`downloadUrl`, `sameAs`); on both legal pages the
header pill beside "Home"; the same places on the German pages. The page
speaks of the app as out on Play, so keep any new copy in that tense.
