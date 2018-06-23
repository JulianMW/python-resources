#List current environments from within Jupyter
!conda-env list

#Creating a new conda virtual environment
$ conda create --name <envname> python=3.6

#Activate virtual environment
$ activate <envname>
or on linux
$ source activate <envname>


#Add the virtual environment to your ipython kernel
$ pip install ipykernel
$ python -m ipykernel install --user --name dsenv --display-name "DataScience"
