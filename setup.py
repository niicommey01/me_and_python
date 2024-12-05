from setuptools import setup, find_packages



setup(
    name = "tasktracker",
    version = "1.0",
    packages = find_packages(),
    install_requires = [],
    entry_points = {
        "console_scripts": [
            "tasktracker=taskTracker.main",
        ]
    },
    author = "Nii Commey",
    author_email = "jude.niicommey@outlook.com",
    description = "A simple task tracking CLI tool",
    url = "https://github.com/niicommey01/task-tracker",
    classifiers = [
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)