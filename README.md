Supported targets: el6, el7, el8

Depending on the target, this build of guacamol-server links with static builds of other components. The goal is to be able to install the package on [CentOS](https://www.centos.org/) without the need for external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used                      | Used on build for |
| :-------------------|:----------------------------------------------|:------------------|
| ffmpeg              | Sources 4.2.2 from upstream                   | el6, el7, el8     |
| freerdp             | Source package 2.0.0-46.rc4 from CentOS 8     | el6               |
| guacamole-server    | Sources 1.1.0 from upstream                   | el6, el7, el8     |
| libjpeg-turbo       | Source package 1.5.3-10 from CentOS 8         | el6               |
| libtelnet           | Source package 0.21-5 from EPEL7              | el8               |
| libssh2             | Source package 1.9.0-3 from Fedora 31         | el8               |
| nasm                | Source package 2.13.03-2 from CentOS 8        | el7, el8          |

Notes:
  - This RPM spec file creates a single package: guacamole-server11z
  - The package can be built easily using the script `rpmbuild-docker` provided in this repository. Docker is needed.
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
