Title: Backup policy
license: https://www.apache.org/licenses/LICENSE-2.0

Infra is committed to maintaining backups of critical systems and data for disaster recovery. Infra does not specifically maintain "historical" backups. Changes to ASF data sets are expected to be reflected in SCM commit history as well as email-based records of commits/changes. SCM systems and email are the primary focus of the Infra backup strategy.

All Infra-managed systems have scheduled nightly file-level and weekly full backups via an automated BackupPC installation, with a retention of approximately 14 days for fulls. _**Backups are pruned regularly due to space constraints, and are not guaranteed to be nightly depending on bandwidth and backup server capacity.**_

Project VM backups: Automated backups via BackupPC are provided as a courtesy, however, _**extra data drives outside the base OS are not backed up due to space and time constraints. Ephemeral data or data sets which generate large numbers of backup errors (transient data, temporary data,) are typically excluded from backup**_. Contact Infra if you have specific backup needs for your project VM beyond the Infra-provided base operating system: /etc, /home, /var, /usr.

Foundation Critical systems receive additional nightly rsync/zfs based snapshots which are retained for approximately 30 days in most cases.

#### Databases ####
  - MySQL and Postgres databases are backed up nightly using a puppet managed tool to /x1/db_dump
  - /x1/db_dump is picked up by the rsync or backuppc process

#### Software repositories ####
  - gitbox.a.o (rsync, backuppc, GitHub mirrors).
  - svn.a.o (rsync, backuppc, azure DR replica).
  - archive.a.o (backuppc).

#### Server logs ####
  - Ephemeral. retained in <a href="https://www.elastic.co/" target="_blank">Elasticsearch</a> for approximately 90 days, but not guaranteed. Not available outside Infra.
  - Compiled statistics available in some cases.

#### Email ####
  - Raw archives (mbox-vm) (rsync/backuppc)
  - qmail source (hermes) (rsync backup + rsync replica)
