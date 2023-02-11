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
