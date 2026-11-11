# Space Array website

The public website of the Space Array Initiative: https://spacearray.org

The site is built with [Astro](https://astro.build). GitHub builds the site and publishes it after every merge to `main`, so nobody needs to run anything on their own computer. A merge goes live within a few minutes.

## Files

Each page is one file in `src/pages/`. The menu, the page head and the footer are in one shared file, `src/layouts/Layout.astro`. Change the menu there, and it changes on every page.

| File | Page |
| --- | --- |
| `src/pages/index.astro` | Home |
| `src/pages/science.astro` | Science |
| `src/pages/sharp.astro` | SHARP |
| `src/pages/technology.astro` | Technology |
| `src/pages/team.astro` | Team (the list comes from `public/team.json`) |
| `src/pages/news.astro` | News |
| `src/pages/contact.astro` | Contact |
| `src/layouts/Layout.astro` | Head, menu and footer for all pages |
| `public/styles.css` | Colors, fonts and layout for all pages |
| `public/images/` | Images |

Files in `public/` go online as they are. For example, `public/images/photo.jpg` is at `https://spacearray.org/images/photo.jpg`.

The page addresses did not change. `src/pages/news.astro` is still at `https://spacearray.org/news.html`.

## How to add a news item

1. Open `src/pages/news.astro` on GitHub and click the pencil icon.
2. Copy one `<article>` block and paste it above the newest item.
3. Change the date, the title and the text.
4. Click **Commit changes**, choose **Create a new branch**, then **Propose changes**.
5. Open the pull request and merge it (see below).

```html
<article class="card" style="margin-bottom:2rem;">
  <div class="kicker">10 June 2026</div>
  <h2>Title of the news item</h2>

  <p>
    Two or three sentences about the news.
  </p>
</article>
```

## How to update the team page

The Team page reads `public/team.json`. The script `tools/csv_to_json.py` builds that file from the sign-up form responses.

1. Export the form responses as a CSV file.
2. Save it in the `data/` folder, with the same file name as the CSV that is there now.
3. Run `python3 tools/csv_to_json.py`. It rewrites `public/team.json`, sorted by last name.
4. Commit the new `public/team.json`.

Do not edit `public/team.json` by hand. The script overwrites it the next time it runs.

## How to review and merge a pull request

A pull request (PR) is a proposed change. Nothing goes live until someone merges it.

1. Open the PR from the **Pull requests** tab.
2. Read the description and look at the before and after screenshots.
3. Click **Files changed** to see the exact lines that change.
4. To ask for a change, write a comment on the PR.
5. When you are happy, click **Merge pull request**, then **Confirm merge**.

To undo a merged PR, open it and click **Revert**. GitHub creates a new PR that undoes the change.

## License

- **Code** (HTML structure, CSS, scripts): MIT License. See [LICENSE](LICENSE).
- **Content** (text and images): Creative Commons Attribution 4.0 International (CC BY 4.0). See [LICENSE-CONTENT](LICENSE-CONTENT).

Images from other sources keep their own license. Their credit lines say where they come from.
