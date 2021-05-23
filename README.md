Supported targets: el6, el7, el8

Depending on the target, this build of guacamole-server links with static builds of other components. The goal is to be able to install the package on [CentOS](https://www.centos.org/) without the need for external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used                      | Used on build for |
| :-------------------|:----------------------------------------------|:------------------|
| ffmpeg              | Sources 4.2.4 from upstream                   | el6, el7, el8     |
| freerdp             | Source package 2.2.0-1 from CentOS 8          | el6               |
| guacamole-server    | Sources 1.3.0 from upstream                   | el6, el7, el8     |
| libjpeg-turbo       | Source package 1.5.3-10 from CentOS 8         | el6               |
| libtelnet           | Source package 0.23-1 from EPEL7              | el6, el8          |
| libvncserver        | Source package 0.9.11-17 from CentOS 8        | el6, el7          |
| nasm                | Source package 2.15.03-3 from CentOS 8        | el6, el7          |

Notes:
  - This RPM spec file creates a single package: guacamole-server13z
  - The package can be built easily using the script `rpmbuild-docker` provided in this repository. In order to use this script, _**a functional Docker environment is needed**_, with ability to pull CentOS images from internet if not already downloaded.
  - Support for Kubernetes in guacd is only included in el7 builds. It requires to link with libwebsockets which is currently only available in EPEL7. Since we did not need Kubernetes support for our tests we did not push to support it for other CentOS versions.

How to build?
```
## run from this git base tree
$ ./rpmbuild-docker -d el6
$ ./rpmbuild-docker -d el7
$ ./rpmbuild-docker -d el8
```

How to check for updates?
```
## run from this git base tree
$ ./check-updates
```
