---
pgtitle: AutoPytorch
title: AutoPytorch
description: Обмен данными между MQL и Python через заранее созданные функции.
---
Это мой вариант AutoML.
Полный перебор вариантов структуры нейронной сети.
В качестве базы данных используется MLFlow.
Используется разбитие на Chunk вместо ТутклассДист.

В описании https://pytorch.org/docs/stable/autograd.html#torch.Tensor.backward
> This function accumulates gradients in the leaves - you might need to zero them before calling it.
Исходник здесь
https://github.com/pytorch/pytorch/blob/91e46855141be6e5b6641dd84327588392bbe941/torch/csrc/autograd/functions/accumulate_grad.h

Поскольку градиенты суммируются, то правильный вариант вычисления градиентов: 
optim.zero_grad()
for i, o in chunks:
	loss(model(i), o).backward()
optim.step()
А вот такой вариант тоже верен, но более медленный:
for i, o in chunks:
	optim.zero_grad()
	loss(model(i), o).backward()
	optim.step()
Разница между этими вариантами похожа на разницу вычисления Скользящей Средней линии:
