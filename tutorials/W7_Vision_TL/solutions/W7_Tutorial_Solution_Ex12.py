def get_cnn_parameter_count() -> int:
    """
    Calculate the number of parameters used by the convolutional network.
    Hint: Casting the result of convnet.parameters() to a list will make it 
          easier to work with

    Returns:
        param_count: The number of parameters in the network
    """

    convnet = ConvNet()
    convnet_parameters = list(convnet.parameters())
    conv_shape = convnet_parameters[0].shape

    param_count = conv_shape[0] * conv_shape[1] * conv_shape[2] * conv_shape[3]
    return param_count

print(get_cnn_parameter_count())
