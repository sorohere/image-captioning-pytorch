import torch

def load_model(state_dict_path: str):

    
    with open(state_dict_path, 'rb') as f:
        state_dict = torch.load(f)
    
    return state_dict


if __name__ == '__main__':
    # given path to saved state_dict of the model, load the model, load the state dict into the model, and return the model

