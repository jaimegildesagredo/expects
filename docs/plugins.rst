Plugins
=======

Introduction
------------

**Expects** is extensible via *plugins*. In fact, the `builtin assertions <reference.html>`_ is a plugin (the default one). Each plugin consists of a *name* and a *callable object* which is the plugin itself.

To use an especific plugin we should call ``expect`` with the plugin name and the subject value as a keyword argument. Doing this will return the result of calling the plugin callable. For example, a *request* plugin would look like this::

    expect(request=my_request_obj).to.have.header('Content-Type')

The *default* plugin could also be called passing the subject value as a positional argument instead of passing its name as a keyword argument::

    expect(default='foo').to.match('\w+')

Will be the same that::

    expect('foo').to.match('\w+')

.. note::

    Clarify that the second option is the prefered way for using the *builtin* assertions (or default plugin).

Writing plugins
---------------

As said above, a *plugin* consists of a *name* and a *callable object* that should return the plugin instance. The name will be the name that we give it when we register the plugin (see below). The callable object, which can be a class or a function that returns an object, should receive the *subject* of the expectation as the first positional argument. Also it should receive a set of positional arguments that will be the initial failure message parts.

Let's start writing our plugin callable::

    class MyPlugin(object):
        def __init__(self, actual, *message):
            self.actual = actual
            self.message = message

When the plugin has been registered and we call ``expect(my_plugin='foo')`` the resulting object will the be same as if we instantiate the ``MyPlugin`` class as follows::

    MyPlugin('foo', 'Expected', 'my_plugin')

Now that we have our initial plugin class we need to register it so we can use it with the ``expect(my_plugin=...)`` syntax. To to that we should use `setuptools to distribute <http://pythonhosted.org//setuptools/setuptools.html#basic-use>`_ our plugin and add the following `entry point <http://pythonhosted.org//setuptools/setuptools.html#entry-points>`_ to the ``setup.py`` file::

    setup(
        [...]

        entry_points={
            'expects.plugins': [
                'my_plugin = my_plugin_module:MyPlugin'
            ]
        }
    )

Then we just need to install our plugin via setuptools and import ``expect`` to start writing assertions with it::

    from expects import expect

    expect('foo').to.have.length(3)
    expect(my_plugin='foo').to.wathever.you.want

.. note::

    To a *more-in-depth* view of how a real plugin can be written take a look at the `default plugin source code <https://github.com/jaimegildesagredo/expects/blob/master/expects/expects.py>`_.
