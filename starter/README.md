# Build With AI Starter Project

This small task dashboard is the course's shared practice project. It has no
dependencies, makes no network requests, and uses synthetic data. You can open
it directly in a browser:

1. Open `starter/index.html`.
2. Confirm that six tasks and four summary values appear.
3. Change the status and risk filters.

Run the deterministic verification from the repository root:

```console
$ node starter/verify.js
```

Or from this directory:

```console
$ node verify.js
```

The clean project should report `8 checks passed`.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Page structure and synthetic task data |
| `styles.css` | Layout, focus states, and responsive styling |
| `task-tools.js` | Pure summary and filter functions |
| `app.js` | Browser rendering and interactions |
| `expected/summary.json` | Expected result for the starter data |
| `verify.js` | Dependency-free validation |

The project deliberately keeps the data inside `index.html`. This lets learners
open the page without starting a server and gives the verifier one canonical
data source.

## Safe experimentation

Create a named checkpoint before asking an agent to change the project:

```console
$ git status --short
$ git add starter
$ git commit -m "Checkpoint starter project"
```

Only commit files you inspected. If you need to recover, follow the
[course recovery guide](../docs/course/recovery-guide.md); do not use blanket
restore or reset commands.
