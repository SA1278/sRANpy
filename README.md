# sRANpy
GUI application for editing srsRAN enb.conf files, very unfinished stuff, backup your configs!

Place the configure_enb.py file in the same folder with your enb.conf file, rest should be self-explanatory.


Requirements (install using pip if needed):
```
pip install tk

pip install configparser
```
![image](https://user-images.githubusercontent.com/42217036/212255933-95a4fd5d-b76e-4b9d-a995-0f6eb825fea1.png)



## For this to work, your enb.conf file can't have the tm and nof_ports parameters commented out. Remove the '#' manually.

> tm = n

> nof_ports = n
