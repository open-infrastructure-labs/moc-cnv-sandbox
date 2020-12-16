# Mass Open Cloud OpenShift + CNV Baremetal Cluster

The MOC CNV cluster is a small OpenShift 4.x cluster operated as a partnership between
the Mass Open Cloud and Red Hat.

The cluster is running on baremetal nodes with support for virtualization via
the Container Native Virtualization ([CNV][]) operator.  See the
[hardware summary](hardware.md) for more information.

[CNV]: https://www.openshift.com/learn/topics/virtualization/

## Request access to the MOC CNV cluster

1. File a ticket in our [issue tracker][]
requesting access.

[issue tracker]: https://github.com/open-infrastructure-labs/moc-cnv-sandbox/issues

1. One of our cluster admins will review your request and approve it if
   appropriate. Currently, accounts are limited to employees of Red Hat,
   the Mass Open Cloud, and affiliated institutions.

## Log into the MOC CNV cluster

The cluster web UI is available at:

- https://console-openshift-console.apps.cnv.massopen.cloud/

When prompted for an authentication method, choose "MOC-SSO" and then
authenticate using your Google or University credentials. You will only be
able to create projects if you have previously requested approval as
described in "[Request access to the MOC CNV cluster][]".

[request access to the moc cnv cluster]: #request-access-to-the-moc-cnv-cluster

## Problems and questions

Please report any problems or questions using the [issue tracker][].
