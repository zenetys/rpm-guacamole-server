Supported targets: el6, el7, el8

Depending on the target, this build of guacamole-server links with static builds of other components. The goal is to be able to install the package on [RedHat](https://www.redhat.com/) and clones without the need for external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used            | Used on build for    |
| :-------------------|:------------------------------------|:---------------------|
| ffmpeg              | Sources 4.2.x from upstream         | el6, el7, el8        |
| freerdp             | Source package from Rocky Linux 8   | el6                  |
| guacamole-server    | Sources from upstream               | el6, el7, el8        |
| libjpeg-turbo       | Source package from Rocky Linux 8   | el6                  |
| libtelnet           | Source package from EPEL7           | el6                  |
| libvncserver        | Source package from Rocky Linux 8   | el6, el7             |
| nasm                | Source package from Rocky Linux 8   | el6, el7             |

Notes:
  - This RPM spec file creates a single package: guacamole-server14z
  - The package can be built easily using the script `rpmbuild-docker` provided in this repository. In order to use this script, _**a functional Docker environment is needed**_, with ability to pull CentOS (el6, el7) or Rocky Linux (el8) images from internet if not already downloaded.
  - Support for Kubernetes in guacd is only included in el7 builds. It requires to link with libwebsockets which is currently only available in EPEL7. Since we did not need Kubernetes support for our tests we did not push to support it for other versions.

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
