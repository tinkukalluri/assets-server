import os

# dir=os.chdir("C:/Users/sintin/Desktop/Projects_3/assets-server/assets_server/images/asset/images")
for filename in os.listdir("C:/Users/sintin/Desktop/Projects_3/assets-server/assets_server/images/asset/images/project1"):
    print(filename)




# this is intresting snippet of code on how to open all file in a list
# import os

# for filename in os.listdir("files"):
#    with open(os.path.join("files", filename), 'r') as f:
#        text = f.read()
#        print(text)
