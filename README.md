# project-fossils
Shared repository for code related to the fossils project in Thomas Serre's lab at Brown University


INSTALLATION:
To install, follow procedure below:

1) git clone https://github.com/JacobARose/leavesdb.git

2) cd leavesdb

3) pip install -e .

ENVIRONMENT SETUP:
Note, this is simply a cloning of the conda environment used to create the package, and thus is not a minimum set of requirements. Creating a minimum environment specification is TBD.

1) Navigate to the root /leavesdb directory containing environment spec file 'leavesdb.yml'

2) conda env create -f leavesdb.yml -n leavesdb

Note, where it says "-n leavesdb' above, you can replace 'leavesdb" with your preferred choice of env name.

GETTING STARTED:
Take a look at leaves_db_demo.ipynb in the root directory for an example of how to interact with the database and query data.

MODIFICATION:
To modify and push changes to git:

1) Navigate to root directory of package (/leavesdb)

2) git add [list of files to commit]
	or
   git add --all

3) git commit -m "message describing changes"

4) git push

5) '[Enter GitHub login credentials]'
