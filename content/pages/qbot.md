Title: Using Qbot with the-asf Slack channels
license: https://www.apache.org/licenses/LICENSE-2.0

The Infrastructure team's **Qbot** is a Slack assistant that can simplify both important and frivolous tasks on Slack channels in the `the-asf` workspace. It can support requests in channels for PMCs, ASF committees, the ASF Board and `asfmembers`.

The name references the tool-maker 'Q', who provides weapons and gadgets for Agent 007 in the James Bond movies.

## What Qbot can do
Qbot has an evolving set of functions:

  - Adding people to private channels
  - Providing to the channel notifications related to your project's Jira tickets - new ticket, new comment, ticket resolved.
  - Displaying information about Jira tickets by project, by keyword, by status.
  - Starting a question queue in the huddle in a channel workspace. (Note: Infra designed this for use with Roundtable events, in case participants had a flood of questions and comments that would need to be queued so everyone had a fair chance to speak. So far, we have not needed to use it.)

It also has a set of 'fun' features, such as rolling dice, flipping a coin, or talking to someone from the (fictional) ASF Human Resoures Department.

## Setting up Qbot in your PMC's channels
If you want to have Qbot available in your PMC's channel, create a Jira ticket for Infra with the request. Include this information:

  - If you want to get Jira-ticket notifications, the name of the channel or channels where notifications about tickets related to your projects should appear
  - How you want notifications to appear. There are five options:
      - No notifications
      - All notifications
      - `nodescription`: All notifications with the title of the ticket, but not its description
      - `nocomments`: No notifications of comments on tickets
      - `createclose`: Just notifications of ticket creation and resolution
  - Specify who can use the `addme` command -- committers, members of your PMC only, ASF Members only...

See also "Jira-related functions", below.

To have Qbot active in a project's private channel, once it is available in your public channels, someone already in the channel has to invite it with the Slack command `/invite @QBot`.
  

## Talking to Qbot
In Slack, there are three ways to talk to Qbot:

  -  Anywhere in the ASF workspace, type `/qbot` and the command you want to give it. If it is a command which you do not have permission to use where you currently are in Slack, the command will fail.
  -  In a channel where Qbot is present, type `qbot` without the slash, and the command.
  -  In the Slack interface, there is a general menu bar at the far left. The next column is the menu bar for the ASF workspace. Below the list of your contacts and channels, there is a section for `Apps`. Qbot appears there.
        -  Click that entry to see a display with three tabs.
        -  Select the `Messages` tab.
        -  Write your command to Qbot without `/` or 'qbot` at the start.
        

## Qbot commands
**Note** we are expanding Qbot's reach, and this list will expand to match its capabilities.

  - `help` - You see a list of the available commands: `/qbot help`.

### Adding yourself to a private channel
  - `addme`- Add yourself to a private channel. (Without Qbot, you have to ask someone already in the channel to add you.) You can make the command from anywhere in the ASF workspace. The syntax is `/qbot addme <NAME OF CHANNEL>`.

### Jira-related functions

You can ask Qbot to provide information about Jira tickets.

**List Jira tickets for a project**

  - List all the project's tickets, regardless of status:
    - basic syntax: `qbot tickets project:<PROJECT>`
    - display the tickets that match a keyword search: `qbot tickets project:<PROJECT> <KEYWORDS>`
  - List the project's unassigned tickets:
    - basic syntax: `qbot tickets unassigned:<PROJECT>`
    - display the project's unassigneed tickets that match a keyword search: `qbot tickets unassigned:<PROJECT> <KEYWORDS>`

**Find specific Jira tickets**

  - Find tickets using <a href="https://www.atlassian.com/blog/jira/jql-the-most-flexible-way-to-search-jira-14" target="_blank">Jira Query Language (JQL)</a>
    - syntax: `qbot tickets jql:<JQL STRING>`
  - Find tickets using a keyword search
    - syntax: `qbot tickets <KEYWORDS>`

*For keyword searches, separate multiple keywords with spaces.*

### Fun stuff

  - `flip` - Qbot flips a coin and tells you whether it came up heads or tails: `/qbot flip`.

  - `lauren` - Lauren works in the (fictional) Human Resources Department at The ASF. You can summon Lauren in any channel in which Qbot is active by typing her name three times in three consecutive posts (the way characters can summon a demon in the movie "Beetlejuice"). **Note** Lauren inhabits a parallel world to ours, one in which The ASF has a physical office with many employees who come in to work each day. Her statements may not bear too much relevance to the world you inhabit. You can also use the following commands to get Laura's input:
    - `lauren announce`: Lauren shares a significant (in Lauren's opinion) announcement.
    - `lauren benefit`: Lauren reveals an employee benefit.
    - `lauren complaint`: Lauren discusses a recent HR complaint with you.
    - `lauren policy`: Lauren reminds you of a corporation policy.
  - `roll` - If you send the command without furthr parameters (`/qbot roll`), Qbot rolls one six-sided die and reports the result.
      - You can roll up to ten dice at a time, and each die can have up to 100 sides or 'pips'.The syntax for a basic dice roll is `/qbot roll NdP`, where `N` is the number of dice (up to 10) and `P` is the number of surfaces each die has (up to 100): `/qbot roll 8d12`.
      - In a role-playing game such as Dungeons and Dragons, when your character gets in trouble you may be able to try a **saving roll** to, well, save them from disaster. The syntax to see if Qbot can help in your current crisis is `/qbot roll saving`.
  - `shanty` - Qbot shares a verse of a sea shanty. The syntax is `/qbot shanty`.

_Note: the following two commands are in 'alpha' development and may not work as expected. If you would like to use them in huddles in your project's Slack spaces, please let us know (see 'Requesting features', below)._

  - `q` - This command starts a  "Q & A" queue in a huddle in your current channel, and makes you the administrator. Such a function can be useful if you anticipate participants submitting a large number of questions. The syntax is `/qbot q start`.
  - `queue` - Performs the same function as `q`. The syntax is `/qbot queue start`.

## Requesting features
If you have an idea for a Qbot service that could help your PMC on Slack (or you just want to add a verse from another sea shanty), please suggest it in the <a href="https://github.com/apache/infrastructure-ideas/discussions/categories/qbot" target="_blank">Infrastructure-ideas repository</a>.
