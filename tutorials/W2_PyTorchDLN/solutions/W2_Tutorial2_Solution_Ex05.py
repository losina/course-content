def training_modes(inputs, targets):

  input_dim = inputs.shape[1]
  output_dim = targets.shape[1]
  hidden = 20

  # Initial Weights and biases
  sigma = 0.001
  w1 = Variable(torch.mul(torch.randn(hidden, input_dim), sigma),
                requires_grad=True)
  b1 = Variable(torch.mul(torch.randn(hidden), 0.0),
                requires_grad=True)

  w2 = Variable(torch.mul(torch.randn(output_dim, hidden), sigma),
                requires_grad=True)
  b2 = Variable(torch.mul(torch.randn(output_dim), 0.0),
                requires_grad=True)

  params = [w1, b1, w2, b2]

  lr  = 2e-3  # learning rate
  num_epochs = 3000

  # Loss function
  criterion = nn.MSELoss()

  # Train for num_epochs
  losses = []
  rank = 5
  modes = np.empty((rank, num_epochs))

  # this few lines would implement a progress bar and loss description
  epoch_range = trange(num_epochs, desc='loss: ', leave=True)
  for epoch in epoch_range:
    if losses:
      epoch_range.set_description("loss: {:.6f}".format(losses[-1]))
      epoch_range.refresh() # to show immediately the update
    time.sleep(0.01)

    preds = modelSVD(inputs, params)
    
    loss = criterion(preds, targets)
    loss.backward()

    # SVD applied on the matrix product
    w_mult = (w1.T @ w2.T).detach().numpy()
    w_svd = np.linalg.svd(w_mult, compute_uv=False, full_matrices=True)
    modes[:,epoch] = w_svd[:rank]
    # Adjust weights & reset gradients
    with torch.no_grad():
      # Gradient descent
      w1 -= w1.grad * lr
      b1 -= b1.grad * lr
      w2 -= w2.grad * lr
      b2 -= b2.grad * lr
      # flush fradients
      w1.grad.zero_()
      b1.grad.zero_()
      w2.grad.zero_()
      b2.grad.zero_()
        
    losses.append(loss.detach().numpy())

  return (losses, modes, num_epochs)


output = training_modes(inputs, targets)
plot_learning_modes(output[0], output[2], output[1], rank=5)
