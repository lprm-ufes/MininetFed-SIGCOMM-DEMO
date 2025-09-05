# Reproducibility Steps

**Requirements**

- Ubuntu LTS +20.04 (22.04 - preferable)
- Containernet - https://github.com/ramonfontes/containernet
- +6.0.0 kernel
- MininetFed - https://github.com/lprm-ufes/MininetFed/tree/v1.0.3

# Running Experiments

## Selection of Clients

To execute the topology.py file, use the script as shown below:

```shell
sudo python3 topology.py [--all|--random|--energy]
```

After running the command, the network and devices will be instantiated. After a few seconds, multiple Xterm windows will open as shown in the figure below

<img src="https://github.com/lprm-ufes/MininetFed-SIGCOMM-DEMO/blob/main/images/figure.png" alt=""/>

In the terminal where the command was executed, the message _Waiting for messages_ will appear, indicating that MininetFed is waiting for the experiment's completion message.

<img src="https://github.com/lprm-ufes/MininetFed-LoWPAN/blob/topology-unico/images/terminal.png" alt=""/>

## Videos

This video shows the execution of the experiment when all clients participate in the federated training.

<video width="640" height="360" controls>
  <source src="https://github.com/lprm-ufes/MininetFed-SIGCOMM-DEMO/raw/main/videos/all.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


This video shows the case where a random subset of clients is selected to participate in each training round.

<video width="640" height="360" controls>
  <source src="https://github.com/lprm-ufes/MininetFed-SIGCOMM-DEMO/raw/main/videos/random.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


This video demonstrates the scenario where the client selection is based on energy constraints, prioritizing devices with higher remaining energy.

<video width="640" height="360" controls>
  <source src="https://github.com/lprm-ufes/MininetFed-SIGCOMM-DEMO/raw/main/videos/energy.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Paper

The paper is available at https://github.com/lprm-ufes/MininetFed-SIGCOMM-DEMO/blob/main/Demo_Sigcomm_2025_FL_MininetFed.pdf

