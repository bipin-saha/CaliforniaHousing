import gzip
import pickle

def decompress_pickle(input_compressed_file, output_file):
    # Open the compressed pickle file for reading
    with gzip.open(input_compressed_file, 'rb') as f:
        data = pickle.load(f)
    
    # Save the uncompressed data into a pickle file
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

# Example usage
input_compressed_pickle_file = 'compressed_forest.pkl.gz'
output_pickle_file = 'uncompressed_forest.pkl'

decompress_pickle(input_compressed_pickle_file, output_pickle_file)
