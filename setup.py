from setuptools import setup

setup(
    name='et-api-python',
    version='0.1.0',
    packages=['et_api', 'et_api.web', 'et_api.endpoints'],
    install_requires=['requests'],
    url='https://github.com/pfptcommunity/et-api-python',
    license='MIT',
    author='Ludvik Jerabek',
    author_email='',
    description='Proofpoint Security Awareness Training Python API Package'
)
