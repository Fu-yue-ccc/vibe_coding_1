<!-- page 18 -->
Claude Code for product design
T eam impact Transformed core workflow 
Claude Code becomes a primary design tool, with Figma and Claude Code 
open 80% of the time.
2-3x faster execution 
Visual and state management changes that previously required extensive 
back-and-forth with engineers now implemented directly.
Weeks to hours cycle time 
Complex projects like GA launch messaging that would take a week of 
coordination now completed in two 30-minute calls.
Two distinct user experiences 
Developers get “augmented workflow” (faster execution), while non-
technical users get “holy crap, I’m a developer workflow” (entirely new 
capabilities previously impossible).
Improved design-engineering collaboration 
Better communication and faster problem-solving because designers 
understand system constraints and possibilities upfront.
T op tips from the 
Product Design team
Get proper setup help from engineers 
Have engineering teammates help with initial repository setup and 
permissions - the technical onboarding is challenging for non-developers, 
but once configured, it becomes transformative for daily workflow.
Use custom memory files to guide Claude’s behavior 
Create specific instructions telling Claude you’re a designer with little 
coding experience who needs detailed explanations and smaller, 
incremental changes, dramatically improving the quality of Claude’s 
responses and making it less intimidating.
Leverage image pasting for prototyping 
Use Command+V to paste screenshots directly into Claude Code - it excels 
at reading designs and generating functional code, making it invaluable 
for turning static mockups into interactive prototypes that engineers can 
immediately understand and build upon.
18 Claude Code for product design
Claude Code for product design 
Team impact 
Top tips from the 
Product Design team 
18 
Transformed core workflow 
Claude Code becomes a primary design tool, with Figma and Claude Code 
open 80% of the time. 
2-3x faster execution 
Visual and state management changes that previously required extensive 
back-and-forth with engineers now implemented directly. 
Weeks to hours cycle time 
Complex projects like GA launch messaging that would take a week of 
coordination now completed in two 30-minute calls. 
Two distinct user experiences 
Developers get "augmented workflow" (faster execution), while non­
technical users get "holy crap, I'm a developer workflow" ( entirely new 
capabilities previously impossible). 
Improved design-engineering collaboration 
Better communication and faster problem-solving because designers 
understand system constraints and possibilities upfront. 
Get proper setup help from engineers 
Have engineering teammates help with initial repository setup and 
permissions - the technical onboarding is challenging for non-developers, 
but once configured, it becomes transformative for daily workflow. 
Use custom memory files to guide Claude's behavior 
Create specific instructions telling Claude you're a designer with little 
coding experience who needs detailed explanations and smaller, 
incremental changes, dramatically improving the quality of Claude's 
responses and making it less intimidating. 
Leverage image pasting for prototyping 
Use Command+V to paste screenshots directly into Claude Code - it excels 
at reading designs and generating functional code, making it invaluable 
for turning static mockups into interactive prototypes that engineers can 
immediately understand and build upon. 
CLAUDE CODE FOR PRODUCT DESIGN

<!-- page 19 -->
Claude Code for RL engineering
The RL Engineering team 
focuses on efficient sampling in 
RL and weight transfers across 
the cluster . They use Claude 
Code primarily for writing small 
to medium features, debugging, 
and understanding complex 
codebases, with an iterative 
approach that includes frequent 
checkpointing and rollbacks.
Main Claude Code use cases
Feature development with supervised autonomy 
The team lets Claude Code write most of the code for small to medium 
features while providing oversight, such as implementing authentication 
mechanisms for weight transfer components. They work interactively, 
allowing Claude to take the lead but steering it when it goes off track.
Test generation and code review 
After implementing changes themselves, they ask Claude Code to add 
tests or review their code. This automated testing workflow saves 
significant time on routine but important quality assurance tasks.
Debugging and error investigation 
They use Claude Code to debug errors with mixed results - sometimes it 
identifies issues immediately and adds relevant tests, while other times 
it struggles to understand the problem, but overall provides value when 
it works.
Codebase comprehension and call stack analysis 
One of the biggest changes in their workflow is using Claude Code to get 
quick summaries of relevant components and call stacks, replacing 
manual code reading or extensive debugging output generation.
Kubernetes operations guidance 
They frequently ask Claude Code about Kubernetes operations that would 
otherwise require extensive Googling, getting immediate answers for 
configuration and deployment questions.
19 Claude Code for RL engineering
Claude Code for RL engineering 
19 
The RL Engineering team 
focuses on efficient sampling in 
RL and weight transfers across 
the cluster. They use Claude 
Code primarily for writing small 
to medium features, debugging, 
and understanding complex 
codebases, with an iterative 
approach that includes frequent 
checkpointing and rollbacks. 
Main Claude Code use cases 
Feature development with supervised autonomy 
The team lets Claude Code write most of the code for small to medium 
features while providing oversight, such as implementing authentication 
mechanisms for weight transfer components. They work interactively, 
allowing Claude to take the lead but steering it when it goes off track. 
Test generation and code review 
After implementing changes themselves, they ask Claude Code to add 
tests or review their code. This automated testing workflow saves 
significant time on routine but important quality assurance tasks. 
Debugging and error investigation 
They use Claude Code to debug errors with mixed results - sometimes it 
identifies issues immediately and adds relevant tests, while other times 
it struggles to understand the problem, but overall provides value when 
it works. 
Codebase comprehension and call stack analysis 
One of the biggest changes in their workflow is using Claude Code to get 
quick summaries of relevant components and call stacks, replacing 
manual code reading or extensive debugging output generation. 
Kubernetes operations guidance 
They frequently ask Claude Code about Kubemetes operations that would 
otherwise require extensive Googling, getting immediate answers for 
configuration and deployment questions. 
CLAUDE CODE FOR RL ENGINEERING

<!-- page 20 -->
Claude Code for RL engineering
Development 
workflow impact
Experimental approach enabled 
They now use a “try and rollback” methodology, frequently committing 
checkpoints so they can test Claude’s autonomous implementation 
attempts and revert if needed, enabling more experimental.
Documentation acceleration 
Claude Code automatically adds helpful comments that save significant 
time on documentation, though they note it sometimes adds comments 
in odd places or uses questionable code organization.
Speed-up with limitations 
While Claude Code can implement small-to-medium PRs with “relatively 
little time” from them, they acknowledge it only works on first attempt 
about one-third of the time, requiring either additional guidance or 
manual intervention.
T op tips from the 
RL Engineering team
Customize your Claude.md file for specific patterns 
Add instructions to your Claude.md file to prevent Claude from making 
repeated tool-calling mistakes, such as telling it to “run pytest not run and 
don’t cd unnecessarily - just use the right path.” This significantly 
improved consistency.
Use a checkpoint-heavy workflow 
Regularly commit your work as Claude makes changes so you can easily 
roll back when experiments don’t work out. This enables a more 
experimental approach to development without risk.
Try one-shot first, then collaborate 
Give Claude a quick prompt and let it attempt the full implementation 
first. If it works (about one-third of the time), you’ve saved significant 
time. If not, then switch to a more collaborative, guided approach.
20 Claude Code for RL engineering
Claude Code for RL engineering 
Development 
workflow impact 
Top tips from the 
RL Engineering team 
20 
Experimental approach enabled 
They now use a "try and rollback" methodology, frequently committing 
checkpoints so they can test Claude's autonomous implementation 
attempts and revert if needed, enabling more experimental. 
Documentation acceleration 
Claude Code automatically adds helpful comments that save significant 
time on documentation, though they note it sometimes adds comments 
in odd places or uses questionable code organization. 
Speed-up with limitations 
While Claude Code can implement small-to-medium PRs with "relatively 
little time" from them, they acknowledge it only works on first attempt 
about one-third of the time, requiring either additional guidance or 
manual intervention. 
Customize your Claude.md file for specific patterns 
Add instructions to your Claude.md file to prevent Claude from making 
repeated tool-calling mistakes, such as telling it to "run pytest not run and 
don't cd unnecessarily - just use the right path." This significantly 
improved consistency. 
Use a checkpoint-heavy workflow 
Regularly commit your work as Claude makes changes so you can easily 
roll back when experiments don't work out. This enables a more 
experimental approach to development without risk. 
Try one-shot first, then collaborate 
Give Claude a quick prompt and let it attempt the full implementation 
first. Ifit works (about one-third of the time), you've saved significant 
time. If not, then switch to a more collaborative, guided approach. 
CLAUDE CODE FOR RL ENGINEERING

<!-- page 21 -->
Claude Code for legal
The Legal team discovered 
Claude Code’s potential through 
experimentation, and a desire to 
learn about Anthropic’s product 
offerings. Additionally, one team 
member had a personal use case 
related to creating accessibility 
tools for family and work 
prototypes that demonstrate 
the technology’s power for 
non-developers.
Main Claude Code use cases
Custom accessibility solution for family members 
Team members have built communication assistants for family members 
with speaking difficulties due to medical diagnoses. In just one hour, they 
created a predictive text app using native speech-to-text that suggests 
responses and speaks them using voice banks, solving gaps in existing 
accessibility tools recommended by speech therapists.
Legal department workflow automation 
They created prototype “phone tree” systems to help team members 
connect with the right lawyer at Anthropic, demonstrating how legal 
departments can build custom tools for common tasks without traditional 
development resources.
Team coordination tools 
Managers have built G Suite applications that automate weekly team 
updates and track legal review status across products, allowing lawyers to 
quickly flag items needing review through simple button clicks rather 
than spreadsheet management.
Rapid prototyping for solution validation 
They use Claude Code to quickly build functional prototypes they can 
show to domain experts (like showing accessibility tools to UCSF 
specialists) to validate ideas and identify existing solutions before 
investing more time.
21 Claude Code for legal
Claude Code for legal 
21 
The Legal team discovered 
Claude Code's potential through 
experimentation, and a desire to 
learn about Anthropic's product 
offerings. Additionally, one team 
member had a personal use case 
related to creating accessibility 
tools for fomily and work 
prototypes that demonstrate 
the technology's power for 
non-developers. 
Main Claude Code use cases 
Custom accessibility solution for family members 
Team members have built communication assistants for family members 
with speaking difficulties due to medical diagnoses. In just one hour, they 
created a predictive text app using native speech-to-text that suggests 
responses and speaks them using voice banks, solving gaps in existing 
accessibility tools recommended by speech therapists. 
Legal department workflow automation 
They created prototype "phone tree" systems to help team members 
connect with the right lawyer at Anthropic, demonstrating how legal 
departments can build custom tools for common tasks without traditional 
development resources. 
Team coordination tools 
Managers have built G Suite applications that automate weekly team 
updates and track legal review status across products, allowing lawyers to 
quickly flag items needing review through simple button clicks rather 
than spreadsheet management. 
Rapid prototyping for solution validation 
They use Claude Code to quickly build functional prototypes they can 
show to domain experts (like showing accessibility tools to UCSF 
specialists) to validate ideas and identify existing solutions before 
investing more time. 
CLAUDE CODE FOR LEGAL

<!-- page 22 -->
Claude Code for legal
Work style and impact Planning in Claude.ai, building in Claude Code 
They use a two-step process where they brainstorm and plan with 
Claude.ai first, then move to Claude Code for implementation, asking it 
to slow down and work step-by-step rather than outputting everything 
at once.
Visual-first approach 
They frequently use screenshots to show Claude Code what they want 
interfaces to look like, then iterate based on visual feedback rather than 
describing features in text.
Prototype-driven innovation 
They emphasize overcoming the fear of sharing “silly” or “toy” 
prototypes, as these demonstrations inspire others to see possibilities 
they hadn’t considered.
Security and 
compliance awareness
MCP integration concerns 
As product lawyers, they immediately identify security implications of 
deep MCP integrations, noting how conservative security postures will 
create barriers as AI tools access more sensitive systems.
Compliance tooling priorities 
They advocate for building compliance tools quickly as AI 
capabilities expand, recognizing the balance between innovation 
and risk management.
T op tips from the 
Legal Department
Plan extensively in Claude.ai first 
Use Claude’s conversational interface to flesh out your entire idea before 
moving to Claude Code. Then ask Claude to summarize everything into a 
step-by-step prompt for implementation.
Work incrementally and visually 
Ask Claude Code to slow down and implement one step at a time so you 
can copy-paste without getting overwhelmed. Use screenshots liberally to 
show what you want interfaces to look like.
Share prototypes despite imperfection 
Overcome the urge to hide “toy” projects or unfinished work - sharing 
prototypes helps others see possibilities and sparks innovation across 
departments that don’t typically interact.
22 Claude  Code  for  legal
Claude Code for legal 
Work style and impact 
Security and 
compliance awareness 
Top tips from the 
Legal Department 
22 
Planning in Claude.ai, building in Claude Code 
They use a two-step process where they brainstorm and plan with 
Claude.ai first, then move to Claude Code for implementation, asking it 
to slow down and work step-by-step rather than outputting everything 
at once. 
Visual-first approach 
They frequently use screenshots to show Claude Code what they want 
interfaces to look like, then iterate based on visual feedback rather than 
describing features in text. 
Prototype-driven innovation 
They emphasize overcoming the fear of sharing "silly" or "toy" 
prototypes, as these demonstrations inspire others to see possibilities 
they hadn't considered. 
MCP integration concerns 
As product lawyers, they immediately identify security implications of 
deep MCP integrations, noting how conservative security postures will 
create barriers as AI tools access more sensitive systems. 
Compliance tooling priorities 
They advocate for building compliance tools quickly as AI 
capabilities expand, recognizing the balance between innovation 
and risk management. 
Plan extensively in Claude.ai first 
Use Claude's conversational interface to flesh out your entire idea before 
moving to Claude Code. Then ask Claude to summarize everything into a 
step-by-step prompt for implementation. 
Work incrementally and visually 
Ask Claude Code to slow down and implement one step at a time so you 
can copy-paste without getting overwhelmed. Use screenshots liberally to 
show what you want interfaces to look like. 
Share prototypes despite hnperfection 
Overcome the urge to hide "toy" projects or unfinished work - sharing 
prototypes helps others see possibilities and sparks innovation across 
departments that don't typically interact. 
CLAUDE CODE FOR LEGAL
