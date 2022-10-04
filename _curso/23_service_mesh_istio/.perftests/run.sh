#!/bin/bash

wrk -t4 -c100 -d30s --latency http://10.107.198.109:8000/
