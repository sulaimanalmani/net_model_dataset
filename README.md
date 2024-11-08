# net_model_dataset
Dataset for creating 5G slice models.

## Instructions

1. **Extract the .zip files:**

   Before you can use the dataset, you need to extract the contents of the `.zip` files. You can do this using any standard file extraction tool. For example, on a Unix-based system, you can use the following command:

   ```bash
   sh extract_data.sh
   ```

2. **Install the required packages:**

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

## Notes

## Data Description

### Input DataFrame

The dataset contains feature extracted from VNF input and output packet traces over 1 second windows.

The input DataFrame contains the following columns:

- **packet_size**: The size of the packets.
- **packet_rate**: The rate at which packets are sent.
- **throughput**: The input throughput.
- **inter_arrival_time_mean**: The mean time between packet arrivals.
- **inter_arrival_time_std**: The standard deviation of the time between packet arrivals.
- **res**: Resource allocation (CPU (milicores) for RAN, and throughput (Mbps) for OvS)
- **time_stamp_arr**: Time stamp array of the packet arrivals. Can be used to calculate the inter-arrival time.

### Output DataFrame

The output DataFrame contains the following columns:

- **packet_size**: The size of the packets.
- **packet_rate**: The rate at which packets are sent (pps)
- **throughput**: The output throughput.
- **inter_arrival_time_mean**: The mean time between packet arrivals.
- **inter_arrival_time_std**: The standard deviation of the time between packet arrivals.
- **time_in_sys_arr**: Array of times each packet spends in the VNF (nan represents packet drop)
- **time_stamp_arr**: Time stamp array of the packet departure.

## File Description

- **ran.zip**: Contains data for the RAN.
- **ovs.zip**: Contains data for OvS.
- **upf.zip**: Contains data for UPF.
- **slice_mono.zip**: Contains data for end-to-end slice.
- **slice.zip**: Contains data for end-to-end slice.

### Usage in paper

- **ran.zip, ovs.zip, upf.zip**: Used to train vNetRunner and Dev-Pkt in the paper.
- **slice_mono.zip**: Used to train Net-Flow.
- **slice.zip**: Used to test the slice models from the different approaches.
