# 现代代码评审中 AI 辅助的编码实践评估

> 译自：AI-Assisted Assessment of Coding Practices in Modern Code Review　｜　来源：本地材料

<!-- machine-translated: zh-CN | unit: pdfs__ai-assisted-code-review-assessment.part03 -->

## 参考文献

[1] 2024.《Google 风格指南》（Google Style Guides）。https://google.github.io/styleguide/。访问日期：2024-03-15。

[2] 2024.《Linux 内核编码风格》（Linux kernel coding style）。https://www.kernel.org/doc/html/v4.10/process/coding-style.html。访问日期：2024-03-15。

[3] 2024.《PEP 8——Python 代码风格指南》（PEP 8 – Style Guide for Python Code）。https://peps.python.org/pep-0008/。访问日期：2024-03-15。

[4] 2024.《Rust 风格指南》（Rust Style Guide）。https://doc.rust-lang.org/nightly/style-guide/。访问日期：2024-03-15。

[5] Alberto Bacchelli and Christian Bird. 2013.《现代代码评审的期望、结果与挑战》（Expectations, outcomes, and challenges of modern code review）。载于《2013 年第 35 届国际软件工程会议论文集》（2013 35th International Conference on Software Engineering, ICSE）。712–721。https://doi.org/10.1109/ICSE.2013.6606617

[6] Moritz Beller, Radjino Bholanath, Shane McIntosh, and Andy Zaidman. 2016.《分析静态分析的现状：开源软件中的大规模评估》（Analyzing the state of static analysis: A large-scale evaluation in open source software）。载于《2016 年 IEEE 第 23 届国际软件分析、演化与再造会议论文集》（2016 IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering, SANER），第 1 卷。IEEE，470–481。

[7] Zimin Chen, Małgorzata Salawa, Manushree Vijayvergiya, Goran Petrović, Marko Ivanković, and René Just. 2023.《MuRS：使用标识符模板的变异体排序与抑制》（MuRS: Mutant Ranking and Suppression using Identifier Templates）。载于《软件工程基础研讨会论文集》（Proceedings of the Symposium on the Foundations of Software Engineering, FSE）。1798–1808。

[8] M. E. Fagan. 1976.《通过设计与代码检查减少程序开发中的错误》（Design and code inspections to reduce errors in program development）。《IBM 系统杂志》（IBM Systems Journal）15, 3 (1976), 182–211。https://doi.org/10.1147/sj.153.0182

[9] Alexander Frömmgen, Jacob Austin, Peter Choy, Nimesh Ghelani, Lera Kharatyan, Gabriela Surita, Elena Khrapko, Pascal Lamblin, Pierre-Antoine Manzagol, Marcus Revaj, Maxim Tabachnyk, Daniel Tarlow, Kevin Villela, Daniel Zheng, Satish Chandra, and Petros Maniatis. 2024.《用机器学习解决代码评审评论》（Resolving Code Review Comments with Machine Learning）。载于《国际软件工程会议：软件工程实践》（International Conference on Software Engineering: Software Engineering in Practice, ICSE-SEIP）。

[10] Sarah Heckman and Laurie Williams. 2011.《面向自动化静态代码分析的可操作告警识别技术的系统性文献综述》（A systematic literature review of actionable alert identification techniques for automated static code analysis）。《信息与软件技术》（Information and Software Technology）53, 4 (2011), 363–387。https://doi.org/10.1016/j.infsof.2010.12.007 专题部分：第 24 届应用计算年会软件工程专题。

[11] Yang Hong, Chakkrit Tantithamthavorn, Patanamon Thongtanunam, and Aldeida Aleti. 2022.《Commentfinder：一种更简单、更快、更准确的代码评审评论推荐方法》（Commentfinder: a simpler, faster, more accurate code review comments recommendation）。载于《欧洲软件工程会议与软件工程基础研讨会联合会议论文集》（Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering, ESEC/FSE）。507–519。

[12] Marko Ivanković, Goran Petrović, René Just, and Gordon Fraser. 2019.《Google 的代码覆盖率》（Code Coverage at Google）。载于《欧洲软件工程会议与软件工程基础研讨会联合会议论文集》（Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering, ESEC/FSE）。955–963。

[13] Marko Ivanković, Goran Petrović, Yana Kulizhskaya, Mateusz Lewko, Luka Kalinovčić, René Just, and Gordon Fraser. 2024.《生产性覆盖率：提升代码覆盖率的可操作性》（Productive Coverage: Improving the Actionability of Code Coverage）。载于《国际软件工程会议：软件工程实践》（International Conference on Software Engineering: Software Engineering in Practice, ICSE-SEIP）。

[14] Brittany Johnson, Yoonki Song, Emerson Murphy-Hill, and Robert Bowdidge. 2013.《为什么软件开发者不使用静态分析工具来发现 bug？》（Why don't software developers use static analysis tools to find bugs?）。载于《2013 年第 35 届国际软件工程会议论文集》（2013 35th International Conference on Software Engineering, ICSE）。IEEE，672–681。

[15] Stephen C Johnson. 1977.《Lint，一个 C 程序检查器》（Lint, a C program checker）。Bell Telephone Laboratories Murray Hill。

[16] Lingwei Li, Li Yang, Huaxi Jiang, Jun Yan, Tiejian Luo, Zihan Hua, Geng Liang, and Chun Zuo. 2022.《Auger：用预训练模型自动生成评审评论》（Auger: Automatically generating review comments with pre-training models）。载于《欧洲软件工程会议与软件工程基础研讨会联合会议论文集》（Proceedings of the Joint Meeting of the European Software Engineering Conference and the Symposium on the Foundations of Software Engineering, ESEC/FSE）。1009–1021。

[17] Zhiyu Li, Shuai Lu, Daya Guo, Nan Duan, Shailesh Jannu, Grant Jenks, Deep Majumder, Jared Green, Alexey Svyatkovskiy, Shengyu Fu, and Neel Sundaresan. 2022.《通过大规模预训练自动化代码评审活动》（Automating code review activities by large-scale pre-training）。载于《第 30 届 ACM 欧洲软件工程会议与软件工程基础研讨会联合会议论文集》（新加坡，新加坡）（Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, ESEC/FSE 2022）。Association for Computing Machinery，New York, NY, USA，1035–1047。https://doi.org/10.1145/3540250.3549081

[18] Goran Petrović, Marko Ivanković, Gordon Fraser, and René Just. 2023.《请修复这个变异体：开发者如何在代码评审中处理被暴露的变异体？》（Please fix this mutant: How do developers resolve mutants surfaced during code review?）。载于《国际软件工程会议：软件工程实践》（International Conference on Software Engineering: Software Engineering in Practice, ICSE-SEIP）。150–161。

[19] Rachel Potvin and Josh Levenberg. 2016.《为什么 Google 在单一代码库中存储数十亿行代码》（Why Google Stores Billions of Lines of Code in a Single Repository）。《ACM 通讯》（Communications of the ACM, CACM）59 (2016), 78–87。http://dl.acm.org/citation.cfm?id=2854146

[20] Peter Rigby, Brendan Cleary, Frederic Painchaud, Margaret-Anne Storey, and Daniel German. 2012.《实践中的当代同行评审：来自开源开发的教训》（Contemporary Peer Review in Action: Lessons from Open Source Development）。《IEEE 软件》（IEEE Software）29, 6 (2012), 56–61。https://doi.org/10.1109/MS.2012.24

[21] Peter C. Rigby and Christian Bird. 2013.《趋同的当代软件同行评审实践》（Convergent contemporary software peer review practices）。载于《2013 年第 9 届软件工程基础联合会议论文集》（圣彼得堡，俄罗斯）（Proceedings of the 2013 9th Joint Meeting on Foundations of Software Engineering, ESEC/FSE 2013）。Association for Computing Machinery，New York, NY, USA，202–212。https://doi.org/10.1145/2491411.2491444

[22] Adam Roberts, Hyung Won Chung, Gaurav Mishra, Anselm Levskaya, James Bradbury, Daniel Andor, Sharan Narang, Brian Lester, Colin Gaffney, Afroz Mohiuddin, et al. 2023.《用 t5x 和 seqio 扩展模型与数据》（Scaling up models and data with t5x and seqio）。《机器学习研究杂志》（Journal of Machine Learning Research）24, 377 (2023), 1–8。

[23] Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, and Alberto Bacchelli. 2018.《现代代码评审：Google 的案例研究》（Modern Code Review: A Case Study at Google）。载于《国际软件工程会议：软件工程实践》（International Conference on Software Engineering: Software Engineering in Practice, ICSE-SEIP）。181–190。

[24] Patanamon Thongtanunam, Chanathip Pornprasit, and Chakkrit Tantithamthavorn. 2022.《Autotransform：支持现代代码评审流程的自动化代码转换》（Autotransform: Automated code transformation to support modern code review process）。载于《国际软件工程会议论文集》（Proceedings of the International Conference on Software Engineering, ICSE）。237–248。

[25] Rosalia Tufano, Ozren Dabić, Antonio Mastropaolo, Matteo Ciniselli, and Gabriele Bavota. 2024.《代码评审自动化：现有技术的优势与不足》（Code Review Automation: Strengths and Weaknesses of the State of the Art）。《IEEE 软件工程汇刊》（IEEE Transactions on Software Engineering, TSE）(2024)。

[26] Rosalia Tufano, Simone Masiero, Antonio Mastropaolo, Luca Pascarella, Denys Poshyvanyk, and Gabriele Bavota. 2022.《使用预训练模型提升代码评审自动化》（Using pre-trained models to boost code review automation）。载于《国际软件工程会议论文集》（Proceedings of the International Conference on Software Engineering, ICSE）。2291–2302。

[27] Carmine Vassallo, Sebastiano Panichella, Fabio Palomba, Sebastian Proksch, Harald C Gall, and Andy Zaidman. 2020.《开发者如何在不同的情境中使用静态分析工具》（How developers engage with static analysis tools in different contexts）。《经验软件工程》（Empirical Software Engineering）25 (2020), 1419–1457。

[28] T. Winters, T. Manshreck, and H. Wright. 2020.《Google 的软件工程：从长期编程中学到的经验》（Software Engineering at Google: Lessons Learned from Programming Over Time）。O'Reilly Media。https://books.google.ch/books?id=TyIrywEACAAJ

收稿日期 2024-04-05；录用日期 2024-05-04
