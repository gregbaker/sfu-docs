# Remote SSH Access to CSIL

There are four CSIL Linux servers that you can connect to remotely: `csil-cpu1` to `csil-cpu4`. You can SSH to port 24 like this (or adapt to your favourit SSH client):

```bash
ssh -p24 USERNAME@csil-cpu1.csil.sfu.ca
```

## Workstations

If you want to connect to one of the workstation (because you want to [use a GPU](csil-gpu.md) or run a VM), you can do so from on-campus or by connecting first to one of the CPU servers as described above.

Then you can SSH to one of the workstations if it's currently booted into Linux. The 
[`csil-linux.py`](csil-linux.py) program here will produce a list of workstations currently in Linux. The SSH command will be like this:

```bash
ssh -p24 asb9700u-z99.csil.sfu.ca
```
