from setuptools import setup, find_packages

# Reads the content of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codemallow",  # Replace with your package's name
    version="0.0.1",           # Specify the version
    author="powerfulbean",         # Replace with your name
    author_email="powerfulbean@gmail.com",  # Replace with your email
    description="A brief description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeMallow/CodeMallow",  # Replace with your repo URL
    packages=find_packages(),  # Automatically finds submodules in your package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify the minimum Python version
    install_requires=[],  # List your package dependencies here
)
