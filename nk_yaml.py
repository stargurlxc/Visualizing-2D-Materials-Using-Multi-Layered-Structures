# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def read_nk(filename,L):

    import yaml
    import numpy as np
    
    len_L = len(L)
    n = np.ones(len_L) + 1j*np.zeros(len_L) #error returns vacuum
    print(f"\nread_nk: reading from '{filename}'")
    
    try:
        with open(filename, "r") as file:
            data_dict = yaml.safe_load(file)
            
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
        print("returning vacuum nk")
    except PermissionError:
        print("Error: You do not have the required permissions to access this file.")
        print("returning vacuum nk")
   
    except OSError as e:
        print(f"System Error: A general I/O fault occurred: {e}")
        print("returning vacuum nk")
  
    except Exception as e:
        print(f"Unexpected Error: {e}")
        print("returning vacuum nk")
       
    else:   
        DATA= data_dict['DATA']
        DATA = DATA[0]
        type = DATA['type']
        print(data_dict['REFERENCES'])
        print(data_dict['COMMENTS'])
        len_L = len(L)
        print(f"Requested {len_L} nk values from {L[0]:.3f} to {L[-1]:.3f} microns.")
         
        match type:
            case "formula 1":
                c = DATA['coefficients']
                c = np.fromstring(c, dtype=float, sep=" ")
                rr = DATA['wavelength_range']
                rr = np.fromstring(rr, dtype=float, sep=" ")
                print(f"Found data type '{type}' valid between {rr[0]:.3f} and {rr[1]:.3f} microns.")
                num_terms = round((len(c)-1)/2)
                cc = np.zeros(len(L))
                cc[:] = c[0]
                LL = L**2
                jj = 1
                for ii in range(num_terms):
                    cc = cc + c[jj]*LL/(LL-c[jj+1]**2)
                    jj = jj+2
                n = np.sqrt(cc+1)
                n = n + 1j*0  
            case "tabulated nk":
                dat = DATA['data']
                dat = np.fromstring(dat, dtype=float, sep=" ")
                rows_dat = round(len(dat)/3)
                dat = dat.reshape(rows_dat,3)
                print(f"Found data type '{type}' from {dat[0,0]:.3f} to {dat[-1,0]:.3f} microns.")
                n = np.interp(L,dat[:,0],dat[:,1])
                k = np.interp(L,dat[:,0],dat[:,2])
                n = n + 1j*k
            case _:
                print(f"unknown type: '{type}'")
                
    return n, L



