### This is a guideline for contributors.

1. **import colors** and necessary helper_functions.
2. Develop every operation under a file.
3. **Maintain the color-code while printing messages.**
4. Export the function to the main function and register it under fire()
5. **If your code is dependent on external modules, please mention in the PR first** and add it to the `requirements.txt` file.
6. **Use `plzz-develop` to build the command and function database. This important, otherwise it won't show in list.** **Run the command from root directory only**.
7. Comment (disable) the `--develop` command under fire() while pushing the code. 
8. If possible use `__pathname_checker` function from `helper_function`.
9. **Write a docstring for the actual function** that will be exported to fire module. **This is a must** because this will your command description.


For build procedure see the `commands.sh` or `build.md` file.
For further information use the discussion.

-----------------------------------------------------------------------------

## This is a guideline for contributors.
2. Import `colors` and necessary `helper_functions`.
3. Develop each operation in a separate file.
4. Maintain color-coding when printing messages.
5. Export your functions to the main function and register it under `fire()`.
6. If your code depends on external modules, please mention it in the pull request (PR) and add it to the `requirements.txt` file.
7. Use `plzz --develop` to build the command and function database. This step is crucial for it to appear in the list. Run the command only from the root directory.
8. Disable the `--develop` command under `fire()` when pushing the code (comment it out).
9. If possible, utilize the `__pathname_checker` function from `helper_function`.
10. Write a docstring for the actual function, that will be exported to the fire module. This is mandatory as it will serve as your command description.
11. For the build procedure, refer to the `commands.sh` or build.md file. For further information, utilize the discussion.
