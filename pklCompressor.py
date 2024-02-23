import gzip
import pickle

def compress_pickle(input_file, output_file):
    # Open the pickle file for reading
    with open(input_file, 'rb') as f:
        data = pickle.load(f)
    
    # Compress the data and save it
    with gzip.open(output_file, 'wb') as f:
        pickle.dump(data, f)

# Example usage
input_pickle_file = 'forest.pkl'
output_compressed_pickle_file = 'compressed_forest.pkl.gz'

compress_pickle(input_pickle_file, output_compressed_pickle_file)
