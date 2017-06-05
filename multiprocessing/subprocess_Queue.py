# -*- coding=utf-8 -*-
import subprocess

from multiprocessing import Process, Queue
import os, time, random

def write(q):
