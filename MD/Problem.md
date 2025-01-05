# **Problems To Tackle**

* How to display the listed options as buttons
* Solution: Use the same logic with Todo App


### How to make renaming and removing work
Using the os module, we can do it, but how do we know which file to remove, that needs some problem solving
we can say :
```
os.remove(self.value)
```
This works!
But for renaming we should use rename()
```
os.rename(self.value)
``` 
This raises a new problem that renaming a file although updates the UI and it also updates in the actual directory, doesn't allow to delete it
This happens because the TextField ID remains the same
TextField ID is self.value
so assigning self.edit_tf.value to self.value resolves the issue