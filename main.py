'''
A simple code to write the names of all .lib (Release) and d.lib (Debug) files into separate text files. 
'''
import os
import fnmatch

visual_studio_ver = "vc16" # Default value is for Visual Studio 2019. You can change it to proper Visual Studio version that you installed
opencv_main_dir = "D:\\OpenCV_with_GPU_support\\" # Change it to directory where you have your compiled OpenCV files located in
opencv_lib_dir = opencv_main_dir + "install\\x64\\" + visual_studio_ver + "\\lib" 
opencv_ver = 454 # Change it to OpenCV version you have installed

is_exist = os.path.exists(opencv_lib_dir)
if not is_exist:
    print("Directory " +  opencv_lib_dir + " is not found")
else:
    print("Directory " +  opencv_lib_dir + " exists")

# .lib files named as <opencv_libname><opencv_version>.lib (e.g. opencv_core454.lib)
filename1 = "\\Libs_Release"
opencvlib_list_path = opencv_lib_dir + filename1 + ".txt"
f1 = open(opencvlib_list_path,"w+")
for filename in os.listdir(opencv_lib_dir):
     if fnmatch.fnmatch(filename, "*" + str(opencv_ver) + ".lib"):
        f1.write(filename + '\n')
f1.close()

# d.lib files named as <opencv_><libname><opencv_version><d>.lib (e.g. opencv_core454d.lib)
filename2 = "\\Libs_Debug"
opencvlib_list_path = opencv_lib_dir + filename2 + ".txt"
f2 = open(opencvlib_list_path,"w+")
for filename in os.listdir(opencv_lib_dir):
     if fnmatch.fnmatch(filename, "*" + str(opencv_ver) + 'd.lib'):
        f2.write(filename + '\n')
f2.close()
