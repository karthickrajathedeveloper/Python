# MQTT Data Logger and Graph Generator

This repository contains a `Python program` that receives data over `MQTT, logs the data`, and generates `visual graphs` based on the logged data. The project is developed using 
 - [Jupyter Notebook](https://jupyter.org/)
 - [PyCharm](https://www.jetbrains.com/pycharm/)
   
## Features
  # MQTT Data Reception:
    Subscribe to an MQTT topic to receive real-time data.
  # Data Logging: 
    Logs received data into a file (CSV format).
  # Graph Generation: 
    Converts the logged data into graphs for visualization.
  # Jupyter & PyCharm Support: 
    The project can be run and edited using either Jupyter Notebook or PyCharm.

```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## Install the required MQTT and plotting libraries:
```pip install paho-mqtt==1.6.1 ```

```
pip install paho-mqtt matplotlib pandas
```
# Usage
  Open the project in Jupyter Notebook or PyCharm.

## Run the program:

* The program will subscribe to the MQTT topic.
* It will log the received data into a CSV file.
* After logging, it will convert the data into graphs for analysis.

## Example
# Receiving Data: 
  The program listens to the MQTT broker for incoming data on a specified topic.

# Creating Logs: 
  The received data is logged into a file (data_log.csv) with timestamps.

# Generating Graphs:
  The data from the logs is used to create visual graphs (e.g., line charts) using matplotlib.

## Dependencies
  - Python 3.x
  - Paho MQTT
  - Matplotlib
  - Pandas

## Author 
[karthickrajathedeveloper](https://github.com/karthickrajathedeveloper)

## LICENSE
[MIT LICENSE](LICENSE)

