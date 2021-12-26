import os
import pandas as pd
import time
from datetime import datetime
#IP_list = ["2.2.2.2", "8.8.8.8", "172.20.0.1", "facebook.com", "twiter.com", "apple.com", "gmail.com"]

#CSV file containing IP addresses
IP_list = "ip_list.csv"
#Parsed to pandas to read as CSV
df = pd.read_csv(IP_list)

ping_stat = []
df_node = []
df_ip = []
for ip in range(df.shape[0]):
    ip_address = df["IP Address"][ip]
    node_name = df["Node Name"][ip]
    
    ping = os.popen(f"ping {ip_address} -c 2", mode='r').read()
    if "rtt" in ping:
        ping_stat.append('up')
        df_node.append(f'{node_name}')
        df_ip.append(f'{ip_address}')
    else:
        ping_stat.append('Offline')
        df_node.append(f'{node_name}')
        df_ip.append(f'{ip_address}')
print("Test Completed")