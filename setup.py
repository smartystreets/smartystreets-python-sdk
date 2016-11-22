import os
from distutils.core import setup

del os.link

setup(
    name='smartystreets_python_sdk',
    packages=['smartystreets_python_sdk'],
    version='0.0.0',
    description='An official library to help Python developers easily access the SmartyStreets APIs',
    long_description='Official Python library for SmartyStreets',
    author='SmartyStreets SDK Team',
    author_email='support@smartystreets.com',
    license='Apache 2',
    url='https://github.com/smartystreets/smartystreets-python-sdk',
    download_url='https://github.com/smartystreets/smartystreets-python-sdk/tarball/0.0.0',
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
