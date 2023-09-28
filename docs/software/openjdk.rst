You can check if a Java Development Kit (JDK) is installed on your system by typing ``javac -version`` at the command line and seeing if you get a valid response. (The version numbers output by Java 8 software sometimes use the notation 1.8, for example ``1.8.0_382``.)

If you need to install a JDK, we recommend OpenJDK; select your operating system below and follow the instructions (as ``root``, except for Homebrew on MacOS):

.. COMMENT OSTABS

.. tab-set::
   :class: sd-bg-light

   .. tab-item:: AlmaLinux OS
      :sync: alma

      .. include:: openjdk-dnf.rst

   .. tab-item:: Arch Linux
      :sync: arch

      .. include:: openjdk-pacman.rst

   .. tab-item:: CentOS
      :sync: centos

      .. tab-set::

         .. tab-item:: CentOS Stream 8-9
            :sync: centosstream8

            .. include:: openjdk-dnf.rst

         .. tab-item:: CentOS 8
            :sync: centos8

            .. include:: openjdk-dnf.rst

         .. tab-item:: CentOS 7
            :sync: centos7

            .. include:: openjdk-yum.rst

   .. tab-item:: Debian
      :sync: debian

      .. include:: openjdk-apt.rst

   .. tab-item:: EuroLinux
      :sync: eurolinux

      .. tab-set::

         .. tab-item:: EuroLinux 8-9
            :sync: eurolinux8

            .. include:: openjdk-dnf.rst

         .. tab-item:: EuroLinux 7
            :sync: eurolinux7

            .. include:: openjdk-yum.rst

   .. tab-item:: Fedora Linux
      :sync: fedora

      .. include:: openjdk-dnf.rst

   .. tab-item:: Linux Mint
      :sync: mint

      .. include:: openjdk-apt.rst

   .. tab-item:: MacOS
      :sync: macos

      .. tab-set::

         .. tab-item:: Homebrew
            :sync: homebrew

            .. include:: openjdk-brew.rst

         .. tab-item:: MacPorts
            :sync: macports

            .. include:: openjdk-port.rst

   .. tab-item:: OpenSUSE
      :sync: opensuse

      .. tab-set::

         .. tab-item:: OpenSUSE Leap 15
            :sync: opensuse15

            .. include:: openjdk-zypper.rst

         .. tab-item:: OpenSUSE Tumbleweed
            :sync: opensusetumbleweed

            .. include:: openjdk-zypper.rst

   .. tab-item:: Oracle Linux
      :sync: oracle

      .. tab-set::

         .. tab-item:: Oracle Linux 8-9
            :sync: oracle8

            .. include:: openjdk-dnf.rst

         .. tab-item:: Oracle Linux 7
            :sync: oracle7

            .. include:: openjdk-yum.rst

   .. tab-item:: RHEL
      :sync: rhel

      .. tab-set::

         .. tab-item:: RHEL 8-9
            :sync: rhel8

            .. include:: openjdk-dnf.rst

         .. tab-item:: RHEL 7
            :sync: rhel7

            .. include:: openjdk-yum.rst

   .. tab-item:: Rocky Linux
      :sync: rocky

      .. include:: openjdk-dnf.rst

   .. tab-item:: Scientific Linux
      :sync: scientific

      .. include:: openjdk-yum.rst

   .. tab-item:: Ubuntu
      :sync: ubuntu

      .. include:: openjdk-apt.rst
