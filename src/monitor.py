import socket
import time
import threading
import psutil
from collections import defaultdict
import statistics

# Configuración
AVG_WINDOW_SIZE = 5  
# Puerto en el que se escuharará el monitor
SERVER_PORT = 9999
# IP en el que se escuchará el monitor
SERVER_IP = "0.0.0.0"

# Estructuras de datos globales 
cpu_util_queue = deque(maxlen=AVG_WINDOW_SIZE)
mem_util_queue = deque(maxlen=AVG_WINDOW_SIZE)
net_recv_queue = deque(maxlen=AVG_WINDOW_SIZE)
net_sent_queue = deque(maxlen=AVG_WINDOW_SIZE)
disk_read_queue = deque(maxlen=AVG_WINDOW_SIZE)
disk_write_queue = deque(maxlen=AVG_WINDOW_SIZE)
