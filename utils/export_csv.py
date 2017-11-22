import tensorflow as tf
import os
import numpy as np
import pandas as pd
from tensorflow import gfile
from tensorflow import flags
from tensorflow import app
from tensorflow import logging
FLAGS=flags.FLAGS


if __name__=='__main__':
    flags.DEFINE_string("input_data_pattern","",
            "File glob for the video dataset(e.g. path/to/dataset/vid*.avi)")
    flags.DEFINE_string("output_csv_file","",
            "the output csv file name(the full path,e.g. path/to/output/file.csv)")



def get_df_form_video(input_data_pattern):
    try:
        logging.info("get filenames form video pattern")
        files=gfile.Glob(input_data_pattern)
    except:
        logging.error("something wrong when open the intput data pattern")
    
    files=np.unique(files)
    num_files=len(files)
    if num_files==0:
        logging.error("there is no file in this data pattern") 
   
    files=np.reshape(files,[num_files,1])
    labels=np.reshape(np.array([None]*num_files),[num_files,1])
    
    data=np.concatenate((files,labels),axis=1)
    
    df=pd.DataFrame(data,columns=["video_path","labels"])
    return df

def main(unused_argv):
    df=get_df_form_video(FLAGS.input_data_pattern)
    df.to_csv(FLAGS.output_csv_file,index=False)
    
if __name__ =="__main__":
    app.run()








