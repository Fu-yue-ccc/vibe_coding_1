<!-- page 1 -->
AI-Assisted Assessment of Coding Practices
in Modern Code Review
Manushree Vijayvergiya
manushree@google.com
Google
Zurich, Switzerland
Małgorzata Salawa
magorzata@google.com
Google
Zurich, Switzerland
Ivan Budiselić
ibudiselic@google.com
Google
Zurich, Switzerland
Dan Zheng
danielzheng@google.com
Google
Mountain View, USA
Pascal Lamblin
lamblinp@google.com
Google
Montreal, Canada
Marko Ivanković
markoi@google.com
Google
Zurich, Switzerland
Juanjo Carin
juanjocarin@google.com
Google
Sunnyvale, USA
Mateusz Lewko
mlewko@google.com
Google
Zurich, Switzerland
Jovan Andonov
jandonov@google.com
Google
Zurich, Switzerland
Goran Petrović
goranpetrovic@google.com
Google
Zurich, Switzerland
Daniel Tarlow
dtarlow@google.com
Google
Montreal, Canada
Petros Maniatis
maniatis@google.com
Google
Mountain View, USA
René Just∗
rjust@cs.washington.edu
University of Washington
Seattle, USA
ABSTRACT
Modern code review is a process in which an incremental code con-
tribution made by a code author is reviewed by one or more peers
before it is committed to the version control system. An important
element of modern code review is verifying that code contributions
adhere to best practices. While some of these best practices can be
automatically verified, verifying others is commonly left to human
reviewers. This paper reports on the development, deployment,
and evaluation of AutoCommenter, a system backed by a large
language model that automatically learns and enforces coding best
practices. We implemented AutoCommenter for four programming
languages (C++, Java, Python, and Go) and evaluated its perfor-
mance and adoption in a large industrial setting. Our evaluation
shows that an end-to-end system for learning and enforcing coding
best practices is feasible and has a positive impact on the devel-
oper workflow. Additionally, this paper reports on the challenges
associated with deploying such a system to tens of thousands of
developers and the corresponding lessons learned.
CCS CONCEPTS
• Software and its engineering→ Software verification and
validation.
∗Work done at Google.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0685-1/24/07
https://doi.org/10.1145/3664646.3665664
KEYWORDS
Artificial Intelligence, Code Review, Coding Best Practices
ACM Reference Format:
Manushree Vijayvergiya, Małgorzata Salawa, Ivan Budiselić, Dan Zheng,
Pascal Lamblin, Marko Ivanković, Juanjo Carin, Mateusz Lewko, Jovan An-
donov, Goran Petrović, Daniel Tarlow, Petros Maniatis, and René Just. 2024.
AI-Assisted Assessment of Coding Practices in Modern Code Review. In
Proceedings of the 1st ACM International Conference on AI-Powered Software
(AIware ’24), July 15–16, 2024, Porto de Galinhas, Brazil. ACM, New York,
NY, USA, 9 pages. https://doi.org/10.1145/3664646.3665664
1 INTRODUCTION
Modern code review [21, 23] (compared to holistic code review [8])
has grown organically over the years in open-source and industrial
settings. A set of common peer-review criteria have emerged [5, 20,
21], which include coding best practices. Many companies, projects,
and even programming languages formally define them in the form
of “style guides” [1–4] that commonly cover the following aspects:
• Formatting: line limits, use of whitespaces and indentation,
placement of parentheses and brackets, etc.;
• Naming: capitalization, brevity, descriptiveness, etc.;
• Documentation: expected placement and content of file-level,
function-level, and other comments;
• Language features: use of specific language features in differ-
ent (code) contexts;
• Code idioms : use of code idioms to improve code clarity,
modularity, and maintainability.
Developers generally report high satisfaction with modern code
review processes [23, 28]. One of their main benefits is the learning
experience for code authors who are not familiar with the codebase,
specific language features, or common code idioms. During a review,
an expert developer educates the code author on best practices, in
arXiv:2405.13565v1  [cs.SE]  22 May 2024

<!-- page 2 -->
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil Manushree Vijayvergiya et al.
addition to reviewing (and learning about) the code contributions
and their implications.
Static analysis tools such as linters [15] can automatically verify
that code adheres to some best practices (e.g., formatting rules), and
some tools can even automatically fix violations. However, nuanced
guidelines or those with exceptions are difficult to automatically
verify in their entirety (e.g., naming conventions and justified devi-
ations in legacy code), and some guidelines cannot be captured by
precise rules at all (e.g., clarity and specificity of code comments)
and rely on human judgement and collective developer knowledge.
As a result, it is generally expected that human reviewers check
code changes for best practice violations.
The biggest cost of the code-review process is the time required,
especially from expert developers. Even with significant automa-
tion in place, and keeping the process as lightweight as possible, a
developer can easily dedicate several hours daily to this task [23].
Recent advances in machine learning, capabilities of large lan-
guage models (LLMs) in particular, suggest that LLMs are suitable
for code-review automation (e.g., [11, 16, 17, 24–26]). However, the
software engineering challenges around deploying an end-to-end
system at scale remain unexplored. Likewise, extrinsic evaluations
of such systems on overall efficacy and user acceptance are missing.
This paper investigates whether it is possible to partially au-
tomate the code-review process, specifically the detection of best
practice violations, thereby providing timely feedback for code
authors and allowing reviewers to focus on overall functionality.
Specifically, this paper reports on our experience of developing,
deploying, and evaluating AutoCommenter—an automated code-
review assistant—in an industrial setting at Google, where it is
currently used by tens of thousands of developers every day.
In summary, the contributions of this paper are:
• A general architecture of an LLM-based code-review assis-
tant system (section 3).
• A description of tool calibration and deployment to tens of
thousands of developers (section 4).
• An evaluation of the system (section 5).
• A summary and discussion of lessons learned (section 6).
2 BACKGROUND
AutoCommenter was developed in a large industrial setting at
Google. The modern code review practices at Google are similar to
those of other industrial and open source projects [23].
2.1 Code Review Process
The code review process at Google is well established, change-
based, and tool-assisted. Ivanković et al . [12] and Petrović et al .
[18] provide a detailed summary of the process. Each change to the
codebase must be reviewed by at least one other developer. Every
day, tens of thousands of changes to the codebase go through the
review process and tens of thousands of developers participate in
the process, as both code authors and reviewers.
Authors and reviewers exchange comments through the code
review system, and a review progresses through snapshots of files
affected by the change. Each reviewer comment is attached to a
specific line and column range in a specific file snapshot. To resolve
a comment, the author typically modifies the file in their local copy
Figure 1: Example comment posted by a human reviewer.
and exports a new snapshot for the next round of code review.
When the author and all reviewers are satisfied and no automated
analysis is blocking the merge, the code is merged into the codebase.
The most expensive part of the code review process is the time
spent by code authors and reviewers “shepherding” a change (from
initial coding, through addressing reviewer comments and ensur-
ing all automated analyses pass, to finally merging the change
into the codebase). While the process is optimized with automated
systems analyzing the code before the review (notably automatic
code formatting without human intervention), code reviews still
cost thousands of developer-years per year. Thus, even single-digit
percentage savings translate into significant business impact.
2.2 Best Practices
A best practice is a specific use of programming language that is
considered superior, and a best practice document describes how
it should be applied and what benefits it brings. Best practice URL
refers to a best practice document or specific section therein, and
best practice violation refers to a specific piece of code that does not
adhere to a best practice, but can be changed to do so. If clear from
context, we use the terms URL and violation to refer to best practice
URL and best practice violation, respectively.
Google’s central code repository contains code in many lan-
guages, with C++, Java, Python and Go exceeding 100 million lines
each [19]. For 15 different languages there are formal style guides
readily available to all developers. Many of these languages have
additional language primers, documentation for core libraries, and
tip-of-the-week style newsletters. While these materials are not
as strictly enforced as style guides, they are frequently referenced
in code reviews. Some languages boast hundreds of pages of such
documentation. Both code authors and reviewers are expected to
verify that the code follows all best practices.
A formal mechanism called “readability”, introduced more than
a decade ago, ensures that best practices are followed consistently.
Dedicated style experts in a given language, called “readability
mentors”, guide inexperienced developers towards proficiency in
the language [ 23]. Readability mentors commonly summarize a
best practice in a few sentences and at the end of the comment
include a URL for the change author as a reference. Figure 1 shows
an example of a comment posted by a readability mentor.

<!-- page 3 -->
AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Training and fine-tuning (on demand)
WorkerWorkerWorkers
Source 
repository
Comment
storage
Scheduler Relevant
code 
comments
WorkerWorkerWorkers Examples 
(temporal 
splits)
WorkerWorkerTPU pods
Tensorboard
Model 
checkpoints
Input/target
format
Large-scale preprocessing (periodic) Dataset curation (on demand)
Figure 2: Architecture of the model-training pipeline.
The readability process has some drawbacks. For authors, it in-
creases development time due to additional review rounds. For read-
ability mentors, it can become a monotonous and time-consuming
task. It requires mastering hundreds of evolving best practices, in-
cluding the identification and deprecation of outdated rules, and
documenting them (with relevant links) in the code-review sys-
tem. Additionally, it requires tracking, sometimes through multiple
iterations, ensuring that all violations have been remedied.
3 APPROACH
In response to the challenges described sections 2.1 and 2.2, we
developed AutoCommenter, a code analysis tool that automatically
detects best practice violations. It aims to provide timely feedback
for code authors and to alleviate the need for manual best-practice
reviews, thereby allowing reviewers to focus on code functionality.
3.1 Model and Task Definition
Automating best practice analysis requires a model that can rep-
resent source code, pinpoint violation locations, and identify the
violated best practice. We target a text-to-text transformation using
a traditional transformer approach based on T5, using T5X [22].
The best practice analysis is one task in a multi-task large se-
quence model. In addition to the standard pretraining task for T5,
span denoising (predicting masked tokens), other tasks used to
train this model include code-review comment resolution, next
edit prediction, variable renaming, and build-error repair [9]. The
training corpus consists of over 3 billion examples, of which the
best practice analysis dataset contributes about 800k examples. The
model was trained using the standard cross-entropy loss, typical for
such models, and tuned to maximize the sequence accuracy metric,
predicting the exact target text for each example.
For the best practice analysis, the input to the model is a task
prompt and source code, and the target is a source code loca-
tion and a URL for a best practice violation. The task prompt is
formatted as a fixed-text code comment, using the programming
language’s appropriate commenting style. It describes the task in
natural language and precedes the source code, which is a direct
textual representation of one file. If the input exceeds the model
context window, it is truncated. The location is a byte offset in the
source code, and the URL references the violated best practice. A do-
main specific language defines the target format, and a special case
is the “empty” target, if there are no violations. In addition to the
target, the model outputs a confidence score ranging from 0 to 1.
Consider the following input/target example for the Go language.
Input
/ / [ ∗ ] T a s k : C h e c k l a n g u a g e b e s t p r a c t i c e s .
/ / P a c k a g e a d d i t i o n p r o v i d e s Add
package a d d i t i o n
/ / R e t u r n a sum
func Add ( value1 , v a l u e 2 i n t ) i n t {
r e t u r n v a l u e 1 + v a l u e 2
}
Target
INSERT 153 COMMENT h t t p s : / / go . d e v / d o c / comment # f u n c
The first line of the input is the fixed-text task prompt; the rest is
the source code. The target gives the location (byte offset 153 corre-
sponds to the start of theAdd function) and a go.dev URL, pointing
to the exact part of the Go language style guide that the function
comment violates (in this case, the usual practice of starting a com-
ment with the function name). Note that the target may contain no,
one, or multiple (concatenated) location-URL pairs, depending on
the number of violations in the source code.
3.2 Model Training
Figure 2 shows the architecture of the model-training pipeline,
which consists of three parts. We split dataset creation into two
steps (preprocessing and curation) because the first step is signifi-
cantly more expensive as it operates on a much larger amount of
data. The output of the preprocessing step is agnostic to the model’s
input/target representation. This separation improves feature ve-
locity by enabling quick iterations on example representations and
other example-level adjustments. The preprocessing step uses a
fault-tolerant scheduling system and periodically extracts relevant
code comments to ensure that new data is readily available.
3.2.1 Large-scale preprocessing. The training examples are created
from real code review data, but not all code comments are suitable
for model training. Therefore, the preprocessing step, identifies
relevant code comments—human authored comments that contain
a URL pointing to a best practice document. For each comment,
the preprocessing step then collects the corresponding source code
and relevant metadata, including the comment’s location in the
source code and its creation time. The output of this step is a set
of relevant code comments, each with all the data necessary for
curating examples for model training.

<!-- page 4 -->
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil Manushree Vijayvergiya et al.
3.2.2 Dataset curation. Dataset curation is a single, on-demand
processing step, implemented as a Beam1 pipeline. It converts each
relevant code comment, based on the input/target format described
in section 3.1, into the standard TensorFlowExample data structure.
3.2.3 Training and fine-tuning. The curated examples are used
directly for model training and evaluation. We use the T5X frame-
work [22] on a fleet of TPUs, store the model checkpoints every
1000 steps, and use Tensorboard for monitoring the training.
3.3 Model Selection
Two intrinsic evaluations on historical data inform our selection of
a model checkpoint, confidence thresholds, and a decoding strategy.
First, an evaluation on the validation and test datasets provides
estimates of precision and recall on a per-file basis. Second, an
evaluation on full historical code reviews provides an estimate of
the total number of comments per code review, indicating how
often developers would interact with AutoCommenter.
3.3.1 Evaluation on Validation and Test Datasets. We temporally
split the dataset to ensure that the model has not been trained on
future code-review snapshots of the code comments in the valida-
tion and test datasets. In our dataset, 85% of files have exactly one
relevant code comment, 11% have two, and 4% have three or more.
We define a prediction to be correct if the predicted code location(s)
and URL(s) match the expected values, regardless of order.
Recall that the model provides a confidence score for each pre-
diction, which introduces another parameter: a prediction can be
suppressed if its confidence score is below some threshold 𝑡. We
define 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 𝑡 as the number of correct predictions whose confi-
dence score is greater than𝑡 divided by the number of all predictions
whose confidence score is greater than 𝑡; we define 𝑅𝑒𝑐𝑎𝑙𝑙 𝑡 analo-
gously. These definitions allow us to estimate how many (in)correct
results would be shown to a user, as a function of 𝑡. 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 𝑡 and
𝑅𝑒𝑐𝑎𝑙𝑙 𝑡 are used for model checkpoint comparisons during training.
While this evaluation avoids data leakage and allow us to auto-
matically evaluate model performance, it has a limitation: while
it is reasonable to assume that the human comments for a given
code-review snapshot are correct, they are not exhaustive. In other
words, it is possible that the code in a given code-review snapshot
could be improved according to multiple best practices, but a hu-
man reviewer did not post comments (with URLs) for all of them.
This can happen for several reasons:
• Missing references: A reviewer may comment on an issue,
but did not include a URL as a reference.
• Selective commenting: A reviewer may comment on an issue
once, expecting the author to apply a fix throughout.
• Varied expertise or focus: A reviewer may not be familiar with
all best practices, or simply choose not to comment on an
issue in the context of a given code review (e.g., focusing
only on changed code).
While most files in our dataset have only one relevant comment,
anecdotal evidence based on manually inspecting “incorrect” pre-
dictions suggests that multiple best-practice comments are typically
possible due to the reasons stated above. Given that our ground-
truth data is incomplete, our precision and recall measures are noisy.
1https://beam.apache.org/
Therefore, we employ a complementary evaluation, described next,
to increase confidence in overall model performance.
3.3.2 Evaluation on Full Historical Code Reviews. To accurately
gauge potential comment volume in a live setting, we evaluate
AutoCommenter on a set of historical code reviews, using a specific
model checkpoint and threshold. The predicted comments are not
retroactively posted in the code review system, but rather logged
in a database for analysis. This allows us to estimate the expected
posting frequency—both at per-file and per-code-review granularity.
Because developers interact with AutoCommenter for an entire
set of code changes subject to code review, this evaluation is an
important step before production deployment. As an added benefit,
this step allows for further optimizations and assessment of posting
frequencies for different user groups, programming languages, etc.
3.4 Inference Infrastructure
The core of AutoCommenter is a central best practice analysis ser-
vice. This service takes as input one or more source files for analysis.
For each file, it constructs a model input (section 3.1), encodes it
in the standard TensorFlow Example data structure, and queries
the model. The model itself is served by a model service that uses
TensorFlow’s Example data structure as a domain agnostic input-
output format. Finally, the best practice analysis service performs
a series of filtering steps (section 4), which suppress low-quality
predictions, and returns the remaining predictions.
3.5 IDE and Code Review Integration
Developers interact with AutoCommenter’s analysis service in
two ways—directly through an IDE plugin, or indirectly through
the code review system. The code review system is used by all
developers at Google, and the IDE by almost all of them.
AutoCommenter’s comments appear in the IDE as diagnostics
marked with a blue curly underline, spanning the relevant code snip-
pet. Hovering over the underlined code reveals the full comment
with a concise summary of the best practice, including a clickable
link to the relevant best practice document. This embedded infor-
mation streamlines the workflow for developers by eliminating the
need to switch between the IDE and a web browser for unfamiliar
best practices. Since comments in the IDE need to be generated in
real-time, we aim to generate comments with sub-second latency.
In the code review system, AutoCommenter runs after each
update (i.e., on each new code-review snapshot), automatically
posting comments if it detects any violations. Comments produced
by automated tools are visually similar to comments produced by
humans, but have a differently colored background.
Figure 3 shows an example comment generated and posted by
AutoCommenter in the code review system. Note the thumbs up
and thumbs down buttons (right), which authors and reviewers can
click if they find a comment particularly useful or not. Also note
the “Please fix” button (left), which is visible to reviewers. If clicked,
a new comment is generated indicating that the reviewer believes
the comment is significant and must be addressed before the code
is merged into the codebase. These feedback buttons are standard
in the code review system, present on all comments generated by
automated tools (e.g., [7, 13]), and provide a signal for a tool’s user
acceptance. The IDE provides a similar feedback mechanism.