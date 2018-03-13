"""hw3_task"""
# pylint: disable=invalid-name
# pylint: disable=too-many-instance-attributes
import time
import json
import psutil
import hw3_config


class monitoring:
    """monitoring class"""
    counter = 0

    def __init__(self):
        """init"""
        self.counter = 0
        self.cpu_per = None
        self.cpu_t = None
        self.virt_mem = None
        self.swap_mem = None
        self.disk_parts = None
        self.disk_use = None
        self.net_addr = None
        self.date = None

    def metrics(self):
        """metrics"""
        self.cpu_per = str(psutil.cpu_percent())
        self.cpu_t = str(psutil.cpu_times())
        self.virt_mem = str(psutil.virtual_memory())
        self.swap_mem = str(psutil.virtual_memory())
        self.disk_parts = str(psutil.disk_partitions())
        self.disk_use = str(psutil.disk_usage('/'))
        self.net_addr = str(psutil.net_if_addrs())
        self.date = str(time.ctime())

    def creating_txt(self):
        """txt"""
        self.metrics()
        self.counter += 1
	txt = open("monitoring.txt", "a")
        txt.write("SNAPSHOT" + str(self.counter) + "\n")
        txt.write("DATE:" + (time.ctime()) + "\n" + "\n")
        txt.write("CPU INFO" + "\n")
        txt.write("cpu percent:" + self.cpu_per)
        txt.write("cpu times:" + self.cpu_t + "\n")
        txt.write("MEMORY INFO" + "\n")
        txt.write("virtual memory:" + self.virt_mem + "\n")
        txt.write("swap memory:" + self.swap_mem + "\n")
        txt.write("DISK INFO" + "\n")
        txt.write("disk partitions:" + self.disk_parts + "\n")
        txt.write("disk usage:" + self.disk_use + "\n")
        txt.write("NET INFO" + "\n")
        txt.write("net addres:" + self.net_addr + "\n" + "\n" + "\n" + "\n")
        txt.close()
        print(str(self.counter) + "txt file created")

    def creating_json(self):
        """json"""
        self.metrics()
        self.counter += 1
        data = {"SNAPSHOT:": str(self.counter), "DATE": time.ctime(),
                "cpu percent": self.cpu_per, "cpu times": self.cpu_t,
                "virtual memory": self.virt_mem, "swap memory":  self.swap_mem,
                "disk partitions":  self.disk_parts,
                "disk usage":  self.disk_use,
                "net addres": self.net_addr}
        with open("monitoring.json", "a") as js:
            json.dump(data, js, sort_keys=True, indent=4, ensure_ascii=False)
            js.write("\n")
        print(str(self.counter) + "json file created")

	
obj = monitoring()

while True:
    if hw3_config.output == "txt":
        obj.creating_txt()
    else:
        obj.creating_json()
    time.sleep(hw3_config.interval*60)
