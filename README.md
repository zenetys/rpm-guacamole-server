| <nobr>Package name</nobr> | <nobr>Supported targets</nobr> |
| :--- | :--- |
| guacamole-server16z | el8, el9 |
<br/>

Depending on the target, this build of guacamole-server links with static
builds of other components. The goal is to be able to install the package
on [RedHat](https://www.redhat.com/) and clones without the need for
external RPM repositories others than [EPEL](https://fedoraproject.org/wiki/EPEL).

| Component           | Sources and patches used            | Used on build for    |
| :-------------------|:------------------------------------|:---------------------|
| ffmpeg              | Sources 4.2.x from upstream         | el8, el9             |
| guacamole-server    | Sources from upstream               | el8, el9             |
<br/>

## Build:

The package can be built easily using the rpmbuild-docker script provided
in this repository. In order to use this script, _**a functional Docker
environment is needed**_, with ability to pull Rocky Linux (el8, el9)
images from internet if not already downloaded.

```
$ ./rpmbuild-docker -d el8
$ ./rpmbuild-docker -d el9
```

## Prebuilt packages:

Builds of these packages are available on ZENETYS yum repositories:<br/>
https://packages.zenetys.com/latest/redhat/
