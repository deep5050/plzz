import os
from setuptools import find_packages
from setuptools import setup

from plzz import __main__

DESCRIPTION = "A CLI to automate daily tasks."
VERSION = __main__.__get_version()


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def required():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="plzz-cli",
    version=VERSION,
    description="A CLI to automate daily tasks of common and advanced users.",
    long_description=readme(),
    keywords="CLI automation file-operations file-organization tasks system-tools app",
    author="Dipankar Pal",
    author_email="dipankarpal5050@gmail.com",
    url="https://github.com/deep5050/plzz",
    license="MIT",
    platforms='any',
    package_data={'plzz': ['plzz/commands/*.*', 'plzz/helper_functions/*']},
    packages=find_packages(),
    install_requires=read('requirements.txt').splitlines(),
    entry_points={
        "console_scripts": [
            "plzz = plzz.__main__:__main__",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/deep5050/plzz/",
        "Upstream": "https://github.com/deep5050/plzz/",
    },
    zip_safe=False
)
