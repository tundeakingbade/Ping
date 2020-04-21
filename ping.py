import os
import csv
from datetime import datetime

#Creating csv file using time and date in other not to overwrite existing file
now = datetime.now()
f = now.strftime("LAT-%d-%m-%H%M.csv")
file_name = open(f, "w", newline="")

# Open file containing IP addresses
ip_list = open('IP_list', 'r')

#creating CSV hearders
fieldname = ["Status", "IP Address",  "Minimum Latency", "Maximum Latency", "Average Latency"]
file_write = csv.DictWriter(file_name, fieldnames=fieldname)
file_write.writeheader()

for ip in ip_list:
    #Stripping White space and tabs in IP addresses
    ip = ip.strip("\n")
    ip = ip.strip("\t")

    response = os.popen(f"ping {ip} -n 2").read()
    print(f"In process.... {ip}")
    
    #Running ping...
    if "Approximate round trip" in response:
        #variable to hold Minimum Latency
        lat_min_f = response.index("Minimum") + 10
        lat_min_l = response.index("ms, Max")
        lat_min = response[lat_min_f:lat_min_l]

        #variable to hold Maximum Latency
        lat_max_f = response.index("Maximum") + 10
        lat_max_l = response.index("ms, A")
        lat_max = response[lat_max_f:lat_max_l]

        #variable to hold Average Latency
        lat_av_f = response.index("Average") + 10
        lat_av = response[lat_av_f:-3]

        #Writing ping result to file if uo
        result_write = {"Status": "UP", "IP Address": ip, "Minimum Latency": lat_min, "Maximum Latency": lat_max, "Average Latency": lat_av }
        file_write.writerow(result_write)

    else:
        #Writing ping result to file if Down
        result_write = {"Status": "DOWN", "IP Address": ip,  "Minimum Latency": "", "Maximum Latency": "", "Average Latency": "" }
        file_write.writerow(result_write)