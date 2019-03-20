"""Routes"""

from os.path import dirname, basename, isfile
from flask_restplus import Api
import glob
api = Api(app, title='My first Python API', version='1.0', doc='/apidocs/', description='A number-crunching API')
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]