def criterion(x):
  margin = 0.5
  loss = torch.mean(-F.cosine_similarity(x[:,0], x[:,1]) +
                    F.cosine_similarity(x[:,0], x[:,2]) +
                    margin)
  
  return loss


x = torch.randn((5, 3, 2))
print(x)

print(criterion(x))
