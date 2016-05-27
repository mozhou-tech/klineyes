from setuptools import setup

setup(name='klineyes',
      version='0.1',
      description='A k-line pattern recognition library written in Python.',
      url='https://github.com/tenstone/klineyes',
      author='Tenstone',
      author_email='tenstone@foxmail.com',
      license='MIT',
      packages=['klineyes'],
      install_requires=[
          'pandas', 'numpy'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)