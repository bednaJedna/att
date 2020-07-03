from setuptools import setup, find_packages

with open('./README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="att",
    version="v0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Radek 'bednaJedna' Bednarik",
    author_email="bednarik.radek@gmail.com",
    description="Python wrapper for using Apitalks API.",
    long_description=long_description,
    keywords="api Apitalks wrapper python3 data library utility",
    url="https://github.com/bednaJedna/att",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
)
