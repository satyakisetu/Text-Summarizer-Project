import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



__version__ = "0.0.0"

REPO_NAME = "Text-Summarize-Project"
AUTHOR_USERNAME = "satyakisetu"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "satyakisetu@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to summarize text",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
