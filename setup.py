from distutils.core import setup
import smartystreets_python_sdk as smarty

setup(
    name='smartystreets_python_sdk',
    packages=['smartystreets_python_sdk'],
    version=smarty.__version__,
    description='A library to help Python developers easily access the SmartyStreets APIs',
    author='SmartyStreets SDK Team',
    author_email='support@smartystreets.com',
    url='https://github.com/smartystreets/smartystreets-python-sdk',
    download_url='https://github.com/smartystreets/smartystreets-python-sdk/tarball/'+smarty.__version__,
    keywords=['smartystreets', 'smarty', 'address', 'validation', 'verification', 'street', 'sdk', 'library']
)
