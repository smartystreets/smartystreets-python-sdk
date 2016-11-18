import os
from distutils.core import setup
import smartystreets_python_sdk as smarty

del os.link

setup(
    name='smartystreets_python_sdk',
    packages=['smartystreets_python_sdk'],
    version=smarty.__version__,
    description='A library to help Python developers easily access the SmartyStreets APIs',
    long_description='Official Python library for SmartyStreets',
    author='SmartyStreets SDK Team',
    author_email='support@smartystreets.com',
    license='Apache 2',
    url='https://github.com/smartystreets/smartystreets-python-sdk',
    download_url='https://github.com/smartystreets/smartystreets-python-sdk/tarball/'+smarty.__version__,
    keywords=['smartystreets', 'smarty', 'address', 'validation', 'verification', 'street', 'sdk', 'library'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    install_requires=['requests']
)
