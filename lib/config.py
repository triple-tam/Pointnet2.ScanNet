import os
from easydict import EasyDict

CONF = EasyDict()

# BASE PATH
ROOT_REPOS = "/home/tam/mydisk/project/00_repos"
#ROOT_REPOS = "/usr/stud/tranthi/project/00_repos"

CONF.ROOT = ROOT_REPOS + "/Pointnet2.ScanNet.Dave2" # TODO change this
CONF.SCANNET_DIR =  ROOT_REPOS + "/Pointnet2_PyTorch/pointnet2/data/ScanNet/scans" # TODO change this
CONF.SCENE_NAMES = os.listdir(ROOT_REPOS + '/Pointnet2_PyTorch/pointnet2/data/ScanNet/scans') # TODO change


CONF.PREP = os.path.join(CONF.ROOT, "preprocessing")
CONF.PREP_SCANS = os.path.join(CONF.PREP, "scannet_scenes")
CONF.SCAN_LABELS = os.path.join(CONF.PREP, "label_point_clouds")
CONF.OUTPUT_ROOT = os.path.join(CONF.ROOT, "outputs")

CONF.SCANNETV2_TRAIN = os.path.join(CONF.ROOT, "data/scannetv2_train.txt")
CONF.SCANNETV2_VAL = os.path.join(CONF.ROOT, "data/scannetv2_val.txt")
CONF.SCANNETV2_FILE = os.path.join(CONF.PREP_SCANS, "{}.npy") # scene_id
CONF.SCANNETV2_LABEL = os.path.join(CONF.SCAN_LABELS, "{}.ply") # scene_id

CONF.NYUCLASSES = [
    'floor', #0
    'wall', 
    'cabinet', 
    'bed', 
    'chair', 
    'sofa', #5
    'table', 
    'door', 
    'window', 
    'bookshelf', 
    'picture', #10
    'counter', 
    'desk', 
    'curtain', 
    'refrigerator', 
    'bathtub', #15
    'shower curtain', 
    'toilet', 
    'sink', 
    'otherprop'#19
]
CONF.NUM_CLASSES = len(CONF.NYUCLASSES)
CONF.PALETTE = [
    (152, 223, 138),		# floor
    (174, 199, 232),		# wall
    (31, 119, 180), 		# cabinet
    (255, 187, 120),		# bed
    (188, 189, 34), 		# chair
    (140, 86, 75),  		# sofa
    (255, 152, 150),		# table
    (214, 39, 40),  		# door
    (197, 176, 213),		# window
    (148, 103, 189),		# bookshelf
    (196, 156, 148),		# picture
    (23, 190, 207), 		# counter
    (247, 182, 210),		# desk
    (219, 219, 141),		# curtain
    (255, 127, 14), 		# refrigerator
    (227, 119, 194),		# bathtub
    (158, 218, 229),		# shower curtain
    (44, 160, 44),  		# toilet
    (112, 128, 144),		# sink
    (82, 84, 163),          # otherfurn
]


CONF.INPUT_CHANNELS = 0 # aka whether to use rgb data or not