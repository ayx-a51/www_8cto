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
| `img/`               | art from the app, resized for the web                 |
| `CNAME`              | `8cto.net`, the Pages custom domain                   |
| `.nojekyll`          | serve the files as they are, no Jekyll pass           |

## Where things come from

Colour and type are the app's own design system: the `Sea` palette from
`lib/ui/theme.dart` in the 8ctoMath repository, copied verbatim, and the
Fredoka variable font the app bundles (`assets/fonts/Fredoka.ttf`), converted
to woff2. Fredoka is self-hosted rather than loaded from Google's CDN so that
rendering a privacy page does not hand a third party the reader's IP address.

Every picture is art from the game — characters, reward props, sticker
thumbnails and the sticker-book page backgrounds — resized and re-encoded as
webp from `assets/art/` in the app repository. There are no mock-ups and no
screenshots: nothing here shows a screen the app does not have.

## At launch

The Play listing for `io.a51.octomath` is not public yet, so the store button
is a "Coming to Google Play" badge. Both places it appears carry a comment with
the anchor to drop in instead — `index.html`, in the hero and in the closing
call.

Set `kPrivacyUrl` in the app (`lib/app/version.dart`) to
`https://8cto.net/privacy.html` once this is live; the About page hides the
link while it is empty.
