from setuptools import setup, find_packages

setup(
    name="ET",
    version="0.1",
    url='https://github.com/nogibjj/djl_mini_project_7',
    author='Daniela',
    email='dj216@duke.edu',
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