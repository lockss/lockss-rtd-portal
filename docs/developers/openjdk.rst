You can check if a Java Development Kit (JDK) is installed on your system by typing ``javac -version`` at the command line and seeing if you get a valid response. (The version numbers output by Java 8 software sometimes use the notation 1.8, for example ``1.8.0_332``.)

If you need to install a JDK, we recommend OpenJDK; select your operating system below and follow the instructions (as ``root``):

.. COMMENT OSTABS

.. tabs::

   .. group-tab:: AlmaLinux

      .. include:: openjdk-dnf.rst

   .. group-tab:: Arch Linux

      .. include:: openjdk-pacman.rst

   .. group-tab:: CentOS

      .. tabs::

         .. group-tab:: CentOS 7

            .. include:: openjdk-yum.rst

         .. group-tab:: CentOS 8

            .. include:: openjdk-dnf.rst

         .. group-tab:: CentOS Stream 8-9

            .. include:: openjdk-dnf.rst

   .. group-tab:: Debian

      .. include:: openjdk-apt.rst

   .. group-tab:: EuroLinux

      .. tabs::

         .. group-tab:: EuroLinux 7

            .. include:: openjdk-yum.rst

         .. group-tab:: EuroLinux 8-9

            .. include:: openjdk-dnf.rst

   .. group-tab:: Fedora

      .. include:: openjdk-dnf.rst

   .. group-tab:: Linux Mint

      .. include:: openjdk-apt.rst

   .. group-tab:: OpenSUSE

      .. tabs::

         .. group-tab:: OpenSUSE Leap 15

            .. include:: openjdk-zypper.rst

         .. group-tab:: OpenSUSE Tumbleweed

            .. include:: openjdk-zypper.rst

   .. group-tab:: Oracle Linux

      .. tabs::

         .. group-tab:: Oracle Linux 7

            .. include:: openjdk-yum.rst

         .. group-tab:: Oracle Linux 8-9

            .. include:: openjdk-dnf.rst

   .. group-tab:: RHEL

      .. tabs::

         .. group-tab:: RHEL 7

            .. include:: openjdk-yum.rst

         .. group-tab:: RHEL 8-9

            .. include:: openjdk-dnf.rst

   .. group-tab:: Rocky Linux

      .. include:: openjdk-dnf.rst

   .. group-tab:: Scientific Linux 7

      .. include:: openjdk-yum.rst

   .. group-tab:: Ubuntu

      .. include:: openjdk-apt.rst
