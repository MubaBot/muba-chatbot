

vector_size = 100
encode_length = 5
label_size = 1000  # number of intent
embed_type = "onehot" #onehot or w2v
# Choose single test
filter_type = "single"
filter_number = 32
filter_size = 2

# Choose multi test
filter_type = "multi"
filter_sizes = [2,3,4,2,3,4,2,3,4,2,3,4,2,3,4]
num_filters = len(filter_sizes)

# train_data_list =  {}

