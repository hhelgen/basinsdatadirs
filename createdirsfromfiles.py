#/usr/bin/env python
# encoding: utf-8
"""
    createdirsfromfiles.py - Parse the .dat file into .csv columns


    :param    None

    :returns None

    :raises None

    Henry Helgen, CSRA helgen.henry@epa.gov 
    

    How to Run
    In IDLE 3.5.1
    Run menu > Check Module Alt+X
    Run > Run Module  F5
    from command line
    python createdirsfromfiles.py 

    Show this docstring by the following commands in the Python Shell
    >>> import createdirsfromfiles
    >>> help(createdirsfromfiles)
    It is also known as the __doc__ dunder for the module.

    Description
    This program reads a directory list of files and creates those files into new directories with
    the same prefix. It uses copy2 which overwrites existing files and preserves permissions
    and timestamps. Assumes that the copy of OldBASINSCore to basinsdata was done before this program ran.
    A typical file has the naming convention  19090305_nhd.exe  The numeric portion becomes the new directory
    to match the old huc directory and file convention.
    The current state of OldBASINSCore is directories and files
    01010001
        01010001_census.exe
        ...
        01010001_nhd.exe
        01010001_pcs3.exe
    The current state of NewBASINSCore is just files
        01010006_census.exe
        ...
        01010006_nhd.exe
    The state after this will be in OldBASINSCore directory and files with NewBASINSCore files overwriting Old.
        

    Naming convention
    module names are lowercase
    classes are CamelCase
    exceptions end with "Error"
    variables are lower_case_with_underscores
    functions and methods are lower_case_with_underscores
    global variables start with g
    input parameters start with p
    return variables start with r
    module level constants are CAPITAL_WITH_UNDERSCORES


    Design
        read newdata directory files into a list
        iterate the list, writing a new directory matching the first 8 characters
        ignore create errors if the directory already exists
        write the new files into the new directory, overwriting existing files. 
        The __future__ import allows a Python3 print function with end='' to work in Python 2

    Testing
        Look for duplicate file replacement in directory 01070006
        

"""
from __future__ import print_function, division

__version__ = "0.1"
__author__  = "Henry Helgen, CSRA  helgen.henry@epa.gov"

### module imports
# 1. standard library imports
import sys
import io
import os
import shutil
import pathlib
#import argparse
import time
import logging

# 2. related third party imports

# 3. location application / library specific imports

# module level constants
#development
GNEW_DIR  = "C:\\h\\2-04CEAM\\basins\\FinalDeliverablesFromRESPEC\\NewBASINSCore"  #input new data core
GOLD_DIR = "C:\\h\\2-04CEAM\\basins\\FinalDeliverablesFromRESPEC\\OldBASINSCore"  #input old data core
GTARGET_DIR = "C:\\h\\2-04CEAM\\basins\\FinalDeliverablesFromRESPEC\\basinsdata"  #combined data core
#production
#GNEW_DIR  = "G:\\developer\\FinalDeliverablesFromRESPEC\\NewBASINSCore"  #input new data core
#GOLD_DIR = "G:\\developer\\FinalDeliverablesFromRESPEC\\OldBASINSCore"  #input old data core
#GTARGET_DIR = "G:\\developer\\FinalDeliverablesFromRESPEC\\basinsdata"  #combined data core

PYTHON_2 = sys.version_info[0] < 3
# trick for py2/3 compatibility
if 'basestring' not in globals():
    basestring = str
if not PYTHON_2:
    unicode = str
    GMAX = sys.maxsize
else:
    GMAX = sys.maxint

logging.basicConfig(level=logging.DEBUG, filename='program.log', format='%(levelname)s %(asctime)s:%(message)s',
                    filemode='w', datefmt='%Y%m%d %H%M%S')

### global variable declarations
global gstart             #program start timer
global gfiles             #file count

        
### class declarations

### function declarations
def main():
    """ main  calls startup, runs process, close_down"

        :param   None
        :returns None
        :raises  None

        Run main() - when invoked directly.
        python createdirsfromfiles.py 
        
    """
    
    print( '\nStart of createdirsfromfiles' )
    logging.info( '\nStart of createdirsfromfiles' )
    logging.info ('main: ' )

    #variable declarations
    global gstart #global start time
    gstart = time.time()
    global gfiles #global file count
    gfiles = 0
    prior_newdir = '' #newdir for comparison
    newdir = ''       #numeric portion of file is directory name

    try:
        # read files into list  
        startup()
        new_file_list = os.listdir(GNEW_DIR)
        logging.debug("newfilelist")
        for newfile in new_file_list:
            gfiles += 1

            # the numeric portion is the subdirectory
            newdir = newfile[0:8] 
            targetdir = os.path.join(GTARGET_DIR,newdir)
            logging.debug("newfile|"+newfile+"|"+" newdir|"+newdir+"|"+"\ntarget|"+targetdir+"|")
            # create the directory ignoring if it already exists
            pathlib.Path(targetdir).mkdir(parents=True, exist_ok=True)
            # copy the file replacing existing files and copying metadata
            shutil.copy2(os.path.join(GNEW_DIR,newfile), targetdir)

            #print dots as progress indicators, newline every 100
            if newdir != prior_newdir:
                print(".", end='')
            if gfiles % 100 == 0:
                print()
               
    except IOError as e:
        print ('main: exception: {0}'.format(e))
        logging.warning('main: exception log')
#        logging.exception('main: exception log')
    finally:
        close_down()  #cleanup
    
    logging.info("%d seconds  %d files" ,(time.time()-gstart) , gfiles)
    print ('\nEnd of createdirsfromfiles\n')
    logging.info('End of createdirsfromfiles\n')
    return


def startup():
    """
        startup validate parameters, 
       
        :param   None
        :returns None
        :raises  None

        Validates the input parameters. 
    """
    
    logging.info ('startup:' )
    logging.debug("new   |"+GNEW_DIR+"|")
    logging.debug("old   |"+GOLD_DIR+"|")
    logging.debug("target|"+GTARGET_DIR+"|")

        
    # function variables
    # must use global keyword in this function to reference global variable, not redifine it as local.

    return   

def close_down():
    """ close_down final processing, close files
    
       :param   None
       :returns None
       :raises  
       
       """
    logging.info ('close_down:' )
    return


###
### main body
if __name__ == '__main__':
    main()
    
### end of createdirsfromfiles.py


