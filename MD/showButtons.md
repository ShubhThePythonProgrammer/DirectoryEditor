# **How to Show Buttons in my software**

* Using ToDo's app logic I can create buttons in my software. But how do I show all of the files and directories in the working directory?
* Let's use a for loop to iterate through all the files and directories in the working directory and create a button for each file or directory.

* let's use the os module to get the list of files and directories in the working directory.

* we can store the files and directories in a list and then use for loop to iterate through the list and create a button for each file or directory.

* once we have done all of the above shit then we can add tools to the side of the button like in ToDo App where I have done the same thing with Tasks.

In Code:
```
import os
from flet import *

... The code needed for other things in the software...

# Get the list of files and directories in the working directory

content = list(os.listdir())

for i in content:
    # Create a button for each file or directory
    FetchFiles(i, self.RemoveFiles)
```

# **This works**