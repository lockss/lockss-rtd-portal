To install OpenJDK, run this Homebrew command:

.. code-block:: shell

   brew install openjdk@8

.. note::

   You may be directed to create symlinks and/or update your :envvar:`PATH` to make OpenJDK visible to your system, for instance:

   .. code-block:: text

      For the system Java wrappers to find this JDK, symlink it with
        sudo ln -sfn /usr/local/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk

      openjdk@8 is keg-only, which means it was not symlinked into /usr/local,
      because this is an alternate version of another formula.

      If you need to have openjdk@8 first in your PATH, run:
        echo 'export PATH="/usr/local/opt/openjdk@8/bin:$PATH"' >> ~/.zshrc

      For compilers to find openjdk@8 you may need to set:
        export CPPFLAGS="-I/usr/local/opt/openjdk@8/include"
