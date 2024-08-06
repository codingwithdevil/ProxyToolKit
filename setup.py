import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyProxy",
    license=' GPL-3.0 license',
    version='1.0.0',
    author="Coding With Devil ( Binshan Iqbal )",
    author_email="codingwithdevil@gmail.com",
    description="Proxy Scraper and Checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codingwithdevil/pyProxy.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        'beautifulsoup4',
        'bs4',
        'certifi',
        'charset-normalizer',
        'idna',
        'PySocks',
        'requests',
        'soupsieve',
        'urllib3',
    ],
)