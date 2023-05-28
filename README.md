| Package&nbsp;name | Supported&nbsp;targets |
| :--- | :--- |
| guacamole-server15z | el7, el8, el9 |
<br/>

Support for el6 has been dropped in package guacamole-server15z. Checkout branch [guacamole-server14z](https://github.com/zenetys/rpm-guacamole-server/tree/guacamole-server14z) for el6.

Depending on the target, this build of guacamole-server links with static builds of other components. The goal is to be able to install the package on [RedHat](https://www.redhat.com/) and clones without the need for external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used            | Used on build for    |
| :-------------------|:------------------------------------|:---------------------|
| ffmpeg              | Sources 4.2.x from upstream         | el7, el8, el9   |
| guacamole-server    | Sources from upstream               | el7, el8, el9   |
| libvncserver        | Source package from Rocky Linux 8   | el7             |
| nasm                | Source package from Rocky Linux 8   | el7             |
<br/>

## Build:

The package can be built easily using the rpmbuild-docker script provided in this repository. In order to use this script, _**a functional Docker environment is needed**_, with ability to pull CentOS (el7) or Rocky Linux (el8, el9) images from internet if not already downloaded.

```
$ ./rpmbuild-docker -d el7
$ ./rpmbuild-docker -d el8
$ ./rpmbuild-docker -d el9
```

## Prebuilt packages:

Builds of these packages are available on ZENETYS yum repositories:<br/>
https://packages.zenetys.com/latest/redhat/
