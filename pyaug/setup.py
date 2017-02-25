from distutils.core import setup

setup(
    name = "pyaug",
    version = "0.0.1",
    author = "PyAugusta",
    author_email = "taylor.cory08@gmail.com",
    description = ("PyAugusta's sample Python package for educational purposes"),
    url = "https://github.com/PyAugusta/git-drills",
    packages = ["pyaug", "tests"],
    package_data = {"pyaug": ["data/*"], "tests": ["testdata/*"]},
)
