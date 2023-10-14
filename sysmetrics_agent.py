#srv agent is for collecting metrics of resources
import psutil,requests,json,logging,time,uuid
CYCLE=8
url='http://127.0.0.1:5000/agents'
data={}
while True:
    memory = psutil.virtual_memory()
    cpu_usage = psutil.cpu_percent(interval=1)
    network = psutil.net_io_counters()
    cons=psutil.net_connections()
    
    data['agentid']=uuid.getnode()
    data['Total']= memory.total
    data['AvailableMemory']= memory.available
    data['UsedMemory']= memory.used
    data['MemoryPercentage']= memory.percent
    data['cpu']=cpu_usage
    data['recvbytes']=network.bytes_recv
    data['sentbytes']=network.bytes_sent
    data['connections']=len(cons)
    
    json_data=json.dumps(data)
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        pass
    else:
        logging.critical(f'Error on sending data {response}')
    time.sleep(8)
