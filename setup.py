from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='RSuck',
      version=version,
      description="Reverse rsync",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ssh rsync',
      author='Whit Morriss',
      author_email='whit at surveymonkey.com',
      url='http://surveymonkey.github.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
