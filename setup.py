"""
Upload to PyPI

python setup.py sdist
twine upload --repository pypitest dist/py-timod-X.X.X.tar.gz
twine upload --repository pypi dist/py-timod-X.X.X.tar.gz
"""
from setuptools import setup, find_packages
from timod import __version__

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except IOError:
    long_description = '''
This library can be used to build modules for ThingsDB using Python code.
'''.strip()

setup(
    name='py-timod',
    version=__version__,
    description='ThingsDB module builder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thingsdb/py-timod',
    author='Jeroen van der Heijden',
    author_email='jeroen@transceptor.technology',
    license='GPLv3+',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'msgpack'
    ],
    keywords='database connector module builder',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
