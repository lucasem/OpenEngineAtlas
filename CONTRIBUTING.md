# Contributing to OpenEngineAtlas

OpenEngineAtlas uses a **suggestion → review → pull request → merge** workflow for new projects.

## 1. Suggest a project

Open a GitHub issue using the **Suggest an engine or tool** issue form. Supply the official website, canonical source repository, upstream license link, suggested category, project type, languages, and a short explanation.

When the issue is opened, repository automation applies:

- `suggestion`
- `needs-review`

A maintainer then checks the inclusion criteria below.

## 2. Maintainer review

Maintainers use these decision labels:

- `accepted` — the project qualifies for the main catalog; a PR is welcome.
- `needs-info` — more evidence or clarification is needed.
- `license-question` — the licensing status needs closer review.
- `duplicate` — the project is already represented by an existing entry/issue.
- `rejected` — the project does not meet the current scope or FOSS criteria.
- `legacy` — useful when a qualifying project belongs in the legacy/archive section.

Applying `accepted` or `rejected` automatically removes `needs-review` and posts a standard next-step comment. Maintainers still control whether/when an issue is closed.

## 3. Add an accepted project

For accepted suggestions, submit a pull request that modifies **`data/engines.json` only for catalog data**. The JSON file is the canonical source of truth.

Each entry requires:

- `name`
- `category`
- `type`
- `dimensions`
- `languages`
- `license`
- `workflow`
- `website`
- `source`
- `notes`

Valid categories are:

- `general-2d-3d`
- `2d-focused`
- `3d-focused`
- `frameworks`
- `specialized`
- `legacy`

Keep `notes` factual and concise. Avoid marketing language.

## 4. Generate and validate

After editing `data/engines.json`, run:

```bash
python scripts/validate.py
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

The catalog tables and notes in `README.md` are generated automatically from `data/engines.json`. Do not hand-edit the content between the generated catalog markers.

CI performs the same checks on every pull request. If the dataset is invalid or the README was not regenerated, the PR will fail.

## 5. Link the PR to the suggestion

Use GitHub's closing syntax in the PR body:

```text
Closes #123
```

When the accepted PR is merged, GitHub closes the linked suggestion issue automatically.

## Inclusion criteria

A proposed entry should:

1. Be directly useful for making or running games: an engine, game framework, genre-specific engine, fantasy console, interpreter/reimplementation engine, or closely related authoring/runtime system.
2. Have source code available under a recognized free/open-source software license.
3. Have a canonical upstream source repository and preferably an official website or documentation site.
4. Be clearly labeled if it is a framework, interpreter, middleware component, archived project, or legacy project rather than a full editor-based engine.

## Exclusions

Do not add proprietary engines merely because they have a free tier. Source-available projects with field-of-use, competitive-product, or non-commercial restrictions should normally go in `docs/NOT_INCLUDED.md` instead of the main list.

## Corrections to existing entries

Small factual corrections do not need a suggestion issue. Open a PR directly, explain the source of the correction, update `data/engines.json`, regenerate the README, and let CI validate the change.
