1. `uv` can be installed using pip ( `pip install uv` ) in Windows. Installation of `uv` will essentially add `uv.exe` in the `Python310/Scripts` folder, which should be a part of your `PATH` environment variable. In case you run into the following issue, run the command in an terminal opened as an Administrator.

    ```terminal
    ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: 'C:\\Python310\\Scripts\\uv.exe'
    Consider using the `--user` option or check the permissions.
    ```

    Installation can be verified by running `uv --version`.

2. After installing `uv`, a new `uv` project can be initiated by running `uv init <folder name>`. Or simply `uv init`, if already within the desired folder.

3. To add a package, run `uv add <package name>`. To add a specific version of the package, run `uv add '<package name>==<package version>'`. To add a dev dependency, run `uv add --dev <package name>`.

4. To remove a package, run `uv remove package`.

5. To run a specific file, run `uv run <filename.py>`.

6. `uv` seems to be working with VS Code's inbuilt debugger with the same `launch.json` as a regular python project. No issues so far.
