from setuptools import setup
from setuptools.command.build_py import build_py

import rtree

# Transfer key env vars to a Python data file.
# http://www.digip.org/blog/2011/01/generating-data-files-in-setup.py.html
class rtree_build_py(build_py):
    def run(self):
        # honor the --dry-run flag
        if not self.dry_run:
            target_dir = self.build_lib

            # mkpath is a distutils helper to create directories
            self.mkpath(os.path.join(target_dir, 'rtree'))

            with open(os.path.join(target_dir, 'rtree/ENVIRON.txt'), 'w') as fobj:
                if 'SPATIALINDEX_C_LIBRARY' in os.environ:
                    fobj.write('SPATIALINDEX_C_LIBRARY=%s\n' % os.environ['SPATIALINDEX_C_LIBRARY'])

        # distutils uses old-style classes, so no super()
        build_py.run(self)


# Get text from README.txt
with open('docs/source/README.txt', 'r') as fp:
    readme_text = fp.read()

import os

if os.name == 'nt':
    data_files = [('Lib/site-packages/rtree',
                  [os.environ['SPATIALINDEX_LIBRARY']
                      if 'SPATIALINDEX_LIBRARY' in os.environ else
                      r'D:\libspatialindex\bin\spatialindex.dll',
                   os.environ['SPATIALINDEX_C_LIBRARY']
                      if 'SPATIALINDEX_C_LIBRARY' in os.environ else
                      r'D:\libspatialindex\bin\spatialindex_c.dll'])]
else:
    data_files = None

setup(
    cmdclass      = {'build_py' : rtree_build_py},
    name          = 'Rtree',
    version       = rtree.__version__,
    description   = 'R-Tree spatial index for Python GIS',
    license       = 'LGPL',
    keywords      = 'gis spatial index r-tree',
    author        = 'Sean Gillies',
    author_email  = 'sean.gillies@gmail.com',
    maintainer        = 'Howard Butler',
    maintainer_email  = 'hobu@hobu.net',
    url   = 'http://toblerity.github.com/rtree/',
    long_description = readme_text,
    packages      = ['rtree'],
    install_requires = ['setuptools'],
    test_suite = 'tests.test_suite',
    data_files = data_files,
    zip_safe = False,
    classifiers   = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
      'Operating System :: OS Independent',
      'Programming Language :: C',
      'Programming Language :: C++',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: GIS',
      'Topic :: Database',
      ],
)
