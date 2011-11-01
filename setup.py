from setuptools import setup, find_packages

version = '0.1'

setup(name='RSuck',
      version=version,
      description="Reverse rsync",
      long_description=open('README.rst').read(),
      classifiers=[], 
      keywords='ssh execnet rsync',
      author='Whit Morriss',
      author_email='whit at surveymonkey.com',
      url='http://surveymonkey.github.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["path.py",
                        "execnet"],
      entry_points="""
      [console_scripts]
      rsuck=rsuck.rrsync:main
      """,
      )
