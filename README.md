# www_8cto

The site at **[8cto.net](https://8cto.net)** — the home page for *8ctoMath*,
plus the two legal pages the Google Play listing links to.

Static files served by GitHub Pages from `main`. No build step: what is in the
repository is what is served.

## Layout

| path                 | what it is                                            |
|----------------------|-------------------------------------------------------|
| `index.html`         | the landing page; its CSS is inline, in one `<style>` |
| `privacy.html`       | privacy policy — the app's `kPrivacyUrl` target       |
| `data_deletion.html` | data deletion policy                                  |
| `legal.css`          | shared by both legal pages, so they cannot drift      |
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
- `img/shots/` are the Play listing's tablet screenshots, rendered by the
  app's `tool/store_shots_test.dart` and kept in `Downloads/8cto/play/tablet`,
  scaled to 1600 px. They are real screens of the app with 8ctoMath+ on.

The script wants Pillow (`python -m pip install pillow`) and the two paths at
its top. Run it, then delete anything in `img/` the pages no longer
reference; the pages reference every file by name, so a grep finds the
strays.

`img/og.png` is the social preview, made once by hand from the same art.

## Keeping the page true

The home page describes the game as it is, not as planned. When the app
changes what it does — rewards, limits, what 8ctoMath+ holds, what the free
version holds back — change the page too, and re-render the screenshots if a
screen it shows has changed. The app's `store/play_listing.md` carries the
same claims for Google Play, so the two should agree.

The word "sum" means addition only. The app practises adding, taking away,
times tables, sharing and big times, so the copy says "calculation" or
"question" for the general case.

## At launch

The Play listing for `io.a51.octomath` is not public yet, so the store button
is a "Coming to Google Play" badge. Both places it appears carry a comment with
the anchor to drop in instead — `index.html`, in the hero and in the closing
call. The closing paragraph says the app is in testing; change that with it.
