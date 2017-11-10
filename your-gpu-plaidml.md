# GPU Accelerated Computing on Your Computer

The [PlaidML](https://github.com/plaidml/plaidml) library makes getting deep learning and your GPU working together much easier than the alternatives (that I have seen, at least).

PlaidML uses [OpenCL](https://en.wikipedia.org/wiki/OpenCL) to talk to the GPU, so it's more flexible than CUDA-based tools, which are NVidia-only.

In theory, you should be able to install the packages with just:
```bash
pip3 install --user plaidml plaidml-keras keras
plaidml-setup
```
You may also want the `clinfo` command (Ubuntu package `clinfo`) to check that your OpenCL libraries are installed correctly. You can usually accept the defaults when running `plaidml-setup`.

The [`plaidml-helloworld.py`](plaidml-helloworld.py) program here should serve as a basic test that your install is working:
```bash
python3 plaidml-helloworld.py
```

## Specific Hardware

### Nvidia GPUs

You need the NVidia drivers installed: see the [PlaidML README](https://github.com/plaidml/plaidml#plaidml) for up-to-date package lists.

Once you have the drivers installed, the commands above should get you started.

### AMD GPUs

The [PlaidML README](https://github.com/plaidml/plaidml#plaidml) contains instructions for AMD GPUs, but I haven't been able to test them. [If anything needs to be added here, a pull-request would be appreciated.]


### Intel GPUs

I have had mixed results with Intel GPUs: different CPUs have different levels of OpenCL support or memory available or something that affect success.

I was able to get PlaidML working on my Ubuntu laptop by installing the package `beignet` for OpenCL drivers and **enabling experimental** devices in `plaidml-setup`.


## Keras Models

Keras models (that aren't recurrent) should work under PlaidML with this simple addition (**before** importing `keras`):

```python
import plaidml.keras
plaidml.keras.install_backend()
```
