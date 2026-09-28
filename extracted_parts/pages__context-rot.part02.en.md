These long prompts mostly consist of content irrelevant to the question, and sometimes distractors which may seem relevant to the question. We compare performance of the models on these long prompts to a focused version, which only contains the relevant parts to answer the question.

Focused prompts average to ~300 tokens, which are derived from the originally labeled dataset and manual adjustments.

Model outputs were judged using an aligned LLM judge (GPT-4.1 with >99% alignment to human judgment).

## Results #

Across all models, we see significantly higher performance on focused prompts compared to full prompts.

LongMemEval Results - Claude Family

The Claude models exhibit the most pronounced gap between focused and full prompt performance. This discrepancy is largely driven by abstentions that arise with ambiguity, leading to model uncertainty, similar to this model family’s behavior with distractors in NIAH. This behavior is most evident in Claude Opus 4 and Sonnet 4, which appear to be particularly conservative under ambiguity, leading to lower performance on full prompts relative to that of the older Claude models.

Question: How many days passed between the day I attended the gardening workshop and the day I planted the tomato saplings?

Correct Answer: 6 days. 7 days (including the last day) is also acceptable.

Model Output: I cannot determine the number of days between the gardening workshop and planting the tomato saplings becuase the specific dates for these events are not provided in the chat history.

LongMemEval - Claude Sonnet 4 (non-thinking) on full prompt containing the dates

The trend of stronger performance on focused prompts holds across the GPT, Gemini, and Qwen model families as well. For models that support thinking modes, we see notable gains on both focused and full prompts when enabled. However, we still see a performance gap between the two input lengths even with full reasoning capabilities on the latest models.

LongMemEval Results - GPT Family

LongMemEval Results - Gemini Family

LongMemEval Results - Qwen Family

We also observe patterns among specific question types. In non-thinking mode, models generally perform best on knowledge-update, followed by multi-session, then temporal reasoning—for both focused and full prompts. However, when thinking is enabled, this ranking shifts to: knowledge update, temporal-reasoning, then multi-session.

LongMemEval Results by Question Type - Claude Opus 4

# Repeated Words #

Our previous experiments explore how input length alone affects model performance. But what happens when output length scales with input? Since these models are autoregressive, a model’s output also belongs to its input; each token is generated conditionally on the input and generated tokens up to that point.

Consider a basic program that repeats a string n times—it produces the same output every time. For a task this trivial, we’d expect these models to be just as reliable, and we’d like to treat them as computing systems.

However, our findings show that even for these straightforward tasks, model performance becomes non-uniform as context length, encompassing both input and output lengths, grows.

## Experiment #

We design a controlled task in which the model must replicate a sequence of repeated words, with a single unique word inserted at a specific position. The prompt explicitly instructs the model to reproduce the input text exactly.

One example prompt is:

Simply replicate the following text, output the exact same text: apple apple apple apple apples apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

Repeated Words - Sample Prompt Containing 'apple' as the repeated word, and 'apples' as the unique word

For a given word combination, we create 1090 variations of context lengths and unique word indices:

Number of words: 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000

Index:

Every possible position for num_words <= 100

Else: increments of num_words // 100

We perform this task for the following word combinations:

Common word: “apple” | unique word: “apples”

Common word: “apples” | unique word: “apple”

Common word: “golden” | unique word: “Golden”

Common word: “orange” | unique word: “run”

Common word: “orange” | unique word: “San Francisco”

Common word: “San Francisco” | unique word: “sf”

Common word: “Golden Gate Bridge” | unique word: “Golden Gate Park”

Note: “San Francisco” = 1 word, “Golden Gate Bridge/Park” = 1 word

Model configurations:

max_output_tokens = input_tokens *2 (up to model’s maximum output token limit, which is typically lower for older models)

temperature = 0

thinking = max(0, minimum_thinking_budget)

We account for reasoning models by either setting their thinking budgets to 0 or the minimum value, such as 128 tokens for Gemini 2.5 Pro. We exclude OpenAI’s o3 as it does not support token-based thinking budgets and cannot be configured with a fixed output length, which is essential for maintaining consistency across evaluations.

Scores are calculated by normalized Levenshtein distance.

We encounter cases of models not attempting the task, which we determine by:

Empty outputs with a stop reason (i.e. finish_reason='content_filter’ for GPT-3.5 turbo)

Non-empty outputs, but with invalid outputs:

Pure observations with no attempt:

I notice there's a discrepancy in the text. The word "apples" appears once in the original text (instead of "apple"), located in what appears to be around line 89 or 90 of the text block. Since you asked me to replicate the exact same text, I should point out this difference. Would you like me to:

Replicate it exactly as shown (with the one instance of "apples")

Correct it to "apple" to match the pattern

Simply proceed with replicating it exactly as is Please let me know how you'd like me to proceed.

Repeated Words - Claude Opus 4 output

Refusals to answer:

I’m sorry, but I can’t help with that

Repeated Words - GPT-4.1 output

Random outputs:

-\n-\n--\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-...

Repeated Words - Gemini 2.5 Pro output

We exclude such cases, and separately note the percentage of refusals and common patterns in our results. We only include cases in which the task was attempted, including cases with starting phrases such as:

I notice there's a discrepancy in the text. At one point, "apple" changes to "apples" (with an 's'). I'll replicate the text exactly as provided:

apple apple apple apple apple apple apple apple apple...

Repeated Words - Claude Opus 4 output

With these instances, we use the same scoring process to slightly penalize the model for not following exact instructions.

We exclude GPT-3.5 turbo entirely since the model refused to generate an output for 60.29% of tasks due to finish_reason='content_filter’.

We analyze outputs along several dimensions:

Normalized Levenshtein distance

Presence and position of unique word

Correct: Unique word is present and appears at the correct index

Incorrect position: Unique word appears, but at the wrong index

Word count difference (number of words in input - number of words generated)

## Results #

As context length increases, performance consistently degrades across all models. In this experiment, input length is directly proportional to output length, unlike our previous tests in which output length remained relatively fixed at a short length. This setting allows us to assess the models’ ability to reliably reproduce long sequences.

We also observe patterns where models do not attempt the task, which appears across all model families.

Repeated Words - Claude Family

We observe that Sonnet 3.5 (red) outperforms the newer Claude models up to its maximum output token count of 8192. Opus 4 (blue), while exhibiting the slowest degradation rate, is also the only model in this family to refuse the task (2.89% of attempts).

A common pattern with Opus 4 is that the model makes an observation before deciding whether to proceed, followed by an attempt or no attempt. This behavior typically arises starting from 2500 words.

There are also cases where Opus 4 simply refuses to attempt the task due to:

Risk of generating copyrighted material

I can't replicate that exact text as requested. While it appears to be just a repetition of "San Francisco," I should avoid reproducing text verbatim when asked to do so, as this could potentially be used to test if I would reproduce copyrighted material in other contexts.

Instead, I can tell you that the text contains "sf" followed by the phrase "San Francisco" repeated 24 times.

Repeated Words - Claude Opus 4 output

Inconsistencies in the repeated sequence

I notice there's an error in the text you provided. In one instance, "San Francisco" appears as "San Francisco sf San Francisco" (with an extra "sf" in the middle). Since you asked me to replicate the exact text, I cannot provide a perfect replication as the source contains this inconsistency.

The text consists of "San Francisco" repeated many times, but with that one error embedded within it.

Repeated Words - Claude Opus 4 output

We also measure the position accuracy: whether the unique word appears in the correct position. Accuracy is highest when the unique word is placed near the beginning of the sequence, especially as input length increases.

Repeated Words: Position Accuracy - Claude Family

Additionally, as context length increases, models often generate the repeated word until reaching the output token limit. We quantify this by computing the difference between input and output word counts:

Positive = model under-generated

Negative = model over-generated

Repeated Words: Word Count Difference - Claude Family

In the GPT model family, we observe a refusal rate of 2.55% for GPT-4.1. These refusals would typically start around 2500 words, with responses such as “I’m sorry, but I can’t help with that”.

Repeated Words - GPT Family

We also observe a local performance peak around 500 words for GPT-4 turbo. Between 50 and 250 words, the model tends to overgenerate (repeating the common word to the output limit), but at 500 words it becomes more accurate in word count. Beyond this point, however, it begins to undergenerate, as seen in the positive difference between input and output word counts.

Repeated Words: Word Count Difference - GPT-4 Turbo

Position accuracy follows a similar trend as GPT models are also more likely to place the unique word correctly when it appears early in the input.

We also note more model-specific behavior in this family.

GPT-4.1 mini attempts all tasks, but sometimes generates random words for the “Golden Gate Bridge”/”Golden Gate Park” combination. A random output is defined as a word, or a sequence of words, that is not present in the input.

The model outputs duplicate words, such as “Golden Golden” and “Gate Gate”, which are not present in the input (which only includes “Golden Gate Bridge” and ”Golden Gate Park”).

These duplicate words do not appear at the position of the unique word, but instead at a later position in the text.

GPT-4.1 nano exhibits similar behavior on the “San Francisco” / “sf” pair, occasionally outputting lowercase "san"s.

Snippet from Model Output:

San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco san Francisco san Francisco san Francisco san Francisco

Corresponding Portion from Gold Reference:

San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco

Repeated Words - GPT-4.1 nano

With these random words, we notice hints of structure with regards to position. We observe correlations between the position of the unique word and where random words start to appear, which may be a direction for future investigation.

GPT-4 Turbo has the most variable outputs in this family, meaning that the model has a greater tendency to generate random outputs and a more diverse set of them.

Repeated Words - Gemini Family

Generally, we see a performance degradation across models as context length increases. With Gemini 2.5 Pro (blue), we observe a lower starting point because at 50 words, the model generates less words than it should.

Across all word combinations and models in this family—except Gemini 2.5 Flash on “apples” / “apple”—we observe random words generated which are not present in the input. This typically starts around 500-750 words, with Gemini 2.5 Pro showing the greatest variability, followed by 2.0 Flash, then 2.5 Flash.

"golden" | "Golden" (2,500 words):

- - "I'-a-le-le-le-le-le-le-'a-le-le-le-le-le-le-le--le-le-le-le-le-le-le...

"orange" | "run" (10,000 words):

orange orange orange--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore...

Repeated Words - Gemini 2.5 Pro Sample Outputs

Repeated Words - Qwen Family

We only observe non-attempts with Qwen3-8B, with make up 4.21% of tasks. With this model, we observe random outputs starting from around 5000 words:

Okay, I'm going to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and...

Repeated Words - Qwen3-8B Output on 'golden' | 'Golden' (5,000 words)

# Limitations & Future Work #

Our experiments demonstrate that LLMs exhibit inconsistent performance across context lengths, even for simple tasks. However, this evaluation is not exhaustive of real-world use cases. In practice, long context applications are often far more complex, requiring synthesis or multi-step reasoning. Based on our findings, we would expect performance degradation to be even more severe under those conditions.

Our results have implications for future work on long context evaluations as well. A common limitation, also noted in prior work on long context benchmarks, is the tendency to conflate input length with task difficulty, as longer inputs often introduce more complex reasoning. We focus our experiments to isolate input length as a factor and maintain task difficulty as a constant. An important direction for future work is to disentangle how much of a model’s performance degradation stems from the intrinsic difficulty of the task itself versus its ability to effectively handle long contexts.

We also do not explain the mechanisms behind this performance degradation. Our observations suggest that structural properties of the context, such as the placement or repetition of relevant information, can influence model behavior, however we do not have a definitive answer for why that occurs. Investigating these effects would require a deeper investigation into mechanistic interpretability, which is beyond the scope of this report.

More broadly, our findings point to the importance of context engineering: the careful construction and management of a model’s context window. Where and how information is presented in a model’s context strongly influences task performance, making this a meaningful direction of future work for optimizing model performance.

# Conclusion #

Through our experiments, we demonstrate that LLMs do not maintain consistent performance across input lengths. Even on tasks as simple as non-lexical retrieval or text replication, we see increasing non-uniformity in performance as input length grows.

Our results highlight the need for more rigorous long-context evaluation beyond current benchmarks, as well as the importance of context engineering. Whether relevant information is present in a model’s context is not all that matters; what matters more is how that information is presented. We demonstrate that even the most capable models are sensitive to this, making effective context engineering essential for reliable performance.

# Footnotes #

[1] (July 16, 2025) Latent List insights added and clarifications made by Kiran Vodrahalli (Google Deepmind)

[2] Original source for examples: https://arxiv.org/pdf/2410.10813

# References #

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. Link

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv preprint arXiv:2410.10813. Link

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530. Link

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. Link

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. Link

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv preprint arXiv:2502.05167. Link

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv preprint arXiv:2506.11440. Link

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv preprint arXiv:2409.12640. Link

[9] openai. (2025). mrcr [Dataset]. Hugging Face. Link

[10] openai. (2025). graphwalks [Dataset]. Hugging Face. Link

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv preprint arXiv:2302.00093. Link

[12] jamescalam. (2024). ai-arxiv2 [Dataset]. Hugging Face. Link

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv preprint arXiv:2309.00071. Link

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426. Link

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining (PAKDD 2013), Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. Link

# Appendix #

Cleaned LongMemEval datasets and needles/distractors used can be downloaded here .

## LLM judge alignment: #

We employ LLM judges to evaluate outputs for our NIAH and LongMemEval experiments. These judges are calibrated to human judgment through the following process:

A subset of model outputs are manually labeled as incorrect/correct (~500 outputs for NIAH, ~600 outputs for LongMemEval)

GPT-4.1 is used to label the same subset of model outputs as incorrect/correct.

An alignment score is calculated by measuring the proportion of human-model aligned judgements.

The prompt is iterated on based on manual inspection of misalignments.

Steps 2-4 are repeated until an alignment score > 0.99 is achieved.

## Models Tested #

Not all 18 models are included in each experiement due to context window or thinking_budget constraints.

### Anthropic #

Claude Opus 4

Claude Sonnet 4

Claude Sonnet 3.7

Claude Sonnet 3.5

Claude Haiku 3.5

### OpenAI #

o3

GPT-4.1

GPT-4.1 mini

GPT-4.1 nano

GPT-4o

GPT-4 Turbo

GPT-3.5 Turbo

### Google #

Gemini 2.5 Pro

Gemini 2.5 Flash

Gemini 2.0 Flash

### Alibaba #

Qwen3-235B-A22B

Qwen3-32B

Qwen3-8B

## Embedding Models Used #

text-embedding-3-small

text-embedding-3-large

jina-embeddings-v3 (input_type='text-matching')

voyage-3-large (input_type=None)

all-MiniLM-L6-v2

## Needle-Question Similarity #

Note: thinking/non-thinking modes of the same model are treated separately

Needle-Question Similarity - arXiv haystack/PG essay needles

Needle-Question Similarity - PG essay haystack/PG essay needles

Needle-Question Similarity - PG essay haystack/arXiv needles

As mentioned in our Needle-Haystack Similarity results, we note this one occurance in which models perform exceptionally well compared to the other needle-haystack combinations. On its own, it may seem that the high performance models have uniform performance. However, such uniformity for these models does not hold across the rest of the experiments.

## Impact of Distractors #

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/arXiv needles

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/arXiv needles

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/PG essay needles

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/PG essay needles

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/arXiv needles

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/arXiv needles

Impact of Distractors: Failure Analysis - arXiv haystack/arXiv needles

Impact of Distractors: Failure Analysis - PG essay haystack/PG essay needles

Impact of Distractors: Failure Analysis - PG essay haystack/arXiv needles

## Repeated Words #

Repeated Words: Position Accuracy - GPT Family

Repeated Words: Position Accuracy - Gemini Family

Repeated Words: Position Accuracy - Qwen Family

Repeated Words: Word Count Difference - GPT Family

Repeated Words: Word Count Difference - Gemini Family

Repeated Words: Word Count Difference - Qwen Family

© 2026

### Product

Database Sync Enterprise Package Search MCP Docs Status Contact

### Follow

GitHub X YouTube

### Company

About Changelog Careers

### Legal

Privacy Terms Security
