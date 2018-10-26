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

## Copying Files

Your home directory is shared between the CPU servers, so you can copy files to or from there by connecting to one of the CPU servers. The files will be available on the workstations. Copying files to CSIL will be something like:
```bash
scp -P24 filename.py USERNAME@csil-cpu1.csil.sfu.ca:
```
And back from CSIL:
```bash
scp -P24 USERNAME@csil-cpu1.csil.sfu.ca:results.txt .
```


