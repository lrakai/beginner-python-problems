import os


def traversal_count(path):
    '''
    Return the number of files traversed when walking the directory tree starting at the given path.
    The returned number should only count files and not directories.

    Arguments
    path: the path to a directory to start the traversal

    Examples (for this host system)
    traversal_count('/opt/yarn/bin/') returns 5
    traversal_count('/usr/share/X11/') returns 191
    '''

    # Store the number of files in the count variable
    count = 0

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will walk the file system starting
    #        from path and count the number of files with the count variable


    # ====================================
    # Do not change the code after this

    return count


if __name__ == '__main__':
    print(traversal_count('/opt/yarn/bin/'))
    print(traversal_count('/usr/share/X11/'))
