{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Numpy Intro\n",
    "An introduction to the [Python Numpy](http://www.numpy.org/) numerical python library.  \n",
    "The core data structure behind Numpy is the n-dimensional [Numpy Array](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html). It is 3x to 10x faster and more memory efficient than Python's lists because, similar to Java arrays, it uses contiguous blocks of memory, and all elements are the same data type so there is no type checking at runtime. The Numpy library also includes many built-in code-saving mathematical functions that can be performed on an entire array or any slice of an array with a single line of code (ie. no for loops).  \n",
    "Numpy n-dimensional arrays are also sometimes referred to as nd-arrays.\n",
    "\n",
    "**Install Numpy** using pip:  pip install numpy\n",
    "The convention for importing numpy is *import numpy as np*.\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "### Creating a Numpy Array\n",
    "There are MANY ways to instantiate a numpy array. I covered the most common ones below. [Docs here cover more constructors](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-creation.html).\n",
    "- Pass in a list to the array() constructor\n",
    "- Use the arange function, similar to the range function but used for Numpy arrays. Uses arguments, (start, stop+1, step).\n",
    "- Use linspace to create an array of n equally spaced values. Uses arguments (start, stop, number of items).\n",
    "- Create an array empty, full of ones or zeros, or full of any fill value. Uses argument (shape) in the form of a tuple.  \n",
    "\n",
    "You can pass in dtype as an optional argument for any of these. This is especially useful if you want to limit memory usage for a very large array of small integers because int8 and int16 use much less space than the default int32."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  3  5  7  9 11]\n",
      "[ 1  3  5  7  9 11]\n",
      "[5.   5.25 5.5  5.75 6.   6.25 6.5  6.75 7.   7.25 7.5  7.75 8.  ]\n",
      "[[0. 0.]\n",
      " [0. 0.]\n",
      " [0. 0.]\n",
      " [0. 0.]]\n",
      "[[1 1 1]\n",
      " [1 1 1]]\n",
      "[88 88 88 88 88 88]\n",
      "[25 30 35 40]\n",
      "[[ 1  3  5]\n",
      " [ 7  9 11]]\n",
      "[[0 0 0]\n",
      " [0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,3,5,7,9,11])\n",
    "print(a)\n",
    "\n",
    "a = np.arange(1, 12, 2)    # (start, stop, step)\n",
    "print(a)\n",
    "\n",
    "a = np.linspace(5, 8, 13)  # (start, stop, number of items)\n",
    "print(a)\n",
    "\n",
    "a = np.zeros((4, 2))\n",
    "print(a)\n",
    "\n",
    "a = np.ones((2, 3), dtype=np.int16)\n",
    "print(a)\n",
    "\n",
    "a = np.full((6,), 88)\n",
    "print(a)\n",
    "\n",
    "a = np.fromstring('25 30 35 40', dtype=np.int, sep=' ')\n",
    "print(a)\n",
    "\n",
    "a = np.array([[1,3,5],[7,9,11]])\n",
    "print(a)\n",
    "\n",
    "b = np.zeros_like(a)    # _like gives you a new array in the same shape as the argument.\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Numpy Array Attributes\n",
    "Get size (number of items), shape (dimensions), itemsize(bytes of memory for each item), and dtype (numpy data type).  \n",
    "See how many bytes of memory space the whole array uses from the product of size and itemsize. See [complete list of attributes and methods](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "(2, 3)\n",
      "2\n",
      "4\n",
      "int32\n",
      "24\n"
     ]
    }
   ],
   "source": [
    "print(a.size)\n",
    "print(a.shape)\n",
    "print(a.ndim)\n",
    "print(a.itemsize)\n",
    "print(a.dtype)\n",
    "print(a.nbytes)  # same as a.size * a.itemsize"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Indexing and Slicing\n",
    "Use square brackets to get any item of an array by index. Multi-dimensional arrays can use multiple square brackets.\n",
    "\n",
    "There are three arguments for slicing arrays, all are optional: [start:stop:step].  \n",
    "    If start is left blank it defaults to 0. If stop is left blank it defaults to the end of the array. Step defaults to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  3  5]\n",
      " [ 7  9 11]]\n",
      "[ 7  9 11]\n",
      "5\n",
      "[]\n",
      "[[1 3 5]]\n",
      "[[ 7  9 11]]\n",
      "[[3]\n",
      " [9]]\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(a[1])\n",
    "print(a[0][2])\n",
    "print(b[2:4])\n",
    "\n",
    "print(a[:1])\n",
    "print(a[1:3:2])\n",
    "print(a[:, 1:2])  # all elements on dimension 0, only element 1 on dimension 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Reshape, Swap Axes, Flatten\n",
    "See full list of [array manipulation routines](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-9 -8 -7]\n",
      " [-6 -5 -4]]\n",
      "[[-9 -6]\n",
      " [-8 -5]\n",
      " [-7 -4]]\n",
      "[-9 -6 -8 -5 -7 -4]\n"
     ]
    }
   ],
   "source": [
    "c = np.arange(-9, -3,).reshape(2,3)\n",
    "print(c)\n",
    "\n",
    "c = c.swapaxes(0,1)\n",
    "print(c)\n",
    "\n",
    "c = c.flatten()\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use dtype to Save Space\n",
    "Default data types (int32 and float64) are memory hogs. If you don't need the higher precision you can save a lot of memory space and improve speed of operations by using smaller data types. For large data sets this makes a big difference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int32 <class 'numpy.int32'>\n",
      "400\n",
      "int8 <class 'numpy.int8'>\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "d = np.arange(0,100)\n",
    "print(d.dtype, type(d[1]))\n",
    "print(d.nbytes)\n",
    "\n",
    "d = np.arange(0,100, dtype='int8')\n",
    "print(d.dtype, type(d[1]))\n",
    "print(d.nbytes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### UpCasting, Rounding, Print Formatting\n",
    "Data type of all Items is upcast to the most precise element. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "float64\n",
      "[[1.57 2.   3.  ]\n",
      " [4.   5.   6.  ]]\n",
      "[[1.57 2.   3.  ]\n",
      " [4.   5.   6.  ]]\n"
     ]
    }
   ],
   "source": [
    "e = np.array([(1.566666,2,3), (4,5,6)])\n",
    "print(e.dtype)\n",
    "\n",
    "e = e.round(4)\n",
    "print(e)\n",
    "\n",
    "np.set_printoptions(precision=2, suppress=True)    # show 2 decimal places, suppress scientific notation\n",
    "print(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Numpy Data Types Available\n",
    "uint is unsigned int, for positive numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'complex': [<class 'numpy.complex64'>, <class 'numpy.complex128'>],\n",
      " 'float': [<class 'numpy.float16'>,\n",
      "           <class 'numpy.float32'>,\n",
      "           <class 'numpy.float64'>],\n",
      " 'int': [<class 'numpy.int8'>,\n",
      "         <class 'numpy.int16'>,\n",
      "         <class 'numpy.int32'>,\n",
      "         <class 'numpy.int32'>,\n",
      "         <class 'numpy.int64'>],\n",
      " 'others': [<class 'bool'>,\n",
      "            <class 'object'>,\n",
      "            <class 'bytes'>,\n",
      "            <class 'str'>,\n",
      "            <class 'numpy.void'>],\n",
      " 'uint': [<class 'numpy.uint8'>,\n",
      "          <class 'numpy.uint16'>,\n",
      "          <class 'numpy.uint32'>,\n",
      "          <class 'numpy.uint32'>,\n",
      "          <class 'numpy.uint64'>]}\n"
     ]
    }
   ],
   "source": [
    "import pprint as pp\n",
    "pp.pprint(np.sctypes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Reading and Writing to Files\n",
    "Can use [loadtxt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt), or [genfromtxt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt) to load data to load an entire file into an array at once. Genfromtxt is more fault tolerant.  \n",
    "Use [savetxt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html#numpy.savetxt) to write an array to file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[9 3 8 7 6 1 0 4 2 5]\n",
      " [1 7 4 9 2 6 8 3 5 0]\n",
      " [4 8 3 9 5 7 2 6 0 1]\n",
      " [1 7 4 2 5 9 6 8 0 3]\n",
      " [0 7 5 2 8 6 3 4 1 9]\n",
      " [5 9 1 4 7 0 3 6 8 2]]\n",
      "int32\n"
     ]
    }
   ],
   "source": [
    "f = np.loadtxt('data.txt', skiprows=1, delimiter=',', dtype=np.int32)\n",
    "print(f)\n",
    "print(f.dtype)\n",
    "\n",
    "np.savetxt('data2.txt', f, delimiter=';', fmt='%d', header='a;b;c;d;e;f;g;h;i;j', comments='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[9 3 8 7 6 1 0 4 2 5]\n",
      " [1 7 4 9 2 6 8 3 5 0]\n",
      " [4 8 3 9 5 7 2 6 0 1]\n",
      " [1 7 4 2 5 9 6 8 0 3]\n",
      " [0 7 5 2 8 6 3 4 1 9]\n",
      " [5 9 1 4 7 0 3 6 8 2]]\n"
     ]
    }
   ],
   "source": [
    "g = np.genfromtxt('data.txt', skip_header=1, delimiter=',', dtype=np.int32)\n",
    "print(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mathematical Functions\n",
    "Numpy has an extensive list of [math and scientific functions](https://docs.scipy.org/doc/numpy/reference/routines.html).  \n",
    "The best part is that you don't have to iterate. You can apply an operation to the entire array or a slice of an array at once."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ True False  True  True  True False False False False  True]\n",
      " [False  True False  True False  True  True False  True False]\n",
      " [False  True False  True  True  True False  True False False]\n",
      " [False  True False False  True  True  True  True False False]\n",
      " [False  True  True False  True  True False False False  True]\n",
      " [ True  True False False  True False False  True  True False]]\n",
      "[[80  8 63 48 35  0 -1 15  3 24]\n",
      " [ 0 48 15 80  3 35 63  8 24 -1]\n",
      " [15 63  8 80 24 48  3 35 -1  0]\n",
      " [ 0 48 15  3 24 80 35 63 -1  8]\n",
      " [-1 48 24  3 63 35  8 15  0 80]\n",
      " [24 80  0 15 48 -1  8 35 63  3]]\n"
     ]
    }
   ],
   "source": [
    "print(g > 4)\n",
    "print(g ** 2 - 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "9\n",
      "270\n",
      "4.5\n",
      "8.25\n",
      "2.8722813232690143\n",
      "[45 45 45 45 45 45]\n",
      "[0 3 1 2 2 0 0 3 0 0]\n",
      "6\n",
      "0\n",
      "[[6 5 8 1 7 9 4 3 2 0]\n",
      " [9 0 4 7 2 8 5 1 6 3]\n",
      " [8 9 6 2 0 4 7 5 1 3]\n",
      " [8 0 3 9 2 4 6 1 7 5]\n",
      " [0 8 3 6 7 2 5 1 4 9]\n",
      " [5 2 9 6 3 0 7 4 8 1]]\n"
     ]
    }
   ],
   "source": [
    "print(g.min())\n",
    "print(g.max())\n",
    "print(g.sum())\n",
    "print(g.mean())\n",
    "print(g.var())         # variance\n",
    "print(g.std())         # standard deviation\n",
    "\n",
    "print(g.sum(axis=1))\n",
    "print(g.min(axis=0))\n",
    "\n",
    "print(g.argmin())      # index of min element\n",
    "print(g.argmax())      # index of max element\n",
    "print(g.argsort())     # returns array of indices that would put the array in sorted order"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Column Operations\n",
    "Apply functions only to specific columns by slicing, or create a new array from the columns you want, then work on them.  \n",
    "But Beware that creating a new pointer to the same data can screw up your data if you're not careful."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[8]\n",
      " [4]\n",
      " [3]\n",
      " [4]\n",
      " [5]\n",
      " [1]]\n",
      "8\n",
      "298.607881119482\n",
      "[[    9     3     8 70000     6     1     0     4     2     5]\n",
      " [    1     7     4 90000     2     6     8     3     5     0]\n",
      " [    4     8     3 90000     5     7     2     6     0     1]\n",
      " [    1     7     4 20000     5     9     6     8     0     3]\n",
      " [    0     7     5 20000     8     6     3     4     1     9]\n",
      " [    5     9     1 40000     7     0     3     6     8     2]]\n"
     ]
    }
   ],
   "source": [
    "print(g[:, 2:3])\n",
    "print(g[:, 2:3].max())\n",
    "\n",
    "col3 = g[:, 3:4]      # not a copy, just a pointer to a slice of g\n",
    "print(col3.std())\n",
    "\n",
    "col3 *= 100           # Beware: this is applied to g data\n",
    "print(g)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Numpy Random Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "np.set_printoptions(precision=5, suppress=True)    # show 5 decimal places, suppress scientific notation\n",
    "h = np.random.random(6)\n",
    "print(h)\n",
    "\n",
    "h = np.random.randint(10, 99, 8)    # (low, high inclusive, size)\n",
    "print(h)\n",
    "\n",
    "np.random.shuffle(h)        # in-place shuffle\n",
    "print(h)\n",
    "\n",
    "print(np.random.choice(h))\n",
    "\n",
    "h.sort()                    # in-place sort\n",
    "print(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
