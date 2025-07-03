# Reproducibility Steps

**Requirements**

- Ubuntu LTS +20.04 (22.04 - preferable)
- Containernet - https://github.com/ramonfontes/containernet
- +6.0.0 kernel
- MininetFed v1.0.2 SIGCOMM - https://github.com/lprm-ufes/MininetFed/

## Installing MininetFed

Go to https://github.com/lprm-ufes/MininetFed/ and download the v1.0.2 SIGCOMM release. Follow the step-by-step instructions described in the documentation for installation.

## Running Experiments

## Selection of All Clients (all)

Run the topology_all.py file using the execution script as shown below

```shell
sudo python3 topology.py [--case_all|--case_random|--case_energy]
```

After running the command, the network and devices will be instantiated. After a few seconds, multiple Xterm windows will open as shown in the figure below

<img src="https://github.com/lprm-ufes/MininetFed-LoWPAN/blob/topology-unico/images/terminais.png" width="600" alt=""/>

In the terminal where the command was executed, the message _Waiting for messages_ will appear, indicating that MininetFed is waiting for the experiment's completion message.

<img src="https://github.com/lprm-ufes/MininetFed-LoWPAN/blob/topology-unico/images/terminal.png" alt=""/>

After finishing the experiment, the following files will be in the directory `sbrc/sbrc_mnist_select_[all|random|energy]`

<img src="https://github.com/lprm-ufes/MininetFed-LoWPAN/blob/topology-unico/images/arquivos.png" alt=""/>

## Cumulative Energy Consumption Graph

```shell
. envs/analysis/bin/activate
```

```shell
python analysis.py [casos_de_uso/sbrc_2025/energia_all.yaml | casos_de_uso/sbrc_2025/energia_random.yaml | casos_de_uso/sbrc_2025/energia_energy.yaml]
```

After execution, a window with the graph is expected to open as shown in the following figure:

<img src="https://github.com/lprm-ufes/MininetFed-LoWPAN/blob/topology-unico/images/grafico.png" width="600" alt=""/>

An .eps file is also generated in the root directory.

## Training Performance Impact Graph

> If you skipped the previous step
>
> ```shell
> . envs/analysis/bin/activate
> ```

```shell
python analysis.py casos_de_uso/sbrc_2025/desempenho.yaml
```

# Troubleshooting

If any problem occurs during execution, use the following command to delete the containers and clean mininet:

```shell
./script/clean.sh
```

After cleaning, try running again.
