import compileall

compileall.compile_dir('/home/zeon/workspace/Python/myGit/', force=True)

# Perform same compilation, excluding files in .svn directories.
import re
compileall.compile_dir('/home/zeon/workspace/Python/myGit/', rx=re.compile('/[.]svn'), force=True)
