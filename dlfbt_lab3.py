#===============================================================================
# DLFBT 2024/2025
# Lab assignment 3
# Authors:
#   Name1 NIA1
#   Name2 NIA2
#===============================================================================

import numpy as np
import tensorflow as tf
import torch
import torch.nn as nn
import torch.nn.functional as F

#===============================================================================
# Exercise 1. Gradient descent to find the minimum of a function
#===============================================================================
def gradient_descent_pytorch(f, x0, learning_rate, niters):
    # Initialize x:
    x_numpy = x0

    # Optimization loop:
    hh = []
    for i in range(niters):
        #-----------------------------------------------------------------------------
        # TO-DO: Define the computational graph using tensors x and y
        #-----------------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------------
        
        #-----------------------------------------------------------------------------
        # TO-DO: Compute the gradient using tensor dx
        #-----------------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------------

        #-----------------------------------------------------------------------------
        # TO-DO: Update x
        #-----------------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------------

        # Append to history:
        hh.append(x.item())

    return np.array(hh)

#===============================================================================
# Exercise 2. Linear regression using pytorch
#===============================================================================
class LinearRegressionModel_pytorch(object):

    def __init__(self, d=2):
        # Initialize weights and bias:
        self.w = torch.tensor(np.random.normal((d, 1)), requires_grad=True) 
        self.b = torch.tensor(np.random.normal((1, 1)), requires_grad=True) 
        
    def predict(self, x):
        #-----------------------------------------------------------------------
        # TO-DO block: Compute the model output y
        # Note that:
        # - x is a Nxd tensor, with N the number of patterns and d the dimension
        #   (number of features)
        # - y must be a Nx1 tensor
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

        return y


    def compute_gradients(self, x, t):
        #-----------------------------------------------------------------------
        # TO-DO block: Compute the gradients db and dw of the loss function 
        # with respect to b and w
        # Note that:
        # - x is a Nxd tensor, with N the number of patterns and d the dimension
        #   (number of features)
        # - t is a Nx1 tensor
        # - y is a Nx1 tensor
        # - The gradient db (eq. dw) must have the same shape as b (eq. w) 
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------
        
        return db, dw
        
    def gradient_step(self, x, t, eta):
        db, dw = self.compute_gradients(x, t)

        #-----------------------------------------------------------------------
        # TO-DO block: Update the model parameters b and w
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

    def fit(self, x, t, eta, num_iters):
        loss = np.zeros(num_iters)
        for i in range(num_iters):
            self.gradient_step(x, t, eta)
            loss[i] = self.get_loss(x, t).detach().numpy()
        return loss

    def get_loss(self, x, t):
        y = self.predict(x)
        loss = torch.mean(0.5*(y - torch.tensor(t))*(y - torch.tensor(t)))
        return loss
        
        
#===============================================================================
# Exercise 3. Recurrent Neural Networks with pytorch
#===============================================================================

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(RNN, self).__init__()

  	self.hidden_size = hidden_size
  	
        #-----------------------------------------------------------------------
        # TO-DO block: Program the __init__ method.
        # Should create the weight matrices as nn.Linear objects.
        # - input_size is the dimension of the input (for each time step)
        # - hidden_size is the dimension of the hidden state
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

    def forward(self, input, hidden):
        batch_size, seq_len, input_size = input.size()

        #-----------------------------------------------------------------------
        # TO-DO block: Program the forward method.
        # Should return the hidden state after applying the recurrent module
        # for seq_len timesteps.
        # - input is batch_size x seq_len x input_size
        # - hidden is batch_size x hidden_size
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

        return hidden


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTM, self).__init__()

        self.hidden_size = hidden_size

        #-----------------------------------------------------------------------
        # TO-DO block: Program the __init__ method.
        # Should create the weight matrices as nn.Linear objects.
        # - input_size is the dimension of the input (for each time step)
        # - hidden_size is the dimension of the hidden and cell states
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

    def forward(self, input, hidden, cell):
        batch_size, seq_len, input_size = input.size()

        #-----------------------------------------------------------------------
        # TO-DO block: Program the forward method.
        # Should return the hidden state after applying the recurrent module
        # for seq_len timesteps.
        # - input is batch_size x seq_len x input_size
        # - hidden is batch_size x hidden_size
        # - cell is batch_size x hidden_size
        #-----------------------------------------------------------------------
        pass
        #-----------------------------------------------------------------------
        # End of TO-DO block 
        #-----------------------------------------------------------------------

        return hidden




