=========================
Sphinx rstdemo extension
=========================

.. include:: ../README


Demo menu
===========

.. contents::
   :local:


Bullet list
-------------

.. rstdemo::

   Some text line.
   Second line will joined to 1st line.

   * item 1
   * item 2

     * item 2-1
     * item 2-2

   * item 3

.. tip:: You need blank line before and after nested items. And nested items need 2 spaces before ``*``.


Numbered list
-------------

.. rstdemo::

   1. item 1
   2. item 2

      #. item 2-1
      #. item 2-2

   3. item 3


.. tip:: `#.` rendering auto numbered list. but it is not human readable.

Code highlight
--------------

Use ``code-block`` directive to rendering code with highlighting.

.. rstdemo::

   .. code-block:: ruby

      class Foo
        def initialize(value)
          puts "value = #{value}"
        end
      end

.. note:: This directive was provided by sphinx. The same feature is provided by docutils-0.9 as :rst:dir:`code` directive.

Link to other pages
-------------------

Use :rst:dir:`toctree` directive to build a tree structure.

.. rstdemo::

   .. toctree::
      :numbered:
      :maxdepth: 2

      spam
      egg

.. note:: This directive was provided by sphinx.


Link to other pages
-------------------
Link between pages by using :rst:dir:`glossary` directive and :rst:role:`term` role:

.. rstdemo::

   .. glossary::

      Sphinx
         Sphinx is a docmentation generator.

      reStructuredText
         reST is markup language to make structured document.

   These glossary terms are linked from other pages
   by using `term` role like :term:`Sphinx`.


Link to other pages
-------------------
Link between pages by using :rst:role:`doc` role:

.. rstdemo::

   Link to another reST page with :doc:`subdir/index`.
   `subdir/index` will be replaced with title of
   that's document file.


Numerical formula
-----------------

Use :rst:dir:`math` directive to rendering numerical formula.

.. rstdemo::

   Pythagoras theorem is :math:`a^2 + b^2 = c^2`.

   .. math:: (a + b)^2 = a^2 + 2ab + b^2

   .. math::
      :nowrap:

      \begin{eqnarray}
         y    & = & ax^2 + bx + c \\
         f(x) & = & x^2 + 2xy + y^2
      \end{eqnarray}

.. note:: This directive was provided by sphinx. Same name directive was provided by docutils-0.8 or later, but it is bit different.


todo extension
-----------------

Add :mod:`sphinx.ext.todo` extension in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.todo',
   ]
   todo_include_todos = True

Then you can use :rst:dir:`todo` directive:

.. rstdemo::

   .. todo:: write test for this function.

and  :rst:dir:`todolist` directive:

.. rstdemo::

   .. todolist::


autodoc extension
-----------------

Add :mod:`sphinx.ext.autodoc` extension in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
   ]

Then you can use :rst:dir:`automodule` directive:

.. rstdemo::

   .. automodule:: person
      :members:


Link over internet
-------------------

Add :mod:`sphinx.ext.intersphinx` extension and intersphinx setting in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',  #<- added
   ]

   intersphinx_mapping = {
      'py': ('http://docs.python.jp/2/', None),
   }

Then your linking markups link remote pages:

.. rstdemo::

   This markup link to Python's official reference page:
   :py:func:`urllib.urlopen` on the :mod:`urllib` page.


Domains
--------

A domain is a collection of markup (directives and roles) to describe and link to objects belonging together.

.. rstdemo::

   .. py:function:: event.register(event_id, user_name)

      (description for this function here).

   You can use :py:func:`event.register` to register.

* ``:py:func:`event.register``` is *py* domain's *func* role that make lnik to the declaration line.
* ``.. py:function:: event.register(event_id, user_name)`` is *py* domain's *function* directive that make declaration of the function and create Sphinx's index page entry.


blockdiag extension
-------------------

Blockdiag extensions is 3rd party extension for sphinx.
Install :ref:`sphinxcontrib-blockdiag` extension:

.. code-block:: bash

   $ easy_install Pillow
   $ easy_install sphinxcontrib-blockdiag
   $ easy_install sphinxcontrib-seqdiag
   $ easy_install sphinxcontrib-actdiag
   $ easy_install sphinxcontrib-nwdiag


.. note::

   Pillow is successor of PIL (Python Imaging Library) that support
   Python3 and 64bit binary distributions.

And add ``sphinxcontrib.blockdiag`` extension in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
       'sphinxcontrib.blockdiag',  #<- added
   ]

Then you can use ``blockdiag`` directive:

.. rstdemo::

   .. blockdiag::

      {
          A [label="ME"];
          A -> B [label="Open"];
          A -> C;

          O -> P -> C;
      }


seqdiag extension
-------------------

Add ``sphinxcontrib.seqdiag`` extension in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
       'sphinxcontrib.blockdiag',
       'sphinxcontrib.seqdiag',  #<- added
   ]

Then you can use ``seqdiag`` directive:

.. rstdemo::

   .. seqdiag::

      {
          A  => B;
          A  -> B;
          A <-- B;

          A => C => D;
      }

