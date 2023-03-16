#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janshykernel
IPKernelApp.launch_instance(kernel_class=janshykernel)
