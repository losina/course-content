a1 = torch.tensor([[1, 2, 4], [5, 5, 7], [10, 15, 1]])
a2 = torch.tensor([[1, 1, 1], [2, 2, 3], [2, 3, 4]])
a3 = torch.tensor([[10, 10, 10], [20, 12, 1], [12, 32, 4]])
A = torch.add(a1 @ a2, a3)
print("A =", A)

# @ and torch.matmul return a multidimensional tensor
b1 = torch.tensor([[3], [5], [7]])
b2 = torch.tensor([[2], [4], [8]])
b = b1.T @ b2
print("b =", b)

# dot function returns a scalar tensor
b1 = torch.tensor([3, 5, 7])
b2 = torch.tensor([2, 4, 8])
b = torch.dot(b1, b2)
print("b =", b)