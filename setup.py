from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    description="A package to automate sending personalized 'Good Morning' messages.",
    author="Nour Kanout",
    author_email="mokan4970@oslomet.no",
    entry_points={
        'console_scripts': [
            'morning_greetings = main:main',
        ],
    }
)
