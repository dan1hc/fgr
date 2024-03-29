Contributing
============

Read our [Code of Conduct](https://github.com/dan1hc/fgr/blob/main/CODE_OF_CONDUCT.md).

* Step 1 - [Create New Issue](https://github.com/dan1hc/fgr/issues/new)
* Step 2 - Create New Branch (Corresponding to New Issue)
* Step 3 - Clone Branch & [Development Install](#development-install)
* Step 4 - Make Changes
* Step 5 - Push & [Create New PR](https://github.com/dan1hc/fgr/pulls)
* Step 6 - Wait for Review / Approval

Development Install
-------------------

```bash
pip install -e ".[develop]"
pre-commit install -f
```

Styling, Testing, and Typing
----------------------------

Assuming you installed pre-commit hooks, the below will happen when you make a commit.

*It will certainly happen on a CI runner when you push your commit.*

```bash
ruff check
python -m mypy .
pytest
```

Coverage requirements: `100%`

Commit Messages
---------------

Additionally, commit messages must adhere to [angular commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits) (templates below).

#### _multi-line_

---

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

#### _single-line_

---

```
<type>(<scope>): <subject>
```

#### Special Rules

* `<subject>` must be a pythonic `__dunder__`.
* If the multi-line template is used, at least one issue ref must be correctly [keyworded](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests) in the footer.


#### _regex_

---

```py
import re

pattern = re.compile(r'^(Merge .*)|^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\(\w+\))?((?=:\s)|(?=!:\s))?(!)?(:\s\_\_.*\_\_)($|( *\n\n)(.+)?(\n\n)((resolve[ds]? \#\d+|fix(ed|es)? \#\d+|close[ds]? \#\d+)(, )?)+$)')

assert bool(pattern.match('feat!: __valid_example__\n\noptional body text\n\ncloses #1, resolve #2')) is True
assert bool(pattern.match('test: __short_valid_example__')) is True

```
