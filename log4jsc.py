
import os

for path, currentDirectory, files in os.walk("logstash-7.15.2"):
    for file in files:
        if file.startswith("log4j-core-"):
            print(os.path.join(path, file))
            string1 = 'JndiLookup'
  

            filex = os.path.join(path, file)
            file1 = open(filex,errors="ignore")
  

            
            indx = 0
  

            for line in file1:  
                if string1 in line:
                    indx =indx+1
                    print ("OK: ", line)
                   
                
            if indx != 0:
                   
                
                print ("you are vuln")
            else:
                print ("you are safe")
               
  
  
            file1.close() 