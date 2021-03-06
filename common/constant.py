import os

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

"""
R file path
"""
R_SCRIPT_PATH = os.path.join(ROOT_PATH, 'R/')
INIT_LIB_R_FILE = os.path.join(R_SCRIPT_PATH, "init_lib.R")
DEP_GRAPH_R_FILE = os.path.join(R_SCRIPT_PATH, "dep-graph.R")
JTREE_R_FILE = os.path.join(R_SCRIPT_PATH, "jtree.R")
INFERENCE_R_FILE = os.path.join(R_SCRIPT_PATH, "inference.R")
SIMULATE_R_FILE = os.path.join(R_SCRIPT_PATH, "simulate.R")

"""
Test file path
"""
TEST_FILE_PATH = os.path.join(ROOT_PATH, 'static/test/')
TEST_ORIGIN_DATA_PATH = os.path.join(TEST_FILE_PATH, 'adults.csv')
TEST_DATA_PATH = os.path.join(TEST_FILE_PATH, 'data2.dat')
TEST_PARSED_FILE = os.path.join(TEST_FILE_PATH, 'data2-coarse.dat')
TEST_JTREE_FILE_PATH = os.path.join(TEST_FILE_PATH, 'data2.jtree')

"""
System configurations
"""
MAX_BIN_NUMBER = 100
MAX_ARRARY_LENGTH = 200000000
MEDIATE_DATA_DIR = os.path.join(ROOT_PATH, "mediate_data/task_%(task_id)s")
COARSE_DATA_NAME = "coarse.csv"
SIM_DATA_NAME_PATTERN = "sim_level_%(privacy_level)s.csv"
SIM_DATA_NAME_PATTERN_EXP = "sim_esp1lv_%(eps_level)s_eps2lv_%(privacy_level)s.csv"
CELERY_PROGRESS = 'PROGRESS'
CELERY_TERMINATED = 'REVOKED'
CELERY_PRO_PERCENT = 'process_percent'
CELERY_STATUS = 'status'
PRO_NAME = 'process_name'

SIM_DATA_URI_PATTERN = "task_%(task_id)s/%(file_name)s"
LOG_FILE_PATH = os.path.join(ROOT_PATH, "log/de_identification.log")

"""
DPTable Default Configurations
"""
EPSILON_1 = 700
