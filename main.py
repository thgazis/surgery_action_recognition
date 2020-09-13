import sys

sys.path.insert(0, './scr')
sys.path.insert(1, './src/data')

from edit_videos import compress_videos

FRAME_WIDTH = 224
FRAME_HEIGHT = 224

compress_videos('data/annotated_data/knot_tying/avi2', 'data/preprocessed_data/knot_tying')