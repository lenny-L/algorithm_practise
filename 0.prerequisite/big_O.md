
### 时间复杂度
时间复杂度是一个函数，它定性描述该算法的运行时间
如何估计程序运行时间:通常会估算算法的操作单元数量来代表程序消耗的时间，这里默认CPU的每个单元运行消耗的时间都是相同的

`print "hello wolrd"`

假设算法的问题规模为n，操作问题的方法为f(n)，随着n的增大，f(n)消耗的时间也相应的增大，如果这个过程的执行时间和f(n)消耗时间的增长是同步且相近的，那么称之为算法的渐进时间复杂度，简称时间复杂度，记为 O(f(n))

**大O用来表示上界的**，当用它作为算法的最坏情况运行时间的上界，就是对任意数据输入的运行时间的上界

![时间复杂度4，一般情况下的时间复杂度](https://img-blog.csdnimg.cn/20200728185745611.png)

业内的默认规定和最坏情况下的时间复杂度是不一样的，面试中**一般是指图中的一般情况**，现场讨论则以具体的数据情况来判断

不同算法的时间复杂度和不同数据规模之间的相对关系：

![时间复杂度，不同数据规模的差异](https://img-blog.csdnimg.cn/20200728191447384.png)

一般而言：我们会忽略常数项(如果常数不是足够大)，且默认以两种时间复杂度的交点之后的情况作为大O

结论：O(1)常数阶 < O(logn)对数阶 < O(n)线性阶 < O(n^2)平方阶 < O(n^3)立方阶 < O(2^n)指数阶



### 复杂的表达式需要化简

`O(2*n^2 + 10*n + 1000)`

1. 去掉加法常数项

   `O(2*n^2 + 10*n)`

2. 去掉常数系数

   `O(n^2 + n)`

3. 只保留最高复杂度项，去掉较低数量级

   `O(n^2)`

4. n就相当于n个n^2的其中一个，对于n^2而言是可以忽略的



### O(logn)的log是以什么为底

![时间复杂度1.png](https://img-blog.csdnimg.cn/20200728191447349.png)

log以2为底n的对数和 VS log以10为底n的对数

$$
O(log_2n) = log_2{10}×O(log_{10}n)\quad\quad log_{2}10是一个常数\\[2ex]
log_in = O(log_ij × log_jn)\quad\quad log_ij是一个常数\\[2ex]
O(log_in) -> O(logn)
$$
如上所示：可以忽略掉前面的常数项，所以以2、10或者n都可以表示为logn

[Typora中如何插入数学公式](https://blog.csdn.net/worse_man/article/details/115563704)

[Cmd Markdown 公式指导手册](https://www.zybuluo.com/codeep/note/163962)



面试例子：找出n个字符串中相同的两个字符串（假设这里只有两个相同的字符串）

这个解释有点复杂，先过一遍，后续再来看


