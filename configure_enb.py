import tkinter as tk
from tkinter import ttk

import configparser


parser = configparser.ConfigParser()

def readEnbConfig():
    parser.read('enb.conf')

    global enb_id
    enb_id = parser['enb']['enb_id']

    global mcc
    mcc = parser['enb']['mcc']

    global mnc
    mnc = parser['enb']['mnc']

    global mme_addr
    mme_addr = parser['enb']['mme_addr']

    global gtp_bind_addr
    gtp_bind_addr = parser['enb']['gtp_bind_addr']

    global s1c_bind_addr
    s1c_bind_addr = parser['enb']['s1c_bind_addr']

    global s1c_bind_port
    s1c_bind_port = parser['enb']['s1c_bind_port']

    global n_prb
    n_prb = parser['enb']['n_prb']

    global tm
    tm = parser['enb']['tm']

    global nof_ports
    nof_ports = parser['enb']['nof_ports']

    global tx_gain
    tx_gain = parser['rf']['tx_gain']

    global rx_gain
    rx_gain = parser['rf']['rx_gain']

    global device_name
    device_name = parser['rf']['device_name']

    global device_args
    device_args = parser['rf']['device_args']

readEnbConfig()


def writeEnbConfig():
    parser['enb']['enb_id'] = enb_id_entry.get()
    parser['enb']['mcc'] = mcc_entry.get()
    parser['enb']['mnc'] = mnc_entry.get()
    parser['enb']['mme_addr'] = mme_addr_entry.get()
    parser['enb']['gtp_bind_addr'] = gtp_bind_addr_entry.get()
    parser['enb']['s1c_bind_addr'] = s1c_bind_addr_entry.get()
    parser['enb']['s1c_bind_port'] = s1c_bind_port_entry.get()
    parser['enb']['n_prb'] = n_prb_entry.get()
    parser['enb']['tm'] = tm_entry.get()
    parser['enb']['nof_ports'] = nof_ports_entry.get()

    parser['rf']['tx_gain'] = tx_gain_entry.get() 
    parser['rf']['rx_gain'] = rx_gain_entry.get()
    parser['rf']['device_name'] = device_name_entry.get()
    parser['rf']['device_args'] = device_args_entry.get()

    
    with open('enb.conf', 'w') as enbConfig:
        parser.write(enbConfig)

enbcfg = tk.Tk()
enbcfg.geometry("720x330")
enbcfg.title('srsENB Config')
enbcfg.resizable(0, 0)

enbcfg.columnconfigure(0, weight=1)
enbcfg.columnconfigure(1, weight=1)

def fillValues():
    readEnbConfig()

    global enb_id_entry
    enb_id_label = ttk.Label(enbcfg, text="eNB ID:")
    enb_id_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    enb_id_entry = tk.Entry(enbcfg)
    enb_id_entry.grid(column=0, row=0)
    enb_id_entry.insert(0, enb_id)

    global mcc_entry
    mcc_label = ttk.Label(enbcfg, text="MCC:")
    mcc_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    mcc_entry = tk.Entry(enbcfg)
    mcc_entry.grid(column=0, row=1)
    mcc_entry.insert(0, mcc)

    global mnc_entry
    mnc_label = ttk.Label(enbcfg, text="MNC:")
    mnc_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
    mnc_entry = tk.Entry(enbcfg)
    mnc_entry.grid(column=0, row=2)
    mnc_entry.insert(0, mnc)

    global mme_addr_entry
    mme_addr_label = ttk.Label(enbcfg, text="MME Addr.:")
    mme_addr_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
    mme_addr_entry = tk.Entry(enbcfg)
    mme_addr_entry.grid(column=0, row=3)
    mme_addr_entry.insert(0, mme_addr)

    global gtp_bind_addr_entry
    gtp_bind_addr_label = ttk.Label(enbcfg, text="GTP-U Addr.:")
    gtp_bind_addr_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
    gtp_bind_addr_entry = tk.Entry(enbcfg)
    gtp_bind_addr_entry.grid(column=0, row=4)
    gtp_bind_addr_entry.insert(0, gtp_bind_addr)

    global s1c_bind_addr_entry
    s1c_bind_addr_label = ttk.Label(enbcfg, text="S1AP Addr.:")
    s1c_bind_addr_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
    s1c_bind_addr_entry = tk.Entry(enbcfg)
    s1c_bind_addr_entry.grid(column=0, row=5)
    s1c_bind_addr_entry.insert(0, s1c_bind_addr)

    global s1c_bind_port_entry
    s1c_bind_port_label = ttk.Label(enbcfg, text="S1AP Port.:")
    s1c_bind_port_label.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
    s1c_bind_port_entry = tk.Entry(enbcfg)
    s1c_bind_port_entry.grid(column=0, row=6)
    s1c_bind_port_entry.insert(0, s1c_bind_port)

    global n_prb_entry
    n_prb_label = ttk.Label(enbcfg, text="PRBs:")
    n_prb_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
    n_prb_entry = tk.Entry(enbcfg)
    n_prb_entry.grid(column=0, row=7)
    n_prb_entry.insert(0, n_prb)

    global tm_entry
    tm_label = ttk.Label(enbcfg, text="TM:")
    tm_label.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
    tm_entry = tk.Entry(enbcfg)
    tm_entry.grid(column=0, row=8)
    tm_entry.insert(0, tm)

    global nof_ports_entry
    nof_ports_label = ttk.Label(enbcfg, text="Ports:")
    nof_ports_label.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
    nof_ports_entry = tk.Entry(enbcfg)
    nof_ports_entry.grid(column=0, row=9)
    nof_ports_entry.insert(0, nof_ports)

    global tx_gain_entry
    tx_gain_label = ttk.Label(enbcfg, text="TX gain:")
    tx_gain_label.grid(column=1, row=0, sticky=tk.W, padx=2, pady=5)
    tx_gain_entry = tk.Entry(enbcfg)
    tx_gain_entry.grid(column=1, row=0)
    tx_gain_entry.insert(0, tx_gain)

    global rx_gain_entry
    rx_gain_label = ttk.Label(enbcfg, text="RX gain:")
    rx_gain_label.grid(column=1, row=1, sticky=tk.W, padx=2, pady=5)
    rx_gain_entry = tk.Entry(enbcfg)
    rx_gain_entry.grid(column=1, row=1)
    rx_gain_entry.insert(0, rx_gain)

    global device_name_entry
    device_name_label = ttk.Label(enbcfg, text="Dev name:")
    device_name_label.grid(column=1, row=2, sticky=tk.W, padx=2, pady=5)
    device_name_entry = tk.Entry(enbcfg)
    device_name_entry.grid(column=1, row=2)
    device_name_entry.insert(0, device_name)

    global device_args_entry
    device_args_label = ttk.Label(enbcfg, text="Dev args:")
    device_args_label.grid(column=1, row=3, sticky=tk.W, padx=2, pady=5)
    device_args_entry = tk.Entry(enbcfg)
    device_args_entry.grid(column=1, row=3)
    device_args_entry.insert(0, device_args)

    read_button = ttk.Button(enbcfg, text='read', command=fillValues)
    read_button.grid(column=0, row=10, sticky='we', padx=5, pady=5)

    write_button = ttk.Button(enbcfg, text='write', command=writeEnbConfig)
    write_button.grid(column=1, row=10, sticky='we', padx=5, pady=5)


    enbcfg.mainloop()

fillValues()