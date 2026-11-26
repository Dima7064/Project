import torch
import torch.nn.functional as F
PAD, BOS, EOS = 0, 1, 2
        logits = self.head(self.dropout(out))
        return logits, hidden
@torch.no_grad()
def sample(model, itos, stoi, style, parts,
           temperature=0.8, top_k=40, top_p=0.9,
           seed=None, max_len=60):
    """Генерирует одно название с заданными условиями."""
    model.eval()
    if seed is not None:
        torch.manual_seed(seed)
        generator = torch.Generator().manual_seed(seed)
    else:
        generator = None
    x = torch.tensor([[BOS]])
    s = torch.tensor([model.style_to_id[style]])
    p = torch.tensor([parts])
    hidden = None
    result = ""
    for _ in range(max_len):
        logits, hidden = model(x, s, p, hidden)
        logits = logits[:, -1, :] / max(1e-6, temperature)
        if top_k > 0 and top_k < logits.size(-1):
            v, _ = torch.topk(logits, top_k)
            threshold = v[:, -1].unsqueeze(-1)
            logits = torch.where(logits < threshold,
                                 torch.full_like(logits, float("-inf")),
                                 logits)
        probs = F.softmax(logits, dim=-1).squeeze(0)
        if 0.0 < top_p < 1.0:
            sorted_probs, sorted_idx = torch.sort(probs, descending=True)
            cumsum = torch.cumsum(sorted_probs, dim=0)
            mask = cumsum - sorted_probs >= top_p
            sorted_probs = sorted_probs.masked_fill(mask, 0.0)
            probs = torch.zeros_like(probs).scatter(0, sorted_idx, sorted_probs)
        probs[PAD] = 0.0
        result += itos[next_id]
        x = torch.tensor([[next_id]])
    return result
