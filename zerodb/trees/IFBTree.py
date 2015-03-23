from BTrees.Interfaces import IIntegerFloatBTreeModule as IBTreeInterface
import BTrees.IFBTree as TreeModule
from zope.interface import moduleProvides

max_internal_size = 100000
max_leaf_size = 50000


class BTree(TreeModule.BTree):
    max_internal_size = max_internal_size
    max_leaf_size = max_leaf_size


class TreeSet(TreeModule.TreeSet):
    max_internal_size = max_internal_size
    max_leaf_size = max_leaf_size


Set = TreeModule.Set
Bucket = TreeModule.Bucket

moduleProvides(IBTreeInterface)