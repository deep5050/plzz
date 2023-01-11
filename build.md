# create the venv

`alias python=python3`

`python -m venev .python`

`source .python/bin/activate`

# tips
Run all the scripts from root directory only. This will help resolve all the relative path issues while deploying.


# Build steps

> **Run  from projects root level only**

1. Run `--develop` to generate all the functions used and their DOC.

2. Build the app `python3 setup.py build`
3. Install into the system `sudo python3 setup.py install`




