from smartystreets_python_sdk_version import __version__

from setuptools import find_packages, setup

setup(
    name='smartystreets_python_sdk',
    packages=find_packages(include=['smartystreets_python_sdk*', 'smartystreets_python_sdk_version*']),
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
        'Programming Language :: Python :: 3'
    ],
    install_requires=['requests']
)
