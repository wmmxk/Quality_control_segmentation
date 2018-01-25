import os.path as osp
import sys
import os
src_dir = osp.dirname(osp.dirname(__file__))
lib_dir = src_dir + os.sep +"libs"
if src_dir not in sys.path:
    sys.path.insert(0,src_dir)


if lib_dir not in sys.path:
    sys.path.insert(0,lib_dir)
