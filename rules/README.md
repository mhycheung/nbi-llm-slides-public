# Rules

One line per rule: its id, the rule, and when it applies. Context files and dispatches cite
rules by id ("R01, R04 apply"); agents open a rule's detail file only when it is cited.
Rules too long for one line get a detail file `rules/R<nn>-<name>.md`. The user and agents
add rules; a rule is added when a real incident or decision paid for it. The rules that must
never be broken are in `AGENTS.md` §0, not here.

| id | rule | applies when |
|---|---|---|
| R01 | State the convention (units, sign, normalisation) before any comparison. | comparing two numbers from different sources |
| R02 | Design every test so that it could refute the project's own thesis. | planning a check |
| R03 | External results are checks, not inputs: derive, cite and test what the project relies on. | using another paper's result |
| R04 | A hard-coded value is declared in one place, cited, and asserted where it is used. | writing constants into code |
| R05 | Every artifact records how it was made: script, parameters, date, inputs. Published results get a `provenance.yaml`. | producing any output |
| R06 | Heavy work goes to the batch system; site settings come from `config/site.local.yaml`. | anything above a few minutes of compute |
| R07 | Reuse caches and existing outputs before recomputing. | starting a computation |
| R08 | Slides follow `slides/FORMAT.md`: white, black, Arial, no text unless the user asks, 16:9, keys turn pages, clicks never do (except dragging the presentation's progress bar, at the user's request). | making or editing any slide |
| R09 | A part session edits and commits only `slides/parts/<name>/` and its task folder (`git commit -- <paths>`), never `git add -A`; shared slide files change only with the user's approval. | working on a slide part in parallel |
| R10 | Commits on `main` are pushed to the private remote and the slides deployed to the public preview repo automatically; the user authorised this. It is not an open-science publish. | committing |
| R11 | A figure from another paper, or anything the user says to cite, gets a gray `.cite` credit, the size of body text (40 px): `Lastname+ (arXiv number)` of the first author, or `LVK (arXiv number)` for an LVK collaboration paper; nothing else. If Cheung is a coauthor but not first author, the credit names Cheung too: `First, Cheung+ (arXiv number)` if Cheung is second author, `First, ..., Cheung+ (arXiv number)` otherwise. "Cheung" is always underlined, `<u>Cheung</u>`, whatever the author position (`slides/FORMAT.md`). | showing another paper's figure or result |
| R12 | A slide that shows ongoing work carries `<div class="ongoing">ongoing work</div>`: bold red, top right (`slides/FORMAT.md`). | showing work that is not yet published |
