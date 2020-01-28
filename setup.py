from setuptools import setup, find_packages

setup(
    name='pip-scripts-hostbits-mvce',
    version='0.0.1',
    description='Test that pip install mains +x bits for scripts',
    python_requires=">=2.7,<3",
    long_description='Test that pip install mains +x bits for scripts',
    url='https://github.com/bsolomon1124/pip-scripts-hostbits-mvce',
    packages=find_packages(),
    scripts=['bin/my_script'],
)
