import os
from datetime import datetime
realdate = datetime.today().strftime('%d.%m.%Y')

source_folder = r'C:\folderex'

for item in os.listdir(source_folder):
    if os.path.isfile(os.path.join(source_folder,item)):
        itemName=item.split("(")[0]
        if item.endswith('.xlsx'):
                os.rename(os.path.join(source_folder,item),
                    os.path.join(source_folder,itemName+"("+realdate+").xlsx")
                    )
                
#Developed by Setsuke 20/05/2024
#https://github.com/setsuke