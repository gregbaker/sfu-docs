# GPU Accelerated Computing in CSIL

[Some of the workstations in CSIL have GPUs](http://www.sfu.ca/computing/about/support/csil/hardware.html): they can be used for CPU-accelerated computing (with [TensorFlow](https://www.tensorflow.org/) and similar tools).
In addition to the computers listed there, all of the workstations in the Big Data computer lab (ASB10928) have 1050Tis installed.
You can work with these in the lab, or [connect remotely](csil-remote.md).

You should find all of the libraries you need installed there.


## PyTorch

[PyTorch](https://pytorch.org/) is installed in the lab and should work. On machines with NVidia GPUs, they should work automatically.
```
ggbaker@asb9999u-a01:~$ python3
Python 3.6.6 |Anaconda custom (64-bit)| (default, Oct  9 2018, 12:34:16) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True

```

## Keras

The [Keras](https://keras.io/) module should work out-of-the-box:
```bash
python3 keras-helloworld.py
```
The [```keras-helloworld.py```](keras-helloworld.py) program included here should run: after that, creating the model is your problem.


## PlaidML

[PlaidML](https://github.com/plaidml/plaidml) is a OpenCL-based neural network toolkit. It should work on the NVidia GPUs in the lab.
```bash
pip3 install --user plaidml plaidml-keras
~/.local/bin/plaidml-setup
python3 plaidml-helloworld.py
```

When you run `plaidml-setup`, you should be able to accept the defaults, and it should be a one-time setup step.

The [`plaidml-helloworld.py`](plaidml-helloworld.py) program included here should run. The only difference between that program and the `keras-helloworld.py` is the first two lines:
```python
import plaidml.keras
plaidml.keras.install_backend()
```
