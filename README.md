> [!NOTE]
> **This branch is not maintained anymore.**

Supported targets:<br/>
el6, el7, el8, el9

Package name:<br/>
guacamole-server14z

Depending on the target, this build of guacamole-server links with static builds of other components. The goal is to be able to install the package on [RedHat](https://www.redhat.com/) and clones without the need for external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used            | Used on build for    |
| :-------------------|:------------------------------------|:---------------------|
| ffmpeg              | Sources 4.2.x from upstream         | el6, el7, el8, el9   |
| freerdp             | Source package from Rocky Linux 8   | el6                  |
| guacamole-server    | Sources from upstream               | el6, el7, el8, el9   |
| libjpeg-turbo       | Source package from Rocky Linux 8   | el6                  |
| libtelnet           | Source package from EPEL7           | el6                  |
| libvncserver        | Source package from Rocky Linux 8   | el6, el7             |
| nasm                | Source package from Rocky Linux 8   | el6, el7             |

Support for Kubernetes in guacd is not included in el6 build.

Build:

The package can be built easily using the rpmbuild-docker script provided in this repository. In order to use this script, _**a functional Docker environment is needed**_, with ability to pull CentOS (el6, el7) or Rocky Linux (el8, el9) images from internet if not already downloaded.

```
$ ./rpmbuild-docker -d el6
$ ./rpmbuild-docker -d el7
$ ./rpmbuild-docker -d el8
$ ./rpmbuild-docker -d el9
```

Prebuilt packages:

Builds of these packages are available on ZENETYS yum repositories:<br/>
https://packages.zenetys.com/latest/redhat/
