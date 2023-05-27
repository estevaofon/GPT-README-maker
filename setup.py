from setuptools import setup, find_packages

setup(
    name='readme-maker ',
    version='0.1.0',
    url='https://github.com/estevaofon/GPT-README-maker',
    author='Estevao',
    author_email='estevaopfon@gmail.com',
    description='A readme maker using GPT-3',
    packages=find_packages(),    
    install_requires=['openai', 'python-dotenv'],
    entry_points={
        'console_scripts': [
            'readme-maker = readme-maker:main',
        ],
    },
)

