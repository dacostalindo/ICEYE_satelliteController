# -*- coding: utf-8 -*-
"""
Author: Manuel da Costa Lindo
Data created: April 22nd 2021
Last modified: xxxx
Purpose: Using Python 3.x, parse all the binary frames in the ‘telemetry.bin’ file attached according
 to thestructure described in ‘TLM_LIST.csv’. Extract time, position and attitude information andexport 
 this data to STK format in order to make the data available to be imported and replayed.

"""
import struct


def read_binary(filename, chunck_size):
    with open(filename, "rb") as file:
        binary = file.read()
        file.close()
        num_chuncks = len(binary)/chunck_size
        time_dict = {}
        print(struct.unpack('BBB', binary[54:57]))
        # for chunck in range(num_chuncks):
        # # for chunck in range(10):
        #     # print("Chunck #{}".format(chunck+1))
        #     counter_position = (chunck*chunck_size)
        #     # print("     The following byte {} is being unpacked.".format(inital_byte_position+1))
        #     counter = struct.unpack('B', binary[counter_position:counter_position+1])
        #     counter = counter[0]
        #     time_position = (chunck*chunck_size)+33 # VERIFY - maybe it's 32 or 34
        #     # print("     The following byte {} is being unpacked.".format(inital_byte_position))
        #     time_TAI = struct.unpack('I', binary[time_position:time_position+4])
        #     time_TAI = time_TAI[0]
        #     # print(time_TAI[0])

        #     #CHECK TIME VALID
        #     if time_TAI not in time_dict.keys():
        #         time_dict[time_TAI] = [counter]
        #     else:
        #         time_dict[time_TAI].append(counter)
        #     time_dict[time_TAI].sort()
        
        # print(time_dict)
        # for time in time_dict.keys():
        #     print(time/(60*60*24*365))
        # print(time_dict.keys())


            

def main():
    filename = "telemetry.bin"
    chunck_size = 2068
    read_binary(filename, chunck_size)


if __name__ == "__main__":
    main()