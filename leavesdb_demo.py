

random_seed = 34
import random
random.seed(random_seed)
import dataset
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from stuf import stuf

import tensorflow as tf;
tf.enable_eager_execution()

import leavesdb
from leavesdb.data_loaders.tensorpack_loaders import get_multiprocess_dataflow



local_db = leavesdb.init_local_db()

db = dataset.connect(f'sqlite:///{local_db}', row_type=stuf)

leavesdb.summarize_db(db)



# data = leavesdb.db_query.load_Fossil_data(db)

data = leavesdb.db_query.load_Leaves_data(db)



data_df = leavesdb.preprocessing.encode_labels(data)

data_df.sample(frac=1).head(10)



def get_class_counts(data_df, verbose=True):
    labels, label_counts = np.unique(data_df['label'], return_counts=True)
    if verbose:
        print('label : count')
        for label, count in zip(labels, label_counts):
            print(label,' : ', count)
    return labels, label_counts
    
def filter_low_count_labels(data_df, threshold=2, verbose = True):
    '''
    Function for omitting samples that belong to a class with a population size below the threshold. Used primarily for omitting classes with only 1 sample.
    '''
    labels, label_counts = np.unique(data_df['label'], return_counts=True)
    filtered_labels = np.where(label_counts >= threshold)[0]
    filtered_data = data_df[data_df['label'].isin(filtered_labels)]
    if verbose:
        print(f'Previous num_classes = {len(label_counts)}, new num_classes = {len(filtered_labels)}')
        print(f'Previous data_df.shape = {data_df.shape}, new data_df.shape = {filtered_data.shape}')
    return filtered_data




test_size = 0.25
val_size = 0.25

data_df = filter_low_count_labels(data_df, threshold=3, verbose = True)

train_data, test_data = train_test_split(data_df, test_size=test_size, random_state=random_seed, shuffle=True, stratify=data_df['label'])
train_data, val_data = train_test_split(train_data, test_size=val_size, random_state=random_seed, shuffle=True, stratify=train_data['label'])





train_gen = get_multiprocess_dataflow(train_data['path'], train_data['label'], size=(299,299), batch_size=32, num_prefetch=25, num_proc=5)

