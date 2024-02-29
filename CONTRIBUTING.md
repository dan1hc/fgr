Contributing
============

* Step 1 - [Create New Issue](https://github.com/dan1hc/fgr/issues/new)
* Step 2 - Create New Branch (Corresponding to New Issue)
* Step 3 - Clone Branch & [Development Install](#development-install)
* Step 4 - Make Changes
* Step 5 - Push & [Create New PR](https://github.com/dan1hc/fgr/pulls)
* Step 6 - Wait for Review / Approval

Commit Messages
---------------

Commit messages must adhere to [angular commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits) (template below).

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

And one more rule:
* `<subject>` must begin with a pythonic \_\_dunder\_\_.

Development Install
-------------------

```bash
pip install -e ".[develop]"
pre-commit install -f
```

Testing
-------

Assuming you installed pre-commit hooks, the below will happen when you make a commit.

*It will certainly happen on a CI runner when you push your commit.*

```bash
ruff check
python -m mypy .
pytest
```

Coverage requirements: `100%`
