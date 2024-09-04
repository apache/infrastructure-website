title: ASF Infrastructure Reporting Dashboard
license: https://www.apache.org/licenses/LICENSE-2.0

The dashboard, at <a href="https://infra-reports.apache.org" target="_blank">infra-reports.apache.org</a>, provides a collection of reports on the overall health and activity of the infrastructure at the ASF. These reports can be helpful in understanding the status of all the ASF 'under the hood' resources, and in assessing the resource cost of some activities, like build processes.

Some of the reports are open to the public, while others are restricted to those who genuinely need them. 

## Reports available to all

  - **Uptime Statistics**: This dashboard provides an overview of uptime of a wide range of services, including email, forums and Confluence wikis, version control systems, and websites.
  - **Public Download Statistics**: On this screen you can select an ASF project and then review and download statistics about how often in a given month the project's product and other artifact have been downloaded. The data is available in .JSON format.
  - **Site Source Checker**: Use this screen to locate and review the source files for an ASF project's website. Yellow or red indicators tell you that the site they are attached to  is not currently being updated.

## Reports available to the Infra team and/or ASF Members

  - **Jira tickets**: Infra uses this dashboard to track resolution of Jira tickets related to infrastructure work. Gauges and charts cover how quickly issues are resolved and whether the number of open tickets for Jira is increasing or decreasing, and provides a drive-by view of all open Jira tickets.
  - **Mail Transport Statistics**: This screen, for the Infrastructure team, gives a visualization of how the system is handling ASF and project email.
  - **Real-time Download Stats**: On this screen, an ASF Member or Committer can select a project to which they belong and get a series of informative charts (over time, by country, by artifact) of downloads of the project's released artifacts.
  - **GitHub Actions Usage**: This screen displays the use of GitHub Actions for projects you belong to. The chart can be configured for project (if you belong to more than one), time range and other options. 

Send questions or suggestions about the dashboard to `users@infra.apache.org`.
