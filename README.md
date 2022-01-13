# Dashboard calculator
Hello everyone. This is a simple calculator that allows you to evaluate the location of blocks on the dashboard. After specifying the structure of the dashboard and the sizes of some blocks, the calculator will calculate the position of all blocks and their sizes. This calculator allows you to easily place blocks by coordinates. All dimensions are in pixels.

Example

![alt text](https://github.com/vonOrso/Dashboard_calculator/blob/main/Examples/Example.png?raw=true)

<details>
  <summary>User Guide</summary>
  
  The main dashboard_calculator function is in the defs_calculator. The Size_notebook contains a small example of how the function works.
  
  You need to specify the size of the dashboard.
  
  ![image](https://user-images.githubusercontent.com/43719238/149387416-85a14bb9-3404-40cf-9c53-26fc273d3f22.png)
  
  You also need to specify the structure of the dashboard. The db_hor_sizes parameter specifies the number of blocks on each line and their width. 
  
  ![image](https://user-images.githubusercontent.com/43719238/149390312-10f827da-25c1-4d88-be9e-aee2369f553f.png)
  
  If you specify 'Auto' instead of size for blocks, the calculator will automatically calculate their sizes depending on the remaining width. That is, if there are 500 pixels left (in width) and 'Auto' was specified for two blocks, then the system will create two blocks of 250 pixels each. The red arrows mark the width that was calculated automatically, and the orange arrows indicate the width that was originally set.

  ![image](https://user-images.githubusercontent.com/43719238/149388631-a29df55c-1f63-4871-bd26-c0c2465972ed.png)
  
  It is not necessary to specify the height of each block, instead db_ver_sizes sets the height for all blocks in the line.
  
  ![image](https://user-images.githubusercontent.com/43719238/149392071-e5c01292-f843-4cad-98c2-642cc9f1415b.png)

  ![image](https://user-images.githubusercontent.com/43719238/149391615-a72c1ef6-c640-48a9-9bbe-cd0a63f9cc00.png)
  
  ![image](https://user-images.githubusercontent.com/43719238/149393189-0dc9584a-4a7e-45df-9a38-f74b3a75055d.png)
  
  These four parameters are required to specify. The result is a picture with the desired coordinates and dimensions.
  
  ![alt text](https://github.com/vonOrso/Dashboard_calculator/blob/main/Examples/Example.png?raw=true)
</details>

<details>
  <summary>Additional Options</summary>
  
  global_borders - size of borders between blocks (type - int, default - 8);
  
  img_name_and_format - path, image name and type (type - st, default - '');
  
  save - should the image be saved? (type - str, default - 'No');
  
  show - should the image be showed? (type - str, default - 'Yes');
  
  font - text font (default - ImageFont.truetype("arial.ttf", size=30)); 
  
  background_color - background color (type - str, default - '#E5E5E5'); 
  
  block_color - block_color (type - str, default - 'white'); 
  
  text_color - text color (type - str, default - '#484848');
  
  outer_padding - outer padding of text (type - int, default - 4); 
  
  text_pos_correction - this setting needs to be adjusted if the default font has been changed (type - int, default - 35).
</details>
