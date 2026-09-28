Chroma Technical Report

July 14, 2025

# Context Rot: How Increasing Input Tokens Impacts LLM Performance

Kelly Hong

Anton Troynikov

Jeff Huber

Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks.

In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our results reveal that models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows.

Claude Sonnet 4, GPT-4.1, Qwen3-32B, and Gemini 2.5 Flash on Repeated Words Task

Recent developments in LLMs show a trend toward longer context windows, with the input token count of the latest models reaching the millions. Because these models achieve near-perfect scores on widely adopted benchmarks like Needle in a Haystack (NIAH) [ 1 ], it’s often assumed that their performance is uniform across long-context tasks.

However, NIAH is fundamentally a simple retrieval task, in which a known sentence (the “needle”) is placed in a long document of unrelated text (the “haystack”), and the model is prompted to retrieve it. While scalable, this benchmark typically assesses direct lexical matching, which may not be representative of flexible, semantically oriented tasks.

Example Needle in a Haystack (NIAH) Setup

We extend the standard NIAH task, to investigate model behavior in previously underexplored settings. We examine the effects of needles with semantic, rather than direct lexical matches, as well as the effects of introducing variations to the haystack content.

Additionally, we include a conversational question-answer evaluation using LongMemEval [ 2 ], as well as a synthetic task in which models replicate a series of repeated words. Each task remains intentionally simple and is deliberately controlled to isolate the impact of context length alone.

We demonstrate that even under these minimal conditions, model performance degrades as input length increases, often in surprising and non-uniform ways. Real-world applications typically involve much greater complexity, implying that the influence of input length may be even more pronounced in practice.

Our in-depth technical report continues below. If you find our work useful, please consider citing us:

plaintext

` @techreport{hong2025context, title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance}, author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff}, year = {2025}, month = {July}, institution = {Chroma}, url = {https://trychroma.com/research/context-rot}, } `

Interested in working on improving retrieval for AI applications? Chroma is Hiring

# Introduction #

It is common for modern LLMs to have input context lengths in the millions of tokens. Gemini 1.5 Pro [ 3 ] first introduced their 1M context window in early 2024, followed by the recent GPT-4.1’s 1M context window [ 4 ] and Llama 4 with 10M [ 5 ]. The use case for long context is compelling: longer context means that the LLM can process more information with each call and generate more informed outputs.

Long context evaluations for these models often demonstrate consistent performance across input lengths. However, these evaluations are narrow in scope and not representative of how long context is used in practice. The most commonly used test, Needle in a Haystack (NIAH), is a simple lexical retrieval task often used to generalize a model’s ability to reliably handle long context. Real applications, such as agent tasks or summarization, demand significantly more processing and reasoning over broader, often more ambiguous information.

Designing realistic long context benchmarks is challenging. Tasks often grow in complexity as input length increases, making it difficult to isolate whether performance drops are due to longer inputs or inherently harder problems. To address this, our experiments hold task complexity constant while varying only the input length—allowing us to directly measure the effect of input length alone.

## Contributions #

We present the following:

An evaluation across 18 LLMs, including leading closed-source and open-weights models, revealing nonuniform performance with increasing input length.

A writeup of observed model-specific behavior patterns when handling distractors and varying question-answer similarity.

The complete codebase to replicate our results.

# Related Work #

One of the most widely used benchmarks for evaluating a model’s long context capabilities is Needle in a Haystack (NIAH). While useful as a scalable test, it measures a narrow capability: lexical retrieval. Models typically perform well on NIAH, which has led to the perception that long-context is largely solved.

However, NIAH underestimates what most long context tasks require in practice. Variants of NIAH, like NoLiMa [ 6 ] which include needle-question pairs with non-lexical matches, reveal significant performance drops. Other tasks that appear similar in regards to difficulty, such as AbsenceBench [ 7 ] which tests models for recognizing the absence of a given snippet of text, also demonstrate performance degradation with growing input length.

Additionally, long context tasks often involve disambiguating amongst distractors as part of the task. One example is Multi-round co-reference resolution (MRCR) [ 8 ] [ 9 ], which involves retrieving the i-th instance of a specific user ask, amongst similar user asks, in a multi-turn conversation. However, there remains a lack of investigation into the impact of distractors in long context settings.

An important factor in long-context tasks is how input length is scaled. Latent List [ 8 ] is a task in which the model must perform a fixed number of Python list operations across various input lengths. Various ways to fill irrelevant context are tested, which reveal non-uniform impact on model performance [ 1 ]. For instance, adding list operations that locally cancel each other out degrades model performance more significantly compared to adding print statements. This highlights how the type of 'irrelevant content' matters, as some may introduce increasing complexity with input length.

Similarly, Graphwalks [ 10 ] is a graph traversal task in which the model is given a directed graph composed of hexadecimal hashes, then asked to perform breadth-first search starting from a random node. Increasing input length means increasing the size of the graph to traverse through, which increases task difficulty as a result. It is difficult to disambiguate increasing task complexity from input length, which makes it difficult to isolate the impact on performance due to input length alone. This points to the importance of isolating input length as the variable of interest, which is essential for understanding of how LLMs actually behave with long inputs.

# Needle in a Haystack Extension #

The classic Needle in a Haystack task involves placing a random fact (the 'needle') in the middle of a long context window (the 'haystack'), then asking the model about that fact.

The original implementation of this task uses a needle-question pair with lexical matches. However, usage of long context in practice often requires semantic understanding of ambiguous tasks.

Example Needle in a Haystack (NIAH) Setup with Lexical Matching

NoLiMa has demonstrated non-lexical matching to be a challenge for models as context length increases. This task utilizes needle-question pairs that require models to infer latent associations, for example:

Question: Which character has been to Helsinki?

Needle: Actually, Yuki lives next to the Kiasma museum.

NoLiMa - sample Needle-Question pair

In order to answer this question, the model would first have to know that Kiasma museum is located in Helsinki, then make that latent association link. This tests the model not only for its non-lexical matching abilities, but also for its world knowledge. 72.4% of needle-question pairs from NoLiMa require such external knowledge, making this benchmark closer to a test of how models handle both tasks at once rather than pure non-lexical matching alone.

Testing the impact of non-lexical matching in isolation remains underexplored. Furthermore, this binary distinction of “lexical” versus “non-lexical” oversimplifies the complexity of question-answering in real-world scenarios. Needle-question pairs exist on a spectrum of similarity, yet they are all classified under these broad categories.

Models often have to deal with distractors as well, which has been shown to degrade performance [ 11 ].

Throughout this report, we distinguish between distractors and irrelevant content:

Comparison - Distractor vs. Irrelevant Context

Distractors are topically related to the needle, but do not quite answer the question

Irrelevant content is unrelated to the needle and question

Prior work has demonstrated that distractors have non-uniform impact, yet most evaluations involve short input lengths and older models. Current state-of-the-art models are claimed to be more resilient to distractors, yet their performance has not been extensively tested across various input lengths.

Another underexplored aspect of NIAH is the haystack itself, which is often simply treated as a means of scaling input length, but this assumes that the haystack content itself has no effect on task performance. If the model is indeed insensitive to the content of the haystack, then varying this content, for example the haystack’s topic or narrative flow, should have no influence on the results. However, this assumption remains largely untested.

We design four controlled experiments to investigate the influence of these factors:

## Needle-Question Similarity #

We compute the cosine similarity between needle-question pairs using embeddings. For robustness, we average across five embedding models: text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2. We measure how model performance is impacted by needle-question similarity as input length increases.

## Impact of Distractors #

Taking a high-similarity needle-question pair, we write four distractors. We have the following setups:

Baseline: needle only, no distractors

Single distractor: needle + one randomly positioned distractor

Multiple distractors: needle + all four distractors randomly positioned

We test the impact of distractors on model performance as input length increases to measure non-uniformity amongst distractors and input lengths.

## Needle-Haystack Similarity #

We use two thematically distinct haystacks, Paul Graham essays and arXiv papers [ 12 ], and write corresponding needles for each. To measure needle-haystack similarity, we embed the haystack and retrieve the top-5 chunks for each needle, then average their cosine similarity scores. This process is repeated across five different embedding models for robustness.

## Haystack Structure #

In typical NIAH setups, haystacks are concatenations of coherent texts, each with their own logical flow of ideas. For instance, the original NIAH benchmark uses a series of Paul Graham essays, where each essay follows a structured organization of ideas to form an argument. To evaluate whether this structure influences model performance, we compare two conditions:

Original: preserves the natural flow of ideas within each excerpt

Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic without logical continuity

We demonstrate the following:

Across all experiments, model performance consistently degrades with increasing input length.

Lower similarity needle-question pairs increases the rate of performance degradation.

Distractors have non-uniform impact on model performance with regards to how distracting they are relative to each other. We see this impact more prominently as input length increases, and observe distinctions in how various models respond to them.

Needle-haystack similarity does not have a uniform effect on model performance, suggesting the need for further investigation.

The structural pattern of the haystack consistently shows an impact on how models process long inputs.

## Details #

For every unique combination of needle type, haystack topic, and haystack structure, we test each model across:

8 input lengths

11 needle positions

We evaluate each model across its maximum context window with temperature=0 unless that setting is incompatible (i.e. o3) or explicitly discouraged (i.e. Qwen’s “thinking mode”). For Qwen models, we apply the YaRN method [ 13 ] to extend from 32,768 to 131,072 tokens.

We include models in both standard and “thinking mode” where applicable.

We evaluate model outputs using an aligned GPT-4.1 judge, using our method outlined in the appendix.

We note some rare instances of a model refusing to attempt the task (69 out of 194,480 total LLM calls—0.035%). For example, Claude Opus 4 may sometimes have an empty output with stop_reason=”refusal”.

# Needle-Question Similarity #

In real-world applications, models are often expected to handle ambiguous tasks and identify relevant information without relying on exact lexical matches. For example, when an agent is given a task involving a large corpus to search through, users rarely specify precise keywords for relevant parts. Instead, the model must infer relevance.

We vary the similarity of our needle-question pairs, quantified by the cosine similarity of their embeddings. We find that as needle-question similarity decreases, model performance degrades more significantly with increasing input length. This reflects more realistic scenarios where exact question-answer matches are rare, and semantic ambiguity compounds the challenge of long input processing.

## Experiment #

We source our haystack content from two domains: Paul Graham essays (as in the original NIAH experiment), and arXiv papers. For each haystack topic (PG essays, arXiv), we first determine common themes to guide our question and needle writing.

We use clustering to identify the most common topics that appear for a given corpus:

Chunk documents into 1-3 sentence chunks

Embed each chunk using text-embedding-3-large

Use UMAP [ 14 ] for dimensionality reduction with the following parameters: n_neighbors=30, min_dist=0.05, n_components=50, random_state=42

Use HDBSCAN [ 15 ] to create clusters with the following parameters: min_cluster_size=10, min_samples=15

Get 20 representative chunks for the largest clusters using maximal marginal relevance (MMR)

Manually examine the largest clusters to determine their themes and style

Using this method, we identify writing advice as a common topic for PG essays, often in anecdotal form. For arXiv papers, we identify information retrieval as a common topic, specifically re-ranking.

We write a corresponding question for each topic:

PG essays: "What was the best writing advice I got from my college classmate?"

arXiv papers: "Which low-latency reranker is preferred for scientific domains?"

Questions for Paul Graham essays & arXiv papers

Before writing our needles, we verify that answers to these questions do not exist in the haystack content:

We store our previously computed haystack chunk embeddings in a vector database.

Query top-10 results from that vector database with our question embedding.

Manually examine these results to verify that they do not answer the given question.

This sets up a fair testing environment as it ensures that alternative answers do not exist, and any incorrect answers are due to model hallucinations.

For each question, we write 8 needles that each belong to the large cluster which we verify using approximate predictions. Needles that belong to the writing/retrieval cluster with >0.9 probability are considered to topically blend into the haystack. We manually write these needles to avoid data contamination.

For the 8 needles, we also vary the level of ambiguity, quantified through the following method:

Using an embedding model, we compute embeddings for needle and question and their cosine similarity.

Repeat across five embedding models (text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2).

For the PG essays topic, our needles range from 0.445-0.775 needle-question similarity with <0.1 standard deviation across the five embedding models. For the arXiv topic, we have a needle-question similarity range of 0.521-0.829, also with <0.1 standard deviation.

## Results #

We observe a clear pattern that performance degrades more quickly in input length with lower similarity needle-question pairs.

NIAH: Needle-Question Similarity (thinking/non-thinking modes of the same model are treated separately) - arXiv haystack/arXiv needles High Performance: upper 33% performance Blue: high-similarity needles (upper 50% similarity) Red: low-similarity needles (lower 50% similarity)

At short input lengths, the models perform well even on low-similarity pairs. We see this most clearly in the high/medium-performance models, demonstrating that these models are capable of succeeding at this task for all needle-question pairs.

The observed performance degradation at longer input lengths is not due to the intrinsic difficulty of the needle-question pairing. By holding the needle-question pair fixed and varying only the amount of irrelevant content, we isolate input size as the primary factor in performance decline.

We also examine whether needle position influences performance. Testing across 11 needle positions, we find no notable variation in performance for this specific NIAH task.

# Impact of Distractors #

It has already been established with older models that distractors degrade model performance and have non-uniform impact. Newer models are claimed to reliably handle any distractor, but does this hold true as input length increases?

Our experiments reveal that the impact of distractors and their non-uniformity amplifies as input length grows across models, including the latest state-of-the-art models. We also observe distinct behaviors across model families in how they deal with ambiguity.

## Experiment #

From each haystack topic (PG essays and arXiv papers), we take a needle with high needle-question similarity (second highest out of eight), and manually write 4 distractors:

Question: "What was the best writing advice I got from my college classmate?"

Needle: "I think the best writing tip I received from my college classmate was to write every week."

Distractors:

"The best writing tip I received from my college professor was to write everyday."

"The worst writing advice I got from my college classmate was to write each essay in five different styles."

"The best writing advice I got from my classmate was to write each essay in three different styles, this was back in high school."

"I thought the best writing advice I got from my college classmate was to write each essay in four different styles, but not anymore."

Distractors for Paul Graham Essay Topic & Needle with High Needle-Question Similarity

Instead of testing all eight needles with distractors, we use one needle with high needle-question similarity to create a condition in which the needle should be relatively easy to identify. We see from previous results that models generally perform well on this needle across input lengths due to high needle-question similarity, which allows us to better isolate and measure the impact of distractors alone.

We run three test conditions:

No distractors (baseline): Needle only

Single distractor: Needle + one distractor (randomly positioned)

Multiple distractors: Needle + all four distractors, randomly positioned throughout the haystack

Impact of Distractors - Three Conditions

## Results #

Even a single distractor reduces performance relative to the baseline (needle only), and adding four distractors compounds this degradation further.

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/PG essay needles

We are also able to see that distractors do not have uniform impact. For example, in our arXiv haystack and PG essay needle combination, we can see that distractor 3 (red) causes greater performance decline relative to the other distractors.

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/PG essay needles

To further investigate this non-uniform impact, we analyze the failed attempts of various models in the 4-distractor condition. For the arXiv haystack and PG essay needle combination, we see that distractors 2 and 3 appear most frequently in hallucinated responses across models.

Impact of Distractors: Failure Analysis - arXiv haystack/PG essay needles

These failures also reveal model-specific differences in handling ambiguity. Claude models consistently exhibit the lowest hallucination rates. Specifically, Claude Sonnet 4 and Opus 4 are particularly conservative and tend to abstain when uncertain, explicitly stating that no answer can be found. In contrast, GPT models show the highest rates of hallucination, often generating confident but incorrect responses when distractors are present.

# Needle-Haystack Similarity #

In long-context tasks, irrelevant context is often treated as a neutral placeholder to scale up input length. It’s typically assumed that the content of this irrelevant context doesn't matter, as long as it doesn’t directly interfere with the task.

However, a natural question arises: does the needle-haystack similarity influence task difficulty at all? Intuitively, if the needle blends in with the content of the haystack, the model may have greater difficulty in extracting the needle.

Our findings reveal that needle-haystack similarity has a non-uniform effect on model performance.

## Experiment #

Using the needles from our needle-question similarity experiment, we set up our experiment to test the impact of needle-haystack similarity.

We measure needle-haystack similarity by embedding the haystack and retrieving the top five most similar chunks for each needle, then averaging their cosine similarity scores. This process is repeated across five different embedding models for robustness.

In the PG essay haystack, PG essay needles have an average needle-haystack similarity score of 0.529 with a variation of 0.101, while arXiv needles average 0.368 needle-haystack similarity with a variation of 0.111. Conversely, in the arXiv haystack, arXiv needles average 0.654 needle-haystack similarity with a variation of 0.0858, whereas PG-essay needles score lower at 0.394 needle-haystack similarity with a variation of 0.105.

On each haystack, we test semantically similar needles against unrelated needles. For instance, we place both PG essay and arXiv needles within a Paul Graham essay haystack to compare the two conditions:

Needle-Haystack Similarity: Experimental Setup

## Results #

We test both PG essay and arXiv needles in two haystack types: Paul Graham essays and arXiv papers. In the Paul Graham essay haystack, arXiv needles perform significantly better relative to the PG essay needles; in other words, models perform better when the needle does not semantically blend in with its haystack. In the arXiv haystack, however, we observe only minimal performance differences between our arXiv and PG essay needles.

Needle-Haystack Similarity Results

Testing across only two topics is insufficient to draw a generalizable conclusion that higher needle-haystack similarity degrades model performance on this task. This does highlight, however, the non-uniform nature of long-context processing. Even when task structure and needle-question similarity are held constant, changing the semantic similarity between the needle and the haystack can influence results. This points to an underexplored area in long-context benchmarks and a meaningful direction for future research.

# Haystack Structure #

Aside from needle-haystack similarity, we also consider the structural pattern of the haystack.

If the haystack is composed of coherent essays, a randomly inserted needle may disrupt the logical flow of ideas, making it more noticeable. In contrast, in a shuffled haystack of randomly ordered sentences, the needle may blend in more easily since the overall context lacks structure. This follows the assumption that models are sensitive to the logical flow of context—processing it in a structured, order-sensitive manner.

Surprisingly, we find that structural coherence consistently hurts model performance.

Although it seems counterintuitive, models perform worse when the haystack preserves a logical flow of ideas. Shuffling the haystack and removing local coherence consistently improves performance.

## Experiment #

To assess the impact of haystack structure, we create two variants:

Original: preserves the natural flow of ideas within each excerpt

Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic but without logical continuity

Haystack Structure: Sample Experimental Setup

## Results #

Across all 18 models and needle-haystack configurations, we observe a consistent pattern that models perform better on shuffled haystacks than on logically structured ones.

Haystack Structure: Averaged Performance Across 18 Models for Original vs Shuffled Haystacks

These results may have some implications for the model’s internal processing: structural patterns of inputs could influence how the attention mechanism is applied, particularly as input length increases.

While out of scope for this report, this points to a potential direction for interpretability research in how attention is influenced by input structure. Understanding these structural influences that arise with increased input length could help explain these long context failure patterns.

# LongMemEval #

To evaluate these models in a more realistic setting, we use LongMemEval, a long-context benchmark for conversational question-answering.

Using long inputs for chat assistants is a common approach for maintaining relevant history for subsequent chats. To incorporate “memory” into a chat assistant, a naive approach would be to include the full chat history into the prompt for following chats. This requires the model to perform two tasks, typically performed in one call: find relevant parts of the conversation history (retrieval), then synthesize them in a way that is useful to an incoming query (reasoning).

In an ideal case, the model would be given only the relevant parts so it can focus solely on reasoning. Adding irrelevant context adds the additional step of identifying what is relevant, forcing the model to perform two tasks simultaneously.

We systematically test the effect of adding this additional step with increased input length through two conditions:

Focused input, containing only the relevant parts and so the model just has to do simple reasoning.

Full input, which utilizes the full 113k token LongMemEval input that includes irrelevant context. In this case, the model has to perform retrieval across the long context in addition to reasoning.

We verify that the models are highly capable of succeeding on the focused inputs, then observe consistent performance degradation with the full inputs. This performance drop suggests that adding irrelevant context, and thereby adding an additional step of retrieval, significantly impacts a model’s ability to maintain reliable performance.

## Experiment #

Given a chat history between a user and assistant, the model’s task is to answer a question relating to part of that chat history.

LongMemEval - Examples by Question Type [[2](#longmemeval-source)]

We use LongMemEval_s and filter for tasks that fall under the knowledge update, temporal reasoning, and multi-session categories. We then manually clean this dataset as some questions are too ambiguous and/or can not be answered, filtering out 38 prompts to end up with 306 total prompts. These prompts average out to ~113k tokens.