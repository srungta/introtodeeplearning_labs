from util.util import print_progress
from util.create_dataset import create_dataset, get_batch
from util.midi_manipulation import noteStateMatrixToMidi


min_song_length  = 128
encoded_songs    = create_dataset(min_song_length)