from setuptools import setup, find_packages

setup (
    name="my_package",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="This is a demo package",
    long_description=open('README.md').read(),
    install_requires=["numpy"],
    url="https://github.com/jkazalekor/MY_PACKAGE",
    author="Joseph Kwami Azalekor",
    author_email="jkazalekor@gmail.com"
)