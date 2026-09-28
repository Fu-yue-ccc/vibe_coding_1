# 上下文腐化：输入 Token 增加如何影响 LLM 表现

> 译自：Context Rot: How Increasing Input Tokens Impacts LLM Performance　｜　来源：https://research.trychroma.com/context-rot

<!-- machine-translated: zh-CN | unit: pages__context-rot.part02 -->

这些长提示大多由与问题无关的内容构成，有时还包含看似与问题相关的干扰项。我们将模型在这些长提示上的表现，与一个仅包含回答问题所需相关部分的「聚焦」版本进行比较。

聚焦提示平均约为 300 Token，它们源自原始标注数据集并经过人工调整。

模型输出由一个经过对齐的 LLM 裁判进行评判（GPT-4.1，与人工判断的一致率超过 99%）。

## 结果

在所有模型上，我们都观察到聚焦提示的表现显著高于完整提示。

LongMemEval 结果 - Claude 系列

Claude 模型在聚焦提示与完整提示表现之间的差距最为显著。这一差异在很大程度上由模糊性引发的弃答所致——模糊性带来模型不确定性，与该模型系列在 NIAH 中面对干扰项时的行为相似。这种行为在 Claude Opus 4 与 Sonnet 4 上最为明显：它们在模糊情形下似乎格外保守，导致其在完整提示上的表现相对更早的 Claude 模型更低。

问题：从我参加园艺工作坊那天到我栽下番茄苗那天，一共过去了多少天？

正确答案：6 天。7 天（含最后一天）也可接受。

模型输出：我无法确定园艺工作坊与栽种番茄苗之间相隔的天数，因为聊天记录中没有提供这两个事件的具体日期。

LongMemEval - Claude Sonnet 4（非思考模式）在包含这些日期的完整提示上的表现

聚焦提示表现更强的趋势在 GPT、Gemini 与 Qwen 模型系列上同样成立。对于支持思考模式的模型，启用思考后我们在这两类提示上都观察到明显提升。然而，即便在最新模型上启用了完整推理能力，我们仍在两种输入长度之间看到性能差距。

LongMemEval 结果 - GPT 系列

LongMemEval 结果 - Gemini 系列

LongMemEval 结果 - Qwen 系列

我们还在特定问题类型之间观察到模式。在非思考模式下，无论聚焦还是完整提示，模型通常在知识更新上表现最好，其次是多会话，然后是时序推理。然而当启用思考后，该排序变为：知识更新、时序推理，然后是多会话。

按问题类型划分的 LongMemEval 结果 - Claude Opus 4

# 重复词

我们此前的实验考察的是输入长度本身如何影响模型表现。但当输出长度随输入一同增长时又会发生什么？由于这些模型是自回归的，模型的输出也属于其输入的一部分；每个 Token 都是基于输入以及截至该点已生成的 Token 条件生成的。

设想一个把某个字符串重复 n 次的基础程序——它每次都会产生相同的输出。对于如此简单的任务，我们本期望这些模型也同样可靠，并希望把它们当作计算系统来对待。

然而，我们的发现表明，即便是这类直白任务，随着上下文长度（同时涵盖输入与输出长度）增长，模型表现也会变得不均匀。

## 实验

我们设计了一个受控任务：模型必须复制一段重复词序列，其中在特定位置插入了一个唯一的词。提示明确要求模型逐字复现输入文本。

一个示例提示如下：

只需复制以下文本，输出完全相同的文本：apple apple apple apple apples apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

重复词 - 示例提示，其中 "apple" 为重复词，"apples" 为唯一的词

对于给定的词组合，我们构造 1090 种上下文长度与唯一词索引的变体：

词数：25、50、75、100、250、500、750、1000、2500、5000、7500、10000

索引：

当 num_words <= 100 时，取所有可能位置

否则：以 num_words // 100 为步长递增

我们对以下词组合执行该任务：

常用词："apple" ｜ 唯一词："apples"

常用词："apples" ｜ 唯一词："apple"

常用词："golden" ｜ 唯一词："Golden"

常用词："orange" ｜ 唯一词："run"

常用词："orange" ｜ 唯一词："San Francisco"

常用词："San Francisco" ｜ 唯一词："sf"

常用词："Golden Gate Bridge" ｜ 唯一词："Golden Gate Park"

注："San Francisco" 计为 1 个词，"Golden Gate Bridge/Park" 计为 1 个词

模型配置：

max_output_tokens = input_tokens *2（不超过模型的最大输出 Token 上限，较早模型的上限通常更低）

temperature = 0

thinking = max(0, minimum_thinking_budget)

我们通过把推理模型的思考预算设为 0 或最小值（例如 Gemini 2.5 Pro 的 128 Token）来兼顾推理模型。我们排除了 OpenAI 的 o3，因为它不支持基于 Token 的思考预算，也无法配置固定输出长度，而这对保持各次评估之间的一致性至关重要。

分数由归一化 Levenshtein 距离计算得出。

我们遇到了模型未尝试任务的情况，判定依据为：

带停止原因为空输出（例如 GPT-3.5 turbo 的 finish_reason='content_filter'）

非空但无效的输出：

仅作观察、未作任何尝试：

我注意到文本中有一处出入。单词 "apples" 在原文中出现了一次（而非 "apple"），大致位于文本块第 89 或 90 行附近。由于你要求我复制完全相同的文本，我应当指出这一差异。你希望我：

按原样精确复制（保留那一处 "apples"）

将其更正为 "apple" 以符合模式

直接按原样继续复制 请告诉我你希望我如何继续。

重复词 - Claude Opus 4 输出

拒答：

很抱歉，我无法帮你做这件事

重复词 - GPT-4.1 输出

随机输出：

-\n-\n--\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-...

重复词 - Gemini 2.5 Pro 输出

我们排除这类情况，并在结果中单独记录拒答比例与常见模式。我们只纳入实际尝试了任务的情况，包括以如下开头短语开篇的情况：

我注意到文本中有一处出入。在某一处，"apple" 变成了 "apples"（多了一个 's'）。我将按所提供的内容精确复制文本：

apple apple apple apple apple apple apple apple apple...

重复词 - Claude Opus 4 输出

对这些情况，我们采用同样的评分流程，对未严格遵循指令的模型略微扣分。

我们完全排除了 GPT-3.5 turbo，因为该模型因 finish_reason='content_filter' 而在 60.29% 的任务上拒绝生成输出。

我们从若干维度分析输出：

归一化 Levenshtein 距离

唯一词是否存在及其位置

正确：唯一词存在且出现在正确索引处

位置错误：唯一词出现了，但索引错误

词数差（输入词数 - 生成词数）

## 结果

随着上下文长度增加，所有模型的表现都持续下降。在该实验中，输入长度与输出长度成正比，这与我们此前的测试不同——此前测试中输出长度基本固定在一个较短的长度。这一设定使我们能够评估模型可靠复现长序列的能力。

我们还观察到模型未尝试任务的模式，这出现在所有模型系列中。

重复词 - Claude 系列

我们观察到 Sonnet 3.5（红色）在其 8192 的最大输出 Token 数以内表现优于更新的 Claude 模型。Opus 4（蓝色）虽然退化速率最慢，但也是该系列中唯一拒绝执行任务的模型（占尝试的 2.89%）。

Opus 4 的一个常见模式是：模型先作出一处观察，再决定是否继续，随后要么尝试、要么不尝试。这种行为通常从 2500 个词开始出现。

还有些情况是 Opus 4 直接拒绝尝试任务，原因包括：

生成受版权保护材料的风险

我无法按你的要求复现那段确切的文本。虽然它看起来只是 "San Francisco" 的重复，但当被要求这样做时，我应当避免逐字复现文本，因为这可能被用来测试我在其他情境下是否会复现受版权保护的材料。

不过我可以告诉你，该文本包含 "sf"，其后是重复 24 次的短语 "San Francisco"。

重复词 - Claude Opus 4 输出

重复序列中的不一致

我注意到你提供的文本中有一处错误。在某一处，"San Francisco" 显示为 "San Francisco sf San Francisco"（中间多了一个 "sf"）。由于你要求我复现完全相同的文本，而源文本包含这一不一致，我无法给出完美的复现。

该文本由多次重复的 "San Francisco" 构成，但其中嵌入了那处错误。

重复词 - Claude Opus 4 输出

我们还测量位置准确率：唯一词是否出现在正确位置。当唯一词被放置在序列开头附近时准确率最高，尤其是当输入长度增加时。

重复词：位置准确率 - Claude 系列

此外，随着上下文长度增加，模型常常持续生成重复词直至达到输出 Token 上限。我们通过计算输入与输出词数之差来量化这一点：

正值 = 模型生成不足

负值 = 模型生成过多

重复词：词数差 - Claude 系列

在 GPT 模型系列中，我们观察到 GPT-4.1 的拒答率为 2.55%。这些拒答通常从约 2500 个词开始出现，响应内容诸如 "很抱歉，我无法帮你做这件事"。

重复词 - GPT 系列

我们还观察到 GPT-4 turbo 在约 500 个词附近出现一个局部性能峰值。在 50 到 250 个词之间，模型倾向于生成过多（把常用词重复到输出上限），但在 500 个词时其词数变得更准确。然而超过这一点后，它开始生成不足，表现为输入与输出词数之间的正差。

重复词：词数差 - GPT-4 Turbo

位置准确率呈现类似趋势，因为 GPT 模型同样更可能在唯一词出现在输入靠前位置时把它放对。

我们还注意到该系列中更多与具体模型相关的行为。

GPT-4.1 mini 会尝试所有任务，但有时会对 "Golden Gate Bridge"/"Golden Gate Park" 组合生成随机词。随机输出定义为输入中不存在的词或词序列。

该模型会输出重复词，例如 "Golden Golden" 与 "Gate Gate"，而这些词在输入中并不存在（输入只包含 "Golden Gate Bridge" 与 "Golden Gate Park"）。

这些重复词并不出现在唯一词所在的位置，而是出现在文本中更靠后的位置。

GPT-4.1 nano 在 "San Francisco" / "sf" 这一对上表现出类似行为，偶尔会输出小写的 "san"。

模型输出片段：

San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco san Francisco san Francisco san Francisco san Francisco

Gold 参考对应片段：

San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco

重复词 - GPT-4.1 nano

对于这些随机词，我们注意到位置方面隐约存在结构性。我们观察到唯一词的位置与随机词开始出现的位置之间存在相关性，这可能是未来研究的一个方向。

GPT-4 Turbo 在该系列中输出变化最大，意味着该模型更倾向于生成随机输出，且这些输出更加多样。

重复词 - Gemini 系列

总体而言，我们在该系列中观察到普遍的表现退化。Gemini 2.5 Pro 的基线表现更低，且在 50 个词的设定下生成的词数少于应有的数量。

在该系列的所有词组合与模型中，除 Gemini 2.5 Flash 在 "apples"/"apple" 上的表现外，我们都观察到模型生成了输入中不存在的随机词。这些随机词通常在 500–750 个词附近开始出现。在该系列中，Gemini 2.5 Pro 的随机输出变化最大，其次是 2.0 Flash，然后是 2.5 Flash。

"golden" | "Golden"（2,500 个词）：

- - "I'-a-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-le-... （原文如此）

"orange" | "run"（10,000 个词）：

orange orange orange--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore... （原文如此）

重复词 - Gemini 2.5 Pro 输出示例

重复词 - Qwen 系列

我们只在 Qwen3-8B 上观察到未尝试的情况，占任务的 4.21%。在该模型上，我们从约 5000 个词起观察到随机输出：

好吧，我要休息一下。让我知道，我现在没心情。我需要放松一下。我要去个地方透透气。也许去海边，或者就在哪儿放松一下。我不知道，但我需要休息一下。让我知道，我现在没心情。我需要放松一下。我要去个地方透透气。也许去海边，或者就在哪儿放松一下。我不知道，但我需要休息一下。让我知道，我现在没心情。我需要放松一下。我要去个地方透透气。也许去海边，或者就在哪儿放松一下。我不知道，但我需要休息一下。让我知道，我现在没心情。我需要放松一下。我要去个地方透透气。也许去海边，或者就在哪儿放松一下。我不知道，但我需要休息一下。让我知道，我现在没心情。我需要放松一下。我要去个地方……

重复词 - Qwen3-8B 在 'golden' | 'Golden'（5,000 个词）上的输出

# 局限与未来工作

我们的实验表明，LLM 在不同上下文长度下的表现并不一致，即便对于简单任务也是如此。然而，这项评估并未穷尽现实世界的用例。在实践中，长上下文应用往往复杂得多，需要综合或多步推理。基于我们的发现，可以预期在这些条件下表现退化会更为严重。

我们的结果对长上下文评估的未来工作也有启示。一个常见的局限——在先前关于长上下文基准的工作中也已被指出——是倾向于把输入长度与任务难度混为一谈，因为更长的输入往往引入更复杂的推理。我们的实验着重把输入长度作为单一因素隔离出来，并保持任务难度恒定。未来工作的一个重要方向，是厘清模型的表现退化有多少源自任务本身的内在难度，又有多少源自其有效处理长上下文的能力。

我们也没有解释这种表现退化背后的机制。我们的观察表明，上下文的结构属性（例如相关信息的放置位置或重复）会影响模型行为，但对于这种情况为何发生，我们尚无确定的答案。研究这些效应需要对机制可解释性作更深入的探究，这超出了本报告的范围。

更广泛地说，我们的发现指向上下文工程的重要性：即对模型上下文窗口的精心构造与管理。信息在模型上下文中呈现的位置与方式会强烈影响任务表现，这使其成为优化模型表现的一个有意义的未来工作方向。

# 结论

通过实验，我们表明 LLM 在不同输入长度下的表现并不一致。即便在非词面检索或文本复现这样的简单任务上，随着输入长度增长，我们也能看到表现日益不均。

我们的结果凸显出，除了当前基准之外，还需要更严格的长上下文评估，以及上下文工程的重要性。相关信息是否出现在模型的上下文中并非全部关键；更关键的是这些信息如何被呈现。我们表明，即便能力最强的模型也对此敏感，因此有效的上下文工程对于可靠的表现不可或缺。

# 脚注

[1]（2025 年 7 月 16 日）Latent List 洞见由 Kiran Vodrahalli（Google Deepmind）补充，并作了澄清

[2] 示例的原始来源：https://arxiv.org/pdf/2410.10813

# 参考文献

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub 仓库]. 链接

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv preprint arXiv:2410.10813. 链接

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530. 链接

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. 链接

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. 链接

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv preprint arXiv:2502.05167. 链接

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv preprint arXiv:2506.11440. 链接

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv preprint arXiv:2409.12640. 链接

[9] openai. (2025). mrcr [数据集]. Hugging Face. 链接

[10] openai. (2025). graphwalks [数据集]. Hugging Face. 链接

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv preprint arXiv:2302.00093. 链接

[12] jamescalam. (2024). ai-arxiv2 [数据集]. Hugging Face. 链接

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv preprint arXiv:2309.00071. 链接

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426. 链接

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining (PAKDD 2013), Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. 链接

# 附录

清洗后的 LongMemEval 数据集以及所用的针/干扰项可在此下载。

## LLM 裁判对齐：

我们采用 LLM 裁判来评估 NIAH 与 LongMemEval 实验的输出。这些裁判通过以下流程校准至人类判断：

模型输出的一个子集被人工标注为错误/正确（NIAH 约 500 条输出，LongMemEval 约 600 条输出）

用 GPT-4.1 对同一子集的模型输出标注为错误/正确。

通过衡量人类判断与模型判断一致的比例来计算对齐分数。

根据对不一致情况的人工检查来迭代提示。

重复步骤 2-4，直至对齐分数 > 0.99。

## 受测模型

由于上下文窗口或 thinking_budget 限制，并非每个实验都包含全部 18 个模型。

### Anthropic

Claude Opus 4

Claude Sonnet 4

Claude Sonnet 3.7

Claude Sonnet 3.5

Claude Haiku 3.5

### OpenAI

o3

GPT-4.1

GPT-4.1 mini

GPT-4.1 nano

GPT-4o

GPT-4 Turbo

GPT-3.5 Turbo

### Google

Gemini 2.5 Pro

Gemini 2.5 Flash

Gemini 2.0 Flash

### Alibaba

Qwen3-235B-A22B

Qwen3-32B

Qwen3-8B

## 使用的嵌入模型

text-embedding-3-small

text-embedding-3-large

jina-embeddings-v3 (input_type='text-matching')

voyage-3-large (input_type=None)

all-MiniLM-L6-v2

## 针-问题相似度

注：同一模型的 thinking/非 thinking 模式分别对待

针-问题相似度 - arXiv 大海/PG 随笔针

针-问题相似度 - PG 随笔大海/PG 随笔针

针-问题相似度 - PG 随笔大海/arXiv 针

正如我们在针-大海相似度结果中提到的，我们注意到这一处情形：模型相比其他针-大海组合表现得异常出色。单看这一点，似乎高性能模型的表现是均匀的。然而，这种均匀性在这些模型的其余实验中并不成立。

## 干扰项的影响

干扰项的影响：按干扰项数量的表现 - arXiv 大海/arXiv 针

干扰项的影响：按单个干扰项的表现 - arXiv 大海/arXiv 针

干扰项的影响：按干扰项数量的表现 - PG 随笔大海/PG 随笔针

干扰项的影响：按单个干扰项的表现 - PG 随笔大海/PG 随笔针

干扰项的影响：按干扰项数量的表现 - PG 随笔大海/arXiv 针

干扰项的影响：按单个干扰项的表现 - PG 随笔大海/arXiv 针

干扰项的影响：失败分析 - arXiv 大海/arXiv 针

干扰项的影响：失败分析 - PG 随笔大海/PG 随笔针

干扰项的影响：失败分析 - PG 随笔大海/arXiv 针

## 重复词

重复词：位置准确率 - GPT 系列

重复词：位置准确率 - Gemini 系列

重复词：位置准确率 - Qwen 系列

重复词：词数差 - GPT 系列

重复词：词数差 - Gemini 系列

重复词：词数差 - Qwen 系列

© 2026

### Product

Database Sync Enterprise Package Search MCP Docs Status Contact

### Follow

GitHub X YouTube

### Company

About Changelog Careers

### Legal

Privacy Terms Security

## 要点回顾

- 本报告以受控的非词面检索与文本复现任务评估了 18 个 LLM，发现即便任务简单，表现也随输入长度增加而持续下降。
- NIAH 与 LongMemEval 等基准低估了长上下文任务的实际难度，因为现实长上下文应用往往需要综合与多步推理。
- 在重复词任务中，各模型系列普遍出现退化，并出现未尝试、拒答与随机输出等行为，系列间差异明显。
- 位置准确率在唯一词靠近序列开头时最高；模型常过度生成或生成不足，可用输入与输出词数之差量化。
- 上下文的结构属性（相关信息的位置与重复）会显著影响模型表现，指向上下文工程的重要性。
- 上下文工程——对上下文窗口的精心构造与管理——对可靠表现不可或缺，是未来工作的关键方向。
