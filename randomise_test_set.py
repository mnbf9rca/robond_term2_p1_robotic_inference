import os, random, shutil
# requires python 3.6 or later
# sometimes random.choices creates duplicates in teh list - just rerun


target_test_size = 0.1 # % to extract for test

num_files = len([name for name in os.listdir('.') if os.path.isfile(name)])
# random.choices is new in 3.6
selected_files = random.choices(os.listdir('.'),k=int(num_files * target_test_size))
for f in selected_files:    
    print(f)
    shutil.move(os.path.join(os.getcwd(), f), os.path.join(os.getcwd(),'test',f))