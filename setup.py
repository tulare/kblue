# -*- encoding: utf-8 -*-

import setuptools

# Get version without import module
exec(compile(open('src/kblue/version.py').read(),
             'kblue/version.py', 'exec'))

setuptools.setup(
    version = __version__,
    package_dir = {
        '' : str('src')
    },
)
