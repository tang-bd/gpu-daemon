# gpu-daemon

A simple daemon to occupy most of the VRAM of your NVIDIA GPUs.

## Usage

1. Configure the [gpu-burn tool](https://github.com/wilicc/gpu-burn).
2. Install pynvml `pip install pynvml`.
3. Modify the parameters and paths in the source code according to your need.
4. Put `gpu-daemon.service` and `gpu-daemon.timer` under the directory `/usr/lib/systemd/system`.
5. Start the service.
   ```bash
   sudo systemctl start gpu-daemon
   sudo systemctl start gpu-daemon.timer
   ```
