from setuptools import setup

setup(name='gwcancellation',
      version='0.0.0',
      description='Experiments in cancellation!',
      author='Chris Harris',
      author_email='chris.harris@kitware.com',
      license='Apache v2',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: Apache Software License'
          'Topic :: Scientific/Engineering :: GIS',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python'
      ],
      entry_points={
          'girder_worker_plugins': [
              'gwcancellation = gwcancellation:GWExamplePlugin',
          ]
      },
      packages=['gwcancellation'],
      zip_safe=False)
