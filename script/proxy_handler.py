import requests
import random
import threading
from typing import List, Dict, Optional
from script.logger import logger

def load_proxies(proxy_list_file: str = 'proxies_list.txt') -> List[str]:
    """
    Load proxies from a file and return them as a list.
    """
    try:
        with open(proxy_list_file, "r") as file:
            proxies = [line.strip() for line in file.readlines() if line.strip()]
            logger.info(f"Proxies loaded successfully: {proxies}")
            return proxies
    except FileNotFoundError:
        logger.error(f"Error: The file '{proxy_list_file}' was not found.")
    except Exception as e:
        logger.error(f"An error occurred while loading proxies: {e}")
    return []
  
def get_proxy_detail(i):
    list = i.split(':')
    username = list[0]
    password = list[1]
    ip = list[2]
    port = list[3]

    return username,password,ip,port

