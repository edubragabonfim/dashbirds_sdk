from setuptools import setup, find_packages


setup(
    name='dashbirds-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'docling',
        'docling-core',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dsb=dashbirds_sdk.cli:main',
        ],
    },
    author='Eduardo Bonfim',
    author_email='eduardo.bonfim.dub@gmail.com',
    description='Pacote de ferramentas Dashbirds.',
)
