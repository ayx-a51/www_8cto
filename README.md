# www_8cto

The site at **[8cto.net](https://8cto.net)** — the home page for *8ctoMath*,
plus the two legal pages the Google Play listing links to, in English and,
under `de/`, `es/` and `fr/`, in German, Spanish and French.

Static files served by GitHub Pages from `main`. No build step: what is in the
repository is what is served.

## Layout

| path                 | what it is                                            |
|----------------------|-------------------------------------------------------|
| `index.html`         | the landing page; its CSS is inline, in one `<style>` |
| `privacy.html`       | privacy policy — the app's `kPrivacyUrl` target       |
| `data_deletion.html` | data deletion policy                                  |
| `de/`                | the same three pages in German: `index.html`, `datenschutz.html`, `datenloeschung.html` |
| `es/`                | in Spanish: `index.html`, `privacidad.html`, `eliminacion-de-datos.html` |
| `fr/`                | in French: `index.html`, `confidentialite.html`, `suppression-des-donnees.html` |
| `legal.css`          | shared by all the legal pages, so they cannot drift   |
| `sitemap.xml`, `robots.txt` | every page in all four languages, for search engines |
| `404.html`           | GitHub Pages serves this for every unknown path, in every folder |
| `fonts/`             | Fredoka, self-hosted                                  |
| `img/`               | art and screens from the app, resized for the web     |
| `tool/site_images.py`| makes everything in `img/` from the app's files       |
| `tool/og_base.png`   | the social preview without a tagline, for the `og` step |
| `CNAME`              | `8cto.net`, the Pages custom domain                   |
| `.nojekyll`          | serve the files as they are, no Jekyll pass           |

The privacy pages' addresses are in the app too (`privacyUrlFor` in
`lib/app/version.dart`), so they keep their names.

`404.html` is one file for every missing path, under `de/`, `es/` and `fr/`
too, so every path in it starts at the root (`/img/…`, `/fonts/…`). A few
lines of script give it the language of the folder the visitor was in:
title, heading, text and the way back to that language's home page. The
English markup is for everywhere else.

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
  icons), resized and re-encoded as webp, shared by every language;
- `img/shots/` (English), `img/shots/de/`, `img/shots/es/` and
  `img/shots/fr/` are the Play listing's tablet screenshots, rendered by the
  app's `tool/store_shots_test.dart` into its `build/store_shots/<lang>/`
  (run that first), scaled to 1600 px. They are real screens of the app with
  8ctoMath+ on.

The script wants Pillow (`python -m pip install pillow`) and the paths at
its top. `python tool/site_images.py` remakes everything; name steps to run
only some of it: `art` (the app's art), `shots` (the screenshots, all four
languages) and `og` (the social previews), e.g.
`python tool/site_images.py og`. Then delete anything in `img/` the pages no
longer reference; the pages reference every file by name, so a grep finds
the strays.

`img/og.png` is the social preview, and `img/og-de.png`, `img/og-es.png` and
`img/og-fr.png` are its twins, each named by its home page's `og:image`. The
`og` step writes all four: `tool/og_base.png` (the picture with the name and
no tagline) with the home page's headline as the tagline, in Fredoka 500 at
42 px, `#8BE3EE`, on two lines from (81, 342) and (81, 399). It refuses a
line wider than 510 px, which would run into 8cto.

| file        | line 1                     | line 2                   |
|-------------|----------------------------|--------------------------|
| `og.png`    | Mental maths that adapts   | to your child            |
| `og-de.png` | Kopfrechnen, das sich      | deinem Kind anpasst      |
| `og-es.png` | Cálculo mental que se      | adapta a tu hijo         |
| `og-fr.png` | Le calcul mental qui       | s’adapte à votre enfant  |

`og.png` and `og-de.png` were first made by hand; the step reproduces them.

## Keeping the page true

The home page describes the game as it is, not as planned. When the app
changes what it does — rewards, limits, what 8ctoMath+ holds, what the free
version holds back — change the page too, and re-render the screenshots if a
screen it shows has changed. The app's `store/play_listing.md` carries the
same claims for Google Play, so the two should agree.

The word "sum" means addition only. The app practises adding, taking away,
times tables, sharing and big times, so the copy says "calculation" or
"question" for the general case. The same goes for "suma" and "somme".

Nowhere "underwater", "unter Wasser", "bajo el agua" or "sous l'eau": they
also mean swamped. The game is set on the seabed (Meeresgrund, fondo del
mar, fond de la mer), and it adapts to your child.

## Four languages

Every page has a twin in each language, German under `de/`, Spanish under
`es/` and French under `fr/`, and a change to one goes into all four. The
file names are in the page's own language (see the layout above). The pages
share the art; each language has its own screenshots (`img/shots/<lang>/`)
and social preview (`img/og-<lang>.png`), English's without the language
(`img/shots/`, `img/og.png`).

Each language follows the app's own words for it (`lib/l10n/app_<lang>.arb`
in the app repository: `app_de.arb`, `app_es.arb`, `app_fr.arb`), the app's
names for things included:

- German: Swiss spelling with "ss", never "ß"; "du" throughout; Plus, Minus,
  Einmaleins, Geteilt, Grosses Mal, Abgleich, Gefahrenzone, Elternbereich.
- Spanish: neutral, for Spain and Latin America alike; "tú" to the parent.
- French: "vous" to the parent; a no-break space (`&nbsp;`, U+00A0, never the
  narrow U+202F) before ; : ! ? and inside « ».

Each page links its twins in three places:

- `<head>`: `rel="alternate"` with `hreflang` for en, de, es and fr, at their
  absolute `https://8cto.net/` addresses, and `x-default` on the English
  page. The home pages also have `og:locale` (en_GB, de_CH, es_ES, fr_FR)
  with the other three as `og:locale:alternate`, and all four in the
  JSON-LD `inLanguage`, the page's own first.
- The language switcher in the header, right before the store pill:
  `<details class="lang">` on the home pages, `<details class="toplink
  lang">` on the legal ones. Its `<summary>` shows the page's language in
  two letters with a chevron, labelled "Language: English", "Sprache:
  Deutsch", "Idioma: español" or "Langue&nbsp;: français", and opens a list
  of the four by their own names, each a link to the same page's twin with
  `hreflang` and `lang`; the page's own is a ticked
  `<span aria-current="page">`, not a link. It works without script; the
  few lines at the end of each page only close it on a click elsewhere, on
  Escape, and on a return through the back button. At 380 px and below it
  goes, and the footer carries the languages. Its CSS is inline and the same
  in every `index.html`, and in `legal.css` for the legal pages.
- The footer: a link to each other language, named in that language, in the
  order English, Deutsch, Español, Français.

A new page or a new language goes into all three places on every twin, and
into `sitemap.xml`.

## Google Play

Every store link goes to
`https://play.google.com/store/apps/details?id=io.a51.octomath`: in
`index.html` the header pill, the hero button, the closing call and the
JSON-LD block in `<head>` (`downloadUrl`, `sameAs`); on both legal pages the
header pill beside "Home"; the same places in every language. The page
speaks of the app as out on Play, so keep any new copy in that tense.
