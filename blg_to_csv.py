import os
import subprocess

#FOR counting
counter=1000

#for relog
def run_file(path):

    global counter 
    counter=counter+1
    subprocess.run(f'relog -f csv {path} -o {str(counter)+'mem'}.csv' ) 
    
# for all file
#r"C:\\Users\\Ariake\\Desktop\\20230214\\log\\\13svnnap\\cpu"

def run_all_files(folder_path):

    for filename in os.listdir(folder_path):
        if filename.endswith(".blg"):
            joined_file = os.path.join(folder_path,filename)
            run_file(joined_file)
 

# folder_path = "C:\\Users\\Ariake\\Desktop\\20230214\\log\\13svnndb\\cpu"
# folder_path ="C:\\Users\\Ariake\\Desktop\\20230214\\log\\13svnndb\\mem"
# folder_path ="C:\\Users\\Ariake\\Desktop\\20230214\\log\\13svnndb\\net"
#folder_path ="C:\\Users\\Ariake\\Desktop\\20230214\\log\\20svnn\\cpu"
folder_path ="C:\\Users\\Ariake\\Desktop\\20230214\\log\\20svnn\\mem"
            
#folder_path ="C:\\Users\\Ariake\\Desktop\\20230214\\log\\20svnn\\net"




run_all_files(folder_path)




