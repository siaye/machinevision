# 项目名称
machinevision
## 简介
本项目基于University-1652数据集，构建一个交叉视角图像匹配系统。通过命令行的方式实现待匹配图像的传入。图像匹配方法使用给出的参考方法。

University-1652数据集：https://drive.usercontent.google.com/download?id=1iVnP4gjw-iHXa0KerZQ1IfIO0i1jADsR

方法：https://github.com/layumi/University1652-Baseline


## 功能列表
1. 用户传入一张无人机图像，系统返回匹配相似度最高的五张卫星图片，并按照相似度进行排序。
2. 用户传入一张卫星图片，系统返回匹配相似度最高的五张无人机图片，并按照相似度进行排序。

## 安装指南
1. 环境要求


   在开始之前，请确保您的环境满足以下要求：

Python 3.6+

GPU 内存 >= 8GB

Numpy > 1.12.1

PyTorch 0.3+

2. 安装步骤

-克隆项目到本地-安装所需的 Python 包-数据准备-训练模型-模型评估
##项目目录及说明
image

	.idea
	__pycache__
	Lib
	LPN-main（其他参考方法）
	Sample4Geo-main（其他参考方法）
	Scripts
	share
	university
	University1652-Baseline-master(本项目使用方法）
		data（数据集）
		image_show（实验结果）
		model（储存训练得出模型点）
		demo.py（实验结果运行）
		test.py（测试）
		train.py（训练）
	.gitignore
	pyvenv.cfg
	README
	testcuda.py（用于测试CUDA、pytorch是否正确安装）

## 使用说明
在终端定位到项目中University1652-Baseline-master文件夹

输入python demo.py --query_index n 

n为传入图片名称
## 配置
config.py 是项目的配置文件，包含了项目的各种配置参数。主要配置项包括：

数据集路径: 指定训练和测试数据集的路径。

模型参数: 定义模型的超参数，如学习率、批量大小等。

训练参数: 定义训练过程中的参数，如训练轮数、优化器等。

测试参数: 定义测试过程中的参数，如评估指标等。


## 版本更新
- v1.0

