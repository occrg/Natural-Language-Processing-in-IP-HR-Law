"""
Supplies functionality to quickly manipulate file paths
"""

import os


def loadListOfFilePaths(folder):
    """
    Gives a list of file paths that are contained in ${folder}. This
    does not include, or go into, folders.

    Arguments:
    folder     (str)   -- the file path of the folder in which the list
                          of files is desired

    Returns:
    filePaths  ([str]) -- a list of strings with each string
                          representing a file in ${folder}
    """
    filePaths = []
    for file in os.listdir(folder):
        if '.' in file:
            path = os.path.join(folder, file)
            filePaths.append(path)
    return filePaths

def changeRootFolderAndExt(path, newRootName, newExt):
    """
    Replaces the root folder of the given path with ${newRootName} and
    replaces the extension of the file with ${newExt} but keeps the
    rest of the path.

    Arguments:
    path         (str) -- the original path to be changed
    newRootName  (str) -- the name of the new root folder
    newExt       (str) -- the name of the new file extension

    Returns:
    newPath      (str) -- the changed file path
    """
    first, rest = path.split('/', 1)
    centre, ext = rest.split('.')
    newPath = '%s/%s.%s' % (newRootName, centre, newExt)
    return newPath

def changeRootFolderAndExtRemoveArea(path, newRootName, newExt):
    """
    Replaces the root folder of the given path with ${newRootName} and
    replaces the extension of the file with ${newExt} and removes any
    folder between the root and filename.

    Arguments:
    path         (str) -- the original path to be changed
    newRootName  (str) -- the name of the new root folder
    newExt       (str) -- the name of the new file extension

    Returns:
    newPath      (str) -- the changed file path
    """
    rest, filenameAndExt = path.rsplit('/', 1)
    filename, ext = filenameAndExt.split('.')
    newPath = '%s/%s.%s' % (newRootName, filename, newExt)
    return newPath
