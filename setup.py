import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slack-cli-webhook",
    version="0.0.1",
    author="Matthijs Roelink",
    author_email="matthijs@roelink.eu",
    description="A Python package for sending messages to Slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matthiti/slack-cli-webhook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)