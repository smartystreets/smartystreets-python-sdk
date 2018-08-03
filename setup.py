import os
from distutils.core import setup

if hasattr(os, 'link'):
    del os.link

package_version='0.0.0'
version_filename = os.path.join(os.path.dirname(__file__), "smartystreets_python_sdk/version.txt")
with open(version_filename, 'r') as version_file:
    package_version=version_file.read().replace('\n', '')

setup(
    name='smartystreets_python_sdk',
    packages=['smartystreets_python_sdk', 'smartystreets_python_sdk.us_street', 'smartystreets_python_sdk.us_zipcode',
              'smartystreets_python_sdk.us_extract', 'smartystreets_python_sdk.us_autocomplete', 'smartystreets_python_sdk.international_street'],
    version=package_version,
    description='An official library to help Python developers easily access the SmartyStreets APIs',
    long_description='Official Python library for SmartyStreets',
    author='SmartyStreets SDK Team',
    author_email='support@smartystreets.com',
    license='Apache 2',
    url='https://github.com/smartystreets/smartystreets-python-sdk',
    download_url='https://github.com/smartystreets/smartystreets-python-sdk/tarball/0.0.0',
    keywords=['smartystreets', 'smarty', 'address', 'validation', 'verification', 'street', 'sdk', 'library', 'geocode'],
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
