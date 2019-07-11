from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# specify requirements of your package here
REQUIREMENTS = ['urlopen', 'bs4', 'requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Intended Audience :: CryptoCurrencies Enthusiasts',
    'Topic :: CryptoCurrencies',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
]

# calling the setup function
setup(name='crypto_monitor',
      version='1.0.0',
      description='A dashboard to view Crypto Prices',
      long_description=long_description,
      url='https://github.com/Alvarenga1/CryptoMonitor',
      author='Renan Soares Alvarenga',
      author_email='renan.alvarenga@protonmail.com',
      license='MIT',
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='bitcoin crypto money'
      )
