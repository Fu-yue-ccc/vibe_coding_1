<!-- page 5 -->
AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Figure 3: Example comment posted by AutoCommenter.
4 DEPLOYMENT
We deployed AutoCommenter to all developers at Google over a
period of time between July 2022 and October 2023:
• until Jul. 2022—teamfooding: this paper’s authors.
• Jul. 2022—early adopters: around 3 thousand volunteers.
• Jul. 2023—A/B experiment: about half of all developers.
• since Oct. 2023—general availability : all developers.
Note that due to industrial confidentiality reasons we are unable
to disclose absolute numbers of code reviews, developers, files,
comments, or distribution of duration of code reviews. We report
on relative measures, where appropriate, and relevant trends.
We continuously evaluated and improved the performance of
AutoCommenter, using an iterative refinement approach:
• Evaluation on historical data (section 3.3) to get directional
insight into how well the model does at the task and to define
thresholds and select a decoding strategy.
• Monitoring and analysis of user interaction and direct feed-
back through feedback buttons and issue reports.
• Targeted human evaluation based on patterns observed dur-
ing other evaluation steps.
Figure 4 shows the ratio of positive to negative developer feed-
back on posted code review comments and IDE diagnostics over
time. The dashed line shows the total count of feedback clicks de-
velopers provided per month. As is expected, this count is much
lower during the early-adopter stage. Additionally, the volatility is
higher in this stage because we actively refined AutoCommenter.
Recall the three feedback buttons within the code review system
(figure 3), which allow developers to express positive and negative
sentiment about a posted comment. We consider comments with a
thumbs up or “Please fix” as positive, and comments with a thumbs
down as negative; we define the useful ratio as the ratio of positive
comments to all comments with feedback.
The remainder of this section describes specific observations
and corresponding refinements that we made during deployment.
4.1 Selecting Threshold and Decoding Strategy
4.1.1 Threshold. During initial deployment we wanted to carefully
manage the trust developers had in AutoCommenter and started
with a high confidence threshold of 𝑡 = 0.98. We manually sampled
Figure 4: Developer feedback throughout deployment.
several hundred results and observed that around 80% of predictions
below the threshold were still correct—that is, the false-negative
rate was very high at 𝑡 = 0.98. Additionally, we observed that
predictions in Python showed a significantly different distribution
of confidence scores, which were disproportionately impacted by
thresholding. We conjecture that the training dataset composition
(number of distinct URLs and URL frequencies) and specificity of the
best practice documents are reasons, but leave a deeper investiga-
tion to future work. An attempt to deploy per-language thresholds
proved ineffective as a single threshold per language still did not
adequately capture the model’s ability to correctly predict hundreds
of diverse best practices. This led to a lack of diversity in predicted
URLs as the model tended to produce higher scores for some URLs
vs. others, irrespective of correctness. These observations led to the
first major change to AutoCommenter: per-URL thresholds com-
puted based on the intrinsic evaluation on the validation dataset.
4.1.2 Decoding. An evaluation using per-URL thresholds with
greedy decoding on full historical code reviews revealed that Auto-
Commenter detects violations in 6% of all changed files. However,
80% of comments would have been posted on lines of code not
modified by the author. Developers typically do not take action on
unchanged code. Consequently, AutoCommenter filters generated
comments on unchanged lines of code, reducing the ratio of com-
ments in changed files to 1.3%. In order to increase this ratio, we
experimented with different decoding strategies: greedy (default),
beam search, top-k, and top-p sampling. We settled on beam search
(generating 𝑛 = 4 potential responses), which tripled the posting
frequency to 3.9%. It also yielded a substantially higher URL diver-
sity: the 10 most-frequently posted URLs accounted for 41% of all
comments, compared to 80% for greedy search.
Latency is another important aspect when choosing a decoding
strategy for deployment. While beam search increased the posting
frequency and diversity, inference became noticeably slower (me-
dian latency of 2 seconds). Given that this latency is prohibitive
for interactive use in the IDE, we ultimately decided to use beam
search for the code review system and greedy search for the IDE.

<!-- page 6 -->
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil Manushree Vijayvergiya et al.
4.2 Suppressing Outdated Best Practices
After launching AutoCommenter to around 3 thousand voluntary
first-adopters, we noticed a large number of issues being filed by
users within a few days. Many of these corresponded to a single
URL2, which describes best practices related to Python imports.
However, the canonical source for some type names had changed
in Python 3.9, and the best practice had also changed in early 2022.
Since our training data stretches before 2022, it contained a num-
ber of best practice comments that were no longer applicable. We
realized that this is a recurring pattern: as languages evolve, or
new libraries are introduced, best practices evolve as well. One
way of mitigating the problem is to filter out such data (whenever
a rule changes), and retrain the model. This is however time and
resource-consuming: it requires full data regeneration, model train-
ing, evaluation, and rollout. In the meantime, the “outdated” model
needs to be either switched off, causing downtime of the system, or
affected predictions need to be suppressed. Otherwise, the system
could quickly lose developer trust. We opted for suppression of spe-
cific best-practice predictions, using conditional filtering (matching
regular expressions on the source code) for two reasons. First, it
can be dynamically deployed and immediately applied. Second, it
allows for granular filtering of predictions.
4.3 Independent Rating of Selected Comments
After several months of early usage, we observed that the useful
ratio plateaued at around 54%. To understand the reasons, iden-
tify areas for improvement, and prepare for a wider deployment,
we conducted an independent human rating study in April 2023,
analyzing a sample of around 370 posted comments that received
developer feedback during our first-adopters deployment.
To gather diverse perspectives on the usefulness of comments we
recruited 15 raters—developers from partner teams. We asked them
to rate AutoCommenter’s comments that received explicit user
feedback. We did not show the original user feedback to the rater, to
avoid biasing their evaluation. The raters assessed each comment’s
usefulness based on the linked best practice and the surrounding
code. We instructed them to focus on comment correctness, but also
whether the comment would be actionable to them as an author
(e.g., would they resolve a comment that is technically correct but
does not seem worth resolving in a specific instance). They were
encouraged to provide free-form feedback on each comment.
The useful ratio from the rater evaluation was 60%, slightly
higher than the 54% from the developer feedback on the same
comments, but well below our target of 80% for wider deployment.
The most interesting finding from this study was that there were
clear patterns of not useful comments. Here are some examples:
Several topics or complex topic: For example, one URL points
to a section that describes multiple guidelines for interacting with
the Python linter, including cases where it often triggers and ways
to suppress it. An author may struggle to understand what specific
guideline a posted comment is referring to and how to resolve it.
Similarly, the guidance on writing good function documentation in
C++ is a full page of dense text. Raters frequently noted a disconnect
between a best practice (and AutoCommenter’s concise summary)
and the actual code, even when it contained a relevant violation.
2https://github.com/google/styleguide/blob/gh-pages/pyguide.md#22-imports
Importance of high-quality summaries: Raters often found
that AutoCommenter’s summary, which was generated by scraping
the document source and sometimes missing, failed to adequately
explain the relevance of the cited guideline to the comment/code.
Subjective and potentially contentious topic: One example
is avoiding flags in library code. Flags can cause problems when
used in libraries, but some libraries are specifically designed to
have many features configurable via flags. Additionally, legacy code
may not adhere to this guideline and reviewers will not enforce it.
The model did not learn these nuances and sometimes predicted a
violation when an author added a new flag to an existing library.
Systematic model error for some guidelines: One interesting
example is a guideline that promotes the use of the member function
push_back over emplace_back for C++ vectors when both functions
can be used with the same arguments to achieve the same effect.
The model had learned to predict this, but it would also predict
it in cases where emplace_back is warranted, and also when an
unrelated type had a member function called push_back.
Correct but low-value comments: A missing period at the
end of a sentence in a code comment is often allowed by human
reviewers. While technically correct, asking the author to go back
to their IDE and fix the issue may provide net negative value.
The insights from the rater study informed two changes to Auto-
Commenter. First, the rater study identified 17 non-actionable URLs,
whose suppression increased the historical useful ratio from 54% to
66% on developer feedback, and from 60% to 74% on rater feedback.
We further analyzed comments linked to similar, unrated URLs
and suppressed an additional 5. Second, we reviewed and manually
updated summaries for all frequently posted URLs. Together, these
changes were sufficient to reach our target useful ratio of 80% for
the next stage of deployment.
4.4 A/B Experiment
In July 2023, we deployed AutoCommenter to about half of all devel-
opers in the context of an A/B experiment. We randomly assigned
developers to a an experiment group (AutoCommenter enabled)
and a control group (AutoCommenter disabled). We randomized
based on the last few digits of the SHA256 hash of the developers
email address, and we verified that both groups did not differ in
size and composition, including distribution of tenure, seniority,
programming languages and business units. We also confirmed that
none of the variables measured during the experiment differed be-
tween the control and the experiment group before the experiment
began. The comment posting frequency during the experiment was
in line with expectations (section 4.1).
We did not detect any statistically significant change in any
of the following: total duration of code reviews, time developers
actively spent on the code review, the number of comment-response
iterations between the author and the reviewer. We did, however,
detect a slight improvement in coding speed. We conjecture that
the reduction in context switches to documentation leads to this
positive effect. We leave a deeper investigation for future work.
Based on the results, we concluded that there are no adverse effects,
and deployed AutoCommenter to all developers in October 2023.

<!-- page 7 -->
AI-Assisted Assessment of Coding Practices in Modern Code Review AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil
Figure 5: Cumulative distribution of comments per URL for
the automated comments generated by AutoCommenter in
production and human comments in the training data.
5 EV ALUATION
Based on the useful ratio and user feedback gathered since March
2023, we conclude that developers are generally satisfied with the
comments produced by AutoCommenter. We continuously refine
our dataset preparation, thresholds, URL suppression and summa-
rization by analyzing user feedback, to ensure that AutoCommenter
delivers high positive impact on the developer workflow.
Beyond developer satisfaction, with several months in wide re-
lease to all of Google, we evaluated three additional aspects of
AutoCommenter’s performance:
(1) Comment resolution: How often do developers modify
their code to resolve AutoCommenter’s posted comments?
(2) AutoCommenter vs. human comments: How well do Au-
toCommenter’s comments cover the best practice documents
that human reviewers reference in their comments?
(3) AutoCommenter vs. linters: To what extent does Auto-
Commenter’s output go beyond the capabilities of traditional
static analysis tools?
5.1 Comment Resolution
Developers rarely give explicit feedback on AutoCommenter’s com-
ments by clicking the thumbs up/thumbs down buttons in the code
review system and IDE, and the “Please fix” button in the code
review system (figure 3): about 10% of automated comments in the
code review system and 2% of diagnostics in the IDE received ex-
plicit feedback, which is comparable to other automated analyses at
Google. At the same time, developers hover over approximately 50%
of the AutoCommenter’s IDE diagnostics, and prior work showed
that developers often resolve automated comments without explicit
feedback [18]. To assess how often developers resolve AutoCom-
menter’s comments, we conducted an offline analysis, estimating
the ratio of comments resolved by subsequent code changes.
To analyze comment resolution, we extracted historical changes
focused on files with automated comments from AutoCommenter.
For each, we extracted the initial snapshot where the comment was
posted and the snapshot that the developer eventually merged into
the codebase. Each comment spans a specific range of lines. We
used an automated AST-based line mapping approach [18] between
these snapshots, to identify comments that the model originally
Code idioms
Documentation
Formatting
Language
Naming
0 5 10
Number of distinct URLs
Linter Yes No/Partially
Figure 6: The top-50 most frequently predicted URLs catego-
rized into types. Linter indicates whether a linter that detects
a violation exists or can easily be built.
predicted on the first snapshot, but did not predict on the merged
snapshot. Such pairs of snapshots indicated that a comment may
have been resolved, but it is possible that unrelated code changes
could have led to a specific comment no longer being predicted.
An automated analysis of 6000 snapshot pairs revealed that in
50% of cases the comment was absent from the submitted snapshot
on the lines it was originally posted. We manually inspected a
random sample of 40 such pairs. We found that in 80% of cases, a
change made by the author directly resolved the issue described
by the posted comment. Therefore, we estimate that the comment-
resolution rate is about 40%, which is significantly larger than the
ratio of comments with explicit positive feedback to all comments.
5.2 AutoCommenter vs. Human Comments
Figure 5 compares the cumulative distribution of comments (per
unique URL to a best practice document) for the automated com-
ments generated by AutoCommenter in production and human
comments in the training data. The x-axis is the rank of the URL
when all URLs ever used in automated comments are sorted by
frequency. For example, the most frequently used URL has rank 1,
and it accounts for 9.9% of all automated comments. This same URL
appeared in 4.3% of the human created comments in the training
data. In total, AutoCommenter has created comments for 330 dis-
tinct URLs. The set of URLs used by AutoCommenter covers 68%
of historical human comments with a best practice URL. This is a
good result: it demonstrates that AutoCommenter is not focusing
on obscure best practices that are rarely referenced by reviewers.
On the other hand, despite utilizing beam search, URL diversity
remains relatively low. The top-85 URLs make up 90% of comments
created by AutoCommenter. The same set of URLs cover 35% of
human comments with best practice URLs. Improving URL diver-
sity and coverage of best practices in automated comments while
maintaining accuracy and low latency is one of our top priorities.
5.3 AutoCommenter vs. Linters
To understand to what extent AutoCommenter provides value be-
yond linters that can efficiently and precisely check some of the
best practices, we sampled the top-50 most frequently predicted
violations—that is, the top-50 URLs in figure 5. For each sampled

<!-- page 8 -->
AIware ’24, July 15–16, 2024, Porto de Galinhas, Brazil Manushree Vijayvergiya et al.
URL, we inspected its best practice document and determined (1) the
best-practice type (section 1) and (2) whether a linter that detects a
corresponding violation exists or can be easily built. Specifically,
three authors, each with over 10 years of experience in building
static analysis tools, read the documentation and independently
categorized the URLs. There were no disagreements on the best-
practice type, but there were disagreements on whether a linter
can be easily built for about 15% of URLs. The three authors re-
solved these disagreements through majority vote and discussion.
Disagreements stemmed from ambiguous best practices, and those
with multiple guidelines. For example, while checking the pres-
ence of code documentation is relatively straightforward, reasoning
about justified exceptions and clarity of content may not.
Figure 6 shows the distribution of the 50 sampled URLs, broken
down by type and whether violations can be detected by a linter.
For 33/50 (66%) of these best practices, violation detection is beyond
the scope of traditional static analysis.
6 LESSONS LEARNED
Based on our experience developing and deploying AutoCommenter,
we summarize a few key lessons learned:
• Complementing traditional analyses: AutoCommenter’s
LLM-backed approach generates comments for 68% of best
practices frequently referenced by human reviewers. Many
of these are out of scope for traditional static analyses.
• Intrinsic evaluation vs. real-world performance : Intrin-
sic evaluations and real-world performance can diverge sig-
nificantly: our intrinsic evaluation, using a dataset of real-
world human comments together with a state of the art
model architecture and training process, indicated a promis-
ing model, but our extrinsic evaluations and system improve-
ments proved essential for a successful deployment.
• Monitoring user acceptance is critical : Even a few nega-
tive user experiences can erode trust in an automated system.
Continuously monitoring and analyzing real-world feedback
was crucial in detecting such instances and identifying reme-
dies. In the case of AutoCommenter, a simple suppression
mechanism was sufficient to strongly improve user accep-
tance to over 80% without major sacrifices in efficacy.
7 RELATED WORK
Johnson [15] introduced the C linter almost 50 years ago in 1977. In
those 50 years, a considerable body of research on automated static
analysis was produced: a recent literature review by Heckman and
Williams [10] identified 17,571 papers. Many studies explore how
developers interact with static analysis. Johnson et al. [14] explore
challenges developers face when trying to use static analysis. The
results of their study highlights the importance of good integration
into existing developer workflows and the importance of develop-
ing and maintaining trust in the tool. Vassallo et al . [27] explore
how developers interact with static analysis in different contexts,
including coding and code review. They too find that integration
into existing workflows plays a major role in developers willing-
ness to use the tools and that high quality of results is extremely
important. Beller et al. [6] studied usage of static code analysis in a
large number of open source projects. Among other findings, they
highlight that how automated analysis is and should be used varies
based on the programming language.
In contrast, using machine learning for code analysis is a compar-
atively new and less understood field. A number of recent publica-
tions (e.g., Hong et al. [11], Li et al. [16], Li et al. [17], Thongtanunam
et al. [24], Tufano et al. [25], and Tufano et al. [26]) report on model
evaluations and propose tools for automated code review. While
these models and the review comment generation task are very sim-
ilar to the model presented in this paper, evaluations largely focused
on historical datasets. As discussed in section 3.3.1 an intrinsic eval-
uation on only historical comments is somewhat limited and can
sometimes fail to predict real-world performance. Another recent
publication by Frömmgen et al. [9] presents an evaluation of a live
system, but for the opposite task: creating code from comments
rather than comments from code.
8 CONCLUSION
Verifying that code adheres to best practices is a common task in
modern code review processes. While some best practices can be
automatically verified with traditional tools such as linters, many
require the knowledge and judgement of experienced developers,
which requires time and effort.
This paper reports on our experience developing, deploying, and
evaluating AutoCommenter, an LLM-backed code review assistant
system. Specifically, it lays out the entire process from task and
model design, over intrinsic evaluations and system calibrations,
to a staged roll out and end-user evaluation.
The evaluation results show that it is feasible to develop an
end-to-end system with capabilities well beyond traditional tools
while achieving a high degree of end-user acceptance. These results
are a promising first step towards the deployment of sophisticated
code-review assistants and automated code reviews.
Our priority was to ensure a positive developer experience by
designing AutoCommenter to have very high precision. While recall
was not the primary focus, we recognize its significance and plan
to explore what changes in the model and system architecture can
improve recall. For example, the model we used in 2022 was state of
the art at the time. However, it has a limited context window of 2048
tokens which suffices for only around 200 lines of code. Current
state of the art models have context windows of tens of thousands of
tokens during training and over a million tokens during inference.
This leap opens up opportunities for new features and significant
improvement in existing ones.
9 ACKNOWLEDGEMENTS
This work is the result of years of collaboration between teams in
Google Core Systems and Google DeepMind. We are grateful for the
support and advice of all our team members and leadership, includ-
ing Alberto Elizondo, Alexander Frömmgen, Ballie Sandhu, Chandu
Thekkath, Chris Gorgolewski, David Tattersall, Ilya Cherny, Jacob
Austin, Katja Grünwedel, Kristóf Molnár, Lera Kharatyan, Luka Ri-
manić, Madhura Dudhgaonkar, Marc Brockschmidt, Marcus Revaj,
Maxim Tabachnyk, Nina Chen, Niranjan Tulpule, Nitya Ramani,
Paige Bailey, Pavel Sychev, Pierre-Antoine Manzagol, Quinn Madi-
son, Roger Fleig, Satish Chandra, Savinee Dancs, Stoyan Nikolov,
Subhodeep Moitra, and Vaibhav Tulsyan.