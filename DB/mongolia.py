"""
TOAD.mongolia

I am the mongodb storage interface for TOAD.
"""
from TOAD.common import *


class CUD:
	#-- Create Update Delete


class Qi:
	#-- Query interface
	def carriers(self, nucls, grpscontext = None):
		"""
		I answer the groups that contain at least one instance of the given nucls.
		"""
		raise NotImplementedError

	def clutches(self, grpscontext = None):
		"""
		I answer the set of clutches that are part of my collection.
		"""
		raise NotImplementedError

	
