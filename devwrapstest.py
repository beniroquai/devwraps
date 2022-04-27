import devwraps

# removes all DLLs
devwraps.remove_dlls()

# look for DLLs according to the paths specified in `dll_paths.py`
devwraps.look_for_dlls()

# print the root folder of this module
print(devwraps.get_root_folder)