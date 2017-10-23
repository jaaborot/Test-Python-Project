from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='tdd_python',
      version='0.1',
      description='Test-driven development in Python',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Test-driven Development :: Object-Oriented Programming',
      ],
      keywords='TDD, OOP',
      url='http://github.com/jaaborot/tdd_python',
      author='Jeffrey A. Aborot',
      author_email='jaaborot@up.edu.ph',
      license='MIT',
      packages=['.'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      test_suite='tests',
      tests_require=['pytest'],
      setup_requires=['pytest-runner'],
      zip_safe=False)
