import torch
import torch.nn as nn
import torch.nn.functional as F
"""Style classifier: char-CNN для различения стилей."""
import random
from pathlib import Path
import torch
import torch.nn as nn
import torch.nn.functional as F
class StyleClassifier(nn.Module):
    def __init__(self, vocab_size: int, styles: list[str],
        self.kernel_size = kernel_size
        self.dropout_p = dropout
        self.emb = nn.Embedding(vocab_size, emb_size, padding_idx=0)
        self.conv = nn.Conv1d(emb_size, num_filters, kernel_size,
                              padding=kernel_size // 2)
        return self.fc(out)
@torch.no_grad()
def predict_proba(model, stoi, name):
    model.eval()
    x = torch.tensor([encode_for_classifier(name, stoi)])
