# DVT
Data Validate and Transform

### 设计目标

- 每个schema有个可导出的超集数据结构

- 可以导出schema所有的校验条件

- 迭代式复合数据校验, 可定制校验顺序


### 演进

- [ ] 什么是meta field

field 是一个有名字的节点，可能包含一些基本功能
名字用来让输入数据找到处理节点
field 基本功能
- 可以依赖其他节点
- 对应某种可序列化的类型
- 有对应的输入输出方式
- 输出必为既定类型

field 的前置转换，后置转换

- [ ] 什么是validate


### 问题场景

- 一个输入字段拆解成两个字段, 干掉输入字段
- 两个字段有依赖
- 两个字段必填一个
- 输入字段裁剪
- 根据输入找到二次数据



