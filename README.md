# net_model_dataset
Dataset for creating 5G slice models.

## Instructions

1. **Extract the .zip files:**

   Before you can use the dataset, you need to extract the contents of the `.zip` files. You can do this using any standard file extraction tool. For example, on a Unix-based system, you can use the following command:

   ```bash
   sh extract_data.sh
   ```

2. **Install the required packages:**

   Make sure to use python3.10, NumPy 2.2 and Pandas 2.2 for the .pkl files to load properly.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run `data_generator.py`:**

   Once the files are extracted, you need to run the `data_generator.py` script to load the data. This script loads the extracted files, and splits the data into train/val/test sets.

   You can run the script using Python:

   ```bash
   python data_generator.py
   ```

   Ensure that you have Python installed and that you are in the correct directory where `data_generator.py` is located.

## Directory structure
- RAN
   - net_model_dataset/ran/input_dataset.pkl
   - net_model_dataset/ran/output_dataset.pkl
- OvS
   - net_model_dataset/ovs/input_dataset.pkl
   - net_model_dataset/ovs/output_dataset.pkl
- UPF
   - net_model_dataset/upf/input_dataset.pkl
   - net_model_dataset/upf/output_dataset.pkl
- Slice Mono
   - net_model_dataset/slice_mono/input_dataset.pkl
   - net_model_dataset/slice_mono/output_dataset.pkl
- Slice
   - net_model_dataset/slice/input_dataset.pkl
   - net_model_dataset/slice/output_dataset.pkl


## Data Description

### Input Data

The dataset contains feature extracted from VNF input and output packet traces over 1 second windows.

The input DataFrame contains the following columns:

- **packet_size**: The size of the packets.
- **packet_rate**: The rate at which packets are sent.
- **throughput**: The input throughput.
- **inter_arrival_time_mean**: The mean time between packet arrivals.
- **inter_arrival_time_std**: The standard deviation of the time between packet arrivals.
- **res**: Resource allocation (CPU (milicores) for RAN and UPF, and throughput (Mbps) for OvS).
- **time_stamp_arr**: Time stamp array of the packet arrivals. Can be used to calculate the inter-arrival time.

### Output Data

The output DataFrame contains the following columns:

- **packet_size**: The size of the packets.
- **packet_rate**: The rate at which packets are sent (pps).
- **throughput**: The output throughput.
- **inter_arrival_time_mean**: The mean time between packet arrivals.
- **inter_arrival_time_std**: The standard deviation of the time between packet arrivals.
- **time_in_sys_arr**: Array of times each packet spends in the VNF (nan represents packet drop).
- **time_stamp_arr**: Time stamp array of the packet departure.


## Using the dataset

Please refer the the following repository which shows a simple example of how to use the dataset for making a slice model, and using the model for dynamic resource allocation:

https://github.com/sulaimanalmani/5GDynamicResourceAllocation
