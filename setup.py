from setuptools import setup, find_packages

setup(
    name="cli-toolkit",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "toolkit=toolkit.cli:main",
        ],
    },
)
