"""
===============================================================================

Purpose: Set of utilities

===============================================================================

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

===============================================================================
"""

import shutil
import os


class MMVUtils:
    def __init__(self):
        self.os = self.get_os()

    # Get operating system [linux, windows, macos]
    def get_os(self):
        return {
            "posix": "linux",
            "nt": "windows",
            "darwin": "macos"
        }.get(os.name)

    # Get a executable from path, returns False if it doesn't exist
    def get_executable_with_name(self, name, extra_paths = []):

        # Force list variable
        extra_paths = self.force_list(extra_paths)
        search_path = os.environ["PATH"] + os.pathsep + os.pathsep.join(extra_paths)

        # Locate it
        locate = shutil.which(name, path = search_path)

        # If it's not found then return False
        if locate is None:
            return False
            
        # Else return its path
        return locate
    
    # If data is string, "abc" -> ["abc"], if data is list, return data
    def force_list(self, data):
        if not isinstance(data, list):
            data = [data]
        return data

    # Get the basename of a path
    def get_basename(self, path):
        return os.path.basename(path)
    
    # Return an absolute path always, recommended
    def get_abspath(self, path, silent = False):
        
        debug_prefix = "[Utils.get_abspath]"

        if self.os == "linux":
            if not silent:
                print(debug_prefix, "Linux: Expanding path with user home folder ~ if any")
            path = os.path.expanduser(path)
       
        abspath = os.path.abspath(path)

        if not silent:
            print(debug_prefix, f"abspath of [{path}] > [{abspath}]")

        return self.get_realpath(abspath)
    
    # Some files can be symlinks on unix or shortcuts on Windows, get the true real path
    def get_realpath(self, path):
        realpath = os.path.realpath(path)

        if not realpath == path:
            print(f"[Utils.get_realpath] Realpath of [{path}] > [{realpath}")
            
        return realpath

    # Get the filename without extension /home/linux/file.ogg -> "file"
    def get_filename_no_extension(self, path):
        return os.path.splitext(os.path.basename(path))[0]