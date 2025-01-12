# -Whack-a-mole-game-attention-assessment-task-
使用打地鼠的注意力测评任务探究空间中的注意力的分布（The whack-a-mole attention assessment task was used to explore the distribution of attention in space）

打地鼠实验设计说明

1.研究问题：
任务难度对空间注意分布不对称性的影响

2.研究背景：
理解我们视觉注意力在空间中的分布机制在理论、方法及实践上都有重大意义。这一问题长期以来受到广泛关注。尤其是近年来人机交互、界面设计、计算机视觉、临床注意障碍研究、教育教学等领域的快速发展(Bakker & Niemantsverdriet,2016; Hüttermann & Memmert, 2017)，使得注意力分布规律这一问题更迫切的需要解答。
针对注意力在空间中的分布模式，以往的研究提出了许多不同的观点。根据Posner提出的聚光灯模型，人类的注意力像一个可移动的聚光灯，会优先处理被照亮区域内的刺激。也就是说，注意的集中区域（聚光灯中心）处理效率最高，边缘处理效率逐渐下降。即注意分布是以中心为重点、不对称且渐变的(Posner, 1980)。而Feature Integration Theory认为注意能够将物体的不同特征整合成单一的感知对象，但这种处理是随机和分散的。注意会优先集中在具有显著特征的区域，而不是均匀分布在整个视觉空间(Treisman & Gelade, 1980)。Inhibition of Return 理论认为：当一个外围视觉线索吸引注意力后，对在该位置出现的靶标检测速度会加快（即促进效应）。当注意力从这个线索位置转移后，原先被提示的位置相对于其他视觉区域的处理速度会变慢(Posner et al., 1985)。Eriksen和James则认为注意力的分布机制更类似于变焦镜头，当注意范围较小时，处理能力更集中；当范围进一步扩大时，注意处理的分辨率会降低(Eriksen & St. James, 1986)。
虽然对注意力在空间中分布的规律尚未被完全揭示，但过去的研究大都支持了注意力在空间中分布不均匀这一结论。但对称性在人的视觉加工中十分重要。一些基于眼动的研究表明，人的视觉模式对对称性十分敏感，人类的注意力通常分布在对称图形的对称轴上，而非随机分布(Locher & Nodine, 1987; Kootstra et al., 2008)。那么最初分布于对称中心的注意力到底受到了哪些因素的影响而变得不对称呢？如果这种不对称性确实存在，那影响不对称性程度的因素有哪些呢？针对这个问题，过往的研究主要采取了Posner线索范式、视觉搜索任务、视觉场地范式、注意窗口测量范式等实验范式。但这些实验方式存在着一些局限性，使我们不能全面的考察影响注意力在不同场景下的分布情况。首先，这些任务的刺激往往比较单一，与现实中复杂的注意集中、转移机制相差较大，因此对真实环境中人的注意力分布考察有限。其次这些实验任务主要针对单个静态目标，而人类的注意分布是动态的(Fiebelkorn & Kastner, 2019 ; Võ et al., 2012)，这些任务不能反映真实的动态注意分布。并且，这些任务很难与影响注意分布的其他的因素相结合（反应目标变化、反应方式等），限制了对影响注意的多因素的研究。另外，传统的范式较为复杂，针对一些特殊群体（年龄较小的小孩或者一些ADHD患者），可能并不使用。
为了探究更广泛的注意力分布规律，本研究创新型地提出了一种新的实验范式，使用“打地鼠”游戏这一注意测评任务，通过地鼠在不同位置的出现，被试在规定时间内击打地鼠，来检测注意力的分布。打地鼠这一游戏用于研究注意分布有诸多好处：1.模拟动态和场景先下的多目标任务，生态效度高，研究结果在实际生活场景中可推论性、可应用性更好；2. 地鼠出现的频率、位置的随机性以及目标和干扰项的数量可以灵活调整，便于研究不同任务负载对注意分布的影响。3. 可以记录参与者对不同位置目标的响应频率和速度，从而更加精确推断注意分布的模式。4.游戏设计浅显易懂，适用于测量广泛人群的注意分布规律。
 具体而言，本研究将使用“打地鼠”这一研究范式，探究任务难度对注意力分布的不对称性的影响。


3.变量定义：
自变量：任务难度（操作化定义为地鼠出现的时间长短）
因变量：注意分布对称模式（操作化定义为在被试在各象限的反应时间）



4.实验参数：
1.将屏幕（800*600）分成2*2的四个象限，代表地鼠可能出现的4个位置。
2.每个block中有40个trials，地鼠在四个象限随机出现，但保证总量是每个象限10次。（在设计矩阵中指定）。
3.地鼠出现后，被试通过鼠标点击地鼠，点击后地鼠不消失，直到凑够时间，记录地鼠出现象限、反应时、正确与否。（以此来代替wait4keys）
4.第一个block是练习block，地鼠出现时间为800ms，只有正确率达到80%才能够进行正式实验。
5.正式实验有两个block，中间有一段30s的休息时间。地鼠呈现时间为第一个block 800ms，第二个600ms。


5.设计矩阵：
第一列：地鼠编号
第二列：出现象限
第三列：地鼠出现时间（前40个为800ms（练习和block 1），后40个为600ms（block 2））
 

6.结果输出
第1-4列：被试信息
第5列：是否正确
第6列: 地鼠出现象限
第7列：反应时
第8列：试次
 

7.说明
//如需本地运行本代码，需将源代码10、13、22行的设计矩阵、背景材料换成本地地址



9.参考文献
Bakker, S., & Niemantsverdriet, K. (2016). The interaction-attention continuum: Considering various levels of human attention in interaction design. International Journal of Design, 10(2), 1–14.

Hüttermann, S., & Memmert, D. (2017). The Attention Window: A Narrative Review of Limitations and Opportunities Influencing the Focus of Attention. Research Quarterly for Exercise and Sport, 88(2), 169–183. https://doi.org/10.1080/02701367.2017.1293228

Posner, M. I. (1980). Orienting of Attention. Quarterly Journal of Experimental Psychology, 32(1), 3–25. https://doi.org/10.1080/00335558008248231

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. Cognitive Psychology, 12(1), 97–136.

Posner, M. I., Rafal, R. D., Choate, L. S., & Vaughan, J. (1985). Inhibition of return: Neural basis and function. Cognitive Neuropsychology, 2(3), 211–228. https://doi.org/10.1080/02643298508252866


Eriksen, C. W., & St. James, J. D. (1986). Visual attention within and around the field of focal attention: A zoom lens model. Perception & Psychophysics, 40(4), 225–240. https://doi.org/10.3758/BF03211502



Locher, P. J., & Nodine, C. F. (1987). Symmetry catches the eye. 收入 Eye movements from physiology to cognition (页 353–361). Elsevier. https://www.sciencedirect.com/science/article/pii/B9780444701138500515


Fiebelkorn, I. C., & Kastner, S. (2019). A Rhythmic Theory of Attention. Trends in Cognitive Sciences, 23(2), 87–101. https://doi.org/10.1016/j.tics.2018.11.009

Võ, M. L.-H., Smith, T. J., Mital, P. K., & Henderson, J. M. (2012). Do the eyes really have it? Dynamic allocation of attention when viewing moving faces. Journal of Vision, 12(13), 3. https://doi.org/10.1167/12.13.3




