#!/usr/bin/env python

import os
import json
import argparse
import unittest

from api import Api

socket = os.getenv('DOCKER_HOST', 'unix://var/run/docker.sock')

# Get command line arguments
parser = argparse.ArgumentParser(description='Run Spyhop')
parser.add_argument('-L', '--list', nargs='?',
                    help='list all containers')
parser.add_argument('-s', '--start',type=str, 
                    help='start container')

parser.add_argument('-t', '--stop',type=str,
                    help='stop container')
args = parser.parse_args()

# Create API connection
docker_api = Api()

def ps():
    all_containers = docker_api.get_all_containers()
    all_containers[0]["start"] = "test"
    all_containers[0]["stop"] = "test"
    return all_containers
if parser.parse_args(['--list']):
    container=ps()
    print container
def start(container_id):
    container_start=docker_api.get_container_start(container_id)
    return container_start
def stop(container_id):
    container_stop=docker_api.get_container_stop(container_id)
    return container_stop

arg_dict = vars(parser.parse_args())
print arg_dict

if "start" in  arg_dict and arg_dict["start"]:
    start_container=start(arg_dict["start"])
    print start_container
elif "stop" in  arg_dict and arg_dict["stop"]:
    print arg_dict["stop"]
    stop_container=stop(arg_dict["stop"])
 
    print stop_container

	
