# opencv-libname-generator
A Python code to generate OpenCV release and debug library names.

While setting the Visual Studio for OpenCV projects, you need to provide names of libraries for release and debug configurations. This code provides a fast solution to extract names of the libraries into seperate text files, so you can copy and paste them into Visual Studio's "Additional Dependencies" menu. All you need to do is to provide a proper \lib path and run the Python code.

You can learn how to install OpenCV with CUDA support by reading this article: 
https://medium.com/@batuhanhangun/opencv454-gpu-support-cpp-bef2cc145090

You can learn how to set your Visual Studio environment for OpenCV by reading this article: 
https://medium.com/@batuhanhangun/setting-visual-studio-up-for-opencv-c-bd1b198b5113
