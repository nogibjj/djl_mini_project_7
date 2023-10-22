from setuptools import setup, find_packages

setup(
    name="ET",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "et_tool = ET.main:main",
        ],
    },
    install_requires=[
        "requests",
        #"sqlite3",
        "prettytable",
    ]
)