from smartystreets_python_sdk_version import __version__

import os
from distutils.core import setup

if hasattr(os, 'link'):
    del os.link

setup(
    name='smartystreets_python_sdk',
    packages=[
        'smartystreets_python_sdk',
        'smartystreets_python_sdk_version',
        'smartystreets_python_sdk.us_street',
        'smartystreets_python_sdk.us_zipcode',
        'smartystreets_python_sdk.us_extract',
        'smartystreets_python_sdk.us_autocomplete',
        'smartystreets_python_sdk.international_street',
        'smartystreets_python_sdk.us_reverse_geo',
        'smartystreets_python_sdk.us_autocomplete_pro',
        'smartystreets_python_sdk.international_autocomplete'
    ],
    version=__version__,
    description='An official library to help Python developers easily access the SmartyStreets APIs',
    long_description='Official Python library for SmartyStreets',
    author='SmartyStreets SDK Team',
    author_email='support@smartystreets.com',
    license='Apache 2',
    url='https://github.com/smartystreets/smartystreets-python-sdk',
    download_url='https://github.com/smartystreets/smartystreets-python-sdk/tarball/' + __version__,
    keywords=[
        'smartystreets',
        'smarty',
        'address',
        'validation',
        'verification',
        'street',
        'sdk',
        'library',
        'geocode',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    install_requires=['requests']
)
