Title: Fingerprints
Notice:    Licensed to the Apache Software Foundation (ASF) under one
           or more contributor license agreements.  See the NOTICE file
           distributed with this work for additional information
           regarding copyright ownership.  The ASF licenses this file
           to you under the Apache License, Version 2.0 (the
           "License"); you may not use this file except in compliance
           with the License.  You may obtain a copy of the License at
           .
             http://www.apache.org/licenses/LICENSE-2.0
           .
           Unless required by applicable law or agreed to in writing,
           software distributed under the License is distributed on an
           "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
           KIND, either express or implied.  See the License for the
           specific language governing permissions and limitations
           under the License.

<style type="text/css">
  table { font-size: 12px }
</style>

### FreeBSD: ###

| Name | Os | HW | CPU | RAM | Disk | Arrays | Services | Location | Comissioned | Class |
|-----|----|----|-----|-----|------|--------|----------|----------|-------------|-------|
| baldr | 9.1-RELEASE | DPE 1950 | E5420@2.50GHz 2x4=8 | 4x2@667MHz + 4x4@667MHz=24GB | 2x931GB@7.2k gpt+zmirror |  | Jails - Services | OSUOSL | 2008/02 | dm |
| minotaur | 9.1-RELEASE | HP DL580G7 | E7540@2.00GHz 4x2x6=48 | 8*4@1333MHz = 32GB | 4x146GB@10k | Powervault 220S:15x500GB@7.2k raidz2 + 2x120GB SSD l2arc | e-mail, SSH, seed | OSUOSL | 2011/04 | people |
| eos | 9.1-RELEASE | DPE r410 | X5550@2.67GHz 2x4x2=16 | 6x8@1333MHz = 48GB | 2x160GB@7.2k gpt+zmirror | Storform D55J:10x300GB@10k +2x75GB SSD raidz2 l2 arch | US: www, rsync, mod_mbox, wiki | OSUOSL | 2010/06 | www, wiki, rsync |
| metis | 9.1-RELEASE | DPE r510 | X5650@2.66GHz 2x6=12 | 8x4@1333MHz = 32GB | 6x600GB@15k 2x100GB SSD | | Jails - TLPs | OSUOSL | 2010/12 | dm |
| harmonia | 9.1-RELEASE | DPE r510 | E5649@2.53GHz 2x6=12 | 6x4@1333MHz = 24GB | 2x300GB SAS@15k, 2x100GB SSD, 6x2TB SATA | | EU: svn, ldap | FUB | 2012/06 | svn |

### SunOS: ###

| name | os | HW | Arrays | Services | Location | Comissioned | Class |
|------|----|----|--------|----------|----------|-------------|-------|
| odyne | 10u5 x86 | n/a |  | Zones | SARA | 2008/05 | zones |
| thor | 10u8 | Sun T5220 Sparc |  | Dist,private arch,Confluence(cwiki) | OSUOSL | 2008/07 | dist |

### Ubuntu: ###

| Name | Os | HW | CPU | RAM | Disk | Arrays | Services | Location | Comissioned | Class |
|-----|----|----|-----|-----|------|--------|----------|----------|-------------|-------|
| arcas | 12.04.2 LTS | r410 | X5550@2.67GHz 2x4x2=16 | 8x8GB@1333MHz = 64GB | | | Jira | OSUOSL | 2010/07 | jira |
| crius | 12.04.5 LTS | r720 | E5-2665@2.6GHz | 4x16=64 @ 1600MHz| 1x200SSD + 2x300SAS RAID1 + 5 x 600SAS |  | CI (Jenkins Master) | OSUOSL | 2013/06 | ci, jenkins |
| lares | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Buildbot slave) | Y! | 2014/07 | ci, bb |
| orcus | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Buildbot slave) | Y! | 2014/07 | ci, bb |
| penates | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Jenkins slave) | Y! | 2014/07 | ci, jenkins |
| pietas | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Jenkins slave) | Y! | 2014/07 | ci, jenkins |
| pomona | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Jenkins slave) | Y! | 2014/07 | ci, jenkins |
| priapus | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Jenkins slave) | Y! | 2014/07 | ci, jenkins |
| proserpina | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Jenkins slave) | Y! | 2014/07 | ci, jenkins |
| silvanus | 14.04 LTS | HP Proliant DL180 G6  |  | 50GB |  |  | CI (Buildbot slave) | Y! | 2014/07 | ci, bb |
| home | 14.04 LTS | DPE r530 | E5 1410@2.8 Ghz 1x4 | 16GB | 4x3072GB SAS | | web space | Iliad | 2015/10 | space |
| themis | 14.04 LTS | DPE r720 | E5-2665@2.4GHz 2x6=12 | 32x8GB@1600MHz = 256GB | 6x300GB SSD | | Websites | OSUOSL | 2014/08 | tlp |



### MacOSX: ###

| name | os | HW | Arrays | Services | Location | Comissioned | Class |
|-----|----|----|--------|----------|----------|-------------|-------|
| adam | 10.6 | Apple Xserve |  | Gump | OSUOSL | 2010/07 | ci |

### vCenter ###
| name | os | HW | CPU | RAM | Disk | Arrays | Services | Location | Comissioned | Class |
|-----|----|----|-----|-----|------|--------|----------|----------|-------------|-------|
| aether | Win 2k8 | DPE r210 | X3430@2.4GHz 1x4=4 | 8x2@1333MHz = 16GB | 2x500GB@7.2k | None | VM mgmt | OSUOSL | 2011/03 | |
| erebus | ESX | DPE r515| 4176HE@2.4GHz 2x6x1=12 | 8x8GB@1333MHz = 64GB | 1x2TB@7.2k | TBD | VM host | OSUOSL | 2010/12 | vms |
| eirene | ESX | DPE r720 | E5-2665@2.4GHz 2x8x2=32 | 256GB | ? = 830GB | ? = 2 x 1.6TB | VM host | OSUOSL | 2013/?? | vms|
| phanes | ESX | DPE r510 | X5670@2.93GHz 2x6x2=24 | 8x16@1066MHz | 2x300GB@10k | (chaos) SM Storform iServ R518.v2.1. 3 x 120GB SSD Front : 24 x 1TB SAS | VM host | OSUOSL | 2012/05 | vms |


### Virtual Machines: ###

| name | VM name | os | HW | Services | Location | Class |
|-----|---------|----|----|----------|----------|-------|
| archiva-vm | archiva-vm | | VM on vCenter | | OSUOSL | nyxvm || bloodhound-vm2 | | VM on vCenter | | OSUOSL | erebusvm |
| allura-vm | allura-vm | Ubuntu 12.04.2 LTS | VM on vCenter | TLP Playground | OSUOSL | erebusvm | 
| analysis | analysis | Ubuntu 10.4.2 LTS | VM on vCenter | CI (Jenkins/Analysis) | OSUOSL | erebusvm, ci |
| bb-fbsd2 | bb-fbsd2 | FreeBSD 9.0-RELEASE | VM on vCenter | CI (Buildbot slave) | OSUOSL | eirenevm, ci, bb |
| bb-openbsd | bb-openbsd | OpenBSD 4.8 | VM on vCenter | CI (Buildbot Slave) | OSUOSL | erebusvm, ci, bb |
| bb-win7 | bb-win7 | Windows 7 | VM on vCenter | CI (Buildbot slave) | OSUOSL | erebusvm, ci |
| bloodhound-vm | bloodhound-vm | | VM on vCenter | | OSUOSL | nyxvm |
| buildbot-vm | buildbot-vm | Ubuntu 14.04 LTS | VM at PNAP | CI (Buildbot Master) | PhoenixNAP | pnapvm, ci, bb |
| bloodhound-vm2 | bloodhound-vm2 | | VM on vCenter | | OSUOSL | eirenevm |
| circonus-broker | circonus-broker | | VM on vCenter | | OSUOSL | eirenevm |
| comdev1-us-west | comdev1 | Ubuntu 14.04.2 LTS | VM at PNAP | Comdev VM | PNAP | pmc |
| devicemap-vm | devicemap-vm | | VM on vCenter | | OSUOSL | nyxvm |
| erebus-ssl | erebus-ssl | | VM on vCenter | | OSUOSL | erebusvm |
| feathercast | feathercast | | VM on vCenter | | OSUOSL | nyxvm |
| hudson-win | hudson-win | Windows 2008 | VM on vCenter | CI (Hudson slave) | OSUOSL | nyxvm, ci |
| id | id | Ubuntu 10.04.1 LTS | VM on vCenter | SelfServe | OSUOSL | erebusvm |
| monitoring | monitoring | Debian 4 - 2.6.29.2 | VM | nagios, nagvis | Bytemark | nagios |
| ofbiz-vm | ofbiz-vm | Ubuntu 10.04.2 LTS | VM on vCenter | demo | OSUOSL | erebusvm, pmc |
| photark-vm | photark-vm | Ubuntu 10.04.2 LTS | VM on vCenter | demo | OSUOSL | nyxvm, pmc |
| ooo-forums | ooo-forums | | VM on vCenter | | OSUOSL | erebusvm |
| ooo-wiki2 | ooo-wiki2 | | VM on vCenter | | OSUOSL | eirenevm |
| openmeetings-vm | openmeetings-vm | Ubuntu 14.04.1 LTS | VM on vCenter | TLP Playground | OSUOSL | eirenevm, pmc |
| pkgrepo | pkgrepo | | VM on vCenter | | OSUOSL | eirenevm |
| projects-vm | projects-vm | Ubuntu 14.04.1 LTS | VM on vCenter | projects.a.o | OSUOSL | nyxvm |
| rave-vm | rave-vm | Ubuntu 12.04 LTS | VM on Vcenter | TLP Playground | OSUOSL | erebusvm, pmc |
| reviews-vm | reviews-vm | Ubuntu 10.04.2.LTS | VM on vCenter | ReviewBoard | OSUOSL | erebusvm, ci |
| struts-vm | struts-vm | | VM on vCenter | | OSUOSL | eirenevm |
| sysconfig | sysconfig | | VM on vCenter | | OSUOSL | eirenevm |
| svn-qavm2 | svn-qavm2 | Ubuntu 10.04.2 LTS | VM on vCenter | TLP playground | OSUOSL | nyxvm, pmc|
| tac-vm | tac-vm2 | | VM on vCenter | | OSUOSL | eirenevm |
| translate-vm2 | translate-vm2 | Ubuntu 10.04 LTS | VM on vCenter | translate | OSUOSL | nyxvm |
| vmbuild | vmbuild | Ubuntu 10.04.2 LTS | VM on vCenter | CI (Continuum) | OSUOSL | erebusvm, ci |
| vmgump | vmgump | Ubuntu 10.04.1 LTS | VM on vCenter | CI (Gump) | OSUOSL | erebusvm, ci |
| whimsy-vm3 | whimsy | | VM on PNAP| | PNAP | pnapvm |

### Zones: ###

| name | os | HW | Arrays | Services | Location | Class |
|-----|----|----|--------|----------|----------|-------|
| community.zones | SunOS | Zone/odyne |  | Community | SARA | |
| hudson-solaris.zones | SunOS | Zone/odyne |  | CI (Hudson slave) | SARA | |
| git.zones | SunOS | Zone/odyne |  | TLP playground | SARA | vc |
| ldapeu.zones | SunOS | Zone/odyne |  | LDAP | SARA | |
| james.zones | SunOS | Zone/hyperion |  | TLP playground | OSUOSL | hyperionzone |
| river.zones | SunOS | Zone/odyne |  | TLP playground | SARA | |
| servicemix.zones | SunOS | Zone/hyperion |  | TLP playground | OSUOSL | hyperionzone |
| solaris2.zones | SunOS | Zone/hyperion | |  | OSUOSL | |
| spamassassin2.zones | SunOS | Zone/odyne |  | TLP playground | SARA | odynezone |

### Jails - Services ###

| name | os | HW | Services | Location | Class |
|-----|----|----|----------|----------|-------|
| cms.zones | FreeBSD 9.1-RELEASE | Jail/baldr | Apache CMS | OSUOSL | baldrjail |
| urd.zones | FreeBSD 9.1-RELEASE | Jail/baldr | comments.a.o gitpubsub svngit2jira | OSUOSL | baldrjail |
| vor.zones | FreeBSD 9.1-RELEASE | Jail/baldr | pear.a.o | OSUOSL | baldrjail |

### Hardware: ###

| name | os | HW | Arrays | Services | Location | Comissioned |
|-----|----|----|--------|----------|----------|-------------|
| console | n/a | Cyclades Alter Path ACS (32 ports) |  | n/a | OSUOSL | n/a |
| r1sw0 | n/a | HP ProCurve |  | public | OSUOSL | 2013/05 |
| r2sw0 | n/a | HP ProCurve |  | public | OSUOSL | 2013/05 |
| r3sw0 | n/a | HP ProCurve |  | public | OSUOSL | 2013/05 |
| switch | n/a | switch |  | public | Sara | ?? |
| osuvpn | n/a | SonicWall SRA 4200 |  | VPN | OSUOSL | 2010/04 |

### Deprecated ###

| name | os | HW | CPU | RAM | Disk | Arrays | Services | Location | Comissioned | Class |
|-----|----|----|-----|-----|------|--------|----------|----------|-------------|-------|
| hyperion | 10u7 | Sun x2100 M2 | | | | | Zones | OSUOSL | 2007/12 | |

### SSH RSA Keys: ###

| name | RSA Key |
|-----|---------|
| baldr | 2048 1f:7d:b4:10:e0:52:38:09:01:89:8e:c1:44:80:d4:85 |
| comdev1-us-west | 2048 6f:85:00:45:24:c0:8b:e4:02:c7:e3:58:f0:3a:b2:fc |
| eos | 2048 2e:8f:6a:67:5a:ee:9c:0d:f9:98:b4:4f:80:25:a0:71 |
| forrest.zones | 2048 ea:15:4b:bf:02:5d:23:c3:22:03:2c:80:2e:bb:04:f7 |
| harmonia | 2048 cb:ae:54:4c:0c:6d:bc:f9:33:b3:eb:fb:03:0c:9f:73 |
| hermes | 2048 d9:e5:9d:61:b0:79:2b:78:0c:db:d1:ab:ef:3b:5a:7e |
| home | 2048 1c:5d:3f:a2:89:97:2e:39:eb:b0:09:9e:cf:c6:8d:f3 |
| minotaur | 1024 51:85:7d:8f:57:54:e7:6f:27:26:98:7a:c7:c1:47:87 |
| projects-vm | 2048 5f:71:42:22:5d:57:9d:dc:c6:c9:85:cb:91:16:c6:01 |
| svn01-us-west | 2048 a8:3b:48:59:35:b8:bb:62:97:56:83:46:be:90:88:7c |
| thor | 2048 5f:bf:4a:de:de:c4:c6:ad:7a:26:21:08:4a:8e:e8:c6 |
| tyr.zones | 2048 c0:95:86:8d:be:6a:ce:fb:a5:a1:fe:c6:98:9d:a7:00 |
| themis | 2048 64:a4:91:4d:b8:53:7d:f8:95:ca:9d:db:e4:8e:2d:5d |
| vmbuild vm | 2048 ce:b4:0d:3c:2c:c9:8a:cb:16:28:9b:21:28:8c:ba:58 |
| whimsy-vm3 | 2048 8c:72:f8:b6:ea:06:94:5c:42:0e:d5:98:1a:02:46:a2 |


### SSH ECDSA Keys: ###

| name | ECDSA Key |
|-----|-----------|
| baldr | 256 74:e1:5c:55:71:5c:42:09:66:81:1d:a0:8c:20:8f:45 |
| eos | 256 82:9b:ad:ba:c7:f4:dd:69:35:71:33:ea:ea:12:f7:34 |
| harmonia | 256 98:23:94:9f:b9:3b:b4:ca:f3:83:d2:54:7f:26:e0:17 |
| hermes | 256 9e:f4:b9:ea:fe:ef:42:26:64:f8:e6:33:4d:8c:41:99 |
| home | 256 23:33:53:16:c4:18:e9:71:e4:c0:18:42:58:7e:ad:99 |
| metis | 256 5e:2e:be:db:e6:ec:d8:ac:5c:fd:c5:06:06:1b:00:98 |
| projects-vm | 256 6f:ed:f8:1d:af:e6:63:cd:ea:68:41:3a:9a:8c:f7:61 |
| svn01-us-west | 256 c3:85:f4:d0:4a:6d:8b:f9:73:4b:8c:92:04:5c:7e:96 |
| syncope-vm2 | 256 da:f1:ed:75:22:1c:7e:7a:d3:73:2c:6a:79:98:42:b6 |
| themis | 256 7f:0e:bb:f9:32:78:94:b9:bf:3f:68:cf:c6:db:89:bb |
| whimsy-vm3 | 256 a1:e3:d1:b4:d7:f6:34:7a:43:e3:50:68:d4:e2:c0:03 |



### SSH ED25519 Keys: ###

| name | ED25519 Key |
|-----|-----------|
| home | 256 79:04:05:a4:79:38:99:d8:f2:e9:49:a1:39:4b:78:bb |



### SSL Keys: ###

| name | Fingerprint |
|-----|-------------|
| svn (deprecated) | BC:5F:40:92:FD:6A:49:AA:F8:B8:35:0D:ED:27:5E:A6:64:C1:7A:1B |
| svn (svn01-us-west, svn-master, sha-256) | 9C:1B:1D:84:DC:4B:F2:7C:E4:CD:48:9E:FC:DF:05:4D:40:9C:3B:A3:95:F3:D3:35:08:68:A8:1D:E5:68:94:18 |
| svn (svn01-us-west, svn-master, sha-1) | 4a:d7:22:dd:04:42:04:36:57:d1:76:f9:c8:1a:ab:66:09:4d:42:23 |
| svn (harmonia, svn.eu, sha-1) | 4a:d7:22:dd:04:42:04:36:57:d1:76:f9:c8:1a:ab:66:09:4d:42:23 |
| osuvpn | 75:49:9A:8D:F2:F0:AA:EA:FE:1E:67:EC:7E:09:48:10:B4:FF:6D:D7 |
| osuvpn (deprecated) | 19:C3:BA:6B:1F:82:42:2A:CE:46:E0:B7:E3:0D:33:CD:53:B4:6E:52 |
| osuvpn (deprecated) | (sha1) BC:5F:40:92:FD:6A:49:AA:F8:B8:35:0D:ED:27:5E:A6:64:C1:7A:1B |
| people (home, sha-256) | 9C:1B:1D:84:DC:4B:F2:7C:E4:CD:48:9E:FC:DF:05:4D:40:9C:3B:A3:95:F3:D3:35:08:68:A8:1D:E5:68:94:18 |
| people (home, sha1) 4a:d7:22:dd:04:42:04:36:57:d1:76:f9:c8:1a:ab:66:09:4d:42:23 |


# Monitoring #
[the public host &amp; service status
page](http://status.apache.org/) 

# Colos #

- OSUOSL: Oregon State University (OSU) Open Source Lab - Corvallis, OR,
USA

- SARA: Surfnet

- FUB: Freie Universität Berlin, Institut für Informatik

- Bytemark:

- Y!: ....

