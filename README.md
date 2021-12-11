# Drawio Convert

A script for export all drawio files to flat images (i.e. png).

I used this frequently for preparing images for my blogs.

It searches for all files with "*.drawio" extension and converts them one by one.
It will also ignore files that have no updates since the last run.

## Dependencies

### Draw.io App

This script assumed that you are on MacOS and you've installed the Draw.io application.

If you don't, install it from here https://github.com/jgraph/drawio-desktop.

This application comes with a command line tool as well.

To double check:

```
$ /Applications/draw.io.app/Contents/MacOS/draw.io --version
15.8.7
```

### Python 3

Check which python is being invoke from shell:

```
$ which python
```

If the output is managed by conda, e.g.:

* `/opt/miniconda3/bin`
* `/Users/yuchen/miniconda3/bin/python`

Then it is all good. We can use that.

Also make sure the version of the Python is 3.9 and above.

```
$ python --version
Python 3.9.1
```

### If Python is Too Old

Check which python is being invoke from shell:

```
$ which python
/usr/bin/python
```

And check which version of the python it is linking to:

```
ls -l /usr/bin/python                            lrwxr-xr-x  1 root  wheel  75  8 Nov  2019 /usr/bin/python -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7
```

Here we can see it is pointing to a pretty old version of python 2.

Let's swap that out with the one managed by miniconda.

```
$ conda activate
$ which python
/Users/yuchen/miniconda3/bin/python
$ python --version
Python 3.7.11
$ ln -s /Users/yuchen/miniconda3/bin/python /usr/local/bin/python
```

And to double check:

```
$ conda deactivate
$ which python
/usr/local/bin/python
$ python --version
Python 3.9.1
```

## Testing & Developing

```
$ python drawio_convert/drawio_convert.py
```

## Installation

```
$ pip install .
Processing /Users/yuchen/Documents/drawio_convert
Installing collected packages: drawio-convert
  Running setup.py install for drawio-convert ... done
Successfully installed drawio-convert-0.1
```

### Create symbolic link for drawio (Optional)

This is optional only if it is not part of `$PATH`.

```
ln -s /Users/yuchen/miniconda3/bin/drawio /usr/local/bin/drawio
```

## Use

In any folder that contains drawio files.

```
$ drawio
```
