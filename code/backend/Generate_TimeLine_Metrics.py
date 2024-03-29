"""
本文件主要目的为给每个点计算'度数'、'脆弱度'、'重要性'、'威胁度'四个指标，把计算方式封装在一个函数里面即可

**输入数据格式详解**

- **nodes**: 一个列表，其中每个元素都是一个字典，表示一个节点。每个节点具有以下两个属性：
  - `"name"`: 字符串类型，表示节点的唯一标识或名称。
  - `"symbolSize"`: 整数类型，表示节点的大小或视觉重要性，具体含义取决于后续的图表渲染库。

- **links**: 一个列表，其中每个元素也是一个字典，表示一条连接两个节点的边。每条边具有以下两个属性：
  - `"source"`: 字符串类型，引用`nodes`列表中某个节点的`"name"`属性，表示这条边的起始节点。
  - `"target"`: 字符串类型，引用`nodes`列表中另一个节点的`"name"`属性，表示这条边的目标节点。

nodes输入类似如下：
[
  {'name': '结点1', 'symbolSize': 10},
  {'name': '结点2', 'symbolSize': 20},
  {'name': '结点3', 'symbolSize': 30}
]

links输入类似如下：
[
  {'source': '结点1', 'target': '结点1'},
  {'source': '结点1', 'target': '结点2'},
  {'source': '结点1', 'target': '结点3'},
  {'source': '结点1', 'target': '结点4'},
  {'source': '结点1', 'target': '结点5'}
]

**各指标计算方法**

- 度数： 计算每个点的度数即可
- 脆弱度：通过计算symbolSize值高的节点和平均节点的symbolSize值的差距占最大symbolSize和最小symbolSize值的百分比来衡量。
- 结构合理性：通过计算网络中任意两点之间的平均最短路径的倒数来衡量。
- 样本适量性：令点的数量和14的差值的绝对值=a，计算1/(a+1)来衡量
"""