from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ok_api',
    version='1.0.1',
    description='Python библиотека для работы с API Одноклассников (API Wrapper ok.ru)',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/needkirem/ok_api',

    author='needkirem',
    author_email='needkirem@gmail.com',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='api ok wrapper',
    python_requires='>=3',
    install_requires=['requests'],
    packages=['ok_api'],

    project_urls={
        'Bug Reports': 'https://github.com/needkirem/ok_api/issues',
        'Source': 'https://github.com/needkirem/ok_api/',
    },
)
