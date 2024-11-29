1. Within a `uv` project, `ruff` can be installed as a `tool` by running `uv tool install ruff`. This will add `ruff.exe` to `~/.local/bin/`, which needs to be added to the `PATH` environment variable.

2. Next comes the ruff configurations. Two of the few options are specifying configurations within the `pyproject.toml`, or creating a `ruff.toml` file.

3. The `uvx ruff check` command checks the code. The `uvx ruff format` command formats the code
