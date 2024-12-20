# TCP Traffic Analysis Project

## Course Assignment for Stream Analytics - G23AI2002

### Assignment Overview

This project delves into TCP traffic analysis using data from the LBNL/ICSI Enterprise Trace dataset, employing the SiLK suite for comprehensive examination. Key areas of focus include:

- Analysis of TCP traffic flow  
- Classification of traffic utilizing VFDT and On-Demand Classification  
- Detection of anomalies in high-volume traffic streams  
- Visualization of traffic patterns and classification outcomes


### System Requirements

- Operating System: Ubuntu 18.04 or newer  
- Python Version: 3.8 or later  
- SiLK suite  
- Python packages as specified in `requirements.txt`

### Installation Guide

Step 1: Install the SiLK suite

sudo apt-get update

sudo apt-get install \-y build-essential libpcap-dev libfixbuf-dev flex bison cmake

Step 2: Install Python dependencies:

pip install \-r requirements.txt

Step 3: Setup SiLK:

\# Set environment variables

export SILK\_DATA\_ROOTDIR=/path/to/SiLK-LBNL-05

export SILK\_CONFIG\_FILE=/etc/silk/silk.conf

\# Create config directory

sudo mkdir \-p /etc/silk

sudo cp SiLK-LBNL-05/silk.conf /etc/silk/

### Project Directory Structure

stream\_analytics/

├── src/

│   ├── tcp\_analyzers.py      \# Main analysis script

│   └── classifiers/          \# Classification algorithms

├── config.csv               \# Configuration parameters

├── requirements.txt         \# Python dependencies

├── README.md               \# Project documentation

└── outputfile.txt          \# Analysis results

### Configuration Details

The config.csv file contains the following parameters:

- anomaly\_threshold: Threshold for anomaly detection (packets/sec)  
- start\_date: Analysis start date  
- end\_date: Analysis end date  
- bin\_size: Time bin size for analysis (seconds)

### Execution Instructions & Analysis

1. Ensure environment variables are set:

export SILK\_DATA\_ROOTDIR=/path/to/SiLK-LBNL-05

export SILK\_CONFIG\_FILE=/etc/silk/silk.conf

2. Run the analyzer:

python src/tcp\_analyzers.py

3. View results:  
- Check outputfile.txt for detailed analysis  
- View visualizations in output/lbnl\_analysis.png

### Output Files

1. outputfile.txt: Contains  
     
   - Overall traffic statistics  
   - Classification results  
   - Anomaly detection results  
   - Summary metrics

   

2. Visualizations (output/lbnl\_analysis.png):  
     
   - TCP traffic over time  
   - Traffic classification distribution  
   - Anomaly detection results

### Authors

- Dinesh Periyasamy - G23AI2002

