import setuptools

with open('requirements.txt','r') as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProxyToolKit",
    license='MIT',
    version='V1',
    author="Coding With Devil ( Binshan Iqbal )",
    author_email="codingwithdevil@gmail.com",
    description="Proxy Scraper and Checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codingwithdevil/ProxyToolKit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ProxyToolKitGui = ProxyToolKit.ProxyToolKitGui:run',
        ],
    }
)