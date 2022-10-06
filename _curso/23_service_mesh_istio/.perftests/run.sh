#!/bin/bash

wrk -t4 -c100 -d30s --latency http://10.99.48.102:8000/
