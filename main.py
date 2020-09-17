import sys

sys.path.insert(0, './scr')
sys.path.insert(1, './src/data')

from src.models import build_model
from src.data import slice_videos

print(slice_videos.slice('data/preprocessed_data/knot_tying', 'data/3dconvdata/sliced_videos'))
