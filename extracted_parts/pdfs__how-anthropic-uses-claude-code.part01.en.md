<!-- page 1 -->
How Anthropic teams
use Claude Code
Anthropic’s internal teams are transforming their workflows with Claude Code, enabling 
developers and non-technical staff to tackle complex projects, automate tasks, and bridge 
skill gaps that previously limited their productivity. 
Through interviews with our own Claude Code power users, we’ve gathered insights on how 
different departments leverage Claude Code, its impact on their work, and tips for other 
organizations considering adoption.
ANTHROP\C 
How Anthropic teams 
use Claude Code 
</> 
Anthropic's internal teams are transforming their workflows with Claude Code, enabling 
developers and non-technical staff to tackle complex projects, automate tasks, and bridge 
skill gaps that previously limited their productivity. 
Through interviews with our own Claude Code power users, we've gathered insights on how 
different departments leverage Claude Code, its impact on their work, and tips for other 
organizations considering adoption.

<!-- page 2 -->
Contents
Claude Code for data infrastructure 3
Claude Code for product development 5
Claude Code for security engineering 7
Claude Code for inference 9
Claude Code for data science and visualization 11
Claude Code for API 13
Claude Code for growth marketing 15
Claude Code for product design 17
Claude Code for RL engineering 19
Claude Code for legal 21
2 How Anthropic teams use Claude Code
Contents 
2 
Claude Code for data infrastructure 
Claude Code for product development 
Claude Code for security engineering 
Claude Code for inference 
Claude Code for data science and visualization 
Claude Code for API 
Claude Code for growth marketing 
Claude Code for product design 
Claude Code for RL engineering 
Claude Code for legal 
3 
5 
7 
9 
11 
13 
15 
17 
19 
21 
HOW ANTHROPIC TEAMS USE CLAUDE CODE

<!-- page 3 -->
Claude Code for data 
infrastructure
The Data Infrastructure team 
organizes all business data for 
teams across the company. They 
use Claude Code for automating 
routine data engineering tasks, 
troubleshooting complex 
infrastructure issues, and 
creating documented workflows 
for technical and non-technical 
team members to access and 
manipulate data independently.
Main Claude Code use cases
Kubernetes debugging with screenshots 
When Kubernetes clusters went down and weren’t scheduling new pods, 
the team used Claude Code to diagnose the issue. They fed screenshots of 
dashboards into Claude Code, which guided them through Google Cloud’s 
UI menu by menu until they found a warning indicating pod IP address 
exhaustion. Claude Code then provided the exact commands to create a 
new IP pool and add it to the cluster,  bypassing the need to involve 
networking specialists.
Plain text workflows for finance team 
The team showed finance team members how to write plain text files 
describing their data workflows, then load them into Claude Code to get 
fully automated execution. Employees with no coding experience could 
describe steps like “query this dashboard, get information, run these 
queries, produce Excel output,” and Claude Code would execute the entire 
workflow, including asking for required inputs like dates.
Codebase navigation for new hires 
When new data scientists join the team, they’re directed to use Claude 
Code to navigate their massive codebase. Claude Code reads their 
Claude.md files (documentation), identifies relevant files for specific 
tasks, explains data pipeline dependencies, and helps newcomers 
understand which upstream sources feed into dashboards. This replaces 
traditional data catalogs and discoverability tools.
End-of-session documentation updates 
The team asks Claude Code to summarize completed work sessions and 
suggest improvements at the end of each task. This creates a continuous 
improvement loop where Claude Code helps refine the Claude.md 
documentation and workflow instructions based on actual usage, making 
subsequent iterations more effective.
Parallel task management across multiple instances 
When working on long-running data tasks, they open multiple instances 
of Claude Code in different repositories for different projects. Each 
instance maintains full context, so when they switch back after hours or 
days, Claude Code remembers exactly what they were doing and where 
they left off, enabling true parallel workflow management without 
context loss.
3 Claude Code for data infrastructure
Claude Code for data 
infrastructure 
3 
The Data Infrastructure team 
organizes all business data for 
teams across the company. They 
use Claude Code for automating 
routine data engineering tasks, 
troubleshooting complex 
infrastructureissues,and 
creating documented workflows 
for technical and non-technical 
team members to access and 
manipulate data independently. 
Main Claude Code use cases 
Kubernetes debugging with screenshots 
When Kubernetes clusters went down and weren't scheduling new pods, 
the team used Claude Code to diagnose the issue. They fed screenshots of 
dashboards into Claude Code, which guided them through Google Cloud's 
UI menu by menu until they found a warning indicating pod IP address 
exhaustion. Claude Code then provided the exact commands to create a 
new IP pool and add it to the cluster, bypassing the need to involve 
networking specialists. 
Plain text workflows for finance team 
The team showed finance team members how to write plain text files 
describing their data workflows, then load them into Claude Code to get 
fully automated execution. Employees with no coding experience could 
describe steps like "query this dashboard, get information, run these 
queries, produce Excel output," and Claude Code would execute the entire 
workflow, including asking for required inputs like dates. 
Codebase navigation for new hires 
When new data scientists join the team, they're directed to use Claude 
Code to navigate their massive codebase. Claude Code reads their 
Claude.md files (documentation), identifies relevant files for specific 
tasks, explains data pipeline dependencies, and helps newcomers 
understand which upstream sources feed into dashboards. This replaces 
traditional data catalogs and discoverability tools. 
End-of-session documentation updates 
The team asks Claude Code to summarize completed work sessions and 
suggest improvements at the end of each task. This creates a continuous 
improvement loop where Claude Code helps refine the Claude.md 
documentation and workflow instructions based on actual usage, making 
subsequent iterations more effective. 
Parallel task management across multiple instances 
When working on long-running data tasks, they open multiple instances 
of Claude Code in different repositories for different projects. Each 
instance maintains full context, so when they switch back after hours or 
days, Claude Code remembers exactly what they were doing and where 
they left off, enabling true parallel workflow management without 
context loss. 
CLAUDE CODE FOR DATA INFRASTRUCTURE

<!-- page 4 -->
Claude Code for data 
infrastructure
T eam impact Resolved infrastructure problems without specialized expertise 
Resolved Kubernetes cluster issues that would normally require pulling in 
systems or networking team members, using Claude Code to diagnose 
problems and provide exact fixes.
Accelerated onboarding 
New data analysts and team members can quickly understand complex 
systems and contribute meaningfully without extensive guidance.
Enhanced support workflow 
Can process much larger data volumes and identify anomalies (like 
monitoring 200 dashboards) that would be impossible for humans to 
review manually.
Enabled cross-team self-service 
Finance teams with no coding experience can now execute complex data 
workflows independently.
T op tips from the 
Data Infrastructure 
team
Write detailed Claude.md files 
The better you document your workflows, tools, and expectations in 
Claude.md files, the better Claude Code performs. This made Claude Code 
excel at routine tasks like setting up new data pipelines when you have 
existing patterns.
Use MCP servers instead of CLI for sensitive data 
They recommend using MCP servers rather than the BigQuery CLI to 
maintain better security control over what Claude Code can access, 
especially for handling sensitive data that requires logging or has 
potential privacy concerns.
Share team usage sessions 
The team held sessions where members demonstrated their Claude Code 
workflows to each other. This helped spread best practices and showed 
different ways to use the tool they might not have discovered on 
their own.
4 Claude Code for data infrastructure
Claude Code for data 
infrastructure 
Team impact 
Top tips from the 
Data Infrastructure 
team 
4 
Resolved infrastructure problems without specialized expertise 
Resolved Kubernetes cluster issues that would normally require pulling in 
systems or networking team members, using Claude Code to diagnose 
problems and provide exact fixes. 
Accelerated onboarding 
New data analysts and team members can quickly understand complex 
systems and contribute meaningfully without extensive guidance. 
Enhanced support workflow 
Can process much larger data volumes and identify anomalies (like 
monitoring 200 dashboards) that would be impossible for humans to 
review manually. 
Enabled cross-team self-service 
Finance teams with no coding experience can now execute complex data 
workflows independently. 
Write detailed Claude.md files 
The better you document your workflows, tools, and expectations in 
Claude.md files, the better Claude Code performs. This made Claude Code 
excel at routine tasks like setting up new data pipelines when you have 
existing patterns. 
Use MCP servers instead of CLI for sensitive data 
They recommend using MCP servers rather than the BigQuery CLI to 
maintain better security control over what Claude Code can access, 
especially for handling sensitive data that requires logging or has 
potential privacy concerns. 
Share team usage sessions 
The team held sessions where members demonstrated their Claude Code 
workflows to each other. This helped spread best practices and showed 
different ways to use the tool they might not have discovered on 
their own. 
CLAUDE CODE FOR DATA INFRASTRUCTURE

<!-- page 5 -->
Claude Code for product 
development
The Claude Code team uses their 
own product to build updates to 
Claude Code, expanding the 
product’s enterprise capabilities 
and agentic loop functionalities.
Main Claude Code use cases
Fast prototyping with auto-accept mode 
Engineers use Claude Code for rapid prototyping by enabling “auto-
accept mode” (shift+tab) and setting up autonomous loops where Claude 
writes code, runs tests, and iterates continuously. They give Claude 
abstract problems they’re unfamiliar with, let it work autonomously, then 
review the 80% complete solution before taking over for final refinements. 
Teams emphasize starting from a clean git state and committing 
checkpoints regularly so they can easily revert any incorrect changes 
if Claude goes off track.
Synchronous coding for core features 
For more critical features touching the application’s business logic, the 
team works synchronously with Claude Code, giving detailed prompts 
with specific implementation instructions. They monitor the process in 
real-time to ensure code quality, style guide compliance, and proper 
architecture while letting Claude handle the repetitive coding work.
Building Vim mode 
One of their most successful async projects was implementing Vim 
key bindings for Claude Code. They asked Claude to build the entire 
feature (despite it not being a priority), and roughly 70% of the final 
implementation came from Claude’s autonomous work, requiring 
only a few iterations to complete.
Test generation and bug fixes 
They use Claude Code to write comprehensive tests after implementing 
features and handle simple bug fixes identified in pull request reviews. 
They also leverage GitHub Actions integration to have Claude 
automatically address Pull Request comments like formatting issues 
or function renaming.
Codebase exploration 
When working with unfamiliar codebases (like the monorepo or API 
side), the team uses Claude Code to quickly understand how systems 
work. Instead of waiting for Slack responses, they ask Claude directly 
for explanations and code references, saving significant time in 
context switching.
5 Claude Code for product development
Claude Code for product 
development 
5 
The Claude Code team uses their 
own product to build updates to 
Claude Code, expanding the 
product's enterprise capabilities 
and agentic loop functionalities. 
Main Claude Code use cases 
Fast prototyping with auto-accept mode 
Engineers use Claude Code for rapid prototyping by enabling "auto­
accept mode" (shift+tab) and setting up autonomous loops where Claude 
writes code, runs tests, and iterates continuously. They give Claude 
abstract problems they're unfamiliar with, let it work autonomously, then 
review the 80% complete solution before taking over for final refinements. 
Teams emphasize starting from a clean git state and committing 
checkpoints regularly so they can easily revert any incorrect changes 
if Claude goes off track. 
Synchronous coding for core features 
For more critical features touching the application's business logic, the 
team works synchronously with Claude Code, giving detailed prompts 
with specific implementation instructions. They monitor the process in 
real-time to ensure code quality, style guide compliance, and proper 
architecture while letting Claude handle the repetitive coding work. 
Building Vim mode 
One of their most successful async projects was implementing Vim 
key bindings for Claude Code. They asked Claude to build the entire 
feature (despite it not being a priority), and roughly 70% of the final 
implementation came from Claude's autonomous work, requiring 
only a few iterations to complete. 
Test generation and bug fixes 
They use Claude Code to write comprehensive tests after implementing 
features and handle simple bug fixes identified in pull request reviews. 
They also leverage GitHub Actions integration to have Claude 
automatically address Pull Request comments like formatting issues 
or function renaming. 
Codebase exploration 
When working with unfamiliar codebases (like the monorepo or API 
side), the team uses Claude Code to quickly understand how systems 
work. Instead of waiting for Slack responses, they ask Claude directly 
for explanations and code references, saving significant time in 
context switching. 
CLAUDE CODE FOR PRODUCT DEVELOPMENT

<!-- page 6 -->
Claude Code for product 
development
T eam impact Faster feature implementation 
Successfully implemented complex features like Vim mode with 70% of 
code written autonomously by Claude.
Improved development velocity 
Can rapidly prototype features and iterate on ideas without getting 
bogged down in implementation details.
Enhanced code quality through automated testing 
Claude generates comprehensive tests and handles routine bug fixes, 
maintaining high standards while reducing manual effort.
Better codebase exploration 
Team members can quickly understand unfamiliar parts of the monorepo 
without waiting for colleague responses.
T op tips from the 
Claude Code team
Create self-sufficient loops 
Set up Claude to verify its own work by running builds, tests, and lints 
automatically. This allows Claude to work longer autonomously and catch 
its own mistakes, especially effective when you ask Claude to generate 
tests before writing code.
Develop task classification intuition 
Learn to distinguish between tasks that work well asynchronously 
(peripheral features, prototyping) versus those needing synchronous 
supervision (core business logic, critical fixes). Abstract tasks on the 
product’s edges can be handled with “auto-accept mode,” while core 
functionality requires closer oversight.
Form clear, detailed prompts 
When components have similar names or functions, be extremely specific 
in your requests. The better and more detailed your prompt, the more you 
can trust Claude to work independently without unexpected changes to 
the wrong parts of the codebase.
6 Claude Code for product development
Claude Code for product 
development 
Team impact 
Top tips from the 
Claude Code team 
6 
Faster feature implementation 
Successfully implemented complex features like Vim mode with 70% of 
code written autonomously by Claude. 
Improved development velocity 
Can rapidly prototype features and iterate on ideas without getting 
bogged down in implementation details. 
Enhanced code quality through automated testing 
Claude generates comprehensive tests and handles routine bug fixes, 
maintaining high standards while reducing manual effort. 
Better codebase exploration 
Team members can quickly understand unfamiliar parts of the monorepo 
without waiting for colleague responses. 
Create self-sufficient loops 
Set up Claude to verify its own work by running builds, tests, and lints 
automatically. This allows Claude to work longer autonomously and catch 
its own mistakes, especially effective when you ask Claude to generate 
tests before writing code. 
Develop task classification intuition 
Learn to distinguish between tasks that work well asynchronously 
(peripheral features, prototyping) versus those needing synchronous 
supervision (core business logic, critical fixes). Abstract tasks on the 
product's edges can be handled with "auto-accept mode," while core 
functionality requires closer oversight. 
Form clear, detailed prompts 
When components have similar names or functions, be extremely specific 
in your requests. The better and more detailed your prompt, the more you 
can trust Claude to work independently without unexpected changes to 
the wrong parts of the code base. 
CLAUDE CODE FOR PRODUCT DEVELOPMENT

<!-- page 7 -->
Claude Code for security 
engineering
The Security Engineering team 
focuses on securing the software 
development lifecycle, supply 
chain security, and development 
environment security. They use 
Claude Code extensively for 
writing and debugging code.
Main Claude Code use cases
Complex infrastructure debugging 
When working on incidents, they feed Claude Code stack traces and 
documentation, asking it to trace control flow through the codebase. This 
significantly reduces time-to-resolution for production issues, allowing 
them to understand problems that would normally take 10-15 minutes of 
manual code scanning in about 5 minutes.
Terraform code review and analysis 
For infrastructure changes requiring security approval, they copy 
Terraform plans into Claude Code to ask “what’s this going to do? Am I 
going to regret this?” This creates tighter feedback loops and makes it 
easier for the security team to quickly review and approve infrastructure 
changes, reducing bottlenecks in the development process.
Documentation synthesis and runbooks 
They have Claude Code ingest multiple documentation sources and 
create markdown runbooks, troubleshooting guides, and overviews. 
They use these condensed documents as context for debugging real 
issues, creating a more efficient workflow than searching through full 
knowledge bases.
Test-driven development workflow 
Instead of their previous “design doc → janky code → refactor → give up 
on tests” pattern, they now ask Claude Code for pseudocode, guide it 
through test-driven development, and periodically check in to steer it 
when stuck, resulting in more reliable and testable code.
Context switching and project onboarding 
When contributing to existing projects like “dependant” (a web 
application for security approval workflows), they use Claude Code 
to write, review, and execute specifications written in markdown and 
stored in the codebase, enabling meaningful contributions within days 
instead of weeks.
7 Claude Code for security engineering
Claude Code for security 
■ ■ 
eng1neer1ng 
7 
The Security Engineering team 
focuses on securing the software 
development lifecycle, supply 
chain security, and development 
environment security. They use 
Claude Code extensively for 
writing and debugging code. 
Main Claude Code use cases 
Complex infrastructure debugging 
When working on incidents, they feed Claude Code stack traces and 
documentation, asking it to trace control flow through the code base. This 
significantly reduces time-to-resolution for production issues, allowing 
them to understand problems that would normally take 10-15 minutes of 
manual code scanning in about 5 minutes. 
Terraform code review and analysis 
For infrastructure changes requiring security approval, they copy 
Terraform plans into Claude Code to ask "what's this going to do? Am I 
going to regret this?" This creates tighter feedback loops and makes it 
easier for the security team to quickly review and approve infrastructure 
changes, reducing bottlenecks in the development process. 
Documentation synthesis and runbooks 
They have Claude Code ingest multiple documentation sources and 
create markdown run books, troubleshooting guides, and overviews. 
They use these condensed documents as context for debugging real 
issues, creating a more efficient workflow than searching through full 
knowledge bases. 
Test-driven development workflow 
Instead of their previous "design doc - janky code - refactor - give up 
on tests" pattern, they now ask Claude Code for pseudocode, guide it 
through test-driven development, and periodically check in to steer it 
when stuck, resulting in more reliable and testable code. 
Context switching and project onboarding 
When contributing to existing projects like "dependant" (a web 
application for security approval workflows), they use Claude Code 
to write, review, and execute specifications written in markdown and 
stored in the codebase, enabling meaningful contributions within days 
instead of weeks. 
CLAUDE CODE FOR SECURITY ENGINEERING

<!-- page 8 -->
Claude Code for security 
engineering
T eam impact Reduced incident resolution time 
Infrastructure debugging that normally takes 10-15 minutes of manual 
code scanning now takes about 5 minutes.
Improved security review cycle 
Terraform code reviews for security approval happen much faster, 
eliminating developer blocks while waiting for security team approval.
Enhanced cross-functional contribution 
Team members can meaningfully contribute to projects within days 
instead of weeks of context building.
Better documentation workflow 
Synthesized troubleshooting guides and runbooks from multiple sources 
create more efficient debugging processes.
T op tips from the 
Security Engineering 
team
Use custom slash commands extensively 
Security engineering uses 50% of all custom slash command 
implementations in the entire monorepo. These custom commands 
streamline specific workflows and speed up repeated tasks.
Let Claude talk first 
Instead of asking targeted questions for code snippets, they now 
tell Claude Code to “commit your work as you go” and let it work 
autonomously with periodic check-ins, resulting in more 
comprehensive solutions.
Leverage it for documentation 
Beyond coding, Claude Code excels at synthesizing documentation and 
creating structured outputs. They provide writing samples and formatting 
preferences to get documents they can immediately use in Slack, Google 
Docs, and other tools to avoid interface switching fatigue.
8 Claude Code for security engineering
Claude Code for security 
■ ■ 
eng1neer1ng 
Team impact 
Top tips from the 
Security Engineering 
team 
8 
Reduced incident resolution time 
Infrastructure debugging that normally takes 10-15 minutes of manual 
code scanning now takes about 5 minutes. 
Improved security review cycle 
Terraform code reviews for security approval happen much faster, 
eliminating developer blocks while waiting for security team approval. 
Enhanced cross-functional contribution 
Team members can meaningfully contribute to projects within days 
instead of weeks of context building. 
Better documentation workflow 
Synthesized troubleshooting guides and runbooks from multiple sources 
create more efficient debugging processes. 
Use custom slash commands extensively 
Security engineering uses 50% of all custom slash command 
implementations in the entire monorepo. These custom commands 
streamline specific workflows and speed up repeated tasks. 
Let Claude talk first 
Instead of asking targeted questions for code snippets, they now 
tell Claude Code to "commit your work as you go" and let it work 
autonomously with periodic check-ins, resulting in more 
comprehensive solutions. 
Leverage it for documentation 
Beyond coding, Claude Code excels at synthesizing documentation and 
creating structured outputs. They provide writing samples and formatting 
preferences to get documents they can immediately use in Slack, Google 
Docs, and other tools to avoid interface switching fatigue. 
CLAUDE CODE FOR SECURITY ENGINEERING

<!-- page 9 -->
Claude Code for inference
The Inference team manages 
the memory system that stores 
information while Claude reads 
your prompt and generates its 
response. Team members, 
especially those who are new to 
machine learning, can use Claude 
Code extensively to bridge that 
knowledge gap and accelerate 
their work.
Main Claude Code use cases
Codebase comprehension and onboarding 
The team relies heavily on Claude Code to quickly understand the 
architecture when joining a complex codebase. Instead of manually 
searching GitHub repos, they ask Claude to find which files call specific 
functionalities, getting results in seconds rather than asking colleagues or 
searching manually.
Unit test generation with edge case coverage 
After writing core functionality, they ask Claude to write comprehensive 
unit tests. Claude automatically includes missed edge cases, completing 
what would normally take significant mental energy in minutes, acting 
like a coding assistant they can review.
Machine learning concept explanation 
Without a machine learning background, team members depend on 
Claude to explain model-specific functions and settings. What would 
require an hour of Google searching and reading documentation now 
takes 10-20 minutes, reducing research time by 80%.
Cross-language code translation 
When testing functionality in different programming languages, they 
explain what they want to test and Claude writes the logic in the required 
language (like Rust), eliminating the need to learn new languages just for 
testing purposes.
Command recall and Kubernetes management 
Instead of remembering complex Kubernetes commands, they ask Claude 
for the correct syntax, like “how to get all pods or deployment status,” and 
receive the exact commands needed for their infrastructure work.
9 Claude Code for inference
Claude Code for inference 
9 
The Inference team manages 
the memory system that stores 
information while Claude reads 
your prompt and generates its 
response. Team members, 
especially those who are new to 
machine learning, can use Claude 
Code extensively to bridge that 
knowledge gap and accelerate 
their work. 
Main Claude Code use cases 
Codebase comprehension and onboarding 
The team relies heavily on Claude Code to quickly understand the 
architecture when joining a complex codebase. Instead of manually 
searching GitHub repos, they ask Claude to find which files call specific 
functionalities, getting results in seconds rather than asking colleagues or 
searching manually. 
Unit test generation with edge case coverage 
After writing core functionality, they ask Claude to write comprehensive 
unit tests. Claude automatically includes missed edge cases, completing 
what would normally take significant mental energy in minutes, acting 
like a coding assistant they can review. 
Machine learning concept explanation 
Without a machine learning background, team members depend on 
Claude to explain model-specific functions and settings. What would 
require an hour of Google searching and reading documentation now 
takes 10-20 minutes, reducing research time by 80%. 
Cross-language code translation 
When testing functionality in different programming languages, they 
explain what they want to test and Claude writes the logic in the required 
language (like Rust), eliminating the need to learn new languages just for 
testing purposes. 
Command recall and Kubemetes management 
Instead of remembering complex Kubernetes commands, they ask Claude 
for the correct syntax, like "how to get all pods or deployment status," and 
receive the exact commands needed for their infrastructure work. 
CLAUDE CODE FOR INFERENCE