## Leaderboard Setup

This repo follows the template design:
- Authoritative data: `leaderboard/leaderboard.csv`
- Auto-generated Markdown: `leaderboard/leaderboard.md`
- Interactive UI: `docs/leaderboard.html` (GitHub Pages)

### How to publish results on GitHub

1. Open a Pull Request that adds:
   - `submissions/inbox/<team_name>/<run_id>/predictions.csv`
   - `submissions/inbox/<team_name>/<run_id>/metadata.json`
   - Format: `filename,prediction`

2. Automatic scoring (GitHub Actions)
   - On PR open, the workflow validates and scores the submission.
   - Hidden labels are provided via the `TEST_LABELS_CSV` GitHub Secret.

3. Leaderboard update (on merge)
   - When the PR is merged, `leaderboard/leaderboard.csv` and
     `leaderboard/leaderboard.md` are regenerated automatically.

4. View the leaderboard UI
   - Open `docs/leaderboard.html` locally, or
   - Enable GitHub Pages with source `main` and folder `/docs`.

### GitHub Pages 

If you want a public web page:
1. Enable GitHub Pages in the repo settings.
2. Use the `main` branch and `/docs` folder.

### Important note

Hidden test labels must not be committed to the repo. Use the
`TEST_LABELS_CSV` GitHub Secret for automatic scoring.
