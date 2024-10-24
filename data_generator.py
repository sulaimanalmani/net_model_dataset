import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import math

class DataGenerator:
    def __init__(self, input_dataset_file, output_dataset_file, vnf_type='ran', norm_type='std', split=[0.8, 0.9, 1.0]):
        if input_dataset_file.endswith('.pkl'):
            self.input_dataset = pd.read_pickle(input_dataset_file)
            self.output_dataset = pd.read_pickle(output_dataset_file)
        else:
            self.input_dataset = pd.read_csv(input_dataset_file)
            self.output_dataset = pd.read_csv(output_dataset_file)

        # Convert throughput from bytes to Mbps
        self.input_dataset['throughput'] = self.input_dataset['throughput'] * 8 / (1e6) 
        self.output_dataset['throughput'] = self.output_dataset['throughput'] * 8 / (1e6)        

        self.timestamp_arr = self.input_dataset['time_stamp_arr']
        self.inter_arrival_time_arr = self.input_dataset['time_stamp_arr'].apply(lambda times: [times[1]-times[0]] + [times[i+1] - times[i] for i in range(len(times) - 1)])
        self.time_in_sys_arr = self.output_dataset['time_in_sys_arr']

        self.norm_type = norm_type
        self.vnf_type = vnf_type
        if self.vnf_type.startswith('slice'):
            self.input_dataset['res_ran'] = self.input_dataset['res'].apply(lambda x: x[0])
            self.input_dataset['res_ran'] = self.input_dataset['res_ran'].astype(float)
            self.input_dataset['res_ovs'] = self.input_dataset['res'].apply(lambda x: x[1])
            self.input_dataset['res_ovs'] = self.input_dataset['res_ovs'].astype(float)
            self.input_dataset['res_upf'] = 1.0
            self.input_dataset['res_upf'] = self.input_dataset['res_upf'].astype(float)
            self.input_dataset.drop(columns=['res'], inplace=True)
        else:
            self.input_dataset['res'] = self.input_dataset['res'].astype(float)


        self.input_feature_list = self.input_dataset.columns.tolist()
        self.output_feature_list = self.output_dataset.columns.tolist()

        # If any 'time_in_sys' is nan, remove the row from both input and output
        valid_indices = ~self.output_dataset['time_in_sys'].isna()  # Create a boolean mask
        self.input_dataset = self.input_dataset[valid_indices].reset_index(drop=True)  # Filter input dataset and reset index
        self.output_dataset = self.output_dataset[valid_indices].reset_index(drop=True)  # Filter output dataset and reset index

        # Shuffle the dataset but use same indices for input and output
        np.random.seed(42)  # Set a random seed for reproducibility
        self.indices = np.arange(len(self.input_dataset))
        np.random.shuffle(self.indices)
        self.input_dataset = self.input_dataset.iloc[self.indices]
        self.output_dataset = self.output_dataset.iloc[self.indices]
        self.timestamp_arr = self.timestamp_arr.iloc[self.indices]
        self.time_in_sys_arr = self.time_in_sys_arr.iloc[self.indices]
        self.inter_arrival_time_arr = self.inter_arrival_time_arr.iloc[self.indices]

        # Split the dataset into train, validation and test
        self.train_idx = int(len(self.input_dataset) * split[0])
        self.val_idx = int(len(self.input_dataset) * split[1])
        self.test_idx = int(len(self.input_dataset) * split[2])

        self.train_input = self.input_dataset[:self.train_idx]
        self.train_output = self.output_dataset[:self.train_idx]
        self.val_input = self.input_dataset[self.train_idx:self.val_idx]
        self.val_output = self.output_dataset[self.train_idx:self.val_idx]
        self.test_input = self.input_dataset[self.val_idx:self.test_idx]
        self.test_output = self.output_dataset[self.val_idx:self.test_idx]   

if __name__ == '__main__':
    ran_data_gen = DataGenerator("./ran/input_dataset.pkl", "./ran/output_dataset.pkl", vnf_type='ran')
    print(ran_data_gen.train_input.head())
    print(ran_data_gen.train_output.head())
