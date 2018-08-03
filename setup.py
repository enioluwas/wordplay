from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='wordplay',
    version='1.0.0a1',
    author='Enioluwa Segun',
    author_email='enioluwasegun@gmail.com',
    description='Easy word filtering and searching from a custom set of words',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/enioluwa23/wordplay',
    packages=['wordplay'],
    package_dir={'wordplay': 'wordplay'},
    package_data={'wordplay': ['data/*.dat']},
    setup_requires=[],
    install_requires=['enum34'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'tox'],
    },
    project_urls={
        'Documentation': 'https://enioluwa23.github.io/wordplay/',
        'Source Code': 'https://github.com/enioluwa23/wordplay',
        'Bug Tracker': 'https://github.com/enioluwa23/wordplay/issues',
    },
    keywords='dictionary word scrabble lookup search criteria',
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
)
