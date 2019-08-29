# bg
 Code accumulated from summer research shenanigans.

## Details of files:
#### read_graph_csv.py
Intends to read csv data and plot it, currently path and file are hard coded. Goal is to include data processing as well as graphing
#### sim.py
An alteration of of the model published in __"Senft V, Stewart TC, Bekolay T, Eliasmith C, Kröger BJ. Reduction of dopamine in basal ganglia and its effects on syllable sequencing in speech: A computer simulation study. Basal Ganglia. 2016;6(1):7-17. doi:10.1016/j.baga.2015.10.003"__ and available [here](http://www.phonetik.phoniatrie.rwth-aachen.de/bkroeger/documents/syllable_sequencing.ipynb)

It's been modified to make it easier to run series of trials, as they can be time consuming to produce. Currently works in tandem with simpar, produces matplotlib graphs and saves them to local directories
#### simpar.py
The script to run the simulator. Has two useful functions, auto_standard()runs a set of simulations parameterizing lg and le from 0.2 to 0 in steps of 0.02 and performing four trials at each pair of values. Similarly, parallel_sim() does the same set of simulations but utilizes the joblib package to decrease simulation time. By default it uses all available cores (as reported by multiprocessing.cpu_count() Both methods can accept arguments for list_lg, list_le, trials, and sim_time. List_lg and list_le must be lists to work but type is not enforced. Trials must be an integer and uses the ascii alphabet to name graphs as <lg><le><string.ascii_letters[:trials]>.png ie 0412b.png to represent lg=0.04, le=0.12, and that it is the second run for that parameter set.
#### syllable_sequencing.py
A mostly unaltered version of the above mentioned model except to run it through a convert from .ipynb to .py
#### syllable_sequencing_altered.py
The first stab at modifying their work for exploration. Originally was operated from a script called "automator" that was kludged together using Spyder IDE magic, later both files were altered to a little less dependent on painfully specific implementation details.
#### zmod.py
Snippets of code primarily, not actually included or used anywhere as of now. Just a place to put neat tricks I saw.

# Dependencies
We used an Anaconda installation with Python 3.7, Windows 10 Enterprise Build #14393, processor as i7-3770 @ 3.4Ghz
Important packages are Nengo and joblib. The model was specified as being ran with Nengo 2.0 but our simulations were using the newer release of 2.8.
